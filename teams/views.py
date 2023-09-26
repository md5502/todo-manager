from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Team, TeamMember
# Create your views here.

@login_required(login_url='login')
def ShowTeam(request):
    user = request.user

    try:
        teammember = TeamMember.objects.get(member=user)
    except TeamMember.DoesNotExist:
        teammember = None
    if teammember:
        teams = teammember.team
        return render(request, 'teams/show_team.html', {'teams': teams})
    else:
        return render(request, 'teams/show_team.html', {'msg': "you dont have any team"})

   