# Generated by Django 3.2 on 2021-10-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0016_delete_doclist'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='is_doc',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='docslist',
            name='is_doc_list',
            field=models.BooleanField(default=True),
        ),
    ]
