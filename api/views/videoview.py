from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from api.lib.getdetail import getvideodetail
from api.serializers.videoserialiser import VideoDetailSerializer


class VideoView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )

    def get(self,request):
        if request.method == 'GET':
            videoId = request.GET.get('videoId', None)
            video_detail = getvideodetail(videoId)
            serializer = VideoDetailSerializer(video_detail)
            return Response(serializer.data)