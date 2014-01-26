from django.db import models

# Create your models here.

class Epic(models.Model):
  # unique ID that is used to identify each epic
  epic_uuid = models.CharField(max_length=64)
  # epic number used to start or create an epic
  epic_num = models.CharField(max_length=6)
  title = models.CharField(max_length=64) 
  description = models.TextField()
  target_day = models.DateField()
  target_time = models.DateTimeField()
  created = models.DateTimeField(auto_now_add=True)