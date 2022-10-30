from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Post(models.Model) : 
    title = models.CharField(max_length=255)
    summery = models.CharField(max_length=255)
    
def __str__(self):
    return self.name

    