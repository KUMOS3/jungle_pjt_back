from django.urls import path
from . import views
# 토큰 라이브러리
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    # 토큰 라이브러리 주소
    path('api-token-auth/', obtain_jwt_token),
]