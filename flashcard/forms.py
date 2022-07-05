from django.forms import ModelForm
from django import forms
from .models import Deck, Flashcard
from django.db import models


class NewDeckForm(ModelForm):

    name = forms.TextInput()
    flashcards = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(), queryset=Flashcard.objects.all())

    class Meta():
        model = Deck
        fields = ["name", "flashcards"]
