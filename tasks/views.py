from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'tasks/create_task.html', {'form': form,  'page' : 'create'})

def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if task.user != request.user:
        messages.error(request, "You don't have permission to edit this task.")
        return redirect('home')

    if request.method == 'POST':
        form = TaskCreateForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, "Task has been updated successfully.")
            return redirect('home')
    else:
        form = TaskCreateForm(instance=task)

    return render(request, template_name='tasks/create_task.html', context={'form': form, 'page' : 'edit', 'id':pk })

def createGoal(request):
    form = GoalCreateForm()
    if request.method == 'POST':
        form = GoalCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'goal create successfully')
            return redirect(showTasks)
    return render(request, 'tasks/create_goal.html', {'form': form})

def editGoal(request, pk):
    task = get_object_or_404(Goal, id=pk)
    
    if task.user != request.user:
        messages.error(request, "You don't have permission to edit this task.")
        return redirect('home')

    if request.method == 'POST':
        form = GoalCreateForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, "Task has been updated successfully.")
            return redirect('home')
    else:
        form = GoalCreateForm(instance=task)

    return render(request, template_name='tasks/create_goal.html', context={'form': form, 'page' : 'edit', 'id':pk})
