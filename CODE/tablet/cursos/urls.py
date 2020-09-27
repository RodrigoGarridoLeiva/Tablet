from django.conf.urls import url,re_path
from django.urls import path, include
from cursos import views

urlpatterns =[

url(r'inicio/',views.inicio_cursos,name="inicio_cursos"),
url(r'materias/(?P<curso_id>\d+)$',views.materias,name="inicio_materias"),
url(r'documentos/(?P<id>\d+)$',views.ver_docs,name="ver_docs"),
url(r'delete/(?P<id>\d+)$',views.borrar_curso, name='borrar_curso'),
url(r'delete/archivo/(?P<id>\d+)$',views.borrar_archivo, name='borrar_archivo'),
url(r'detalle/(?P<id>\d+)$',views.detalles_curso, name='detalle_curso'),
url(r'^eliminar_alumno_curso/(?P<id_a>\d+)/(?P<id_c>\d+)$',views.quitar_alumno_de_curso, name="quitar_alumno_de_curso"),

]