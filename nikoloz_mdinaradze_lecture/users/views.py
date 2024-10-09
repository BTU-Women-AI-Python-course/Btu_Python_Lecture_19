from time import sleep

from django.http import HttpResponse

from users.tasks import heavy_process


# Create your views here.

def index(request):
    heavy_process.delay()  # heavy functionality
    return HttpResponse('Done')
