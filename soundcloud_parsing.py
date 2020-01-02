# -*- coding: utf-8 -*-
from locale import *
import csv,sys,os

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

import soundcloud
from music.models import SoundParsing
from datetime import datetime, date, time


client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 200
all_tracks = client.get('/tracks', order='created_at', limit=page_size, linked_partitioning=1)
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
        try:
            label_name = track.label_name[:50]
        except:
            label_name = ''
        SoundParsing.objects.create(
                                id=track.id,
                                artwork_url=track.artwork_url,
                                bpm=track.bpm,
                                created_at=created_at,
                                duration=track.duration,
                                genre=track.genre,
                                permalink=track.permalink,
                                stream_url=stream_url,
                                streamable=track.streamable,
                                release_month=track.release_month,
                                release_year=track.release_year,
                                title=track.title,
                                uri=track.uri,
                                label_name=label_name,
                                user=track.user[2],
                                )
while all_tracks.next_href != None and all_tracks.count() < 301:
    all_tracks = client.get(all_tracks.next_href, order='created_at', limit=page_size, linked_partitioning=1)
    for track in all_tracks.collection:
        created_at = track.created_at
        created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        try:
            SoundParsing.objects.get(id=track.id)
        except:
            SoundParsing.objects.create(
                                    artwork_url=track.artwork_url,
                                    bpm=track.bpm,
                                    created_at=created_at,
                                    duration=track.duration,
                                    genre=track.genre,
                                    permalink=track.permalink,
                                    stream_url=track.stream_url,
                                    streamable=track.streamable,
                                    release_month=track.release_month,
                                    release_year=track.release_year,
                                    title=track.title,
                                    isrc=track.isrc,
                                    label_name=track.label_name[:50],
                                    )
