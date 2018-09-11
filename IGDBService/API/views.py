import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from IGDBService.importdata.models import IGDBGame
from IGDBService.API.serializers import GameSerializer, GamesSteamSerializer, GameNameSerializer


class GamesListView(APIView):
    serializer_class = GameSerializer
    def get(self, request, format=None):
        serializer = self.serializer_class(IGDBGame.objects.all(), many=True)
        return Response(serializer.data)


class GamesNameListView(APIView):
    serializer_class = GameNameSerializer
    def get(self, request, format=None):
        serializer = self.serializer_class(IGDBGame.objects.all(), many=True)
        return Response(serializer.data)


class GamesSteamListView(APIView):
    serializer_class = GamesSteamSerializer
    def get(self, request, format=None):
        serializer = self.serializer_class(IGDBGame.objects.exclude(steam__isnull=True).exclude(steam=None), many=True)
        return Response(serializer.data)
