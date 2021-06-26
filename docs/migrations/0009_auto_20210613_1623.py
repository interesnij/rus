# Generated by Django 3.2 on 2021-06-13 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0008_auto_20210613_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='list',
        ),
        migrations.AddField(
            model_name='doc',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doc_list', to='docs.doclist'),
        ),
    ]
