from time import sleep

from celery import shared_task


@shared_task
def heavy_process():
    """Emulate heavy cpu or i/o bound operation that takes long time"""
    sleep(10)  # heavy functionality
    return 'Done'
