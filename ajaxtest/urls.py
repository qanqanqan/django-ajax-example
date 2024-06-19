from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('get-profiles/', get_profiles, name='get_profiles'),

]
