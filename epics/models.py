from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class EpicUser(AbstractBaseUser):
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = EpicUserManager()

  USERNAME_FIELD = 'email'


class Epic(models.Model):
  # unique ID that is used to identify each epic
  epic_uuid = models.CharField(max_length=64)

  # organizer info
  organizer_id = models.CharField(max_length=128)
  user = models.ForeignKey(EpicUser, null=True)

  # epic info
  title = models.CharField(max_length=64) 
  # epic number used to start or create an epic
  epic_num = models.CharField(max_length=6)
  lon = models.FloatField()
  lat = models.FloatField() 
  description = models.TextField()
  target_day = models.DateField()
  target_time = models.DateTimeField()
  public = models.BooleanField(default = False)

  REPEAT_CHOICES = (
    (0, 'Daily'),
    (1, 'Weekly'),
    (2, 'Weekdays'),
    (3, 'MWF'),
    (4, 'TTh'),
    (5, 'Weekends'),
    (6, 'Monthly'),
  )

  repeated = models.IntegerField(choices=REPEAT_CHOICES, default=REPEAT_CHOICES[0][0])
  created = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
  # device unique ID, for logging when device connects 
  device_id = models.CharField(max_length=128, db_index=True)
  lon = models.FloatField()
  lat = models.FloatField()
  connected = models.DateTimeField(auto_now_add=True)

class EpicSubscription(models.Model):
  epic = models.ForeignKey(Epic)
  # device id of participant
  participant_id = models.CharField(max_length=128, db_index=True)
  # user entry might never have been created yet until registration
  user = models.ForeignKey('EpicUser', null=True)
  created = models.DateTimeField(auto_now_add=True)

