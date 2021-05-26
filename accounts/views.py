from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import UserLoginSerializer, UserInfoSerializer, UserSignupSerializer, AchievementSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import User, Achievement

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserLoginSerializer 통해 데이터 직렬화
    serializer = UserSignupSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def profile(request, pk):
    if request.method == 'GET':
        User = get_user_model()
        user_info = User.objects.get(pk=pk)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def achievement(request):
    if request.method == 'GET':
        achievements = get_list_or_404(Achievement)
        serializer = AchievementSerializer(achievements, many=True)
        return Response(serializer.data)

    # if request.method == 'POST':
    #     achievement = get_object_or_404(Achievement, pk=pk)
    #     achievement.achieved_users.add(request.user)
    #     print(request.user)
    #     user_info = User.objects.get(username=request.user)
    #     print(user_info)
    #         # liked = True # flag
    #     serializer = AchieveSerializer(achievement)
    #     if len(user_info.like_movies) == 1:
    #         serializer.data["acheive"] = 
    #     print(serializer.data)
    #     return Response(serializer.data)