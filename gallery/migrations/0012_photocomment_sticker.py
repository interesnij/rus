# Generated by Django 3.2 on 2021-07-06 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20210706_1418'),
        ('gallery', '0011_alter_photo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocomment',
            name='sticker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.stickers'),
        ),
    ]