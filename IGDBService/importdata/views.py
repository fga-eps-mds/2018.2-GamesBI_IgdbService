import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import IGDBGame, Genre
from .serializers import GameSerializer, GamesSteamSerializer, GameNameSerializer
from django.shortcuts import render


class IgDBView(APIView):
    '''
        View that calls IGDB API
        and return some relevant
        information about a game
        and filter for Null value
    '''

    def get(self, request, format=None):
        IGDBGame.objects.all().delete()
        header = {'user-key': '8ac128e6b3e9709134ad83ac072d0d59',
        'Accept': 'application/json'}
        url = 'https://api-endpoint.igdb.com/games/?fields=id,name,hypes,popularity,aggregated_rating,time_to_beat,external,genres&filter[rating][gte]=60&order=popularity:desc&limit=1&scroll=1'
        data = requests.get(url, headers=header)
        max_result = int(data.headers['x-count']) # retorna o a quantidade de itens do endpoint

        max_result = 50 # apenas para fins de teste  , para nao estourar o limite da user_key (retornara apenas 50 games)

        for page in range(0, max_result, 50): #cada solicitaçao retona no maximo 50 valores, assim o for pega todos os itens do endpoint
            url = 'https://api-endpoint.igdb.com/games/?fields=id,name,hypes,popularity,aggregated_rating,time_to_beat,external,genres&filter[rating][gte]=60&order=popularity:desc&limit=50&offset='+str(page)
            data = requests.get(url, headers=header)
            ndata = data.json()

            for gamedata in ndata:
                filtered_data = self.filter_data(gamedata)
                self.save_game(filtered_data)
                self.get_genres(gamedata['genres'])

            games = IGDBGame.objects.all()


        return Response(data=ndata)

    def filter_data(self, gamedata):

        if 'id' in gamedata:
            id = gamedata['id']
        else:
            id = None

        if 'name' in gamedata:
            name = gamedata['name']
        else:
            name = None

        if 'hypes' in gamedata:
            hypes = gamedata['hypes']
        else:
            hypes = None

        if 'popularity' in gamedata:
            popularity = gamedata['popularity']
        else:
            popularity = None

        if 'aggregated_rating' in gamedata:
            aggregated_rating = gamedata['aggregated_rating']
        else:
            aggregated_rating = None

        if 'time_to_beat' in gamedata:
            if 'normally' in gamedata['time_to_beat']:
                time_to_beat = gamedata['time_to_beat']['normally']
            else:
                time_to_beat = None
        else:
            time_to_beat = None

        if 'genres' in gamedata:
            genres = gamedata['genres']
        else:
            genres = None

        if 'external' in gamedata:
            steam = gamedata['external']['steam']
        else:
            steam = None


        filtered_data = {
            'id': id,
            'name': name,
            'hypes': hypes,
            'popularity': popularity,
            'aggregated_rating': aggregated_rating,
            'time_to_beat': time_to_beat,
            'steam':steam,
            'genres': genres

        }

        return filtered_data

    def save_game(self, filtered_data):
        new_game = IGDBGame(
            id = filtered_data['id'],
            name = filtered_data['name'],
            hypes = filtered_data['hypes'],
            popularity = filtered_data['popularity'],
            aggregated_rating = filtered_data['aggregated_rating'],
            time_to_beat = filtered_data['time_to_beat'],
            steam = filtered_data['steam']

        )

        new_game.save()
        genres = self.get_genres(filtered_data['genres'])

        for genre in genres:
            new_game.genres.add(genre)
            new_game.save()


    def get_genres(self, genres_id_list):
        genres = []

        for genre_id in genres_id_list:
            url = 'https://api-endpoint.igdb.com/genres/{}?fields=name'.format(genre_id)
            header = {'user-key': '8ac128e6b3e9709134ad83ac072d0d59',
            'Accept': 'application/json'}

            data = requests.get(url, headers=header)
            ndata = data.json()


            genre = Genre(
                id = ndata[0]['id'],
                name = ndata[0]['name']
            )
            genre.save()

            genres.append(genre)

        return genres
