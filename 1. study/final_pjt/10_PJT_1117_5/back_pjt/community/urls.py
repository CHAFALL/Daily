from django.urls import path
from . import views



urlpatterns = [
    path('review/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('reviews/<int:review_pk>/comments/',views.comment_create),
]