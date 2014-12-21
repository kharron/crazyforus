import os, sys
sys.path.append('/www/sites/crazyforus.com')
os.environ['DJANGO_SETTINGS_MODULE'] = 'crazyforus.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
