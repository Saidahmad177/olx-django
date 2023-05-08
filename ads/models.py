from django.db import models
from django.utils import timezone


class Ad(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    price = models.CharField(max_length=18)
    description = models.TextField(max_length=9000)
    created_time = models.DateTimeField(auto_now=timezone.now)


class Image(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/', defaul='default_img.jpg')


class Category(models.Model):
    pass


class CategoryCity(models.Model):
    pass
