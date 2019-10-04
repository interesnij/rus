from django.views.generic.base import TemplateView
from posts.forms import PostCommentForm
from users.models import User
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.helpers import ajax_required, AuthorRequiredMixin
from posts.models import Post, PostComment
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods


class PostsView(TemplateView):
    template_name="posts.html"


class PostDeleteView(TemplateView):
    success_url = '/'
    template_name="post_confirm_delete.html"

    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if post.creator == self.request.user:
            post.is_deleted=True
            post.save()
            return HttpResponse("!")
        return super(PostDeleteView,self).get(request,*args,**kwargs)


class PostLikeView(TemplateView):
    template_name="post_like_window.html"

    def get(self,request,*args,**kwargs):
        self.post_like = Post.objects.get(pk=self.kwargs["pk"])
        self.post_like.notification_like(request.user)
        return super(PostLikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostLikeView,self).get_context_data(**kwargs)
        context["post_like"]=self.post_like
        return context


class PostCommentLikeView(TemplateView):
    template_name="post_comment_like_window.html"

    def get(self,request,*args,**kwargs):
        self.post_comment_like = PostComment.objects.get(pk=self.kwargs["pk"])
        return super(PostCommentLikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostCommentLikeView,self).get_context_data(**kwargs)
        context["post_comment_like"]=self.post_comment_like
        return context


class PostDislikeView(TemplateView):
    template_name="post_dislike_window.html"

    def get(self,request,*args,**kwargs):
        self.post_dislike = Post.objects.get(pk=self.kwargs["pk"])
        self.post_dislike.notification_dislike(request.user)
        return super(PostDislikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostDislikeView,self).get_context_data(**kwargs)
        context["post_dislike"]=self.post_dislike
        return context


class PostCommentDislikeView(TemplateView):
    template_name="post_comment_dislike_window.html"

    def get(self,request,*args,**kwargs):
        self.post_comment_dislike = PostComment.objects.get(pk=self.kwargs["pk"])
        return super(PostCommentDislikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostCommentDislikeView,self).get_context_data(**kwargs)
        context["post_comment_dislike"]=self.post_comment_dislike
        return context


@login_required
@require_http_methods(["GET"])
def post_get_comment(request):

    post_id = request.GET['post']
    post = Post.objects.get(uuid=post_id)
    form_comment = PostCommentForm()
    comments = post.comments.filter(parent_comment=None).order_by("created")
    replis = post.comments.exclude(parent_comment=None).order_by("created")
    posts_html = render_to_string("generic/post.html", {"object": post})
    thread_html = render_to_string(
        "generic/post_comments.html", {"comments": comments,"replis": replis,"form_comment": form_comment,"parent": post})
    return JsonResponse({
        "uuid": post_id,
        "post": posts_html,
        "comments": thread_html,
    })

@login_required
@ajax_required
@require_http_methods(["POST"])
def post_comment(request):

    user = request.user
    comment = request.POST['text']
    par = request.POST['parent']
    parent = Post.objects.get(pk=par)
    comment = comment.strip()
    if parent:
        new_comment = parent.comments.create(text=comment, commenter=request.user)
        html = render_to_string('generic/post_parent_comment.html',{'comment': new_comment,'request': request})
        return JsonResponse(html, safe=False)

        notification_handler(
            user, parent.creator, Notification.POST_COMMENT, action_object=reply_posts,
            id_value=str(parent.uuid), key='social_update')

    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
@require_http_methods(["POST"])
def post_reply_comment(request):

    user = request.user
    text = request.POST['text']
    com = request.POST['comment']
    comment = PostComment.objects.get(pk=com)
    text = text.strip()
    if comment:
        new_comment = PostComment.objects.create(text=text, commenter=request.user,parent_comment=comment,object_id=comment.object_id,content_type_id=comment.content_type_id)
        html = render_to_string('generic/post_reply_comment.html',{'reply': new_comment,'request': request})
        return JsonResponse(html, safe=False)

        notification_handler(
            user, parent.creator, Notification.POST_COMMENT, action_object=reply_posts,
            id_value=str(com.id), key='social_update')

    else:
        return HttpResponseBadRequest()


@login_required
@require_http_methods(["POST"])
def post_update_interactions(request):
    data_point = request.POST['id_value']
    post = Post.objects.get(uuid=data_point)
    data = {'likes': post.count_likers(), 'dislikes': post.count_dislikers(), 'comments': post.count_thread()}
    return JsonResponse(data)
