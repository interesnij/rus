from django.views.generic.base import TemplateView
from communities.models import Community
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from posts.forms import PostForm
from posts.models import Post, PostsList
from users.models import User
from common.check.user import check_user_can_get_list
from common.check.community import check_can_get_lists
from common.templates import get_detect_platform_template


class UUCMPostWindow(TemplateView):
    """
    форма репоста записи пользователя к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.post = Post.objects.get(pk=self.kwargs["pk"])
        self.can_copy_item = self.post.list.is_user_can_copy_el(request.user.pk)
        self.template_name = get_detect_platform_template("posts/repost/u_ucm_post.html", request.user, request.META['HTTP_USER_AGENT'])
        if self.post.creator.pk != request.user.pk:
            check_user_can_get_list(request.user, self.post.creator)
        return super(UUCMPostWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UUCMPostWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.post
        context["can_copy_item"] = self.can_copy_item
        return context

class CUCMPostWindow(TemplateView):
    """
    форма репоста записи сообщества к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.post = Post.objects.get(pk=self.kwargs["pk"])
        self.can_copy_item = self.post.list.is_user_can_copy_el(request.user.pk)
        self.template_name = get_detect_platform_template("posts/repost/c_ucm_post.html", request.user, request.META['HTTP_USER_AGENT'])
        check_can_get_lists(request.user, self.post.community)
        return super(CUCMPostWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CUCMPostWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.post
        context["can_copy_item"] = self.can_copy_item
        return context

class UUCMPostsListWindow(TemplateView):
    """
    форма репоста списка записей пользователя к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.list = PostsList.objects.get(pk=self.kwargs["pk"])
        self.can_copy_item = self.list.is_user_can_copy_el(request.user.pk)
        if self.list.creator.pk != request.user.pk:
            check_user_can_get_list(request.user, self.list.creator)
        self.template_name = get_detect_platform_template("posts/repost/u_ucm_post_list.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(UUCMPostsListWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UUCMPostsListWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.list
        context["can_copy_item"] = self.can_copy_item
        return context

class CUCMPostsListWindow(TemplateView):
    """
    форма репоста списка записей сообщества к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        self.can_copy_item = self.list.is_user_can_copy_el(request.user.pk)
        check_can_get_lists(request.user, self.post.community)
        self.template_name = get_detect_platform_template("posts/repost/c_ucm_post_list.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(CUCMPostsListWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CUCMPostsListWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.list
        context["can_copy_item"] = self.can_copy_item
        return context


class UUPostRepost(View):
    """
    создание репоста записи пользователя на свою стену
    """
    def post(self, request, *args, **kwargs):
        parent, form_post, attach, lists, count, creator = Post.objects.get(pk=self.kwargs["pk"]), PostForm(request.POST), request.POST.getlist('attach_items'), request.POST.getlist('lists'), 0, request.user
        if parent.creator.pk != creator.pk:
            check_user_can_get_list(creator, parent.creator)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for list_pk in lists:
                post_list = PostsList.objects.get(pk=list_pk)
                post.create_post(creator=creator, list=post_list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=False, votes_on=post.votes_on, community=None)
                count += 1
            parent.repost += count
            parent.save(update_fields=["repost"])

            from common.notify.notify import user_notify, user_wall
            user_notify(creator, None, parent.pk, "POS", "create_u_post_notify", "RE")
            user_wall(creator, None, parent.pk, "POS", "create_u_post_wall", "RE")
            creator.plus_posts(count)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CUPostRepost(View):
    """
    создание репоста записи сообщества на свою стену
    """
    def post(self, request, *args, **kwargs):
        from common.notify.notify import community_notify, community_wall

        parent, form_post, attach, lists, count, creator = Post.objects.get(pk=self.kwargs["pk"]), PostForm(request.POST), request.POST.getlist('attach_items'), request.POST.getlist('lists'), 0, request.user
        check_can_get_lists(creator, parent.community)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for list_pk in lists:
                post_list = PostsList.objects.get(pk=list_pk)
                post.create_post(creator=creator, list=post_list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=False, votes_on=post.votes_on, community=None)
                count += 1
                community_notify(creator, parent.community, None, parent.pk, "POS", "create_c_post_notify", "RE")
                community_wall(creator, parent.community, None, parent.pk, "POS", "create_c_post_wall", "RE")

            parent.repost += count
            parent.save(update_fields=["repost"])

            creator.plus_posts(count)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class UCPostRepost(View):
    """
    создание репоста записи пользователя на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        from common.notify.notify import user_notify, user_wall

        parent, form_post, attach, lists, count, creator = Post.objects.get(pk=self.kwargs["pk"]), PostForm(request.POST), request.POST.getlist('attach_items'), request.POST.getlist('lists'), 0, request.user

        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)

            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for list_pk in lists:
                post_list = PostsList.objects.get(pk=list_pk)
                if post_list.is_user_can_create_el(creator.pk):
                    community = post_list.community
                    post.create_post(creator=creator, list=post_list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, community=community)
                    count += 1
                    community.plus_posts(1)

                    user_notify(creator, community, parent.pk, "POS", "create_u_post_notify", "CR")
                    user_wall(creator, None, parent.pk, "POS", "create_u_post_wall", "CR")

            parent.repost += count
            parent.save(update_fields=["repost"])

            creator.plus_posts(count)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CCPostRepost(View):
    """
    создание репоста записи сообщества на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        from common.notify.notify import community_notify, community_wall

        parent, form_post, attach, lists, count, creator = Post.objects.get(pk=self.kwargs["pk"]), PostForm(request.POST), request.POST.getlist('attach_items'), request.POST.getlist('lists'), 0, request.user
        check_can_get_lists(creator, parent.community)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for list_pk in lists:
                post_list = PostsList.objects.get(pk=list_pk)
                if post_list.is_user_can_create_el(creator.pk):
                    community = post_list.community
                    post.create_post(creator=creator, list=post_list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, community=community)
                    count += 1
                    community_notify(creator, parent.community, community.pk, parent.pk, "POS", "create_c_post_notify", "CR")
                    community_wall(creator, parent.community, community.pk, parent.pk, "POS", "create_c_post_wall", "CR")

            parent.repost += count
            parent.save(update_fields=["repost"])

            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class UMPostRepost(View):
    """
    создание репоста записи пользователя в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        parent, connections, form_post, attach, count = Post.objects.get(pk=self.kwargs["pk"]), request.POST.getlist("chat_items"), PostForm(request.POST), request.POST.getlist('attach_items'), 0
        if parent.creator != request.user:
            check_user_can_get_list(request.user, parent.creator)
        if not connections:
            return HttpResponseBadRequest()

        if request.is_ajax() and form_post.is_valid():
            from chat.models import Message, Chat

            post = form_post.save(commit=False)
            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for object_id in connections:
                if object_id[0] == "c":
                    chat = Chat.objects.get(pk=object_id[1:])
                    message = Message.send_message(chat=chat, creator=request.user, repost=parent, parent=None, text="Репост записи пользователя", attach=attach, sticker=None, transfer=None)
                elif object_id[0] == "u":
                    user = User.objects.get(pk=object_id[1:])
                    message = Message.get_or_create_chat_and_send_message(creator=request.user, user=user, repost=parent, text="Репост записи пользователя", attach=attach, sticker=None, transfer=None)
                count += 1

            parent.repost += count
            parent.save(update_fields=["repost"])

        else:
            return HttpResponseBadRequest()
        return HttpResponse()

class CMPostRepost(View):
    """
    создание репоста записи сообщества в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        parent, connections, form_post, attach, count = Post.objects.get(pk=self.kwargs["post_pk"]), request.POST.getlist("chat_items"), PostForm(request.POST), request.POST.getlist('attach_items'), 0
        check_can_get_lists(request.user, parent.community)

        if not connections:
            return HttpResponseBadRequest()
        if request.is_ajax() and form_post.is_valid():
            from chat.models import Message, Chat

            post = form_post.save(commit=False)
            if parent.parent:
                parent = parent.parent
            else:
                parent = parent
            for object_id in connections:
                if object_id[0] == "c":
                    chat = Chat.objects.get(pk=object_id[1:])
                    message = Message.send_message(chat=chat, creator=request.user, repost=parent, parent=None, attach=attach, text="Репост записи пользователя", transfer=None, sticker=None)
                elif object_id[0] == "u":
                    user = User.objects.get(pk=object_id[1:])
                    message = Message.get_or_create_chat_and_send_message(creator=request.user, user=user, repost=parent, text="Репост записи пользователя", attach=attach, sticker=None)
                count += 1

            parent.repost += count
            parent.save(update_fields=["repost"])
        else:
            return HttpResponseBadRequest()
        return HttpResponse()


class UUPostsListRepost(View):
    """
    создание репоста списка записей пользователя на свою стену
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        form_post = PostForm(request.POST)
        attach = request.POST.getlist('attach_items')
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=list.creator, community=None, attach="lpo"+str(list.pk))
            new_post = post.create_post(creator=request.user, list=post.list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=None, votes_on=post.votes_on, community=None)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CUPostsListRepost(View):
    """
    создание репоста списка записей сообщества на свою стену
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        form_post = PostForm(request.POST)
        check_can_get_lists(request.user, community)
        attach = request.POST.getlist('attach_items')
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=list.creator, community=community, attach="lpo"+str(list.pk))
            new_post = post.create_post(creator=request.user, list=post.list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=None, votes_on=post.votes_on, community=None)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class UCPostsListRepost(View):
    """
    создание репоста списка записей пользователя на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        communities = request.POST.getlist("communities")
        attach = request.POST.getlist('attach_items')
        if not communities:
            return HttpResponseBadRequest()
        form_post = PostForm(request.POST)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=list.creator, community=community, attach="lpo"+str(list.pk))
            for community_id in communities:
                if request.user.is_staff_of_community(community_id):
                    new_post = post.create_post(creator=request.user, list=post.list, attach=attach, text=post.text, category=post.category,  parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, community=Community.objects.get(pk=community_id))
        return HttpResponse()


class CCPostsListRepost(View):
    """
    создание репоста списка записей сообщества на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        check_can_get_lists(request.user, community)
        communities = request.POST.getlist("communities")
        attach = request.POST.getlist('attach_items')
        if not communities:
            return HttpResponseBadRequest()
        form_post = PostForm(request.POST)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=list.creator, community=community, attach="lpo"+str(list.pk))
            for community_id in communities:
                if request.user.is_staff_of_community(community_id):
                    new_post = post.create_post(creator=request.user, list=post.list, attach=attach, text=post.text, category=post.category, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, community=Community.objects.get(pk=community_id))
        return HttpResponse()


class UMPostsListRepost(View):
    """
    создание репоста списка записей пользователя в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        repost_message_send(list, "lpo"+str(list.pk), None, request, "Репост списка записей пользователя")
        return HttpResponse()


class CMPostsListRepost(View):
    """
    создание репоста списка записей сообщества в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        list = PostsList.objects.get(pk=self.kwargs["list_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        check_can_get_lists(request.user, community)
        repost_message_send(list, "lpo"+str(list.pk), community, request, "Репост списка записей сообщества")
        return HttpResponse()
