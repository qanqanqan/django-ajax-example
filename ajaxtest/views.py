from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Profile


def index(req):
    return render(req, 'ajaxtest/index.html')


# ==================================================
# Getting data with GET method
def show_profiles(req):
    return render(req, 'ajaxtest/profiles.html')


def get_profiles(req):
    profiles = Profile.objects.all()
    return JsonResponse({'profiles': list(profiles.values())})
# ==================================================


# ===================================
# Creating data with POST method
def change_form(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        is_staff = True if req.POST['is_staff'] == 'on' else False

        new_profile = Profile(name=name, enail=email, is_staff=is_staff)
        new_profile.save()

        return HttpResponse('Profile has been created')
    return render(req, 'ajaxtest/form.html')
# ===================================
