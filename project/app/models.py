from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Phone(models.Model):
	number = models.TextField(max_length=15)

	def __str__(self):
		return self.number
