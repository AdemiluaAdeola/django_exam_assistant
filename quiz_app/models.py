from django.db import models
from blog_app.models import *
from ckeditor.fields import RichTextField

# Create your models here.
class Quiz(models.Model):
    topic = models.ForeignKey(Topics, related_name="quiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="question", on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.quiz.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
    correct = models.BooleanField(default=False, verbose_name='True or False')

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.choice

class PracticeQuestion(models.Model):
    course = models.ForeignKey(Courses, related_name="practice", default=1, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Topics, related_name="practice", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    isverified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Practice Question'
        verbose_name_plural = 'Practice Questions'

    def __str__(self):
        return self.chapter.name