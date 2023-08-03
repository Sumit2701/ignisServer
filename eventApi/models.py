from django.db import models
from django.db import models
from django.db import models

from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    data = models.CharField(max_length=200)
    time = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
