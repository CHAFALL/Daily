from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # variable routing (변수명으로 view에서 인자로 받을 것임)
    path('articles/<int:num>/',views.detail, name='detail'),
    path('hello/<str:name>/',views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
]
