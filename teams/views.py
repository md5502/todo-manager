from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Team, TeamMember
from .forms import CreateTeamForm

@login_required(login_url='login')
def show_team(request):
    user = request.user

    team_member = get_team_member(user)

    if team_member:
        team = team_member.team
        team_leaders = get_team_leaders(team)
        return render(request, 'teams/show_team.html', {'team': team, 'team_leaders': team_leaders})
    else:
        return render(request, 'teams/show_team.html', {'msg': "You don't have any team"})

@login_required(login_url='login')
def create_team(request):
    user = request.user
    form = CreateTeamForm()

    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.creator = user
            team.save()
            create_team_member(team, user, is_leader=True)
            messages.success(request, 'Team created successfully')
            return redirect('home')

    return render(request, 'teams/create-team.html', {'form': form, 'page': 'create'})

def get_team_member(user):
    try:
        return TeamMember.objects.get(member=user)
    except TeamMember.DoesNotExist:
        return None

def get_team_leaders(team):
    return [teammember.member.username for teammember in get_list_or_404(TeamMember, team=team, is_leader=True)]

def create_team_member(team, member, is_leader=False):
    TeamMember.objects.create(team=team, member=member, is_leader=is_leader)
