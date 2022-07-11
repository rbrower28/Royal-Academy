from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path("", views.FlashcardListView.as_view(), name="flashcard-list"),
    path("flashcard-menu", views.flashcards_menu, name="flashcard-menu"),
    path("play/<str:id>", views.play_flashcards, name="play_flashcards"),
    path("add-deck", views.create_deck, name="create_deck"),
    path("add-flashcard", views.create_flashcard, name="create_flashcard"),
    path("add-subject", views.create_subject, name="create_subject"),
    path("delete-flashcard", views.delete_flashcard, name="delete_flashcard")
]
