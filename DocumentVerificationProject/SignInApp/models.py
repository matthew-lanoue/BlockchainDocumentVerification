from django.db import models # type: ignore

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)   
    password = models.CharField(max_length=200)   
    