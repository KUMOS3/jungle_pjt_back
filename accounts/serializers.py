from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import LikeMoviesSerializer, DislikeMoviesSerializer, WishMoviesSerializer
from .models import User, Achievement
User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'nickname',
            'favorite_movie',
            'birth_year',
            ]


class AchievementSerializer(serializers.ModelSerializer):
    class Meta():
        model = Achievement
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    like_movies = LikeMoviesSerializer(many=True)
    dislike_movies = LikeMoviesSerializer(many=True)
    wish_movies = LikeMoviesSerializer(many=True)
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'username',
            'date_joined',
            'nickname',
            'favorite_movie',
            'birth_year',
            'like_movies',
            'dislike_movies',
            'wish_movies',
            'achievements'
        ]
        # exclude = ['password',]

    # movie_like_users='like_movies'
    # movie_dislike_users='dislike_movies'
    # wish_users='wish_movies'

#  칭호 획득 후 response하는 serializer
class AchieveSerializer(serializers.ModelSerializer):
    class Meta():
        model = Achievement
        # 추후 업적 시스템에 활용할 데이터들
        fields = '__all__'


class UserNameSerializer(serializers.ModelSerializer):
    like_movies = LikeMoviesSerializer(many=True)
    dislike_movies = LikeMoviesSerializer(many=True)
    wish_movies = LikeMoviesSerializer(many=True)
    achievements = AchievementSerializer(many=True)
    
    class Meta():
        model = User
        fields = [
            'id',
            'last_login',
            'nickname',
            'favorite_movie',
            'like_movies',
            'dislike_movies',
            'wish_movies',
            'achievements'
        ]