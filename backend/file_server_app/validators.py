import os
from django.core.exceptions import ValidationError
from django.db.models import FileField
from django.utils.translation import gettext as _


def validate_file_extension(value: FileField) -> None:
    """
    Checking valid extensions
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".doc", ".docx", ".jpg", ".jpeg", ".png"]
    if not ext.lower() in valid_extensions:
        raise ValidationError(_("Unsupported file extension."), code="invalid", params={"value": value})
