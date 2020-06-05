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
	return render(request, "list.html", {'all_appointments': all_appointments})