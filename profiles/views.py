from django.shortcuts import render
# from django.decorators import loginRequired
from .models import Profile


def profile(request, *args, **kwargs):
    if request.method == "GET":
        profile = Profile.objects.all()
        context = {
            'profile': profile
        }
        return render(request, 'profile.html', context=context)