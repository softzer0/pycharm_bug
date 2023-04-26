from celery import Celery

app = Celery('pycharm_bug')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.set_default()