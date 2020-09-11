import re
MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
from django.views.generic.base import TemplateView
from users.models import User
from video.models import VideoAlbum, Video
from django.views.generic import ListView
from video.forms import VideoForm
from common.template.video import get_template_user_video
from common.template.user import get_settings_template


class UserVideoList(ListView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.album = VideoAlbum.objects.get(uuid=self.kwargs["uuid"])
        if self.user == request.user:
            self.video_list = self.album.get_my_queryset()
        else:
            self.video_list = self.album.get_queryset()

        self.template_name = get_template_user_video(self.user, "u_album_list/", "list.html", request.user)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserVideoList,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserVideoList,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['album'] = self.album
        return context

    def get_queryset(self):
        video_list = self.video_list
        return video_list


class UserVideoInfo(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from stst.models import VideoNumbers

        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.video = Video.objects.get(uuid=self.kwargs["uuid"])
        if request.user.is_authenticated:
            try:
                VideoNumbers.objects.get(user=request.user.pk, video=self.video.pk)
            except:
                if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
                    VideoNumbers.objects.create(user=request.user.pk, video=self.video.pk, platform=1)
                else:
                    VideoNumbers.objects.create(user=request.user.pk, video=self.video.pk, platform=0)

        self.template_name = get_template_user_video(self.user, "u_video_info/", "video.html", request.user)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserVideoInfo,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserVideoInfo,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['object'] = self.video
        return context


class UserVideoDetail(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from stst.models import VideoNumbers

        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.video = Video.objects.get(uuid=self.kwargs["uuid"])
        if request.user.is_authenticated:
            try:
                VideoNumbers.objects.get(user=request.user.pk, video=self.video.pk)
            except:
                if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
                    VideoNumbers.objects.create(user=request.user.pk, video=self.video.pk, platform=1)
                else:
                    VideoNumbers.objects.create(user=request.user.pk, video=self.video.pk, platform=0)

        self.template_name = get_template_user_video(self.user, "u_video_detail/", "video.html", request.user)
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            self.template_name = "mob_" + self.template_name
        return super(UserVideoDetail,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserVideoDetail,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['object'] = self.video
        return context

class UserCreateVideoAttachWindow(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.template_name = get_settings_template("user_create/create_video_attach.html", request)

        return super(UserCreateVideoAttachWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserCreateVideoAttachWindow,self).get_context_data(**kwargs)
        context['form_post'] = VideoForm()
        return context

class UserCreateListWindow(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.template_name = get_settings_template("user_create/create_list.html", request)
        return super(UserCreateListWindow,self).get(request,*args,**kwargs)


class UserCreateVideoListWindow(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.album = VideoAlbum.objects.get(uuid=self.kwargs["uuid"])
        self.template_name = get_settings_template("user_create/create_list_video.html", request)
        return super(UserCreateVideoListWindow,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserCreateVideoListWindow,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['album'] = self.album
        context['form_post'] = VideoForm({'album': self.album})
        return context
