from django.db import models # type: ignore
from django.contrib.auth import *


UserA = get_user_model()
# Create your models here.
class Document(models.Model):
    docname = models.CharField(max_length=200)   
    authors = models.ManyToManyField(UserA, related_name="upload_documents")
    fileHash = models.CharField(max_length=64, default='-1') 
    uploadTime = models.DateTimeField(auto_now_add=True)