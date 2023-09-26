from django.urls import path
from .views import ShowTeam

urlpatterns = [
    path('my-team', view=ShowTeam, name='show-team'),
]