from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals
        from main.tasks import start_job
        start_job()
