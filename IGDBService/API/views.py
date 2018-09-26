import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from IGDBService.importdata.models import IGDBGame, Genre
from .serializers import GameSerializer, GamesSteamSerializer, GameNameSerializer, GenreSerializer, GameSerializerList


class GamesSteamListView(APIView):
    serializer_class = GamesSteamSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(
            IGDBGame.objects.exclude(steam=None),
            many=True
        )

        return Response(serializer.data)


class GamesNameListView(APIView):
    serializer_class = GameNameSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(
            IGDBGame.objects.all(),
            many=True
        )

        return Response(serializer.data)


class GamesAllListView(APIView):
    serializer_class = GameSerializerList

    def get(self, request, format=None):
        serializer = self.serializer_class(
            IGDBGame.objects.all(),
            many=True
        )

        return Response(serializer.data)


class GenreListView(APIView):
    serializer_class = GenreSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(
            Genre.objects.all(),
            many=True
        )

        return Response(serializer.data)
