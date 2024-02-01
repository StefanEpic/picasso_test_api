from rest_framework import routers
from django.urls import path, include

from .views import UploadFileView, GetFileListView

router = routers.DefaultRouter()
router.register(r"upload", UploadFileView, basename="upload")
router.register(r"files", GetFileListView, basename="files")


urlpatterns = [
    path("", include(router.urls)),
]
