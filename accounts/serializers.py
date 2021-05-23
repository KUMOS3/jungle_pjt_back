from movies.serializers import LikeMoviesSerializer, DislikeMoviesSerializer, WishMoviesSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
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


class UserInfoSerializer(serializers.ModelSerializer):
    like_movies = LikeMoviesSerializer(many=True)
    dislike_movies = LikeMoviesSerializer(many=True)
    wish_movies = LikeMoviesSerializer(many=True)
    class Meta:
        model = User
        fields = [
            'last_login',
            'username',
            'date_joined',
            'nickname',
            'favorite_movie',
            'birth_year',
            'like_movies',
            'dislike_movies',
            'wish_movies',
        ]
        # exclude = ['password',]

    # movie_like_users='like_movies'
    # movie_dislike_users='dislike_movies'
    # wish_users='wish_movies'