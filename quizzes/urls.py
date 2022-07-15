from django.urls import path

from . import views

app_name = 'quizzes'

urlpatterns = [
    # base route shows the list of quizzes
    path('', views.QuizListView.as_view(), name='quiz-list'),
    # route for taking a quiz
    path('quiz/<str:id>/take', views.take_quiz, name='take_quiz'),
    # route for submitting a quiz
    path('quiz/<str:id>/submit_attempt', views.submit_quiz_attempt, name='submit_quiz_attempt'),
    # route for showing the results of a quiz
    path('results/<str:id>', views.quiz_results, name='quiz_results'),
]