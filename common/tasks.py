from datetime import datetime, timedelta
from celery import shared_task, current_task, task
from celery import Celery
from tr import celery_app
from posts.models import PostsList
from tr.celery import app


class MyTask(celery_app.Task):
    def run(self):
        list = PostsList.objects.get(pk=1)
        list.name = "бубубу"
        list.save(update_fields=["name"])

app.tasks.register(MyTask())
