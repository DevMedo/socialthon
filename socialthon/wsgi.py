"""
WSGI config for socialthon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os
import sys

path = '/home/socialthon/socialthon'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'socialthon.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()