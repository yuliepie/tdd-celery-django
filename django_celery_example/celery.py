"""
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_celery_example.settings')

# Create celery application
app = Celery("django_celery_example")

# read config from Django settings.
# django settings prefixed with `CELERY` would be used
# to config Celery app.
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# Define a task!
@app.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y
