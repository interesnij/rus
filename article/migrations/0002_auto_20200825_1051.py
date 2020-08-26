# Generated by Django 3.1 on 2020-08-25 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        ('posts', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_attach',
            field=models.ManyToManyField(blank=True, related_name='attached_comment', to='posts.PostComment'),
        ),
        migrations.AddField(
            model_name='article',
            name='community',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='article',
            name='item_attach',
            field=models.ManyToManyField(blank=True, related_name='attached_item', to='posts.Post'),
        ),
    ]
