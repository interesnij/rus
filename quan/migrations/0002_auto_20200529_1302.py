# Generated by Django 2.2.5 on 2020-05-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionscategory',
            name='icon',
            field=models.CharField(max_length=400, verbose_name='svg icon'),
        ),
    ]
