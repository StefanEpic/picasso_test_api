from django.apps import AppConfig


class FileServerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "file_server_app"

    def ready(self) -> None:
        import file_server_app.signals
