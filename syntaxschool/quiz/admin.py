# admin.py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('section', 'question_text', 'correct_answer')  # Columns to display
    list_filter = ('section',)  # Filter by section
    search_fields = ('question_text',)  # Searchable fields
    ordering = ('section',)  # Default ordering

    # Optional: Customize form layout
    fieldsets = (
        (None, {
            'fields': ('section', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
        }),
    )

admin.site.register(Question, QuestionAdmin)
