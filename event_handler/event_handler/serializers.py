from rest_framework import serializers
from .models import EventHandler

'''
This is the serializer class converts between the Django Model and JSON 
It defines the exact arguments we expect and requires them.
It will also validate that we have the correct number of entries. 
'''
class EventHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHandler
        # This defines the allowed fields in the model and assigns all of them as required to reject
        # requests that don't conform to the JSON format.
        fields = ['event_type', 'mitre_threat_no', 'description', 'timestamp']  
        extra_kwargs = {
            'event_type': {'required': True},
            'mitre_threat_no': {'required': True},
            'description': {'required': True},
            'timestamp': {'required': True} 
        }

    # The validate function verfies that the incoming data has the correct set of fields
    def validate(self, data):
        extra_fields = set(self.initial_data.keys()) - set(self.fields.keys())
        if extra_fields:
            raise serializers.ValidationError(f"Extra fields not allowed: {extra_fields}")
        return data