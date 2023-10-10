from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from .views import UploadFileView, GetFileListView

router = routers.DefaultRouter()
router.register(r"upload", UploadFileView, basename="upload")
router.register(r"files", GetFileListView, basename="files")


urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
