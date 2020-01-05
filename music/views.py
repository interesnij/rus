from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render_to_response
from music.models import SoundParsing, SoundList
import json
from common.utils import safe_json


class AllMusicView(TemplateView):
    template_name="all_music.html"


class AllMusicListView(View):

    def get(self,request,*args,**kwargs):
        context = {}
        player = SoundList.objects.get(id=2)
        all_tracks = player.get_json_playlist()
        current_page = Paginator(all_tracks, 30)
        page = request.GET.get('page')
        context['all_tracks'] = all_tracks
        context['player'] = player
        return render_to_response('all_music_list2.html', context)


class AllSearchMusicView(View):
    template_name="search_music.html"
    def get(self,request,*args,**kwargs):
        client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
        if request.method == 'GET':
            q = request.GET.get('music_search')
            s_tracks = client.get('/tracks', q=q, license='cc-by-sa')
            response = render(request,'all_music.html',{'tracks_list':s_tracks,'q':q})
            return response
        return super(AllSearchMusicView,self).get(request,*args,**kwargs)
