from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


#ADD APPOINTMENTS PAGE
def home(request):
	#typein = respond.Get['entry']
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


#NOLIST PAGE
#def nolist(request):
#	if request.method == 'POST':
#		if form.is_valid():
#			form.save()
#			return redirect('list')
#		else:
#			messages.success(request, ('Seems Like There was an Error'))
#			return render(request, "home.html", {})
#	else:
#		return render(request, "home.html", {})

	

#LIST PAGE
def list(request):
	all_appointments = Appointment.objects.all
	search_name = ""
	if 'search' in request.GET:
		search_name = request.GET['search']
		all_appointments = Appointment.objects.filter(name=search_name) #Add the Startswith
	return render(request, "list.html", {'all_appointments': all_appointments, 'search_name': search_name})



#EDIT PAGE
def edit(request, list_id):
	if request.method == 'POST':
		current_appointment = Appointment.objects.get(pk=list_id)
		form = AppointmentForm(request.POST or None, instance=current_appointment)
		if form.is_valid():
			form.save()
			messages.success(request, ('Appointment Has Been Edited...'))
			return redirect('list')
		else:
			messages.success(request, ('Seems Like There Was an Error...'))
			return render(request, 'edit.html', {})
	else:
		get_appointment = Appointment.objects.get(pk=list_id)
		return render(request, 'edit.html', {'get_appointment': get_appointment})




#DELETE PAGE
def delete(request, list_id):
	if request.method == 'POST':
		current_appointment = Appointment.objects.get(pk=list_id)
		current_appointment.delete()
		messages.success(request, ('Appointment Has Been Deleted...'))
		return redirect('list')
	else:
		messages.success(request, ('Nothing To See Here...'))
		return redirect('list')

		