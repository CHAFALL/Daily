from django.urls import path
from . import views
# TIP(다른 앱 views 사용시)
# from 다른 앱 import views as views2

# 앱이 하나여서 app_name 안 써보겠음
urlpatterns = [
    path('', views.index),
    path('example/', views.example),
]
