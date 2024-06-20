from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),

    # Getting data with GET method
    path('profiles/', show_profiles, name='profiles'),
    path('get-profiles/', get_profiles, name='get_profiles'),

    # Creating data with POST method
    path('change-form/', change_form, name='change_form')
]
