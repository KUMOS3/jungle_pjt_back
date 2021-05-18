from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list), # 이제 앱 네임 필요없음
    
]