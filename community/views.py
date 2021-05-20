from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Review
from .serializers import ReviewListSerializer, ReviewSerializer

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

@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
def likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.review_like_users.filter(pk=request.user.pk).exists():
        review.review_like_users.remove(request.user)
    else:
        review.review_like_users.add(request.user)