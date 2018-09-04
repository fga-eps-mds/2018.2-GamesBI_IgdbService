from .models import IGDBGame
from rest_framework import serializers

class IGDBGameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = '__all__'