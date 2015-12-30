from api.models.models import videos
from api.lib.youtube import youtube_search
from api.helper.youtubehelper import search_video


def getvideodetail(videoId):
    try:
        return videos.objects.get(videoId=videoId)
    except videos.DoesNotExist:
        search_video(videoId)
        return videos.objects.get(videoId=videoId)


def getchanneldetail(channelId):
    print channelId
    v = videos.objects.filter(channelId=channelId)
    if not v:
        youtube_search(channelId=channelId)
        v = videos.objects.filter(channelId=channelId)
    return v
