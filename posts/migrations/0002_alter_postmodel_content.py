# Generated by Django 4.0.4 on 2022-04-21 17:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
    ]
