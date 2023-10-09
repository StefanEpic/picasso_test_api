import datetime
import os

from django.db import models
from pytils.translit import slugify


class File(models.Model):
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def get_slug_name(self, filename: str) -> str:
        name, extension = os.path.splitext(filename)
        transliterated_name = slugify(name)
        new_filename = f"{transliterated_name}{extension}"
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        path = "".join([f"files/{year}/{month}/{day}/", new_filename])
        return path

    def __str__(self) -> str:
        filename = self.file.name.split("/")[-1]
        return filename

    file = models.FileField(upload_to=get_slug_name, max_length=40, verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время загрузки")
    processed = models.BooleanField(default=False, verbose_name="Обработан")
