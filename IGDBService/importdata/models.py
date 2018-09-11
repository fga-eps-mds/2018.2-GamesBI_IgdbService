from django.db import models

class Genre(models.Model):

	id = models.IntegerField(
		('Genre ID'),
		help_text=("Genre id at IGDB"),
		primary_key=True,
	)

	name = models.CharField(
		('Genre name'),
		help_text=("Genre name"),
		max_length=100,
	)


class IGDBGame(models.Model):

	id = models.IntegerField(
		('IGDB ID'),
		help_text=("Id do jogo na IGDB"),
		primary_key=True,
	)

	name = models.CharField(
		('Name'),
		help_text=("Name of game"),
		max_length=100,
		null=True
	)

	hypes = models.IntegerField(
		('Hypes'),
		help_text=("Number of access in the game befores its release"),
		null=True
	)

	popularity = models.FloatField(
		('Popularity'),
		help_text=("Popularity of game"),
		null=True
	)

	aggregated_rating = models.FloatField(
		('Critics Rating'),
		help_text=("Rating based on external critic scores"),
		null=True
	)

	time_to_beat = models.FloatField(
		('Time To Beat'),
		help_text=("Avarage time to beat the game"),
		null=True
	)

	steam = models.IntegerField(
		('Steam Id'),
		null=True
	)

	genres = models.ManyToManyField(
		Genre,
		blank=True
	)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.name

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("IGDB Game")
	    verbose_name_plural = ("IGDB Games")


class IGDBKeys(models.Model):

	key = models.CharField(
		('IGDB Key'),
		help_text=("key to make requests on IGDB API"),
		max_length=100,
	)

	requests_count = models.IntegerField(
		('Requests Count'),
		help_text=("Number of times this key has been used"),
	)

	available = models.BooleanField(
		default=False
	)