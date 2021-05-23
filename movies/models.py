from django.db import models
from django.conf import settings
# from djangovalidators.validators import validate_comma_separated_integer_list

# Create your models here.

class Movie(models.Model):
    adult = models.BooleanField(null=True)
    backdrop_path = models.TextField(null=True)
    # genre_ids = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    genre_ids = models.CharField(max_length=100, null=True)
    original_title = models.CharField(max_length=50, null=True)
    overview = models.TextField(null=True)
    popularity = models.IntegerField(null=True)
    poster_path = models.TextField(null=True)
    # 나중에 기반 알고리즘 시에는 DateField나 기타 방법을 고려해야
    release_date = models.CharField(max_length=50, null=True) 
    title = models.CharField(max_length=50, null=True)
    vote_average = models.IntegerField(null=True)

    vote_count = models.IntegerField(null=True)
    
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies', blank=True)
    movie_wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies', blank=True)

   

    # review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    # favorite_movie = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    favorite_users = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='favorite_genres')