from django.db import models

# Create your models here.


class SignUp(models.Model):
    username = models.CharField(max_length=15)
    email_id = models.EmailField()
