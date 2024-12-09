from rest_framework import serializers
from .models import EventHandler

class EventHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHandler
        fields = '__all__'