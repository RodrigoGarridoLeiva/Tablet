from django.conf.urls import url,re_path
from django.urls import path, include
from docente import views

urlpatterns =[

url(r'home/	',views.home_d,name="home_d"),
url(r'editar/docente/',views.editarperfil_docente,name="editar_docente"),
url(r'lista/cursos',views.lista_cursos_docente,name="lista_cursos_docente"),
url(r'logout/',views.logout_view,name="logout")

]