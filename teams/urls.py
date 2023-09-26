from django.urls import path
from .views import show_team, create_team

urlpatterns = [
    path('my-team', view=show_team, name='show-team'),
    path('create-team', view=create_team, name='create-team'),
]