from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content
        
