from IGDBService.importdata.models import IGDBGame, Genre
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = '__all__'

class GamesSteamSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = ['steam']

class GameNameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = ['name']


class GenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = ['name']

class GameSerializerList(serializers.ModelSerializer):
	genres = GenreSerializer(
		many=True
	)

	class Meta:

		model = IGDBGame
		fields = '__all__'