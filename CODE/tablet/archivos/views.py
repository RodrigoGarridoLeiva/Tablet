from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView ,View
from .models import Archivo
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm



from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

@login_required
def main_arch(request,id_c):
	archivo = Archivo.objects.all()    
	return render(request,'arch_home.html',{'archivo':archivo}, {'id':id})


@login_required
def model_form_upload(request,id_c):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_cursos_docente'))
    else:
        form = DocumentForm()
    
    context = {

        "form": form,
        "id": int(id_c),
    }
    

    return render(request,'form_archivos.html',context)

@login_required
def archivo_edit(request,id):
    
    current_user = request.user
    archivo=Archivo.objects.get(id=id)

    if request.method=='GET':
        form1=DocumentForm(instance=archivo)
    else:
        form1=DocumentForm(request.POST,instance=archivo)
        if form1.is_valid():
            form1.save()
        return HttpResponseRedirect(reverse('lista_cursos_docente'))
    return render(request,'form_archivos_edit.html',{'form1':form1,'archivo':archivo})