# Generated by Django 4.1 on 2023-05-18 11:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_ad_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
