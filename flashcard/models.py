from django.db import models
import uuid

# Create your models here.


class Subject(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,  # Generates unique id
                          editable=False)

    name = models.CharField(max_length=64, blank=False, null=False, default="")

    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(
        auto_now_add=True, db_index=True, editable=False)

    # change default plural name
    # class Meta:
    #     verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class Flashcard(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,  # Generates unique id
                          editable=False)
    
    
    # models.do_nothing leaves the cards undeleted.
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(
        auto_now_add=True, db_index=True, editable=False)

    front_content = models.CharField(
        max_length=200, blank=False, null=False, default="")

    back_content = models.CharField(
        max_length=200, blank=False, null=False, default="")

    def __str__(self):
        return str(self.front_content)


class Deck(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=30, blank=False, null=False, default="")

    flashcards = models.ManyToManyField(Flashcard)

    def __str__(self):
        return str(self.name)
