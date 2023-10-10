from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from .models import File
from .serializers import UploadFileSerializer, GetFileSerializer


class UploadFileView(ViewSetMixin, CreateAPIView):
    serializer_class = UploadFileSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)

        if status.HTTP_400_BAD_REQUEST:
            return Response(status=400)


class GetFileListView(ViewSetMixin, ListAPIView):
    queryset = File.objects.all().order_by("-id")
    serializer_class = GetFileSerializer
