import os

from django.utils import timezone
from pytils.translit import slugify


def get_dir_name_by_extension(extension: str) -> str:
    """
    Create dir name by extension
    """
    image_extensions = [".jpg", ".jpeg", ".png"]
    text_extensions = [".pdf", ".doc", ".docx"]
    dir_name = "unsorted"
    if extension in image_extensions:
        dir_name = "images"
    elif extension in text_extensions:
        dir_name = "text"
    return dir_name


def get_sorted_slug_path_by_file_extension(filename: str) -> str:
    """
    Get slugged path by file extension
    """
    name, extension = os.path.splitext(filename)
    transliterated_name = slugify(name)
    new_filename = f"{transliterated_name}{extension}"
    year = timezone.now().year
    month = timezone.datetime.now().month
    day = timezone.datetime.now().day
    dir_name = get_dir_name_by_extension(extension)
    path = "".join([f"files/{dir_name}/{year}/{month}/{day}/", new_filename])
    return path
