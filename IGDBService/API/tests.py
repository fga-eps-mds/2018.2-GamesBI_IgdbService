from django.urls import reverse
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from model_mommy import mommy
from IGDBService.importdata.models import IGDBGame

import requests_mock


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

    @requests_mock.Mocker(kw='mock')
    def test_get(self, **kwargs):
        header = {'user-key': '8ac128e6b3e9709134ad83ac072d0d59',
        'Accept': 'application/json'}
        url = 'https://test.com'

        result = [{"list": {"type": "gama"},
                   "id": "123456",
                   "type": {"id": "123456", "name": "CS"}}]

        kwargs['mock'].get(url, text=json.dumps(result))

        current_time = datetime.now().__str__()
        raw_data = request.get(current_time, url)
        assert raw_data.response.status_code == 200
        #assert raw_data.data == result
        assert raw_data.data_length == 1
