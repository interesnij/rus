# Generated by Django 3.2 on 2021-07-05 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210430_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Категория смайликов',
                'verbose_name_plural': 'Категории смайликов',
            },
        ),
        migrations.AlterField(
            model_name='customlink',
            name='link',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название ссылки, уникально для П. и С.'),
        ),
        migrations.CreateModel(
            name='Smiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='smiles/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.smilecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Смайл',
                'verbose_name_plural': 'Смайлы',
            },
        ),
    ]
