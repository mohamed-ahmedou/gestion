from django.db import models

class Post(models.Model):
    test = models.CharField(max_length=200, unique=True)
    

# Create your models here.
