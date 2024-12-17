from rest_framework import serializers
from .models import EventHandler

class EventHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHandler
        fields = ['event_type', 'mitre_threat_no', 'description', 'timestamp']  # Only allow fields defined in model
        extra_kwargs = {
            'event_type': {'required': True},
            'mitre_threat_no': {'required': True},
            'description': {'required': True},
            'timestamp': {'required': False} # due to auto now add setting
        }

    def validate(self, data):
        # Reject any extra fields not defined in fields
        extra_fields = set(self.initial_data.keys()) - set(self.fields.keys())
        if extra_fields:
            raise serializers.ValidationError(f"Extra fields not allowed: {extra_fields}")
        return data