# Generated by Django 2.2.5 on 2020-01-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20200103_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundparsing',
            name='permalink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
