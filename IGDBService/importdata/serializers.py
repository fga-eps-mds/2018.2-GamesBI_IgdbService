from .models import IGDBGame, Genre
from rest_framework import serializers

class IGDBGameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = '__all__'