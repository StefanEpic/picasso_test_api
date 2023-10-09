from rest_framework import serializers

from .models import File


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file"]


class GetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file", "uploaded_at", "processed"]
