from django.shortcuts import render
from rest_framework.response import Response

from .models import events
from .serializers import eventsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def eventlist(request):
    Event = events.objects.all()
    serializer = eventsSerializer(Event, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def eventcreate(request):
    serializer = eventsSerializer(data=request.data)
    if (serializer.is_valid()) :
        serializer.save()
    return Response(serializer.data)
