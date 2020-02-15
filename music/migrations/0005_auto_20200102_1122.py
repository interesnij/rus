# Generated by Django 2.2.5 on 2020-01-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20200102_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundparsing',
            name='artwork_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='bpm',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='isrc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='label_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='permalink',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='permalink_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='release',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='release_day',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='release_month',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='release_year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='stream_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='streamable',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='tag_list',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='uri',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
