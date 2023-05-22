from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(
        unique=True,
        validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
