# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from superapp.apps.tasks.celery_entrypoint import celery_app

__all__ = ('celery_app',)
