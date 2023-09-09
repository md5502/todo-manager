from django.shortcuts import render
from .models import Task, Goal

# Create your views here.


def home(request):
    return render(request, template_name='tasks/home.html')
