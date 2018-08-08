import os

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ace.settings")

application = get_wsgi_application()
if not os.environ.get('DEBUG'):
    application = DjangoWhiteNoise(application)
