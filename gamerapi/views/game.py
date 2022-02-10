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
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    
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
    
    
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = '__all__'
        depth = 2