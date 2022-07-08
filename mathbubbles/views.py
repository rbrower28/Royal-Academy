from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def index(request):
    template = get_template("mathbubbles/index.html")
    return HttpResponse(template.render({"user": request.user}, request))