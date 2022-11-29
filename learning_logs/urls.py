'''Defines the URL schemes for learning_logs'''

from django.urls import path  # Necessary to create a URL with views
from . import views  # The dot tells Python to import the views from the directory where the current urls.py module is located

# The app_name variable helps Django to distinguish this urls.py file from files with the same name in other applications in the project
app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # We added topics/ to the regular expression argument used with the homepage URL
]
