from django.conf.urls import url,re_path
from django.urls import path, include
from edit import views

urlpatterns =[

url(r'docente_perfil/',views.docente_perfil,name="home_perfil_docente"),
url(r'alumno_perfil/',views.alumno_perfil,name="home_perfil_alumno"),
url(r'docente_edit/',views.docente_edit,name="docente_edit"),
url(r'docente/password/edit',views.docente_contraseña_edit, name="docente_contra_edit"),
url(r'alumno/password/edit',views.alumno_contraseña_edit, name="alumno_contra_edit"),
url(r'paint',views.paint, name="paint"),
url(r'passcorrectad',views.docente_contraseña_correcta, name="docente_contraseña_correcta"),
url(r'passcorrectaa',views.alumno_contraseña_correcta, name="alumno_contraseña_correcta"),

]