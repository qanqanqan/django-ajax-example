from django.shortcuts import render
from django.http import JsonResponse

from .models import Profile


def index(req):
    return render(req, 'ajaxtest/index.html')


def get_profiles(req):
    profiles = Profile.objects.all()
    return JsonResponse({'profiles': list(profiles.values())})
