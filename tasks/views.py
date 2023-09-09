from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Task, Goal
from .forms import TaskCreateForm, GoalCreateForm

# Create your views here.


def home(request):
    return render(request, template_name='home.html')

def showTasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/show_tasks.html', {'tasks': tasks})

def createTask(request):
    form = TaskCreateForm()
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'task create successfully')
            return redirect(showTasks)
    return render(request, 'tasks/create_task.html', {'form': form})

def createGoal(request):
    form = GoalCreateForm()
    if request.method == 'POST':
        form = GoalCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'goal create successfully')
            return redirect(showTasks)
    return render(request, 'tasks/create_goal.html', {'form': form})
