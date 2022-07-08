from django.urls import path

from . import views

app_name = 'mathbubbles'

urlpatterns = [
    path("", views.index, name="game"),
]
