from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from .docs import upload_file_summary, get_file_summary
from .models import File
from .serializers import UploadFileSerializer, GetFileSerializer


@upload_file_summary
class UploadFileView(ViewSetMixin, CreateAPIView):
    serializer_class = UploadFileSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@get_file_summary
class GetFileListView(ViewSetMixin, ListAPIView):
    queryset = File.objects.all().order_by("-id")
    serializer_class = GetFileSerializer
