'''Defines the URL schemes for learning_logs'''

from django.urls import path  # Necessary to create a URL with views
from . import views  # The dot tells Python to import the views from the directory where the current urls.py module is located

# The app_name variable helps Django to distinguish this urls.py file from files with the same name in other applications in the project
app_name = 'learning_logs'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topics'),

    # Page that shows all topics
    path('topic/', views.topic, name='topics'),
    # We added topics/ to the regular expression argument used with the homepage URL

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Table for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
