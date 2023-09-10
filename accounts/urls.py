from django.urls import path
from .views import loginUser, logoutUser, registerUser

urlpatterns = [
    path('login/', view=loginUser, name='login'),
    path('register/', view=registerUser, name='register'),
    path('logout/', view=logoutUser, name='logout'),
]