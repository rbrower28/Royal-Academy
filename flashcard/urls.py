from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path("", views.FlashcardListView.as_view(), name="flashcard-list"),
    path("flashcard-menu", views.flashcards_menu, name="flashcard-menu"),
    path("play/<str:id>", views.play_flashcards, name="play_flashcards"),
]
