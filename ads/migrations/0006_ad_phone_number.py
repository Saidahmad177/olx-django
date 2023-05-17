# Generated by Django 4.1 on 2023-05-16 21:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_ad_image_ad_image2_ad_image3_ad_image4_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='phone_number',
            field=models.IntegerField(default=987654321, validators=[django.core.validators.MinValueValidator(9), django.core.validators.MaxValueValidator(9)]),
            preserve_default=False,
        ),
    ]