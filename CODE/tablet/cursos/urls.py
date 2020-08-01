from django.conf.urls import url,re_path
from django.urls import path, include
from cursos import views

urlpatterns =[

url(r'inicio/',views.inicio_cursos,name="inicio_cursos")


]