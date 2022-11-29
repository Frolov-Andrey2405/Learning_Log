from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    '''The home page for Learning Log'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    # A query to the database for Topic objects sorted by the date_added attribute is issued
    # The context to be passed to the template is defined
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""

    topic = Topic.objects.get(id=topic_id)
    # Uses get() to retrieve the topic, just as we did in the Django shell

    entries = topic.entry_set.order_by('-date_added')
    # At we get the entries associated with this topic,
    # and we order them according to date_added.
    # The minus sign in front of date_added sorts the
    # results in reverse order, which will display the most
    # recent entries first

    context = {
        'topic': topic,
        'entries': entries,
    }
    # We store the topic and entries in the context dictionary

    return render(request, 'learning_logs/topic.html', context)
    # Send context to the template topic.html
