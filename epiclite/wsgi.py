"""
WSGI config for epiclite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epiclite.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

application = Cling(MediaCling(get_wsgi_application()))
