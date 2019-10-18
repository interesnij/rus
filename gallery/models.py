from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class Album(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    cover_photo = models.ForeignKey('Photo', related_name='+', blank=True,
                                    null=True, verbose_name="Обожка")
    is_public = models.BooleanField(default=True, verbose_name="Виден другим")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    order = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user', null=False, blank=False, verbose_name="Создатель")

    class Meta:
        indexes = (
            BrinIndex(fields=['created']),
        )
        ordering = ['order']



class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=upload_to)
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_public = models.BooleanField(default=True, verbose_name="Виден другим")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создано")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = (
            BrinIndex(fields=['created']),
        )
        ordering = ['order']
