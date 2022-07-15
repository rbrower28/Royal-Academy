
import uuid
from django.contrib.auth.models import User
from django.db import models

# This model will store the name of the quiz
class Quiz(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)

    name = models.CharField(max_length=64, blank=False, null=False, default="")

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)

    class Meta:
        verbose_name_plural = "Quizzes"
    
    def __str__(self):
        return self.name


# This model will store a question that belongs to a quiz
class Question(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)

    quiz = models.ForeignKey(Quiz, blank=False, null=False, on_delete=models.CASCADE)

    title = models.CharField(max_length=256, blank=False, null=False, default="")

    def __str__(self):
        return "Quiz: " + str(self.quiz) + " Question: " + self.title


# This model will store the options for answers that belong to a question
class QuestionOption(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)

    question = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)

    title = models.CharField(max_length=256, blank=False, null=False, default="")

    ordering = models.CharField(max_length=8, blank=False, null=False, default="3")

    correct = models.BooleanField(default=False)

    def __str__(self):
        return 'Answer for ' + str(self.question) + ': ' + self.title


# This model will store the user's attempt to respond to a quiz
class QuizAttempt(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)

    quiz = models.ForeignKey(Quiz, blank=False, null=False, on_delete=models.CASCADE)

    completed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)

    def __str__(self):
        return str(self.quiz) + ' completed by ' + str(self.completed_by) + ' at ' + str(self.timestamp)


# This model will store the user's response to a question on a quiz as part of an attempt
class QuestionAttempt(models.Model):
    id = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)

    attempt = models.ForeignKey(QuizAttempt, blank=False, null=False, on_delete=models.CASCADE)

    question = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE)

    user_response = models.ForeignKey(QuestionOption, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.attempt.completed_by) + ' answered ' + str(self.user_response) + ' on ' + str(self.question)