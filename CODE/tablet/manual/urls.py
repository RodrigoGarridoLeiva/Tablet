from django.conf.urls import url,re_path
from django.urls import path, include
from manual import views

urlpatterns =[

url(r'home/	',views.home_manual,name="home_manual"),
url(r'home/manual/docente/a	',views.manual_docente_a,name="m_d_a"),
url(r'home/manual/alumno/a ',views.manual_alumno_a,name="m_a_a")

]