from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie
from .serializers import MovieListSerializer, LikeSerializer, DislikeSerializer, WishSerializer
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = MovieListSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
        # return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def like(request, movie_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.movie_like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
        like_status = {
            'liked': liked
        }
        return JsonResponse(like_status)# json 형태로 반환
    elif request.method == 'POST':
        print(movie.movie_like_users)
        # 좋아요 해제
        # if request.user in review.like_users.all():
        # if movie.movie_like_users.filter(pk=request.user.pk).exists():
        if movie.movie_like_users.filter(pk=request.user.pk).exists():
            movie.movie_like_users.remove(request.user)
            # liked = False
        # 좋아요 눌렀으므로 좋아요 리스트 추가, 별로에요 리스트에 있다면 해제
        else:
            movie.movie_like_users.add(request.user)
            if movie.movie_dislike_users.filter(pk=request.user.pk).exists():
                movie.movie_dislike_users.remove(request.user)
            # liked = True # flag
        serializer = LikeSerializer(movie)
        return Response(serializer.data)

        # (사용함!)
        # # 아니면
        # from django.http.response import JsonResponse
        # #
        
        # like_status = {
        #     'liked': liked
        # }
        # return JsonResponse(like_status)# json 형태로 반환

@api_view(['GET', 'POST'])
def dislike(request, movie_pk):
    
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.movie_dislike_users.filter(pk=request.user.pk).exists():
            disliked = True
        else:
            disliked = False
        dislike_status = {
            'disliked': disliked
        }
        return JsonResponse(dislike_status)
    elif request.method == 'POST':
        print('dislike')
        if movie.movie_dislike_users.filter(pk=request.user.pk).exists():
            movie.movie_dislike_users.remove(request.user)
        # 별로에요 눌렀으므로 별로에요 리스트 추가, 좋아요 리스트에 있다면 해제
        else:
            movie.movie_dislike_users.add(request.user)
            if movie.movie_like_users.filter(pk=request.user.pk).exists():
                movie.movie_like_users.remove(request.user)
        serializer = DislikeSerializer(movie)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def wish(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.movie_wish_users.filter(pk=request.user.pk):
            wished = True
        else:
            wished = False
        wish_status = {
            'wished': wished
        }
        return JsonResponse(wish_status)
    elif request.method == 'POST':
        if movie.movie_wish_users.filter(pk=request.user.pk):
            movie.movie_wish_users.remove(request.user)
        # 별로에요 눌렀으므로 별로에요 리스트 추가, 좋아요 리스트에 있다면 해제
        else:
            movie.movie_wish_users.add(request.user)
        serializer = WishSerializer(movie)
        return Response(serializer.data)



# def todo_list_create(request):
#     if request.method == 'GET':
#         # todos = Todo.objects.all()
#         serializer = TodoSerializer(request.user.todos, many=True) # request.user.todos
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # 1대1관계가 형성되었으므로 user도 넣어서 저장
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)