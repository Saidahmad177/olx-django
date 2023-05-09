from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)


class CategoryCity(models.Model):
    name = models.CharField(max_length=50)


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False)
    # slug = models.SlugField(max_length=100)
    slug = slugify(title)
    price = models.CharField(max_length=18)
    description = models.TextField(max_length=9000)
    created_time = models.DateTimeField(auto_now=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_city = models.ForeignKey(CategoryCity, on_delete=models.CASCADE)


class Image(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/', default='default_img.jpg')

