from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import EventHandlerSerializer
from .models import EventHandler

class EventHandlerViewSet(viewsets.ModelViewSet):
    queryset = EventHandler.objects.all()
    serializer_class = EventHandlerSerializer

    #TODO: Finish this handler for filtering GET requests by start/end date
    @action(detail=False, methods=['get'], url_path='(?P<start>[^/.]+)/(?P<end>[^/.]+)')
    def filter_events(self, request, start=None, end=None):
        pass
