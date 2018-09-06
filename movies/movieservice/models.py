from django.db import models

class Movie(models.Model):
    title_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text

class Actors(models.Model):
	actors_text = models.CharField(max_length=200)
	def __str__(self):
		return self.answer_text