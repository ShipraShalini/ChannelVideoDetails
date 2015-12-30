from src.common.models.models import videos
from src.common.helper.youtubehelper import search_video


def get_video(videoId):
    try:
        return videos.objects.get(videoId=videoId)
    except videos.DoesNotExist:
        print"B"
        search_video(videoId)
        return videos.objects.get(videoId=videoId)


