from django.conf.urls import url,re_path
from django.urls import path, include
from manual import views

urlpatterns =[

url(r'home/	',views.home_manual,name="home_manual")

]