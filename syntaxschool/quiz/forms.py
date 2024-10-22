from django import forms
from .models import *

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for idx, question in enumerate(questions):
            self.fields[f'question_{idx}'] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    (1, question.option_a),
                    (2, question.option_b),
                    (3, question.option_c),
                    (4, question.option_d),
                ],
                widget=forms.RadioSelect
            )
