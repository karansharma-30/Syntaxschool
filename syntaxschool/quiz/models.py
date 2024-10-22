# models.py
from django.db import models

class Question(models.Model):
    SECTION_CHOICES = [
        ('python', 'Python'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('javascript', 'JavaScript'),
    ]
    
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)  # Assuming A, B, C, or D

    def __str__(self):
        return f"{self.section} - {self.question_text[:50]}..."

