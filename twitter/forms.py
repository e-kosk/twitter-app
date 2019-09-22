from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator

import re

from django.forms import ModelForm

from .models import *


class NewTweetForm(forms.Form):
    content = forms.CharField(max_length=255, label='Treść')


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=64, label='Nazwa')
    first_name = forms.CharField(max_length=64, label='Imię')
    last_name = forms.CharField(max_length=64, label='Nazwisko')
    email = forms.CharField(validators=[EmailValidator, ], max_length=128, label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=64, label="Hasło")
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=64, label="Powtórz hasło")
    