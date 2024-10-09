from time import sleep

from celery.result import AsyncResult
from django.http import HttpResponse

from users.tasks import heavy_process


# Create your views here.

def index(request):
    result = heavy_process.delay()  # heavy functionality
    return HttpResponse(f'Received {result.id}')


def task_status(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        response = f'Task {task_id} is {result.status}'
    else:
        response = f'Task {task_id} is running'
    return HttpResponse(response)
