from users.models import User
from posts.models import *
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views import View
from posts.forms import *
from django.http import Http404
from django.views.generic.base import TemplateView


class AddPostsListInUserCollections(View):
    def get(self,request,*args,**kwargs):
        from common.check.user import check_user_can_get_list

        list = PostsList.objects.get(pk=self.kwargs["pk"])
        check_user_can_get_list(request.user, list.creator)
        if request.is_ajax() and list.is_user_can_add_list(request.user.pk):
            list.add_in_user_collections(request.user)
        return HttpResponse()

class RemovePostsListFromUserCollections(View):
    def get(self,request,*args,**kwargs):
        from common.check.user import check_user_can_get_list

        list = PostsList.objects.get(pk=self.kwargs["pk"])
        check_user_can_get_list(request.user, list.creator)
        if request.is_ajax() and list.is_user_can_delete_list(request.user.pk):
            list.remove_in_user_collections(request.user)
        return HttpResponse()

class PostUserCreate(View):
    def post(self,request,*args,**kwargs):
        form_post, list, attach = PostForm(request.POST), PostsList.objects.get(pk=self.kwargs["pk"]), request.POST.getlist('attach_items')

        if request.is_ajax() and form_post.is_valid() and list.is_user_can_create_el(request.user.pk):
            post = form_post.save(commit=False)
            creator = request.user
            if post.text or attach:
                from common.templates import render_for_platform
                new_post = post.create_post(
                                            creator=creator,
                                            text=post.text,
                                            category=post.category,
                                            list=list,
                                            attach=attach,
                                            parent=None,
                                            comments_enabled=post.comments_enabled,
                                            is_signature=post.is_signature,
                                            votes_on=post.votes_on,
                                            community=None
                                            )

                from common.notify.progs import user_send_notify, user_send_wall
                from notify.models import Notify, Wall

                Wall.objects.create(creator_id=creator.pk, type="POS", object_id=new_post.pk, verb="ITE")
                user_send_wall(new_post.pk, None, "create_u_post_wall")
                for user_id in creator.get_user_main_notify_ids():
                    Notify.objects.create(creator_id=creator.pk, recipient_id=user_id, type="POS", object_id=new_post.pk, verb="ITE")
                    user_send_notify(new_post.pk, creator.pk, user_id, None, "create_u_post_notify")
                creator.plus_posts(1)

                return render_for_platform(request, 'posts/post_user/my_post.html', {'object': new_post})
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()


class UserSaveCreatorDraftPost(View):
    def post(self,request,*args,**kwargs):
        form_post, list = PostForm(request.POST), PostsList.objects.get(pk=self.kwargs["pk"])

        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            new_post = post.create_creator_draft_post(
                                        creator=request.user,
                                        text=post.text,
                                        category=post.category,
                                        list=list,
                                        attach=request.POST.getlist('attach_items'),
                                        comments_enabled=post.comments_enabled,
                                        votes_on=post.votes_on,
                                        )
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class UserSaveOfferDraftPost(View):
    def post(self,request,*args,**kwargs):
        form_post, list = PostForm(request.POST), PostsList.objects.get(pk=self.kwargs["pk"])

        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            new_post = post.create_offer_draft_post(
                                        creator=request.user,
                                        text=post.text,
                                        category=post.category,
                                        list=list,
                                        attach=request.POST.getlist('attach_items'),
                                        comments_enabled=post.comments_enabled,
                                        votes_on=post.votes_on,
                                        )
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class PostUserEdit(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from common.templates import get_my_template
        self.post = Post.objects.get(pk=self.kwargs["pk"])
        if request.user.pk != self.post.creator.pk:
            raise Http404
        self.template_name = get_my_template("posts/post_user/edit_post.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(PostUserEdit,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostUserEdit, self).get_context_data(**kwargs)
        context['post'] = self.post
        context['form'] = PostForm(instance=self.post)
        return context

    def post(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        form_post, attach = PostForm(request.POST, instance=post), request.POST.getlist('attach_items')

        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            if post.text or attach:
                from common.templates import render_for_platform
                new_post = post.edit_post(
                                            text=post.text,
                                            category=post.category,
                                            list=post.list,
                                            attach=attach,
                                            comments_enabled=post.comments_enabled,
                                            is_signature=post.is_signature,
                                            votes_on=post.votes_on,
                                            )
                return render_for_platform(request, 'posts/post_user/my_post.html', {'object': new_post})
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()

class PostUserFixed(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user == post.creator:
            post.fixed_post(post.creator)
            return HttpResponse()
        else:
            raise Http404

class PostUserUnFixed(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user == post.creator:
            post.unfixed_post()
            return HttpResponse()
        else:
            raise Http404


class PostUserOffComment(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user == post.creator and request.is_ajax():
            post.comments_enabled = False
            post.save(update_fields=['comments_enabled'])
            return HttpResponse()
        else:
            raise Http404

class PostUserOnComment(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user == post.creator and request.is_ajax():
            post.comments_enabled = True
            post.save(update_fields=['comments_enabled'])
            return HttpResponse()
        else:
            raise Http404

class PostUserDelete(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.pk == post.creator.pk:
            post.delete_item(None)
            return HttpResponse()
        else:
            raise Http404

class PostUserRecover(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.pk == post.creator.pk:
            post.restore_item(None)
            return HttpResponse()
        else:
            raise Http404


class UserOnVotesPost(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and post.creator == request.user:
            post.votes_on = True
            post.save(update_fields=['votes_on'])
            return HttpResponse()
        else:
            raise Http404

class UserOffVotesPost(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and post.creator == request.user:
            post.votes_on = False
            post.save(update_fields=['votes_on'])
            return HttpResponse()
        else:
            raise Http404


class PostGetVotes(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        data = {'like_count': post.likes_count(), 'dislike_count': post.dislikes_count()}
        return JsonResponse(data)


class UserChangePostPosition(View):
    def post(self,request,*args,**kwargs):
        import json

        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == user.pk:
            for item in json.loads(request.body):
                post = Post.objects.get(pk=item['key'])
                post.order=item['value']
                post.save(update_fields=["order"])
        return HttpResponse()

class UserChangePostsListPosition(View):
    def post(self,request,*args,**kwargs):
        import json
        from users.model.list import UserPostsListPosition

        user = User.objects.get(pk=self.kwargs["pk"])
        if request.user.pk == user.pk:
            for item in json.loads(request.body):
                list = UserPostsListPosition.objects.get(list=item['key'], user=user.pk)
                list.position=item['value']
                list.save(update_fields=["position"])
        return HttpResponse()
