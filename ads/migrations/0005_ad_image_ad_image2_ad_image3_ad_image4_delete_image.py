# Generated by Django 4.1 on 2023-05-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_category_image_alter_ad_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(default='default_img.jpg', upload_to='ads/'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image2',
            field=models.ImageField(default='default_img.jpg', upload_to='ads/'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image3',
            field=models.ImageField(default='default_img.jpg', upload_to='ads/'),
        ),
        migrations.AddField(
            model_name='ad',
            name='image4',
            field=models.ImageField(default='default_img.jpg', upload_to='ads/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
