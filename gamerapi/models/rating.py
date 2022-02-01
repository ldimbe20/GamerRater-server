from django.db import models

class Rating(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    playerId = models.ForeignKey("Player", on_delete=models.CASCADE)
    rating = models.CharField(max_length=25)
        
        
        
        
   
        
     