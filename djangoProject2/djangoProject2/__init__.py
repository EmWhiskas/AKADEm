from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'djangoProject2'

    def ready(self):
        import djangoProject2.signals