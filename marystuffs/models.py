from django.db import models

class Appointment(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	occupation = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	start = models.CharField(max_length=200)
	end = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	loc_name = models.CharField(max_length=200, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=200, blank=True, null=True)
	zipcode = models.CharField(max_length=200, blank=True, null=True)


	def __str__(self):
		return self.name
