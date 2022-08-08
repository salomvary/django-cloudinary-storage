import django
if django.VERSION[0] >= 4:
    from django.urls import re_path as url
else:
    from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from .views import index

urlpatterns = [
    url(r'^$', index, name='index')
]

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns.append(url(r'^admin/', admin.site.urls))
