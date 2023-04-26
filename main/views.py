from django.http import HttpResponse

from .tasks import test


def test_request(request):
    test.delay()
    return HttpResponse("Task has been sent to the Celery worker")
