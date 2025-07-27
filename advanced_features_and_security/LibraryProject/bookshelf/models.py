from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
