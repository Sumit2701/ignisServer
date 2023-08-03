from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'data', 'time', 'location', 'image', 'likes', 'username']
        extra_kwargs = {'image': {'required': False}}

    # Explicitly define the data field as a CharField
    data = serializers.CharField(max_length=200, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        event = Event.objects.create(
            event_name=validated_data['event_name'],
            data=validated_data['data'],
            time=validated_data['time'],
            location=validated_data['location'],
            image=validated_data.get('image', None),
            likes=validated_data.get('likes', 0),
            username=validated_data['username']
        )
        return event
