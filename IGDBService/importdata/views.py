import requests
import os

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import IGDBGame, Genre, IGDBKeys
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
        games_salved = IGDBGame.objects.all()
        games_salved = 0
        #while (games_salved % 50 != 0):
        #    games_salved = games_salved - 1

        start_result = games_salved
        # apenas para fins de teste  , para nao estourar o limite da user_key (retornara apenas 50 games)
        max_result = 100
        # max_result = int(data.headers['x-count']) # retorna o a quantidade de itens do endpoint

        # cada solicitaçao retona no maximo 50 valores, assim o for pega todos os itens do endpoint
        for page in range(start_result, max_result, 50):

            key = self.get_key()
            if key == None:
                ndata = {
                    'mensagem de erro': 'nao ha mais chaves disponiveis'
                }

                return Response(data=ndata)

            if((max_result - key.requests_count) > 2):

                header = {'user-key': key.key,
                          'Accept': 'application/json'}

                url = 'https://api-endpoint.igdb.com/games/?fields=id,name,hypes,popularity,aggregated_rating,time_to_beat,external,genres&filter[rating][gte]=90&order=popularity:desc&limit=50&offset=' + str(
                    page)
                data = requests.get(url, headers=header)
                key.requests_count += 1
                key.save()
                ndata = data.json()

                for gamedata in ndata:
                    filtered_data = self.filter_data(gamedata)
                    self.save_game(filtered_data, key)
            else:
                key.available = False
                key.save()
                continue

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
            'steam': steam,
            'genres': genres

        }

        return filtered_data

    def save_game(self, filtered_data, key):
        new_game = IGDBGame(
            id=filtered_data['id'],
            name=filtered_data['name'],
            hypes=filtered_data['hypes'],
            popularity=filtered_data['popularity'],
            aggregated_rating=filtered_data['aggregated_rating'],
            time_to_beat=filtered_data['time_to_beat'],
            steam=filtered_data['steam']

        )

        new_game.save()

        if filtered_data['genres'] is not None:
            genres = self.get_genres(filtered_data['genres'], key)

            for genre in genres:
                new_game.genres.add(genre)
                new_game.save()

        print(new_game.name)
        for genre in new_game.genres.all():
            print(genre.name)

    def get_genres(self, genres_id_list, key):

        genres = []

        if len(genres_id_list) >= 3:
            url = 'https://api-endpoint.igdb.com/genres/{},{},{}?fields=name'.format(
                genres_id_list[0], genres_id_list[1], genres_id_list[2]
            )
        if len(genres_id_list) == 2:
            url = 'https://api-endpoint.igdb.com/genres/{},{}?fields=name'.format(
                genres_id_list[0], genres_id_list[1]
            )
        else:
            url = 'https://api-endpoint.igdb.com/genres/{}?fields=name'.format(
                genres_id_list[0]
            )

        header = {'user-key': key.key,
                  'Accept': 'application/json'}

        data = requests.get(url, headers=header)
        key.requests_count += 1
        key.save()
        ndata = data.json()

        for genre in ndata:

            genre = Genre(
                id=genre['id'],
                name=genre['name']
            )
            genre.save()

            genres.append(genre)

        return genres

    def get_key(self):
        for key in IGDBKeys.objects.all():
            if key.available == True:
                return key
        return None
