# Generated by Django 3.2 on 2021-05-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_delete_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electnewscategory',
            options={'ordering': ['order', 'name'], 'verbose_name': 'категория активностей', 'verbose_name_plural': 'категория активностей'},
        ),
    ]
