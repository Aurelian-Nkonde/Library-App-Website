from django import forms
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy

user = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    email = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]