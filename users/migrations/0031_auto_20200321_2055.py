# Generated by Django 2.2.5 on 2020-03-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20200320_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=17, verbose_name='Телефон'),
        ),
    ]
