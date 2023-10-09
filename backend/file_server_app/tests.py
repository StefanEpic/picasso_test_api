from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")


class FileServerApiTestCase(APITestCase):
    def test_file_upload(self) -> None:
        url = "/upload/"
        data = {"file": image}

        response = self.client.post(url, data, format="multipart")

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
