from epics.models import Epic
from rest_framework import serializers


class EpicSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Epic
    fields = ('epic_uuid', 'epic_num', 'title', 'description', 'target_day', 'target_time')
