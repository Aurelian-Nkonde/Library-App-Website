from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class AdminModel(admin.ModelAdmin):
    list_display = ('city',)