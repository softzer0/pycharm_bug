from time import sleep

from celery import shared_task


@shared_task()
def test():
    sleep(4)  # Simulate expensive operation(s) that freeze Django
    print("DONE")