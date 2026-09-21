from django.urls import path
main
from . import views

app_name = 'actividades'

urlpatterns = [
    path('', views.lista_actividades, name='lista'),
    path('crear/', views.crear_actividad, name='crear'),
    path('<int:pk>/', views.detalle_actividad, name='detalle'),
]


from . import views

app_name = "actividades"

urlpatterns = [
    path( "mi-panel/", views.panel_actividades_organizador,name="panel_actividades_organizador",),
    path(  "crear/",views.crear_actividad,name="crear_actividad", ),
    path( "<int:actividad_id>/editar/", views.editar_actividad,name="editar_actividad"),
]

main
