# Generated by Django 2.2.5 on 2020-01-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200102_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundparsing',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
