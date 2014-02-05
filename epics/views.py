from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, link, action, renderer_classes
from epics.models import Epic, EpicSubscription
from epics.serializers import EpicSerializer, DeviceSerializer, EpicSubscriptionSerializer
from rest_framework.renderers import JSONRenderer, YAMLRenderer
import random

# Create your views here.
class EpicViewSet(viewsets.ModelViewSet):
  queryset = Epic.objects.all()
  serializer_class = EpicSerializer

  # retrieve needs a decorator that approves the user because
  # the user is looking at epic they created or joined.  Also
  # for searching public Epic

@api_view(['POST'])
def app_opened(request):
  # TODO: register device id

  if request.method == 'POST':
    serializer = DeviceSerializer(data=request.DATA)
    if serializer.is_valid():
      serializer.save()
      request.session['device_id'] = serializer.data['device_id']
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def active_epics(request):
  # TODO: need to restrict by epics that you have subscribed to 
  if request.method == 'POST':
    active_epics = EpicSubscription.objects.filter(participant_id=request.DATA['device_id']) 
    return Response(EpicSubscriptionSerializer(active_epics, many=True).data)

@api_view(['GET'])
def join_epic(request, epic_num):
  # TODO: need to find an epic with epicnum in current geographical area
  epic = Epic.objects.get(epic_num=epic_num)
  if not epic:
    return Response({"Error": "No epic found"})
  if request.user.is_anonymous():
    subscription, created = EpicSubscription.objects.get_or_create(epic=epic, 
                                      participant_id=request.session['device_id'],
                                      join_location=request.DATA['location'])
  else:
    subscription, created = EpicSubscription.objects.get_or_create(epic=epic, 
                                      participant_id=request.session['device_id'], 
                                      join_location=request.DATA['location'],
                                      user=request.user)
  return Response(EpicSubscriptionSerializer(subscription).data)


@api_view(['GET'])
def public_epics(request):
  # TODO: need to restrict within geographical limits
  public_epics = Epic.objects.filter(public=True)
  return Response(EpicSerializer(public_epics, many=True).data)

@api_view(['GET', 'POST'])
def start_epic(request):
  if request.method == 'GET':
    # generate a random 4 digit number that is not in current geography
    epic_num = random.randint(1000, 9999)
    return Response(JSONRenderer().render({"epic_num": epic_num})) 
  elif request.method == 'POST':
    serializer = EpicSerializer(data=request.DATA)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def leave_epic(request, epic_id=None):
  subscription = EpicSubscription.objects.filter(epic__id=epic_id, participant_id=request.session['device_id'])
  if subscription.exists():
    # this is an epic I am subscribed to so now leaving
    my_subscription = subscription[0]
    my_subscription.leave = datetime.now() 
    my_subscription.leave_location = request.DATA['location']
    my_subscription.save()
    return Response(EpicSubscriptionSerializer(my_subscription).data)
  return Response({'Error': 'Not subscribed to {0}'.format(epic_id)}, status=status.HTTP_400_BAD_REQUEST)
 


