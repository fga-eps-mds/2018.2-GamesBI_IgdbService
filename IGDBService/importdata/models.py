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

<<<<<<< HEAD
<<<<<<< 978ad1a266c7a4ba0addacb34b11258d22173b8f
=======
>>>>>>> 346b6f6090b05b07a05a4d7a04f46b8e658e2345
	steam = models.IntegerField(
		('Steam Id'),
		null=True
	)

<<<<<<< HEAD
	genres = models.ManyToManyField(
		Genre,
		blank=True
=======
	genres = models.ManyToManyField(
		Genre
>>>>>>> [ADD] #89 Created Model for IGDB Service
=======
	genres = models.ManyToManyField(
		Genre,
		blank=True
>>>>>>> 346b6f6090b05b07a05a4d7a04f46b8e658e2345
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