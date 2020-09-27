from django.conf.urls import url,re_path
from django.urls import path, include
from archivos import views

urlpatterns =[

url(r'subir_archivo/(?P<id_c>\d+)$',views.model_form_upload,name='form_archivos'),
url(r'editar_archivo/(?P<id>\d+)$',views.archivo_edit,name='form_archivos_edit')

]

