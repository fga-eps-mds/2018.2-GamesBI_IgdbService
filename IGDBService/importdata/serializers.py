from .models import IGDBGame, Genre
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = '__all__'


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


