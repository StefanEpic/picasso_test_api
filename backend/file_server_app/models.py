from django.db import models
from file_server_app.utils import get_sorted_slug_path_by_file_extension
from file_server_app.validators import validate_file_extension


class File(models.Model):
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def get_file_path(self, filename: str) -> str:
        """
        Convert filename to slug format and split by extensions
        """
        path = get_sorted_slug_path_by_file_extension(filename)
        return path

    def __str__(self) -> str:
        filename = self.file.name.split("/")[-1]
        return filename

    file = models.FileField(
        upload_to=get_file_path, max_length=40, validators=[validate_file_extension], verbose_name="Файл"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время загрузки")
    processed = models.BooleanField(default=False, verbose_name="Обработан")
