from django.conf.urls import url,re_path
from django.urls import path, include
from archivos import views

urlpatterns =[

url(r'homearch/	',views.main_arch,name="archivos_home"),
url(r'^subir_archivo/$',views.model_form_upload,name='form_archivos')

]