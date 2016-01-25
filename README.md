#ChannelVideoDetails

Using:
- django
- django Rest Framework
- Python YouTube API client
- MySQL

Please update DEVELOPER_KEY in api/constants/backendconstants.py


####Videos
Displays the Following details of Video for a given videoId:  
- title  
- videoId  
- description  

**For video details:**  
    GET http://localhost:8000/video?id=videoId

####Channels
Displays a list of all the videos in a channel for a given channelId.
  
**For list of videos in a Channel:**  
    GET http://localhost:8000/channel?id=channelId
    

