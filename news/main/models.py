import datetime

from django.db import models

# Create your models here.

class Yangilik(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title


class Trend(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author


class Aboutus(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    content = models.TextField()
    klas = models.CharField(max_length=50)
    rasm = models.TextField()

    def __str__(self):
        return  self.title






