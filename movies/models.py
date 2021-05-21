from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    # 나중에 기반 알고리즘 시에는 DateField나 기타 방법을 고려해야
    release_date = models.CharField(max_length=50) 
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.IntegerField(null=True)
    popularity = models.IntegerField(null=True)
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    movie_wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    # review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    # favorite_movie = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    favorite_users = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='favorite_genres')