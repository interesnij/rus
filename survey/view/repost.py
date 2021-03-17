from django.views.generic.base import TemplateView
from communities.models import Community
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from posts.forms import PostForm
from posts.models import Post
from survey.models import Survey
from users.models import User
from common.check.user import check_user_can_get_list
from common.check.community import check_can_get_lists
from common.processing.post import get_post_processing, repost_message_send
from common.template.user import get_detect_platform_template
from common.notify.photo import *


class UUCMSurveyWindow(TemplateView):
    """
    форма репоста опроса пользователя к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        self.user = User.objects.get(pk=self.kwargs["pk"])
        if self.user != request.user:
            check_user_can_get_list(request.user, self.user)
        self.template_name = get_detect_platform_template("survey/repost/u_ucm_survey.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(UUCMSurveyWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UUCMSurveyWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.survey
        context["user"] = self.user
        return context

class CUCMSurveyWindow(TemplateView):
    """
    форма репоста опроса сообщества к себе на стену, в свои сообщества, в несколько сообщений
    """
    template_name = None

    def get(self,request,*args,**kwargs):
        self.survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        self.community = Community.objects.get(pk=self.kwargs["pk"])
        check_can_get_lists(request.user, self.community)
        self.template_name = get_detect_platform_template("survey/repost/c_ucm_survey.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(CUCMSurveyWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CUCMSurveyWindow,self).get_context_data(**kwargs)
        context["form"] = PostForm()
        context["object"] = self.survey
        context["community"] = self.community
        return context


class UUSurveyRepost(View):
    """
    создание репоста опроса пользователя на свою стену
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        lists, attach = request.POST.getlist("lists"), request.POST.getlist('attach_items')
        if user != request.user:
            check_user_can_get_list(request.user, user)
        form_post = PostForm(request.POST)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=survey.creator, community=None, attach="sur")
            new_post = post.create_post(creator=request.user, attach=attach, text=post.text, category=post.category, lists=lists, community=None, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, status="PG")
            get_post_processing(new_post)
            user_survey_notify(request.user, survey.creator.pk, None, survey.pk, None, None, "u_survey_repost", "RE")
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CUSurveyRepost(View):
    """
    создание репоста опроса сообщества на свою стену
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        lists, attach = request.POST.getlist("lists"), request.POST.getlist('attach_items')
        form_post = PostForm(request.POST)
        check_can_get_lists(request.user, community)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=survey.creator, community=community, attach="sur")
            new_post = post.create_post(creator=request.user, attach=attach, text=post.text, category=post.category, lists=lists, community=None, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, status="PG")
            get_post_processing(new_post)
            community_survey_notify(request.user, community, None, survey.pk, None, None, "c_survey_repost", 'RE')
            return HttpResponse("")
        else:
            return HttpResponseBadRequest()


class UCSurveyRepost(View):
    """
    создание репоста опроса пользователя на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        communities = request.POST.getlist("communities")
        lists, attach = request.POST.getlist("lists"), request.POST.getlist('attach_items')
        if not communities:
            return HttpResponseBadRequest()
        form_post = PostForm(request.POST)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=survey.creator, attach="pho")
            for community_id in communities:
                if request.user.is_staff_of_community(community_id):
                    new_post = post.create_post(creator=request.user, attach=attach, text=post.text, category=post.category, lists=lists, community_id=community_id, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, status="PG")
                    get_post_processing(new_post)
                    user_survey_notify(request.user, survey.creator.pk, community_id, survey.pk, None, None, "u_survey_repost", 'CR')
        return HttpResponse()


class CCSurveyRepost(View):
    """
    создание репоста опроса сообщества на стены списка сообществ, в которых пользователь - управленец
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        check_can_get_lists(request.user, community)
        communities = request.POST.getlist("communities")
        lists, attach = request.POST.getlist("lists"), request.POST.getlist('attach_items')
        if not communities:
            return HttpResponseBadRequest()
        form_post = PostForm(request.POST)
        if request.is_ajax() and form_post.is_valid():
            post = form_post.save(commit=False)
            parent = Post.create_parent_post(creator=survey.creator, community=community, attach="pho")
            for community_id in communities:
                if request.user.is_staff_of_community(community_id):
                    new_post = post.create_post(creator=request.user, attach=attach, text=post.text, category=post.category, lists=lists, community_id=community_id, parent=parent, comments_enabled=post.comments_enabled, is_signature=post.is_signature, votes_on=post.votes_on, status="PG")
                    get_post_processing(new_post)
                    community_survey_notify(request.user, community, community_id, survey.pk, None, None, "c_survey_repost", 'CR')
        return HttpResponse()


class UMSurveyRepost(View):
    """
    создание репоста опроса пользователя в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        repost_message_send(survey, "sur", None, request, "Репост опроса пользователя")
        return HttpResponse()


class CMSurveyRepost(View):
    """
    создание репоста опроса сообщества в беседы, в которых состоит пользователь
    """
    def post(self, request, *args, **kwargs):
        survey = Survey.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        check_can_get_lists(request.user, community)
        repost_message_send(survey, "sur", community, request, "Репост опроса сообщества")
        return HttpResponse()
