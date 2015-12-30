from rest_framework.views import APIView
from rest_framework import generics
from rest_framework  import mixins
from rest_framework import permissions
from rest_framework.response import Response
from src.common.serializers.videoserialiser import *
from src.api.lib.details import get_video

class detailsview(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )

    def get(self,request):
        if request.method == 'GET':
            videoId = request.GET.get('videoId', None)
            video_detail = get_video(videoId)
            serializer = VideoDetailSerializer(video_detail)
            return Response(serializer.data)