from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cursos.models import Cursos, Materia, ListaAlumno
from usuarios.models import Docente

@login_required
def home_l(request):

	current_user = request.user
	c = Cursos.objects.all()
	l = ListaAlumno.objects.all()
	docente = Docente.objects.all()

	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"id_alumno": current_user.id,
		"lista":l,
		"curso": c,
		"docente":docente,

	}
	
	return render(request,"home_l.html", context)

	
@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")


@login_required
def editarperfil_alumno(request):
	current_user = request.user
	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
	}
	
	return render(request,"editar_alumno.html",context)