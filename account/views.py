from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm


class RegisterUser(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"