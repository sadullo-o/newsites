import datetime

from django.db import models

# Create your models here.

class Yangilik(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title