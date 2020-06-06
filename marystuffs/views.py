from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


#ADD APPOINTMENTS PAGE
def home(request):
	if request.method == 'POST':
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Appointment Has Been Added'))
			return redirect('list')
		else:
			messages.success(request, ('Seems Like There was an Error'))
			return render(request, "home.html", {})
	else:
		return render(request, "home.html", {})

	

#LIST PAGE
def list(request):
	all_appointments = Appointment.objects.all
	search_name = ""
	if 'search' in request.GET:
		search_name = request.GET['search']
		all_appointments = Appointment.objects.filter(name=search_name) #Add the Startswith
	return render(request, "list.html", {'all_appointments': all_appointments, 'search_name': search_name})