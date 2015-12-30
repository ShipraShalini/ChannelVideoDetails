from api.helper.youtubehelper import *

youtube = ytbuildurl()

def add_videos(search_response, channelId):
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == KIND:
            videos.objects.create(
                                videoId = search_result["id"]["videoId"],
                                channelId = channelId,
                                title = search_result["snippet"]["title"],
                                description = search_result["snippet"]["description"]
                                )


def youtube_search(channelId):
  search_response = search_channel(youtube, channelId, nextPageToken=None)
  totalResults = search_response["pageInfo"]["totalResults"]

  if totalResults > MAX_RESULTS:
      resultsPerPage = search_response["pageInfo"]["resultsPerPage"]
      no_of_iterartions = totalResults/resultsPerPage +1
  else:
      no_of_iterartions =1

  for i in range(no_of_iterartions):
      add_videos(search_response=search_response, channelId=channelId)
      try:
        nextPageToken = search_response["nextPageToken"]
      except KeyError:
          pass
      else:
          search_response= search_channel(youtube, channelId, nextPageToken=nextPageToken)
