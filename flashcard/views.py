from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

# Create your views here.

from .models import Flashcard

class FlashcardListView(ListView):

    model = Flashcard

def play_flashcards(request, subject):
    pass


