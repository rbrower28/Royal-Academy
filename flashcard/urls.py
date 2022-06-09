from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path("", views.FlashcardListView.as_view(), name="flashcard-list")
]
