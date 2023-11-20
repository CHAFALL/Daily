from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie),
    path('genres/', views.genre),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/movie_reviews/',views.movie_review_list_create),
    path('movie_reviews/<int:movie_review_pk>/', views.movie_review_detail),
    
]