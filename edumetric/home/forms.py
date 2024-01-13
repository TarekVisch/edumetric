from django import forms
from allauth.account.forms import SignupForm
from .models import User


class RegisterForm(SignupForm):
    role = forms.ChoiceField(required=True, choices=[('student', 'Student'), ('teacher', 'Teacher')])
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    def save(self, request):
        user = super(RegisterForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user
