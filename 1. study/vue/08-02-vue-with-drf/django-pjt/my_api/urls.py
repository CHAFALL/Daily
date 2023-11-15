"""
URL configuration for my_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # include 쪽을 보면 우리가 만든 urls가 아니다.
    # 'dj_rest_auth'가 제공하는 urls를 사용하는 것임.
    path('accounts/', include('dj_rest_auth.urls')),
    # signup만 따로 있는 것.(위의 것은 signup이 빠져있음)
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),

    # path를 2개만 추가 했는데 실제로 만들어지는 path는 더 many(7)
]
