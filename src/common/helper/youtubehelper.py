from src.common.constants.constants import *
from apiclient.discovery import build
from src.common.models.models import videos
def ytbuildurl():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

def search_channel(youtube, channelId, nextPageToken=None):
    if nextPageToken:
        search_response= youtube.search().list(
            channelId=channelId,
            part="id,snippet",
            pageToken=nextPageToken,
            maxResults=MAX_RESULTS
          ).execute()
    else:
        search_response = youtube.search().list(
        channelId=channelId,
        part="id,snippet",
        maxResults=MAX_RESULTS
        ).execute()
    return search_response



def search_video(videoId):
    youtube = ytbuildurl()
    search_response= youtube.search().list(
            q=videoId,
            part="id,snippet"
          ).execute()
    search_result = search_response.get("items", [])[0]

    video = videos.objects.create(
                                videoId = videoId,
                                channelId = search_result["snippet"]["channelId"],
                                title = search_result["snippet"]["title"],
                                description = search_result["snippet"]["description"])


    return video




