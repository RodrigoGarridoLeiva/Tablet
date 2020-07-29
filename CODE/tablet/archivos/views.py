from django.shortcuts import render
from .models import Archivo
from django.contrib.auth.decorators import login_required

@login_required
def biblioteca(request):
	archivo = Archivo.objects.all()    
	return render(request,'biblioteca.html',{'archivo':archivo})


