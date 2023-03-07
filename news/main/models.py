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


class Blog(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today())
    img = models.ImageField()
    content = models.TextField()
    author = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name



class AboutLN(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    img1 = models.ImageField()
    img2 = models.ImageField()

    def __str__(self):
        return self.title




