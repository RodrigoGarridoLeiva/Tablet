from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView ,View
from .models import Archivo
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm


from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

@login_required
def main_arch(request):
	archivo = Archivo.objects.all()    
	return render(request,'arch_home.html',{'archivo':archivo})


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('archivos_home'))
    else:
        form = DocumentForm()
    return render(request, 'form_archivos.html', {
        'form': form
    })


#FALTA SI ES WORD CONVERTIRLO EN PDF