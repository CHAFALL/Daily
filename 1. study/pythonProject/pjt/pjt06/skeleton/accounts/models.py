from django.db import models
# 어떻게 클래스처럼 . 으로 접근할 수 있을까?(폴더명/폴더명/ 이런식이 아닌) -> 그 역할을 해주는 것이 __init__.py이다!!
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass