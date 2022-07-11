from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView
from flashcard.forms import NewDeckForm, AddCard, AddSubject, DeleteFlashcard
from .models import Flashcard, Deck, Subject

class FlashcardListView(ListView):

    model = Flashcard


def flashcards_menu(request):

    decks = Deck.objects.all()

    template = get_template("flashcard/flashcards_menu.html")
    return HttpResponse(template.render({"decks": decks}, request))


def play_flashcards(request, id):  # Also add subject as second argument
    #Deck = get_object_or_404(Deck, id=id)
    # Deck.objects.all()
    deck = get_object_or_404(Deck, id=id)
    flashcards = deck.flashcards.all()

    template = get_template("flashcard/flashcard_game.html")
    return HttpResponse(template.render({"deck": deck, "flashcards": flashcards}, request))


def create_deck(request):

    form = NewDeckForm(request.POST)
    if form.is_valid():
        form.save()
        form = NewDeckForm()

    template = get_template("flashcard/render_form.html")
    return HttpResponse(template.render({"form": form, "value": "Save"}, request))


def create_flashcard(request):

    form = AddCard(request.POST)
    if form.is_valid():
        form.save()
        form = AddCard()

    template = get_template("flashcard/render_form.html")
    return HttpResponse(template.render({"form": form, "value": "Save"}, request))


def create_subject(request):

    form = AddSubject(request.POST)
    if form.is_valid():
        form.save()
        form = AddSubject()

    template = get_template("flashcard/render_form.html")
    return HttpResponse(template.render({"form": form, "value": "Save"}, request))


def delete_flashcard(request):
    

    form = DeleteFlashcard(request.POST)
    if form.is_valid():
        field = form.cleaned_data["front_content"]
        flashcard = Flashcard.objects.get(front_content=field)
        flashcard.delete()        

    template = get_template("flashcard/render_form.html")
    return HttpResponse(template.render({"form": form, "value": "Delete"}, request))
