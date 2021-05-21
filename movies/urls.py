from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list), # 이제 앱 네임 필요없음
    path('<int:movie_pk>/like/', views.like),
    path('<int:movie_pk>/dislike/', views.dislike),
    path('<int:movie_pk>/wish/', views.wish),
]