from django.contrib import admin

from .models import Quiz,Question,QuestionOption,QuizAttempt,QuestionAttempt

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(QuizAttempt)
admin.site.register(QuestionAttempt)