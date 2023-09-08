from django.db import models
from django.contrib.admin.models import User
from uuid import uuid4
# Create your models here.
class Task(models.Model):
    IMPORTANCE_TAGS = [
        ('L', 'Low'),
        ('M', 'Middle'),
        ('H', 'High'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    goal = models.ManyToManyField('Goal')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    importance_tag = models.CharField(max_length=1, choices=IMPORTANCE_TAGS)
    
    id = models.CharField(unique=True, ForeignKey=True, default=uuid4, editable=False)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Goal(models.Model):
    IMPORTANCE_TAGS = [
        ('L', 'Low'),
        ('M', 'Middle'),
        ('H', 'High'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    importance_tag = models.CharField(max_length=1, choices=IMPORTANCE_TAGS)
    death_line = models.DateField()
    
    id = models.CharField(unique=True, ForeignKey=True, default=uuid4, editable=False)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
