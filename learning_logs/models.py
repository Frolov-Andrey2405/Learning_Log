from django.db import models

# Create your models here.


class Topic(models.Model):
    '''The topic the user is studying.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns a string representation of the model'''
        return self.text


class Entry(models.Model):
    '''Information studied by the user on the topic.'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''The Meta class is embedded in the Entry class. 
        The Meta class stores additional information about the model management'''
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Returns the string representation of the model'''
        return f'{self.text[:50]}...'
