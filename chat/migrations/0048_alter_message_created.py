# Generated by Django 3.2 on 2022-01-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0047_alter_message_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
