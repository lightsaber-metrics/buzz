from rest_framework import serializers
from streams.models import Stream
from .players import PlayerSerializerNoDates

class StreamSerializer(serializers.ModelSerializer):

    player = PlayerSerializerNoDates()
    service = serializers.CharField(source='get_service_display')
    
    class Meta:
        model = Stream
        fields = [
            'name', 'username', 'user_id', 'player', 'stream_id', 'service',
            'is_live', 'start_time', 'end_time', 'link', 'max_viewer_count',
            'thumbnail'
        ]
