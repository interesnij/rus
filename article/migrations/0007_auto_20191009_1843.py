# Generated by Django 2.2.5 on 2019-10-09 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_articlecomment_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='article.Article'),
        ),
    ]
