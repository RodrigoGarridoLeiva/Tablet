from django.conf.urls import url,re_path
from django.urls import path, include
from alumno import views

urlpatterns =[

url(r'home/',views.home_l,name="home_l"),
url(r'ingresar/curso/',views.ingresar_curso,name="ingresar_curso"),
url(r'materia/(?P<id>\d+)$',views.cursos_alumno,name="materia_alumno"),
url(r'editar/alumno/',views.editarperfil_alumno,name="editar_alumno"),
url(r'archivos/alumno/(?P<id>\d+)$',views.archivos,name="archivos_curso")

]