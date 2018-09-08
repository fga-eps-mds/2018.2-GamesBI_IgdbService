from .models import IGDBGame, Genre
from rest_framework import serializers

from .models import IGDBGame
from rest_framework import serializers

class IGDBGameSerializer(serializers.ModelSerializer):

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


class GenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = '__all__'


class GameSerializerList(serializers.ModelSerializer):
	genres = GenreSerializer(
		many=True
	)

	class Meta:

		model = Genre
		fields = '__all__'
