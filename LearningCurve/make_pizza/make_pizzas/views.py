from django.shortcuts import render
from django.contrib.admin.models import LogEntry, ADDITION,CHANGE,DELETION

# Create your views here.

def index(request):
    return render(request, 'make_pizzas/index.html')

# This "templates" folder must be proprietary 专有 term,