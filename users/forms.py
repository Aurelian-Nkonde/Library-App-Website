from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('lastName', 'location')


class CustomChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('lastName', 'location')