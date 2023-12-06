from django.urls import path
from profiles.views import add_profile

urlpatterns = [
    path('add/', add_profile, name='add_profile')
]
