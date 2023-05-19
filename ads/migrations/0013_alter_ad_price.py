# Generated by Django 4.1 on 2023-05-19 19:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0012_alter_ad_image_alter_ad_image2_alter_ad_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999999999)]),
        ),
    ]