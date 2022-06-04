from django.urls import path

from . import views

app_name = 'quizzes'

urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz/<str:id>/take', views.take_quiz, name='take_quiz'),
    path('quiz/<str:id>/submit_attempt', views.submit_quiz_attempt, name='submit_quiz_attempt')
]