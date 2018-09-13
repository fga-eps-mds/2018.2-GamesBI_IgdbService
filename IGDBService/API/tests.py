from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy
from IGDBService.importdata.models import IGDBGame


class EndpointsTestCase(APITestCase):

	def setUp(self):
		"""
			Set up will run before any test
		"""
		self.game = mommy.make(
			IGDBGame,
            id=0,
            name="JogoTeste",
            steam=None,
        )

		self.steam_endpoint = 'http://igdbweb:8000/api/get_igdb_games_list/id_steam'

	def tearDown(self):
		IGDBGame.objects.all().delete()

	def test_status_steam_endpoint(self):

		response = self.client.get(self.steam_endpoint)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_response_steam_endpoint(self):

		response = self.client.get(self.steam_endpoint)
		data = response.json()

		self.assertNotEqual(IGDBGame.objects.all().count(), 0)