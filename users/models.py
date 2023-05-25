from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(
        unique=True,
        validators=[MaxValueValidator(999999999), MinValueValidator(100000000)], null=True)


class Contact(models.Model):
    user = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    phone_number = models.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])

    def __str__(self):
        return self.user
