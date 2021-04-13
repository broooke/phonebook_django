from django.apps import AppConfig


class SubordinateOrganizationsConfig(AppConfig):
    name = 'subordinate_organizations'
        
    def ready(self):
        from . import signals
