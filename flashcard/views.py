from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

# Create your views here.

from .models import Flashcard, Deck, Subject

class FlashcardListView(ListView):

    model = Flashcard

def flashcards_menu(request):

    decks = Deck.objects.all()

    template = get_template("flashcard/flashcards_menu.html")
    return HttpResponse(template.render({"decks": decks}, request))

def play_flashcards(request, id): #Also add subject as second argument
    #Deck = get_object_or_404(Deck, id=id)
    #Deck.objects.all()
    deck = get_object_or_404(Deck, id=id)
    flashcards = deck.flashcards.all()
   
    template = get_template("flashcard/flashcard_game.html")
    return HttpResponse(template.render({"deck": deck, "flashcards": flashcards}, request))

def create_deck(request):
    
    template = get_template("flashcard/add_deck.html")
    return HttpResponse(template.render({}, request))
    