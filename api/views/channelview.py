from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.serializers.videoserialiser import VideoListSerializer
from api.lib.getdetail import getchanneldetail


class ChannelView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        if request.method == 'GET':
            channelId = request.GET.get('channelId', None)
            video_list= getchanneldetail(channelId)
            serializer = VideoListSerializer(video_list, many=True)
            return Response(serializer.data)
