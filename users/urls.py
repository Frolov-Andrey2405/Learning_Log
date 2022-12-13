"""Defines URL schemes for users"""

from django.urls import path, include
# First the path function is imported and then the include function
# to include the default authentication URLs defined by Django

from . import views

app_name = 'users'
# The app_name variable is set to 'users' so that the Django infrastructure
# can distinguish these URLs from URLs belonging to other applications

urlpatterns = [
    # Turn on the default authorization URL.
    path('', include('django.contrib.auth.urls')),
    # http://localhost:8000/users/login/

    # Registration page
    path('register/', views.register, name='register'),
]
