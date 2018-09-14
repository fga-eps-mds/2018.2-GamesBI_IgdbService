from django.urls import reverse
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from model_mommy import mommy
from IGDBService.importdata.models import IGDBGame


class EndpointsTestCase(APITestCase, URLPatternsTestCase):

	urlpatterns = [
        path('api/', include('IGDBService.API.urls')),
    ]

	def setUp(self):
		"""
			Set up will run before any test
		"""
		self.game_steam = mommy.make(
			IGDBGame,
            id=0,
            name="JogoTesteSteam",
            steam=123,
        )

		self.game = mommy.make(
			IGDBGame,
            id=1,
            name="JogoTesteNaoSteam",
            steam=None,
        )

		self.steam_endpoint = reverse('get_igdb_games_id_steam_list')
		self.name_endpoint = reverse('get_igdb_games_name_list')

	def tearDown(self):
		'''
			Tear Down will run
			after any test
		'''
		IGDBGame.objects.all().delete()

	def test_status_steam_endpoint(self):

		'''
			Check endpoint status
		'''

		response = self.client.get(self.steam_endpoint)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_response_steam_endpoint(self):

		'''
			Test if steam endpoint
			is returning only steam game
		'''

		response = self.client.get(self.steam_endpoint, format='json')

		self.assertEqual(IGDBGame.objects.all().count(), 2)
		#Assert response len 1 because there is just one steam game
		self.assertEqual(len(response.data),1)

	def test_status_name_endpoint(self):

		'''
			Check endpoint status
		'''

		response = self.client.get(self.name_endpoint)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_response_name_endpoint(self):

		'''
			Test if name endpoint
			is returning all games
		'''

		response = self.client.get(self.name_endpoint, format='json')

		self.assertEqual(IGDBGame.objects.all().count(), 2)
		self.assertEqual(len(response.data),2)