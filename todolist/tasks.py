from celery import shared_task
import time
import logging
from celery import group


@shared_task
def add(x, y):
    return x + y


@shared_task
def long_task():
    time.sleep(10)
    return 'Task Completed'


logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3)
def divide(self, x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.error(f"Division by zero: {e}")
        raise self.retry(exc=e, countdown=60)
    return result


@shared_task
def process_data(data):
    pass


def process_large_dataset(dataset):
    job = group(process_data.s(chunk) for chunk in dataset)  # Разбиение на подзадачи
    result = job.apply_async()
