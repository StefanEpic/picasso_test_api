from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import File
from .serializers import UploadFileSerializer, GetFileSerializer


class UploadFileViewset(viewsets.ModelViewSet):
    serializer_class = UploadFileSerializer
    http_method_names = ["post", "head", "options"]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)

        if status.HTTP_400_BAD_REQUEST:
            return Response(status=400)


class GetFileListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all().order_by("-id")
    serializer_class = GetFileSerializer
    http_method_names = ["get", "head", "options"]
