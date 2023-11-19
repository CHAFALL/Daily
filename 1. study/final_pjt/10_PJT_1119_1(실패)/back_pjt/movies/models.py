from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model) :
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    # )
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    overview = models.TextField()
    vote_avg = models.FloatField()
    poster_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)
    

    def __str__(self):
        return self.title