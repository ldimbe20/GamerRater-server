from django.db import models 

class Game(models.Model):
    description = models.TextField()
    designer = models.CharField(max_length=25)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    game_duration = models.CharField(max_length=25)
    age_recommendation = models.IntegerField()
    title = models.CharField(max_length=50)
    
    
    
    
   