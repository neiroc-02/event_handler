from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from .models import EventHandler
from .serializers import EventHandlerSerializer

class EventHandlerViewSet(viewsets.ModelViewSet):
    queryset = EventHandler.objects.all()
    serializer_class = EventHandlerSerializer

    @action(detail=False, methods=['get'], url_path='(?P<start>[^/.]+)/(?P<end>[^/.]+)')
    def filter_events(self, request, start=None, end=None):
        # Parse the start and end datetime strings
        start_dt = parse_datetime(start)
        end_dt = parse_datetime(end)

        # Validate the parsed datetimes
        if not start_dt or not end_dt:
            return Response(
                {"error": "Invalid datetime format. Use YYYY-MM-DDTHH:MM:ss."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if timezone.is_naive(start_dt):
            start_dt = timezone.make_aware(start_dt, timezone.get_current_timezone())
        if timezone.is_naive(end_dt):
            end_dt = timezone.make_aware(end_dt, timezone.get_current_timezone())

        # Filter events based on the timestamp field
        filtered_events = EventHandler.objects.filter(timestamp__range=[start_dt, end_dt])
        serializer = self.get_serializer(filtered_events, many=True)
        return Response(serializer.data)
