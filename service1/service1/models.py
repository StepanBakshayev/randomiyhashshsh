from enum import Enum
from operator import attrgetter

from django.core import validators
from django.db import models


class Function(models.Model):
	class Type(Enum):
		first = 'y=t*t+2/t'
		second = 'y=sin(t)'

	type = models.CharField(choices=tuple((t.value, t.name) for t in Type), max_length=max(map(len, map(attrgetter('value'), Type))))
	interval = models.IntegerField(validators=(validators.MinValueValidator(1),))
	dt = models.IntegerField(validators=(validators.MinValueValidator(1),))


class Chart(models.Model):
	function = models.ForeignKey(Function, unique=True, on_delete=models.CASCADE)
	chart = models.ImageField(upload_to='chart/')
	generated_at = models.DateTimeField()


class Error(models.Model):
	function = models.ForeignKey(Function, unique=True, on_delete=models.CASCADE)
	message = models.TextField()
	generated_at = models.DateTimeField()
