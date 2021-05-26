from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    favorite_movie = models.CharField(max_length=50)
    birth_year = models.IntegerField(null=True)

class Achievement(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    achieved_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='achievements', blank=True)