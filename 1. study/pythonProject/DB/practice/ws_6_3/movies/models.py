from django.db import models
from django.conf import settings

# 클래스를 미리 선언해주고 이용해야됨,아래 위치 잘볼 것

class Hashtag(models.Model):
    content = models.CharField(max_length=15, unique=True)

class Movie(models.Model):
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_movies"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # shell_plus 쓸 때 보기 편하게하려고 씀
    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
