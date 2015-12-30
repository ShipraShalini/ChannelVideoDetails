from src.common.models.models import *
from rest_framework.serializers import ModelSerializer

class VideoSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('videoId', 'title', 'channelId', 'description')

class VideoListSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('title',)