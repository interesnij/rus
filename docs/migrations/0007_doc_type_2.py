# Generated by Django 3.2 on 2021-06-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_rename_status_doc_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='type_2',
            field=models.CharField(choices=[('BOO', 'Книга'), ('ART', 'Статья'), ('PU', 'Заметка'), ('FIL', 'Файл'), ('OTH', 'Другое')], default='_PRO', max_length=5),
        ),
    ]