from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

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


def new_topic(request):
    """
    Defines a new topic.

    The new_topic() function receives a request object as a parameter. 
    When the user first requests this page, his browser sends a GET request. 
    When the user has already filled out and submitted the form, his browser sends a POST request. 
    Depending on the type of request, we determine whether the user has requested a 
    blank form (GET request) or offers to process a completed form (POST request).
    """

    if request.method != 'POST':
        # No data was sent; an empty form is created
        form = TopicForm()
    else:
        # POST data sent; data processing
        form = TopicForm(data=request.POST)
        if form.is_valid():  # Sent information cannot be saved in the database until it is verified

            # If all data are valid, you can call the save() method,
            # which writes data from the form to the database
            form.save()

            # A call to redirect the browser to the topics page,
            # where the user where the user will see
            # the topic he/she just entered in the general list of topics
            return redirect('learning_logs:topics')

    # Output a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
