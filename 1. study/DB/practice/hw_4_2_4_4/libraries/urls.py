from django.urls import path
from . import views
app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/reviews/', views.reviews_create, name = 'reviews_create'),
    path('<int:book_pk>/reviews/<int:review_pk>/delete/', views.reviews_delete, name='reviews_delete')
]
