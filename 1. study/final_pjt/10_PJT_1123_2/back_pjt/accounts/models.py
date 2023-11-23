from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


def genre_default():
    return {'12': 10, '14': 10, '16': 10, '18': 10, '27': 10, '28': 10, '35': 10, '36': 10, '37': 10, '53':10, '80': 10, '99':10, '878':10, '9648':10, '10402':10, '10749':10, '10751':10, '10752':10, '10770':10 }

class User(AbstractUser):
    genre_dict = models.JSONField(default=genre_default)

