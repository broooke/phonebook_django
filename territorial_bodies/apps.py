from django.apps import AppConfig


class TerritorialBodiesConfig(AppConfig):
    name = 'territorial_bodies'
    
    def ready(self):
        from . import signals
