from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomChangeForm, CustomCreationForm

@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    admin = CustomUser
    list_display = ('username', 'lastName', 'email')