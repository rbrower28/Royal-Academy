from django.contrib import admin
from .models import Subject, Flashcard, Deck

# Register your models here.
admin.site.register(Subject)
admin.site.register(Flashcard)
admin.site.register(Deck)
