from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CategoryCity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    description = models.TextField(max_length=9000)
    created_time = models.DateTimeField(auto_now=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_city = models.ForeignKey(CategoryCity, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/', default='default_img.jpg')

    def __str__(self):
        return self.ad_id.title
