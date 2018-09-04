import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from IGDBService.importdata.models import IGDBGame
from IGDBService.importdata.serializers import IGDBGameSerializer

class IgDBView(APIView):

	def get(self, request, format=None):

		header = {'user-key': '9c3039ea4ad4cb83bfb126100764c483', 'Accept':'application/json'}
		url = 'https://api-endpoint.igdb.com/games/?fields=id,name,hypes&filter[rating][gte]=60&order=popularity:desc&limit=50&offset=0'
		data = requests.get(url, headers=header)
		ndata = data.json()

		for item in ndata:

			serializer = IGDBGameSerializer(data=item)

			if serializer.is_valid():
				print("deu certo")
				serializer.save()
			else:
				print("deu errado")

		for game in IGDBGame.objects.all():
			print(game)

		IGDBGame.objects.all().delete()

		return Response(data=ndata)
