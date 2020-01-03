# -*- coding: utf-8 -*-
from locale import *
import csv,sys,os

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

import soundcloud
from music.models import SoundParsing, SounGenres
from datetime import datetime, date, time


genres_list = SounGenres.objects.values('name')
genres_list_names = [name['name'] for name in genres_list]
client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 10
all_tracks = client.get('/tracks', order="playback_count", limit=page_size, linked_partitioning=1)
count = 0

for track in all_tracks.collection:
    created_at = track.created_at
    created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    try:
        SoundParsing.objects.get(id=track.id)
    except:
        try:
            stream_url = track.stream_url
        except:
            stream_url = ''
        if track.genre and track.genre in genres_list_names:
            SoundParsing.objects.create(
                                id=track.id,
                                artwork_url=track.artwork_url,
                                bpm=track.bpm,
                                created_at=created_at,
                                duration=track.duration,
                                genre=track.genre.replace('"', ''),
                                permalink=track.permalink,
                                stream_url=stream_url,
                                streamable=track.streamable,
                                release_month=track.release_month,
                                release_year=track.release_year,
                                title=track.title,
                                uri=track.uri,)
        count = count + 1

while all_tracks.next_href != None and count < 21:
    all_tracks = client.get(all_tracks.next_href, order="playback_count", limit=page_size, linked_partitioning=1)
    for track in all_tracks.collection:
        created_at = track.created_at
        created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        try:
            SoundParsing.objects.get(id=track.id)
        except:
            try:
                stream_url = track.stream_url
            except:
                stream_url = ''
            if track.genre and track.genre in genres_list_names:
                SoundParsing.objects.create(
                                    id=track.id,
                                    artwork_url=track.artwork_url,
                                    bpm=track.bpm,
                                    created_at=created_at,
                                    duration=track.duration,
                                    genre=track.genre.replace('"', ''),
                                    permalink=track.permalink,
                                    stream_url=stream_url,
                                    streamable=track.streamable,
                                    release_month=track.release_month,
                                    release_year=track.release_year,
                                    title=track.title,
                                    uri=track.uri,)
        count = count + 1
