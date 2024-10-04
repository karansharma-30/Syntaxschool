import random
import time
from django.shortcuts import render
from .models import Question, QuizResult
from .forms import QuizForm

def quiz_view(request):
    total_questions = Question.objects.count()  # Count the number of questions in the database

    if total_questions < 10:
        num_questions = total_questions  # Adjust to available questions
    else:
        num_questions = 10  # Use 10 questions if enough are available

    if request.method == 'POST':
        question_ids = request.session['questions']  # Get question IDs from session
        questions = Question.objects.filter(id__in=question_ids)  # Retrieve Question objects
        form = QuizForm(request.POST, questions=questions)  # Pass Question objects to the form

        if form.is_valid():
            score = 0
            for idx, question in enumerate(questions):
                user_answer = int(form.cleaned_data.get(f'question_{idx}'))
                if user_answer == question.correct_option:
                    score += 1

            passed = score >= 6
            username = request.user.username if request.user.is_authenticated else "Anonymous"
            result = QuizResult(user=username, score=score, passed=passed)
            result.save()
            return render(request, 'quiz_result.html', {'score': score, 'passed': passed})

    else:
        # Select random questions
        questions = random.sample(list(Question.objects.all()), num_questions)
        question_ids = [q.id for q in questions]  # Store only question IDs in session
        request.session['questions'] = question_ids  # Store question IDs in session
        request.session['start_time'] = time.time()  # Store quiz start time

        form = QuizForm(questions=questions)  # Pass Question objects to the form

    return render(request, 'quiz.html', {'form': form})
