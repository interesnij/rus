# Generated by Django 3.2 on 2021-06-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_rename_survey_survey_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
    ]