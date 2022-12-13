from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    '''Registers a new user'''

    # Checking if a function responds to a POST request
    if request.method != 'POST':

        # Outputs a blank registration form.    
        # If not, an instance of the UserCreationForm is created that does not contain the source data
        form = UserCreationForm()
    else:
        # Processing a completed form. 
        # If a POST request is responded to, an instance of UserCreationForm is created based on the data sent
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            '''
            Data authentication:
            - user name contains correct characters
            - passwords match
            - user does not attempt to insert malicious constructs into the data sent
            '''

            new_user = form.save()
            # If the data sent is correct, we call the save() method of 
            # the form to save the username and password hash to the database

            # Logging in and redirecting to the home page
            login(request, new_user)
            '''
            The login() function is called with the request and new_user objects, 
            which creates a valid session for a new user
            '''

            return redirect('learning_logs:index')
            '''
            The user is redirected to the home page, where the welcome message 
            in the header informs that the registration was successful
            '''

    # Output a blank or invalid form
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
