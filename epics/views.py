from django.shortcuts import render
from rest_framework import viewsets
from epics.models import Epic
from epics.serializers import EpicSerializer


# Create your views here.
class EpicViewSet(viewsets.ModelViewSet):
  queryset = Epic.objects.all()
  serializer_class = EpicSerializer
