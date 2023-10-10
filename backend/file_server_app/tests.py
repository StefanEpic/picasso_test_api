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
        self.assertEqual(1, len(response.data))

    def test_get_file_list(self) -> None:
        url = "/files/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
