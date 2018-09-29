from django.urls import reverse
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from model_mommy import mommy
from IGDBService.importdata.models import IGDBGame


import requests_mock
from  unittest.mock import Mock, patch
from IGDBService.importdata.views import IgDBView
#from nose.tools import assert_list_equal, assert_true


class EndpointsTestCase(APITestCase, URLPatternsTestCase, object):

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
		for data in response.data:
			self.assertNotEqual(data['steam'], None)

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
	@classmethod
	def setup_class(cls):
		cls.mock_get_patcher = patch('IGDBService.importdata.views.IgDBView')
		cls.mock_get = cls.mock_get_patcher.start()

	@classmethod
	def teardown_class(cls):
		cls.mock_get_patcher.stop()

	def test_getting_todos_when_response_is_ok(self):
		# Configure the mock to return a response with an OK status code.
		#self.mock_get.return_value.ok = True

		todos = [{
			'id': "id",
			'name': "name",
			'hypes': "hypes",
			'popularity': "popularity",
			'aggregated_rating': "aggregated_rating",
			'time_to_beat': "time_to_beat",
			'steam':"steam",
			'genres': "genres"
		}]
		self.mock_get.return_value = Mock()
		self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
		response = self.mock_get.get()

        # If the request is sent successfully, then I expect a response to be returned.
		self.assert_list_equal(response.json(), todos)
	def test_getting_todos_when_response_is_not_ok(self):
		# Configure the mock to not return a response with an OK status code.
		#self.mock_get.return_value.ok = False

		# Call the service, which will send a request to the server.
		response = self.mock_get.get()

		# If the response contains an error, I should get no todos.
		self.assert_is_none(response)
