from django.db import models

# Create your models here.
class Movies(models.Model):
    movieName = models.CharField(max_length=40)
    director = models.CharField(max_length=30)
    description = models.TextField()
    image = models.TextField()
    ratings = models.IntegerField()

