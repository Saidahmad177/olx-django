# Generated by Django 4.1 on 2023-05-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_category_slug_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
