# Generated by Django 2.2.16 on 2020-09-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_goodalbum_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена товара'),
        ),
    ]
