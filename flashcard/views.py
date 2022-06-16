from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

# Create your views here.

from .models import Flashcard, Deck, Subject

class FlashcardListView(ListView):

    model = Flashcard

def play_flashcards(request, subject):
    Deck = get_object_or_404(Deck, subject=subject)
    
    template = get_template("flashcard/flashcard_game.html")
    return HttpResponse(template.render({"deck": Deck}, request))


