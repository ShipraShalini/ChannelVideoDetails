from src.common.models.models import videos
from src.common.lib.youtube import youtube_search
from django.http import Http404


def get_video(videoId):
    try:
        return videos.objects.get(videoId=videoId)
    except videos.DoesNotExist:
        raise Http404


