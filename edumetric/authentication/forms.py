from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    role = forms.RadioSelect()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["role", "username", "email", "password", "password2"]