from rest_framework.serializers import ModelSerializer

from api.models.models import *


class VideoDetailSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('videoId', 'title', 'description')

class VideoListSerializer(ModelSerializer):
    class Meta:
        model = videos
        fields = ('title',)