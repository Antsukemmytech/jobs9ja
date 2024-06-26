from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm():
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserLoginForm():
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


