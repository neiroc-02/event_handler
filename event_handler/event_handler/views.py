from rest_framework import viewsets
from .serializers import EventHandlerSerializer
from .models import EventHandler

class EventHandlerViewSet(viewsets.ModelViewSet):
    queryset = EventHandler.objects.all()
    serializer_class = EventHandlerSerializer