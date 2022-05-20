from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):

    return render(request, 'home/index.html')

    # returns the html file found at
    # 'academy/home/templates/home/index.html'

    # Django searches through every folder called
    # 'templates' to find the page requested

    # putting html files in a subfolder with the same
    # name as the module will keep index files separate