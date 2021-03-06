from django.urls import path
from apps.consultas.views import ColaEnfermeriaList, ColaEnfermeriaCreate, ColaEnfermeriaUpdate, ColaEnfermeriaDelete, \
	ColaConsultaList, ColaConsultaCreate, ColaConsultaUpdate, ColaConsultaDelete, ColaConsultaDepartamento, \
	ConsultaMedicaList, ConsultaMedicaCreate, ConsultaMedicaUpdate, ConsultaMedicaDelete

app_name = 'consultas'

urlpatterns = [

	# Cola Enfermeria
	path('cola_enfermeria/', ColaEnfermeriaList.as_view(), name='cola_enfermeria_list'),
	path('cola_enfermeria/<pk>/add/', ColaEnfermeriaCreate.as_view(), name='cola_enfermeria_create'),
	path('cola_enfermeria/<pk>/change/', ColaEnfermeriaUpdate.as_view(), name='cola_enfermeria_update'),
	path('cola_enfermeria/<pk>/delete/', ColaEnfermeriaDelete.as_view(), name='cola_enfermeria_delete'),

	# Cola Consulta Médica
	path('cola_consulta/', ColaConsultaList.as_view(), name='cola_consulta_list'),
	path('cola_consulta/<pk>/', ColaConsultaDepartamento.as_view(), name='cola_consulta_departamento'),
	path('cola_consulta/<pk>/<int:departamento>/add/', ColaConsultaCreate.as_view(), name='cola_consulta_create'),
	path('cola_consulta/<pk>/change/', ColaConsultaUpdate.as_view(), name='cola_consulta_update'),
	path('cola_consulta/<pk>/delete/', ColaConsultaDelete.as_view(), name='cola_consulta_delete'),

	# Consulta Médica
	path('consulta_medica/', ConsultaMedicaList.as_view(), name='consulta_medica_list'),
	path('consulta_medica/<pk>/add/', ConsultaMedicaCreate.as_view(), name='consulta_medica_create'),
	path('consulta_medica/<pk>/change/', ConsultaMedicaUpdate.as_view(), name='consulta_medica_update'),
	path('consulta_medica/<pk>/delete/', ConsultaMedicaDelete.as_view(), name='consulta_medica_delete'),
]