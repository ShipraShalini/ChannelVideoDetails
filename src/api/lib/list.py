
from src.common.models.models import videos
from src.common.lib.youtube import youtube_search

def list_video(channelId):
    print channelId
    v = videos.objects.filter(channelId=channelId)
    if not v:
        youtube_search(channelId=channelId)
        v = videos.objects.filter(channelId=channelId)
    return v



