from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """A class named TopicForm is defined that inherits from forms.ModelForm"""
    class Meta:
        model = Topic  # The form is created based on the Topic model
        fields = ['text']  # and only the text field is placed on it
        # The code tells Django not to generate a signature for a text field
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    '''The EntryForm class inherits from forms.ModelForm and 
    contains a nested Meta class specifying the model on which it is based and 
    the field included on the form'''
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {'text': 'Entry:', }
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        