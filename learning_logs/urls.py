"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]
