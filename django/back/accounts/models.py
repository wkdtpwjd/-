from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    gender = models.BooleanField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)

    