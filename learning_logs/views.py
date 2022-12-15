from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def index(request):
    '''The home page for Learning Log'''
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # A query to the database for Topic objects sorted by the date_added attribute is issued
    # The context to be passed to the template is defined
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""

    topic = Topic.objects.get(id=topic_id)
    # Uses get() to retrieve the topic, just as we did in the Django shell

    # Checks that the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    '''
    If the topic does not belong to the current user, 
    an Http404 exception is thrown, and Django 
    returns page with a 404 error.

    '''

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


@login_required
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


@login_required
def new_entry(request, topic_id):
    '''Adds a new entry on a specific topic.

    new_entry() contains the topic_id parameter to store the value obtained from the URL. 
    The topic_id is needed to display the page and process the form data
    '''

    # For to get the right subject matter
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data was sent; an empty form is created
        form = TopicForm()
    else:
        # POST data sent; data processing
        form = TopicForm(data=request.POST)
        if form.is_valid():  # Sent information cannot be saved in the database until it is verified

            new_entry = form.save(commit=False)
            # When calling save(), we include the commit=False argument to create
            # a new record object and save it to new_entry without saving it to the database yet

            new_entry.topic = topic
            new_entry.save()
            # We assign to the topic attribute of the new_entry object the topic
            # read from the database at the beginning of the function and then call save() without arguments.
            # The result is that the entry is saved in the database database with the correctly associated topic.

            return redirect('learning_logs:topic', topic_id=topic_id)
            # The redirect() call takes two arguments: the name of the view to which control is transferred
            # and the argument for the view function

    # Output a blank or invalid form
    context = {'topic': topic, 'form': form, }
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_edit):
    '''Edits an existing entry'''

    # Getting the object of the of the entry that the user wants to change, and the topic associated with that entry
    entry = Entry.objects.get(id=entry_edit)
    topic = entry.topic

    if topic.owner != request.users:
        raise Http404
    # Whether the topic owner matches the current user; 
    # an Http404 exception is thrown if it does not.

    if request.method != 'POST':
        # Initial query; the form is filled with the data of the current record
        form = EntryForm(instance=entry)
        # The argument tells Django to create a form, pre-filled with information from
        # an existing record object. The user sees his existing data and can edit it.

    else:
        # Send POST data; process the data
        form = EntryForm(instance=entry, data=request.POST)
        # They command Django to create a form instance based on the information of an existing record object,
        # updated with data from request.POST

        if form.is_valid():
            form.save()  # If the data is correct, a call to save() without arguments follows

            # Then the user is redirected to the topic page and sees the updated version of the post he edited
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {
        'entry': entry,
        'topic': topic,
        'form': form,
    }
    return render(request, 'learning_logs/edit_entry.html', context)
