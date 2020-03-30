from music.models import *
from django.views.generic.base import TemplateView


class TagMusicGet(TemplateView):
    template_name="music/get/tag_music.html"

    def get(self,request,*args,**kwargs):
        self.tag = SoundTags.objects.get(pk=self.kwargs["pk"])
        self.list = SoundcloudParsing.objects.filter(tag=self.tag)
        self.parse_list = json.dumps(self.list)
        return super(TagMusicGet,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        import json
        from django.http import HttpResponse

        context = super(TagMusicGet,self).get_context_data(**kwargs)
        context["tag"] = self.tag
        context["list"] = self.parse_list
        return context
