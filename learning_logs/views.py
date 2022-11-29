from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    '''The home page for Learning Log'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    '''"Show all topics'''
    topics = Topic.objects.order_by('date_added')
    # A query to the database for Topic objects sorted by the date_added attribute is issued
    # The context to be passed to the template is defined
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
