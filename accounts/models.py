from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    favorite_movie = models.CharField(max_length=50)
    birth_year = models.DateTimeField()