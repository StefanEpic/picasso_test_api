from celery import shared_task

from file_server_app.models import File


@shared_task
def update_file_process(file_id: int) -> None:
    file = File.objects.get(pk=file_id)
    file.processed = True
    file.save()
