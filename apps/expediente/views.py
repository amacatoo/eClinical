from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.expediente.models import SignoVital
from apps.expediente.forms import SignoVitalForm

# Create your views here.

# SIGNOS VITALES #

class SignoVitalList(ListView):
	model = SignoVital
	template_name = 'expediente/signo_vital_list.html'

class SignoVitalCreate(SuccessMessageMixin, CreateView):
	model = SignoVital
	form_class = SignoVitalForm
	template_name = 'expediente/signo_vital_form.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales registrados correctamente'

class SignoVitalUpdate(SuccessMessageMixin, UpdateView):
	model = SignoVital
	form_class = SignoVitalForm
	template_name = 'expediente/signo_vital_form.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales editados correctamente'

class SignoVitalDelete(SuccessMessageMixin, DeleteView):
	model = SignoVital
	template_name = 'expediente/signo_vital_delete.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales eliminados correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(SignoVitalDelete, self).delete(request, *args, **kwargs)