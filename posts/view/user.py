import re
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from users.models import User
from posts.models import Post, PostComment
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.views import View
from common.checkers import check_is_not_blocked_with_user_with_id, check_is_connected_with_user_with_id
from posts.forms import CommentForm


class PostUserCommentList(ListView):
    template_name = None
    paginate_by = 15

    def get(self,request,*args,**kwargs):
        self.item = Post.objects.get(uuid=self.kwargs["uuid"])
        self.user = User.objects.get(pk=self.kwargs["pk"])

        if request.user.is_authenticated:
            if self.user.pk == request.user.pk:
                self.template_name = "u_post_comment/my_comments.html"
            elif request.user.is_post_manager():
                self.template_name = "u_post_comment/staff_comments.html"
            elif self.user != request.user:
                check_is_not_blocked_with_user_with_id(user=request.user, user_id=self.user.id)
                if self.user.is_closed_profile():
                    check_is_connected_with_user_with_id(user=request.user, user_id=self.user.id)
                self.template_name = "u_post_comment/comments.html"
        elif request.user.is_anonymous:
            if self.user.is_closed_profile():
                raise PermissionDenied('Это закрытый профиль. Только его друзья могут видеть его информацию.')
            else:
                self.template_name = "u_post_comment/anon_comments.html"

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + template_name
        return super(PostUserCommentList,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostUserCommentList, self).get_context_data(**kwargs)
        context['parent'] = self.item
        context['user'] = self.user
        return context

    def get_queryset(self):
        comments = self.item.get_comments()
        return comments


class PostCommentUserCreate(View):

    def post(self,request,*args,**kwargs):
        from common.utils import get_or_create_csrf_token

        form_post = CommentForm(request.POST, request.FILES)
        user = User.objects.get(pk=request.POST.get('id'))
        post = Post.objects.get(uuid=request.POST.get('item'))

        if form_post.is_valid():
            get_or_create_csrf_token(request)
            comment=form_post.save(commit=False)

            if request.user.pk != user.pk:
                check_is_not_blocked_with_user_with_id(user=request.user, user_id = user.pk)
                if user.is_closed_profile():
                    check_is_connected_with_user_with_id(user=request.user, user_id = user.pk)
            if request.POST.get('text') or  request.POST.get('photo') or request.POST.get('video') or request.POST.get('music') or request.POST.get('good') or request.POST.get('article'):
                from common.comment_attacher import get_comment_attach
                new_comment = comment.create_comment(commenter=request.user, parent_comment=None, post=post, text=comment.text)
                get_comment_attach(request, new_comment)
                new_comment.notification_user_comment(request.user)
                return render_to_response('u_post_comment/my_parent.html',{'comment': new_comment, 'request_user': request.user, 'request': request})
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()


class PostReplyUserCreate(View):
    def post(self,request,*args,**kwargs):
        from common.utils import get_or_create_csrf_token

        form_post = CommentForm(request.POST, request.FILES)
        user = User.objects.get(uuid=request.POST.get('uuid'))
        parent = PostComment.objects.get(pk=request.POST.get('pk'))

        if form_post.is_valid():
            get_or_create_csrf_token(request)
            comment=form_post.save(commit=False)

            if request.user != user:
                check_is_not_blocked_with_user_with_id(user=request.user, user_id = user.id)
                if user.is_closed_profile():
                    check_is_connected_with_user_with_id(user=request.user, user_id = user.id)
            if request.POST.get('text') or  request.POST.get('photo') or request.POST.get('video') or request.POST.get('music') or request.POST.get('good') or request.POST.get('article'):
                from common.comment_attacher import get_comment_attach
                new_comment = comment.create_comment(commenter=request.user, parent_comment=parent, post=None, text=comment.text)
                get_comment_attach(request, new_comment)
                new_comment.notification_user_reply_comment(request.user)
            else:
                return HttpResponseBadRequest()
            return render_to_response('u_post_comment/my_reply.html',{'reply': new_comment, 'comment': parent, 'user': user, 'request_user': request.user, 'request': request})
        else:
            return HttpResponseBadRequest()

class PostCommentUserDelete(View):
    def get(self,request,*args,**kwargs):
        comment = PostComment.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == comment.commenter.pk:
            comment.is_deleted = True
            comment.save(update_fields=['is_deleted'])
            return HttpResponse("")
        else:
            return HttpResponse("")

class PostCommentUserAbortDelete(View):
    def get(self,request,*args,**kwargs):
        comment = PostComment.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == comment.commenter.pk:
            comment.is_deleted = False
            comment.save(update_fields=['is_deleted'])
            return HttpResponse("")
        else:
            return HttpResponse("")


def post_update_interactions(request):
    data_point = request.POST['id_value']
    item = Post.objects.get(uuid=data_point)
    data = {'likes': item.count_likers(), 'dislikes': item.count_dislikers(), 'comments': item.count_thread()}
    return JsonResponse(data)


def user_fixed(request, uuid):
	item = Post.objects.get(uuid=uuid)
	if request.user == item.creator:
		item.get_fixed_for_user(request.user.pk)
		return HttpResponse("!")
	else:
		return HttpResponse("Закрепляйте, пожалуйста, свои записи!")

def user_unfixed(request, uuid):
	item = Post.objects.get(uuid=uuid)
	if request.user == item.creator:
		item.is_fixed=False
		item.save(update_fields=['is_fixed'])
		return HttpResponse("!")
	else:
		return HttpResponse("Открепляйте, пожалуйста, свои записи!")


def user_off_comment(request, uuid):
	item = Post.objects.get(uuid=uuid)
	if request.user == item.creator:
		item.comments_enabled=False
		item.save(update_fields=['comments_enabled'])
		return HttpResponse("!")
	else:
		return HttpResponse("Пожалуйста, отключайте комментарии к своим записям!")

def user_on_comment(request, uuid):
	item = Post.objects.get(uuid=uuid)
	if request.user == item.creator:
		item.comments_enabled=True
		item.save(update_fields=['comments_enabled'])
		return HttpResponse("!")
	else:
		return HttpResponse("Пожалуйста, включайте комментарии к своим записям!")


class PostUserDelete(View):
    def get(self,request,*args,**kwargs):
        item = Post.objects.get(uuid=self.kwargs["uuid"])
        if request.user.pk == item.creator.pk:
            item.is_deleted = True
            item.save(update_fields=['is_deleted'])
            return HttpResponse("")
        else:
            return HttpResponse("")

class PostUserAbortDelete(View):
    def get(self,request,*args,**kwargs):
        item = Post.objects.get(uuid=self.kwargs["uuid"])
        if request.user.pk == item.creator.pk:
            item.is_deleted = False
            item.save(update_fields=['is_deleted'])
            return HttpResponse("")
        else:
            return HttpResponse("")


class PostUserDetail(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.item = Post.objects.get(uuid=self.kwargs["uuid"])
        self.template_name = self.user.get_template_user(folder="post_user/", template="detail.html", request=request)
        return super(PostUserDetail,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostUserDetail,self).get_context_data(**kwargs)
        context["object"]=self.item
        return context


class UserOnVotesPost(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(uuid=self.kwargs["uuid"])
        if post.creator == request.user:
            post.votes_on = True
            post.save(update_fields=['votes_on'])
        return HttpResponse("!")

class UserOffVotesPost(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(uuid=self.kwargs["uuid"])
        if post.creator == request.user:
            post.votes_on = False
            post.save(update_fields=['votes_on'])
        return HttpResponse("!")
