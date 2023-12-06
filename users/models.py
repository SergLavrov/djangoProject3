from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=25, default='')
    address = models.CharField(max_length=50)
