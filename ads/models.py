from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CategoryCity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999999999)])
    currency = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ads/', default='default_img.jpg')
    image2 = models.ImageField(upload_to='ads/', default='default_img.jpg')
    image3 = models.ImageField(upload_to='ads/', default='default_img.jpg')
    image4 = models.ImageField(upload_to='ads/', default='default_img.jpg')
    description = models.TextField(max_length=9000)
    created_time = models.DateTimeField(auto_now=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_city = models.ForeignKey(CategoryCity, on_delete=models.CASCADE)
    phone_number = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Ad, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title) + f"-{self.id}"
            self.save()

        # else:
        #     existing_slug = self.slug
        #     new_slug = slugify(self.title)
        #     if new_slug != existing_slug:
        #         self.slug = f"{new_slug}-{self.id}"

    def __str__(self):
        return self.title

