# Generated by Django 2.2.5 on 2020-01-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200102_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundparsing',
            name='label_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
