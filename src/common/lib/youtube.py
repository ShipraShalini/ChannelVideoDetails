#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from src.common.models.models import videos


DEVELOPER_KEY = "AIzaSyCn2HoAL1qpLEFpMZttS7bv71iSS1aFFkI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
KIND = "youtube#video"
MAX_RESULTS =50



def add_videos(search_response, channelId):
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == KIND:
            videos.objects.create(
                                videoId = search_result["id"]["videoId"],
                                channelId = channelId,
                                title = search_result["snippet"]["title"],
                                description = search_result["snippet"]["description"]
                                )



def search(youtube, channelId, nextPageToken=None ):
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




def youtube_search(channelId):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = search(youtube, channelId, nextPageToken=None )


  totalResults = search_response["pageInfo"]["totalResults"]
  if totalResults > MAX_RESULTS:
      resultsPerPage = search_response["pageInfo"]["resultsPerPage"]
      no_of_iterartions = totalResults/resultsPerPage +1
      print "Total Results: ", totalResults
      print "Results Per Page: ", resultsPerPage
      print "No of Iteration : ", no_of_iterartions
  else:
      no_of_iterartions =1


  for i in range(no_of_iterartions):
      add_videos(search_response=search_response, channelId=channelId)
      try:
        nextPageToken = search_response["nextPageToken"]
        print "nextPageToken", nextPageToken
      except KeyError:
          pass
      else:
          search_response= search(youtube,channelId, nextPageToken=nextPageToken )
