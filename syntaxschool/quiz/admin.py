from django.contrib import admin
from .models import Question, QuizResult

# Customize how Question is displayed in the admin panel
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option')
    search_fields = ['question_text']
    list_filter = ['correct_option']

# Customize how QuizResult is displayed in the admin panel
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'passed', 'date')
    search_fields = ['user']
    list_filter = ['passed', 'date']

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
