from celery import Celery, current_app as current_celery_app


def create_celery() -> Celery:
    celery_app = current_celery_app._get_current_object()
    celery_app.config_from_object('celery_app.settings', namespace="CELERY")
    celery_app.conf.update(broker_connection_retry_on_startup=True)
    return celery_app
