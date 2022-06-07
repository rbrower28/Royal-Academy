from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Quiz

class QuizListView(ListView):

    model = Quiz
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def take_quiz(request, id):
    quiz = get_object_or_404(Quiz, id=id)

    template = get_template("quizzes/take_quiz.html")
    return HttpResponse(template.render({"quiz": quiz}, request))

def submit_quiz_attempt(request, id): 
    # quiz = get_object_or_404(Quiz, id=id)

    # TODO - make this save the form submission.
    return HttpResponse("Form handling not yet implemented")


    # template = get_template("quizzes/take_quiz.html")
    # return HttpResponse(template.render({"quiz": quiz}, request))