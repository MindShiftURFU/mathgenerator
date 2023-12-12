from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)


@login_required()
def login_test(request):
    return HttpResponse("Закрытая страница")

# Create your views here.
