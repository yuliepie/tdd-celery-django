# Import the Celery app on Django startup
# so that shared_task will use the Celery app
from .celery import app as celery_app

__all__ = ('celery_app',)
