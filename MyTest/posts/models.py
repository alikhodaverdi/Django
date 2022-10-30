from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Post(models.Model) : 
    title = models.CharField(max_length=255)
    summery = models.CharField(max_length=255)
    
    last_updated_on = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    
    
def __str__(self):
    return self.name

    