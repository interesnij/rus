from datetime import datetime, timedelta
from celery import shared_task, current_task, task
from celery import Celery
from tr import celery_app
from posts.models import PostsList


class MyTask(celery_app.Task):
    print ("it's work!")
    list = PostsList.objects.get(pk=1)
    list.name = "бубубу"
    list.save(update_fields=["name"])


MyTask.apply_async(eta=timezone.now() + timezone.timedelta(seconds=20))
