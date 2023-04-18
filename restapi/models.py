from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    works = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_TYPES = (
        ('Y', 'Youtube'),
        ('I', 'Instagram'),
        ('O', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=1, choices=LINK_TYPES)
