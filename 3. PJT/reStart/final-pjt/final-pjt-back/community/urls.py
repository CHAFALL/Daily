from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.like),
    path('<int:article_pk>/comments/', views.article_comments),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.comment_like),
    path('<int:article_pk>/comments/<int:comment_pk>/recomment/', views.recomment),
    path('<str:username>/articles/', views.user_articles),
    path('<str:username>/comments/', views.user_comments),
    path('<str:username>/like/articles/', views.like_articles),
]