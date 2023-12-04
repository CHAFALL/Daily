from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('genres/', views.get_genres),
    path('recommend/', views.recommend),
    path('genres/<int:genre_pk>/', views.get_genre_movies),
    path('actor/<int:actor_pk>/', views.actor_detail),
    path('search/<str:word>/', views.movie_search),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/actors/', views.movie_actors),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/scores/', views.movie_scores),
    path('<int:movie_pk>/comments/', views.movie_comments),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.movie_comments_detail),
    path('<str:username>/like/movies/', views.like_movies),
]