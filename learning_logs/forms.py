from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    """A class named TopicForm is defined that inherits from forms.ModelForm"""
    class Meta:
        model = Topic  # The form is created based on the Topic model
        fields = ['text']  # and only the text field is placed on it
        labels = {'text': ''} # The code tells Django not to generate a signature for a text field