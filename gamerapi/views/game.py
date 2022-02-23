# Viewset which contains logic of what should happen when a clientside request is made


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerapi.models import Game

class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    # ABOVE IS FUNCTION TO GET ITEM BY ID
    

    def list(self, request):
        games = Game.objects.all()
        #using ORM to query the database- returns a python object
        serializer = GameSerializer(games, many=True)
        # creating a JSON representaton of python object, use many=True because all games are being sent back
        return Response(serializer.data)
    
     #ABOVE IS A FUNCTION TO GET ALL GAMES
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
   
        
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
     #ABOVE IS A FUNCTION TO UPDATE GAMES
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
      

        game = Game.objects.create(
            description=request.data["description"],
            designer=request.data["designer"],
            year_released=request.data["year_released"],
            number_of_players=request.data["number_of_players"],
            game_duration=request.data["game_duration"],
            age_recommendation=request.data["age_recommendation"],
            title=request.data["title"]
            
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        
        game = Game.objects.get(pk=pk)
        serializer = PutGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = '__all__'
       
class PutGameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'description', 'designer', 'year_released', 'number_of_players', 'game_duration', 'age_recommendation', 'title' )
       