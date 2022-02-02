from django.db import models

class Rating(models.Model):
    playerId = models.ForeignKey("Game", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Player", on_delete=models.CASCADE)
    rating = models.IntegerField()
        
        
        
        
   
        
     