from django import forms
from .models import Task, Goal

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'goal', 'user', 'is_completed', 'importance_tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'goal': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'importance_tag': forms.Select(attrs={'class': 'form-control'}),
        }

class GoalCreateForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'user', 'is_completed', 'importance_tag', 'death_line']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input mx-1'}),
            'importance_tag': forms.Select(attrs={'class': 'form-control'}),
            'death_line': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
