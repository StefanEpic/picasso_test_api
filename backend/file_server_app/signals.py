from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import File
from .tasks import update_file_process


@receiver(post_save, sender=File)
def notify_about_new_post(sender, instance, created, **kwargs) -> None:
    if created:
        update_file_process(instance.id)
