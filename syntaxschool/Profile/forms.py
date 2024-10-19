# profile/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

