from django.contrib import admin
from .models import Team, TeamMember
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    pass

class TeamMemberAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
