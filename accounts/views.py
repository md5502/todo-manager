from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import CustomUserCreationForm

def loginUser(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.warning(request, "Username does not exist.")
            return redirect('login')
        
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            messages.success(request, "You're logged in.")
            return redirect('home')
        else:
            messages.warning(request, "Username or password is incorrect.")
    
    return render(request, template_name='accounts/login-register.html', context={'page': 'login'})

def logoutUser(request):
    logout(request=request)
    messages.success(request, "You're logged out.")
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            messages.success(request, 'The user account was created.')
            return redirect('home')
        else:
            messages.warning(request, 'An error occurred during registration.')
    else:
        form = CustomUserCreationForm()

    return render(request, template_name='accounts/login-register.html', context={'page': 'register', 'form': form})