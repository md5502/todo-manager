from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid4, editable=False)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username