from django.conf.urls import url,re_path
from django.urls import path, include
from alumno import views

urlpatterns =[

url(r'home/',views.home_l,name="home_l")

]