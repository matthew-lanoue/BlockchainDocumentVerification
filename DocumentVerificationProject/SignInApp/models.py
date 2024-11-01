from django.db import models # type: ignore
from django.contrib.auth import *


UserA = get_user_model()
# Create your models here.
class Document(models.Model):
    docname = models.CharField(max_length=200)   
    authors = models.ManyToManyField(UserA, related_name="documents")
    