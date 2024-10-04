from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=255)  # Make sure this field exists
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # store 1, 2, 3, or 4 to indicate the correct option

    def __str__(self):
        return self.question_text


class QuizResult(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    passed = models.BooleanField()
    date = models.DateTimeField(default=timezone.now)  # Ensure this field is correct

    def __str__(self):
        return f'{self.user} - {self.score}'
