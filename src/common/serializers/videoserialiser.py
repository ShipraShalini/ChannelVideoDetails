from src.common.models.models import *
from rest_framework.serializers import ModelSerializer

class VideoDetailSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('videoId', 'title', 'description')

class VideoListSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('title',)