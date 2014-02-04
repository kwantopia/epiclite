from django.contrib.gis.db import models
from django.conf import settings
import gettext

_ = gettext.gettext

# Create your models here.

class Epic(models.Model):
  # unique ID that is used to identify each epic
  epic_uuid = models.CharField(max_length=64)

  # organizer info
  organizer_id = models.CharField(max_length=128)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

  # epic info
  title = models.CharField(max_length=64) 
  # epic number used to start or create an epic
  epic_num = models.CharField(max_length=6)
  location = models.PointField(_('Point'), default='POINT(0.0 0.0)')
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

  objects = models.GeoManager()


class Device(models.Model):
  # device unique ID, for logging when device connects 
  device_id = models.CharField(max_length=128, db_index=True)
  location = models.PointField(_('Point'), default='POINT(0.0 0.0)')
  connected = models.DateTimeField(auto_now_add=True)

  objects = models.GeoManager()


class EpicSubscription(models.Model):
  epic = models.ForeignKey(Epic)
  # device id of participant
  participant_id = models.CharField(max_length=128, db_index=True)
  # user entry might never have been created yet until registration
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
  created = models.DateTimeField(auto_now_add=True)


