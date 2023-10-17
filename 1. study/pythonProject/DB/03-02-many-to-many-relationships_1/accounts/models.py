from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 만약에 우리가 이전에 이렇게 대체를 해 놓지 않았다면 이 팔로워 기능 구현 불가, (왜냐하면 내장 유저모델은 이렇게 노출 x)
# 그때 가서 대체를 한다면 데이터베이스 초기화 필요...(이미 해둔 이유)
class User(AbstractUser):
    # 기본값(symmetrical=True)
    # 왜 이번엔 마이그레이션 할 때 아무것도 안 물어보지??
    # ManyToManyField의 특징 : 필드가 기존 필드에 추가 되지 않음, 중계 테이블을 만듬, 그래서 기존의 user 테이블에 변화가 없어서 안 물어봄
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

