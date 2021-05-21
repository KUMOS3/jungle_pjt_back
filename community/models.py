from django.db import models
from django.conf import settings

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    
    num_choices = zip(range(1,6), range(1,6))
    movie_rate = models.IntegerField(choices=num_choices, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_like_users = models.ManyToManyField('self', symmetrical=False, related_name='like_reviews')


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()