# Generated by Django 4.1 on 2023-05-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ad_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='currency',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ad',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
