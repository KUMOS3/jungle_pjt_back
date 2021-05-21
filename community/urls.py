from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/delete/', views.review_delete),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('<int:review_pk>/likes/', views.likes),
]