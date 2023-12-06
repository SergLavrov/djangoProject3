from django.db import models

# Create your models here.

class Tasks(models.Model):
    task_name = models.CharField(max_length=25)
    number = models.CharField(max_length=25)
    execute_time = models.IntegerField(default=0)
