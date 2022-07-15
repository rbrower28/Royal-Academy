from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Quiz, QuizAttempt, QuestionAttempt, QuestionOption

# This will list all of the quizzes that have been created
class QuizListView(ListView):
    model = Quiz

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
# This will show the questions of a quiz and allow the user to answer them
def take_quiz(request, id):
    quiz = get_object_or_404(Quiz, id=id)

    template = get_template("quizzes/take_quiz.html")
    return HttpResponse(template.render({"quiz": quiz}, request))

# This will record the user's answers to the quiz
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

# This will show the results of the quiz
def quiz_results(request, id):
    attempt = get_object_or_404(QuizAttempt, id=id)

    template = get_template("quizzes/quiz_results.html")
    return HttpResponse(template.render({"attempt": attempt}, request))