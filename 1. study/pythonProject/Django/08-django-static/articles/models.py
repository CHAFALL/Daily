from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 이거 안 해두면(blank=True): 게시글 쓸 때마다 이미지를 넣어줘야 한다.
    # 게시글 쓸 때 이미지를 공백으로 둬도 된다를 의미(아래)
    # upload_to: ~로 올리겠다
    # image = models.ImageField(blank=True, upload_to='images/')
    # 날짜 파일로 해서 관리 하겠다.(날짜별 분류)
    # 아니면 함수를 만들어서 함수 값에 따라 관리를 할 수도 있음(유저명이라던가.)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
