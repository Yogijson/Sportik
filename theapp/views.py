from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sport, Equipment, UserProfile, MyCart, User
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('theapp:index')
	else:
		form = UserCreationForm()

	args = {'form': form}
	return render(request, 'theapp/registration_form.html', args)


class IndexView(generic.ListView):
	template_name = 'theapp/index.html'
	context_object_name = 'all_sports'

	def get_queryset(self):
		return Sport.objects.all()


class EquipmentView(generic.DetailView):
	model = Sport
	template_name = 'theapp/equipment.html'


class DetailView(generic.DetailView):
	model = Equipment
	template_name = 'theapp/detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		equip_alt = Equipment.objects.get(id=self.kwargs.get('pk_alt', ''))
		context['equip_alt'] = equip_alt
		return context


class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('theapp/index.html')
	template_name = 'theapp/registration_form.html'

class AddItem(CreateView):
	model = Equipment
	fields = ['sport','equipment_name', 'equipment_pic', 'price','desc', 'stock']
	success_url = reverse_lazy('theapp:index')


class SportUpdate(UpdateView):
	model = Sport
	fields = ['sport_name','sport_logo']


class DeleteItem(DeleteView):
	model = Equipment
	fields = ['equipment_name']
	success_url = reverse_lazy('theapp:index')
