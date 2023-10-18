from django.db import models
from django.contrib import admin
class Football_Player(models.Model):
    player_name=models.CharField(max_length=20)
    player_age=models.IntegerField()
    team_name=models.CharField(max_length=20)
    player_position=models.CharField(max_length=20)
    player_jersey_no=models.IntegerField()
class Football_PlayerAdmin(admin.ModelAdmin):
    list_display=('player_name','player_age','team_name','player_position','player_jersey_no')    
