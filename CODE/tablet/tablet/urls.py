"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from redireccion import urls as red
from docente import urls as docente_urls
from alumno import urls as alumno_urls
from archivos import urls as archivos_urls
from cursos import urls as cursos_urls
from perfiles import urls as perfiles_urls
from edit import urls as main_urls
from anuncio import urls as anuncio_urls
from manual import urls as manual_urls



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path(r'',include('Home.urls')),
    path(r'docente/',include(docente_urls)),
    path(r'alumno/',include(alumno_urls)),
    path(r'red/',include(red)),
    path(r'arch/',include(archivos_urls)),
    path(r'cursos/',include(cursos_urls)),
    path(r'perfil/',include(perfiles_urls)),
    path(r'editar/',include(main_urls)),
    path(r'manual/',include(manual_urls)),
    path(r'anuncio/',include(anuncio_urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
