from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.IntegerField()
    popularity = models.IntegerField()
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    # review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    # favorite_movie = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_genres')