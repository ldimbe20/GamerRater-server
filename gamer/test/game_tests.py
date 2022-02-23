from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from gamerapi.models import Game

class GameTests(APITestCase):
    def setUp(self):
        url = '/register'

        user = {
            "username": "steve",
            "password": "Admin8*",
            "last_login": "NULL",
            "is_superuser": "false",
            "email": "steve@stevebrownlee.com",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "is_staff": "false",
            "is_active":"true",
            "date_joined": "2020-08-28 14:51:39.989000"
            
           
        }

        response = self.client.post(url, user, format='json')

        self.token = Token.objects.get(pk=response.data['token'])

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.game = Game()
        self.game.description = "Cool game"
        self.game.title = "Sorry"
        self.game.designer = "Milton Bradley"
        self.game.year_released = "2020-01-15"
        self.game.number_of_players = 4
        self.game.game_duration = "Five hours"
        self.game.age_recommendation=7

        # Save the Game to the testing database
        self.game.save()
        
    def test_create_game(self):
        """Create game test"""
        url = "/games"

        # Define the Game properties
        game = {
            "title": "Clue",
            "designer": "Milton Bradley",
            "number_of_players": 5,
            "description": "cool gamesssss",
            "age_recommendation": 6,
            "game_duration": "Five hours",
            "year_released": "2020-01-15"
        }

        response = self.client.post(url, game, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["title"], game['title'])
        self.assertEqual(response.data["designer"], game['designer'])
        self.assertEqual(response.data["description"], game['description'])
        self.assertEqual(
            response.data["age_recommendation"], game['age_recommendation'])
        self.assertEqual(response.data["number_of_players"], game['number_of_players'])
        self.assertEqual(response.data["game_duration"], game['game_duration'])
        self.assertEqual(response.data["year_released"], game['year_released'])

