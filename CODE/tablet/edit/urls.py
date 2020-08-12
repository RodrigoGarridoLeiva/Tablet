from django.conf.urls import url,re_path
from django.urls import path, include
from edit import views

urlpatterns =[

url(r'docente_perfil/',views.docente_perfil,name="home_perfil_docente"),
url(r'alumno_perfil/',views.alumno_perfil,name="home_perfil_alumno"),
url(r'docente_edit/',views.docente_edit,name="docente_edit")

]