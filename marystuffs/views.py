from django.shortcuts import render
from .models import Appointment


#HOME PAGE
def home(request):
	return render(request, "home.html", {})

#LIST PAGE
def list(request):
	all_appointments = Appointment.objects.all
	return render(request, "list.html", {'all_appointments': all_appointments})