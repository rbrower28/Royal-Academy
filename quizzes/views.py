from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Quiz, QuizAttempt, QuestionAttempt, QuestionOption

class QuizListView(ListView):
    model = Quiz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# def create_quiz(request):
#     return HttpResponse("Create quiz not yet implemented")
    
def take_quiz(request, id):
    quiz = get_object_or_404(Quiz, id=id)

    template = get_template("quizzes/take_quiz.html")
    return HttpResponse(template.render({"quiz": quiz}, request))

def submit_quiz_attempt(request, id): 
    quiz = get_object_or_404(Quiz, id=id)

    attempt = QuizAttempt.objects.create(quiz=quiz, completed_by=request.user)

    for question in quiz.question_set.all():
        selected_option = QuestionOption.objects.get(id=request.POST[str(question.id)])

        QuestionAttempt.objects.create(
                attempt=attempt,
                question=question,
                user_response=selected_option
                )

    template = get_template("quizzes/quiz_completion_confirmation.html")
    return HttpResponse(template.render({"quiz": quiz, "attempt": attempt}, request))

def quiz_results(request, id):
    attempt = get_object_or_404(QuizAttempt, id=id)

    template = get_template("quizzes/quiz_results.html")
    return HttpResponse(template.render({"attempt": attempt}, request))