from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    leaders = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    id = models.CharField(max_length=255, unique=True, primary_key=True, default=uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)