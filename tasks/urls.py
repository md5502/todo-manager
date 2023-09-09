from django.urls import path

from .views import home, showTasks, createTask, createGoal


urlpatterns = [
    path('', name='home', view=home),
    path('show-tasks/', name='show-tasks', view=showTasks),
    path('create-task/', name='create-task', view=createTask),
    path('create-goal/', name='create-goal', view=createGoal),
]