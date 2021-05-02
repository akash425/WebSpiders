from django.db import models
from django.urls import reverse
# Create your models here.

class Resume(models.Model):
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)
    address =  models.TextField()
    
    def get_absolute_url(self):
        return reverse("resume:list")
    
