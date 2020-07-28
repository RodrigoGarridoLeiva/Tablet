from django.conf.urls import url,re_path
from django.urls import path, include
from docente import views

urlpatterns =[

url(r'home/	',views.home_d,name="home_d")

]