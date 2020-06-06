from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ["name", "last", "email", "phone", "occupation", "category", "date", "start", "end", "location", "loc_name", "address", "city", "state", "zipcode"]
