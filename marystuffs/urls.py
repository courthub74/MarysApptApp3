from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('list/', views.list, name='list'),
	path('search/', views.list, name='search'),
	path('edit/<list_id>', views.edit, name='edit'),
	#path('delete/<list_id>', views.delete, name='delete'),
]