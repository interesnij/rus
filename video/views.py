from django.views.generic.base import TemplateView
from users.models import User
from video.models import VideoList, VideoAlbum
from django.views.generic import ListView


class AllVideoView(TemplateView):
    template_name="all_video.html"


class UserBasicVideoList(ListView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(uuid=self.kwargs["uuid"])
        self.list = VideoList.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_template_user(folder="user_basic_list/", template="list.html", request=request)
        return super(UserBasicVideoList,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserBasicVideoList,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['playlist'] = self.list
        return context

    def get_queryset(self):
        video_list = self.list.playlist_too()
        return video_list


class UserVideoList(ListView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(uuid=self.kwargs["uuid"])
        self.album = VideoAlbum.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_template_user(folder="user_album_list/", template="list.html", request=request)
        return super(UserVideoList,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserVideoList,self).get_context_data(**kwargs)
        context['user'] = self.user
        context['album'] = self.album
        return context

    def get_queryset(self):
        video_list = self.album.playlist_too()
        return video_list
