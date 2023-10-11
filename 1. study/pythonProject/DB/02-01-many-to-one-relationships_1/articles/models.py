from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 만약에 게시글에 댓글이 작성되어있는데 게시글 작성자가 게시글을 지운다면 어떻게 처리를 할 것인가??
    
    # 게시글은 그냥 지워지면 상관없는데, 댓글은 본인이 가지고 있는 외래키 필드의 참고하고 있는 Article의 정보들을 가지고 있는데 이게 쓸모 x해짐-> 이게 DB에서 무결성 원칙 위반하게 됨
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    