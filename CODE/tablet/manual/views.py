from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home_manual(request):

	return render(request,"home_manual.html")

def manual_docente_a(request):
	return render(request,"manual_d_a.html")

def manual_alumno_a(request):
	return render(request,"manual_a_a.html")