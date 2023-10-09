from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from .views import UploadFileViewset, GetFileListViewset

router = routers.DefaultRouter()
router.register(r"upload", UploadFileViewset, basename="upload")
router.register(r"files", GetFileListViewset, basename="files")


urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
