from django.db import models

# Create your models here.
# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)  # User의pk정수값이 들어감
#     title = models.CharField(max_length=10)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)