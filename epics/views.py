from django.shortcuts import render
from rest_framework import viewsets
from epics.models import Epic
from epics.serializers import EpicSerializer


# Create your views here.
class EpicViewSet(viewsets.ModelViewSet):
  queryset = Epic.objects.all()
  serializer_class = EpicSerializer

  @link
  def public_epics(self, request):
    # TODO: need to restrict within geographical limits
    public_epics = Epic.objects.filter(public=True):
    return Response(public_epics)

  @link
  def active_epics(self, request):
    # TODO: need to restrict by epics that you have subscribed to 
    active_epics = EpicSubscription.objects.filter() 
    return Response()

  @action
  def join_epic(self, request, epic_num):
    # TODO: need to find an epic with epicnum in current geographical area
    epic = Epic.objects.get(epic_num=epic_num)
    if request.user:
      EpicSubscription(epic, participant_id=request.session['device_id'], user=request.user)
    else:
      EpicSubscription(epic, participant_id=request.session['device_id'])
    return Response()

  @api_view(['GET', 'POST'])
  def start_epic(self, request):
    if request.method == 'GET':
      return Response() 
    elif request.method == 'POST':
    return Response()

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
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)