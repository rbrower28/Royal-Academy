from re import L
from django.shortcuts import render

# from django.views.generic import ListView

# Create your views here.


def index(request):
    return render(request, 'typer/index.html')


"""
class IndexView(ListView):
    template_name = "typer/index.html"
    model = HighScore
    ordering = ["-score"]
    context_object_name = "scores"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:10]
        return data
"""

def test(request):
    return render(request, 'typer/test.html')