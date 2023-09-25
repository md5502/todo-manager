from django.urls import path

from .views import home, showTasks, createTask, createGoal, editTask, editGoal


urlpatterns = [
    path('', name='home', view=home),
    path('show-tasks/', name='show-tasks', view=showTasks),
    path('create-task/', name='create-task', view=createTask),
    path('edit-task/<str:pk>', name='edit-task', view=editTask),
    path('create-goal/', name='create-goal', view=createGoal),
    path('edit-goal/<str:pk>', name='edit-goal', view=editGoal),
]