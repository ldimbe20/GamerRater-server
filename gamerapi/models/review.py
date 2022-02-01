from django.db import models

class Review(models.Model):
  playerId = models.ForeignKey("Player", on_delete=models.CASCADE)
  gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
  review = models.TextField()