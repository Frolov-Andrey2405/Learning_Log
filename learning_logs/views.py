from django.shortcuts import render

# Create your views here.

def index(request):
    '''Learning Log Homepage'''
    return render(request, 'Learning_logs/index.html')
    