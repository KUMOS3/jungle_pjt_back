from rest_framework import serializers
from .models import Movie
from .models import MovieRecommend
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Genre
        fields = ['name']

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta():
        model = Movie
        fields = '__all__'

# 리뷰에서 개별 무비 id를 기반으로 이름을 알려주는 serializer
class MovieNameSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ['title', 'id', 'overview']


class MovieRecommendSerializer(serializers.ModelSerializer):
    class Meta():
        model = MovieRecommend
        fields = '__all__'

#  좋아요 후 response하는 serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        # 추후 업적 시스템에 활용할 데이터들
        fields = ['title', 'release_date', 'vote_average', 'popularity', 'movie_like_users']

#  별로에요 후 response하는 serializer
class DislikeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        # 추후 업적 시스템에 활용할 데이터들
        fields = ['title', 'release_date', 'vote_average', 'popularity', 'movie_dislike_users']

#  찜 후 response하는 serializer
class WishSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        # 추후 업적 시스템에 활용할 데이터들
        fields = ['title', 'release_date', 'vote_average', 'popularity', 'movie_dislike_users']


# user가 참조하는 속성들의 serializer, user serializer에 사용
class LikeMoviesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ['id']

class DislikeMoviesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ['id']

class WishMoviesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Movie
        fields = ['id']
    # movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # movie_dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    # wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')