# views.py
from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def quiz(request):
    if request.method == 'POST':
        answers = request.POST.getlist('answers')
        score = sum(1 for answer in answers if answer == 'correct')
        result = 'Pass' if score >= 22 else 'Fail'
        return render(request, 'certificate/result.html', {'score': score, 'result': result})

    return render(request, 'certificate/select_language.html')

@login_required
def start_quiz(request, language):
    questions = Question.objects.filter(section=language)
    return render(request, 'certificate/quiz.html', {'questions': questions})
def select_language(request):
    # Your logic here
    return render(request, 'certificate/select_language.html')