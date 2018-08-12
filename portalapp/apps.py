from __future__ import unicode_literals

from django.apps import AppConfig


class PortalappConfig(AppConfig):
    name = 'portalapp'

    def ready(self):
        import portalapp.signals
