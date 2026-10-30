from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)