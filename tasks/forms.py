from django import forms
from .models import Task, Goal

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'goal', 'user', 'is_completed', 'importance_tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'goal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'importance_tag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GoalCreateForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'user', 'is_completed', 'importance_tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'importance_tag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }