from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Установите значение по умолчанию для переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskproject.settings')

app = Celery('taskproject')

# Здесь мы загружаем настройки из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка задач модулей для зарегистрированных приложений Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)