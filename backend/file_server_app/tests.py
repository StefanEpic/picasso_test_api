from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from file_server_app.models import File


class FileServerApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.text = SimpleUploadedFile("test_text.doc", b"file_content", content_type="text/doc")
        self.video = SimpleUploadedFile("test_video.avi", b"file_content", content_type="video/avi")
        self.url_upload = reverse("upload-list")
        self.url_get = reverse("files-list")
        self.year = timezone.now().year
        self.month = timezone.now().month
        self.day = timezone.now().day

    def test_valid_image_file_upload(self) -> None:
        data = {"file": self.image}
        response = self.client.post(self.url_upload, data, format="multipart")
        correct_file_path = f"/media/files/images/{self.year}/{self.month}/{self.day}/testimage.jpg"

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["file"], correct_file_path)

        # Test model
        file = File.objects.get(id=1)
        self.assertEqual(file.file.name.split("/")[-1], str(file))

    def test_valid_text_file_upload(self) -> None:
        data = {"file": self.text}
        response = self.client.post(self.url_upload, data, format="multipart")
        correct_file_path = f"/media/files/text/{self.year}/{self.month}/{self.day}/testtext.doc"

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["file"], correct_file_path)

    def test_invalid_audio_file_upload(self) -> None:
        data = {"file": self.video}
        response = self.client.post(self.url_upload, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["file"][0], "Unsupported file extension.")

    def test_get_file_list(self) -> None:
        response = self.client.get(self.url_get)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
