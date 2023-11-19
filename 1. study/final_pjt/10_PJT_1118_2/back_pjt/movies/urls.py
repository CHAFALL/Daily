from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie),
    path('genres/', views.genre),
    path('movies/<int:movie_pk>/', views.movie_detail),
    
]