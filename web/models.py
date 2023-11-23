from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class movie(models.Model):
    movie_name = models.CharField(max_length=256)
    gener = models.CharField(max_length=256)


class Room(models.Model):
    room_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    movie_id = models.ManyToManyField(movie)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
