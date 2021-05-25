from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Review
from .serializers import ReviewSerializer, LikeSerializer, CommentSerializer, CreateReviewSerializer
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = CreateReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk) # 언제든 쓰므로 앞으로 뺀다.
    review.delete()
    data = {
        'success': True,
        'message': f'{review_pk}번글 삭제'
    }
    return Response(data, status=200) 

@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review) # 여기서 저장
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        if review.review_like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
        like_status = {
            'liked': liked
        }
        return JsonResponse(like_status)
    elif request.method == 'POST':
        print(review.review_like_users)
        if review.review_like_users.filter(pk=request.user.pk).exists():
            review.review_like_users.remove(request.user)
        else:
            review.review_like_users.add(request.user)
        serializer = LikeSerializer(review)
        return Response(serializer.data)