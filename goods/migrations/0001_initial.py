# Generated by Django 3.2 on 2021-04-29 19:14

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import goods.helpers
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.PositiveIntegerField(blank=True, default=0, verbose_name='Цена товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание товара')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=goods.helpers.upload_to_good_directory, verbose_name='Главное изображение')),
                ('status', models.CharField(choices=[('PRO', 'Обработка'), ('DRA', 'Черновик'), ('PUB', 'Опубликовано'), ('TDEL', 'Удалено'), ('PRI', 'Приватно'), ('TCLO', 'Закрыто модератором'), ('MAN', 'Созданный персоналом'), ('TDELP', 'Удалённый приватный'), ('TDELM', 'Удалённый менеджерский'), ('TCLOP', 'Закрытый приватный'), ('TCLOM', 'Закрытый менеджерский')], default='PRO', max_length=6, verbose_name='Статус')),
                ('comments_enabled', models.BooleanField(default=True, verbose_name='Разрешить комментарии')),
                ('votes_on', models.BooleanField(default=True, verbose_name='Реакции разрешены')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name='Кол-во комментов')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('ad_views', models.PositiveIntegerField(default=0, verbose_name='Кол-во рекламных просмотров')),
                ('reposts', models.PositiveIntegerField(default=0, verbose_name='Кол-во репостов')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')),
                ('image', models.ImageField(blank=True, upload_to='goods/list', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'категория товаров',
                'verbose_name_plural': 'категории товаров',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='GoodSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер подкатегории')),
                ('image', models.ImageField(blank=True, upload_to='goods/list', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goodcategory', verbose_name='Категория-родитель')),
            ],
            options={
                'verbose_name': 'Подкатегория товаров',
                'verbose_name_plural': 'Подкатегории товаров',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='GoodList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='uuid')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('type', models.CharField(choices=[('MAI', 'Основной'), ('LIS', 'Пользовательский'), ('PRI', 'Приватный'), ('MAN', 'Созданный персоналом'), ('TPRO', 'Обработка'), ('TDEL', 'Удалённый'), ('TDELP', 'Удалённый приватный'), ('TDELM', 'Удалённый менеджерский'), ('TCLO', 'Закрытый менеджером'), ('TCLOP', 'Закрытый приватный'), ('TCLOM', 'Закрытый основной'), ('TCLOMA', 'Закрытый менеджерский')], default='TPRO', max_length=6, verbose_name='Тип альбома')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('order', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_list_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Подборка товаров',
                'verbose_name_plural': 'Подборки товаров',
            },
        ),
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=goods.helpers.upload_to_good_directory, verbose_name='Изображение')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.good')),
            ],
        ),
        migrations.CreateModel(
            name='GoodComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('text', models.TextField(blank=True, null=True)),
                ('attach', models.CharField(blank=True, max_length=200, verbose_name='Прикрепленные элементы')),
                ('status', models.CharField(choices=[('PUB', 'Опубликовано'), ('EDI', 'Изменённый'), ('PRO', 'Обработка'), ('TDEL', 'Удалённый'), ('TDELE', 'Удалённый изменённый'), ('TCLO', 'Закрытый менеджером'), ('TCLOE', 'Закрытый изменённый')], default='PRO', max_length=5, verbose_name='Тип альбома')),
                ('reposts', models.PositiveIntegerField(default=0, verbose_name='Кол-во репостов')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.good')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='good_comment_replies', to='goods.goodcomment', verbose_name='Родительский комментарий')),
            ],
            options={
                'verbose_name': 'комментарий к записи',
                'verbose_name_plural': 'комментарии к записи',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='list',
            field=models.ManyToManyField(blank=True, related_name='good_list', to='goods.GoodList'),
        ),
        migrations.AddField(
            model_name='good',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodsubcategory', verbose_name='Подкатегория'),
        ),
        migrations.AddIndex(
            model_name='goodlist',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='goods_goodl_created_bf9ff4_brin'),
        ),
        migrations.AddIndex(
            model_name='goodcomment',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='goods_goodc_created_4f76f1_brin'),
        ),
        migrations.AddIndex(
            model_name='good',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='goods_good_created_414618_brin'),
        ),
    ]