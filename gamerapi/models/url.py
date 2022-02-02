from pyexpat import model
from django.db import models

class URL(models.Model):
    playerId = models.ForeignKey("Player", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    image_url=models.CharField(max_length=300)