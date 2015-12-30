from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from src.common.serializers.videoserialiser import *
from src.api.lib.list import list_video



class listview(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        if request.method == 'GET':
            channelId = request.GET.get('channelId', None)
            video_list= list_video(channelId)
            serializer = VideoListSerializer(video_list, many=True)
            return Response(serializer.data)






