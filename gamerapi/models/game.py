from django.db import models 

class Game(models.Model):
    description = models.TextField()
    designer = models.CharField(max_length=25)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    game_duration = models.IntegerField()
    age_recommendation = models.IntegerField()
    title = models.CharField(max_length=50)
    
    
    
    
   