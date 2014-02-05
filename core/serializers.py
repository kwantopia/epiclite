from core.models import EpicUser
from rest_framework import serializers

class EpicUserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = EpicUser
    fields = ('email', 'first_name', 'last_name')