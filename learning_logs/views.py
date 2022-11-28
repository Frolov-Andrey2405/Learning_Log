from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    '''Learning Log Homepage'''
    return render(request, 'Learning_logs/index.html')

def topics(request):
    '''Выводит список тем'''
    topics = Topic.objects.order_by('date_added') # A query to the database for Topic objects sorted by the date_added attribute is issued
    context = {'topics': topics} # The context to be passed to the template is defined
    return render(request, 'Learning_logs/index.html', {context})
