# Generated by Django 2.2.5 on 2019-10-22 11:28

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goodphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='goods/%Y/%m/%d', verbose_name='изображение 5'),
        ),
        migrations.DeleteModel(
            name='GoodPhoto',
        ),
    ]
