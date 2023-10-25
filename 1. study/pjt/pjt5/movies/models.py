from django.db import models
from django.conf import settings


GENRE_CHOICES = (
    ('COMEDY', 'Comedy'),
    ('FANTASY', 'Fantasy'),
    ('ROMANCE', 'Romance')
)

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=15)
    description = models.TextField()
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    score = models.FloatField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.CharField(max_length=200)
