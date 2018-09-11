from IGDBService.importdata.models import IGDBGame
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = '__all__'

class GamesSteamSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		depth = 1
		fields = ['steam']

class GameNameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		depth = 1
		fields = ['name']
