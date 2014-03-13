from django.contrib.gis.db import models
from django.conf import settings
import gettext
import uuid

_ = gettext.gettext

# Create your models here.

class Epic(models.Model):
  # unique ID that is used to identify each epic
  epic_uuid = models.CharField(max_length=64)

  # organizer info
  organizer_id = models.CharField(max_length=128)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

  # epic info
  title = models.CharField(max_length=64) 
  # epic number used to start or create an epic
  epic_num = models.CharField(max_length=6)
  location = models.PointField(_('Point'), default='POINT(0.0 0.0)')
  address = models.CharField(max_length=128, null=True, blank=True)
  city = models.CharField(max_length=64, null=True, blank=True)
  state = models.CharField(max_length=64, null=True, blank=True)
  zipcode = models.CharField(max_length=16, null=True, blank=True)
  country = models.CharField(max_length=64, null=True, blank=True)
  description = models.TextField()
  target_day = models.DateField()
  target_time = models.DateTimeField()
  public = models.BooleanField(default = True)

  REPEAT_CHOICES = (
    (0, 'One Time'),
    (1, 'Daily'),
    (2, 'Weekly'),
    (3, 'Weekdays'),
    (4, 'MWF'),
    (5, 'TTh'),
    (6, 'Weekends'),
    (7, 'Monthly'),
  )

  repeated = models.IntegerField(choices=REPEAT_CHOICES, default=REPEAT_CHOICES[0][0], blank=True)
  created = models.DateTimeField(auto_now_add=True)

  objects = models.GeoManager()

  def save(self, *args, **kwargs):
    self.epic_uuid = uuid.uuid4()
    super(Epic, self).save(*args, **kwargs)

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
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
  join_location = models.PointField(_('Point'), default='POINT(0.0 0.0)')
  leave = models.DateTimeField(default=None, null=True, blank=True)
  leave_location = models.PointField(_('Point'), default='POINT(0.0 0.0)')
  created = models.DateTimeField(auto_now_add=True)

  objects = models.GeoManager()

