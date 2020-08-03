from django.conf.urls import url,re_path
from django.urls import path, include
from cursos import views

urlpatterns =[

url(r'inicio/',views.inicio_cursos,name="inicio_cursos"),
url(r'materias/(?P<curso_id>\d+)$',views.materias,name="inicio_materias"),
url(r'ver/materias/(?P<curso_id>\d+)$',views.ver_materias,name="ver_materias")


]