from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for idx, question in enumerate(questions):
            self.fields[f'question_{idx}'] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    (1, question.option_1),
                    (2, question.option_2),
                    (3, question.option_3),
                    (4, question.option_4)
                ],
                widget=forms.RadioSelect
            )
