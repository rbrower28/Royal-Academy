# Generated by Django 4.0.1 on 2022-06-02 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=256)),
                ('ordering', models.CharField(default='3', max_length=8)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAttempt',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quizattempt')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.question')),
                ('user_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.questionoption')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz'),
        ),
    ]
