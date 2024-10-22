from django.urls import path
from .views import *

urlpatterns = [
      path('quiz/', quiz, name='quiz'),
      path('quiz/<str:language>/', start_quiz, name='start_quiz'),
      path('select-language/', select_language, name='select_language'),
]
