from django.db import models

  
    
    # upload = models.ImageField(upload_to ='uploads/')

class URL(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=25)
    
    # image_url=models.ImageField(upload_to=None)