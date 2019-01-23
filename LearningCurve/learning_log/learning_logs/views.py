from django.shortcuts import render

# Create your views here.
def home(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/home.html')

