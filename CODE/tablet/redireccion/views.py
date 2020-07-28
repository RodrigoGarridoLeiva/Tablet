from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Docente, Alumno, Perfil
from django.contrib.auth.models import User
from usuarios.views import Registro_View
from django.contrib.auth.decorators import login_required

@login_required
def redireccion(request):
	current_user = request.user
	queryset = get_object_or_404(Perfil, usuario_id=current_user.id)
	actual = queryset.rol

	if actual == "DOCENTE":
		return HttpResponseRedirect(reverse('home_d')) 

	if actual == "ALUMNO":
		return HttpResponseRedirect(reverse('home_l'))
	
	if actual != "ALUMNO" or  actual != "DOCENTE":
		return HttpResponseRedirect(reverse('home_l')) #CAMBIAR A ERROR


	return render(request,"salto.html")
