from epics.models import Epic, Device, EpicSubscription
from rest_framework import serializers
from core.serializers import EpicUserSerializer


class EpicSerializer(serializers.HyperlinkedModelSerializer):
  user = EpicUserSerializer()

  class Meta:
    model = Epic
    fields = ('epic_uuid', 'epic_num', 'organizer_id', 'user', 'location', 
            'title', 'description', 'target_day', 'target_time', 'public', 'repeated')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Device
    fields = ('device_id', 'location')

class EpicSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
  epic = EpicSerializer()

  class Meta:
    model = EpicSubscription
    fields = ('epic', 'participant_id', 'user')