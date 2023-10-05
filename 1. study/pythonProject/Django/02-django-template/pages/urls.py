
from django.urls import path 
from . import views
# from articles import views

app_name='pages'
urlpatterns = [
    path('asdsdad', views.index, name='index')
]
