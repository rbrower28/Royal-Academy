from django.forms import ModelForm
from django import forms
from .models import Deck, Flashcard, Subject
from django.db import models


class NewDeckForm(ModelForm):

    name = forms.TextInput()
    flashcards = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(), queryset=Flashcard.objects.all())

    class Meta():
        model = Deck
        fields = ["name", "flashcards"]


class AddCard(ModelForm):
    subject = forms.ModelChoiceField(
        widget=forms.Select(), queryset=Subject.objects.all())
    front_content = forms.TextInput()
    back_content = forms.TextInput()

    class Meta():
        model = Flashcard
        fields = ["subject", "front_content", "back_content"]


class AddSubject(ModelForm):
    name = forms.TextInput()

    class Meta():
        model = Subject
        fields = ["name"]


class DeleteFlashcard(ModelForm):

    front_content = forms.ModelChoiceField(
        widget=forms.Select(), queryset=Flashcard.objects.all())

    class Meta():
        model = Flashcard
        fields = ["front_content"]
