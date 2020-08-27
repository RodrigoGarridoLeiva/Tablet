from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cursos.models import Cursos, Materia, ListaAlumno
from usuarios.models import Docente
from archivos.models import Archivo
from django.contrib.auth.models import User
from cursos.forms import Lista_Form

@login_required
def home_l(request):

	current_user = request.user
	c = Cursos.objects.all()
	l = ListaAlumno.objects.all()
	docente = Docente.objects.all()
	usuarios = User.objects.all()

	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"id_alumno": current_user.id,
		"lista":l,
		"curso": c,
		"docente":docente,
		"users":usuarios,
	}
	
	return render(request,"home_l.html", context)


@login_required
def ingresar_curso(request):
	current_user = request.user
	form = Lista_Form(request.POST or None)
	c = Cursos.objects.all()
	l = ListaAlumno.objects.all()
	usuarios = User.objects.all()

#Hacer if para que no se repitan y no se guarden cursos ya guardados o inexistentes

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('ingresar_curso'))

	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"id_al": int(current_user.id),
		"cursos": c,
		"user":usuarios,
		"lista":l,
	}
	
	return render(request,"ingresar_alumno.html",context)


	
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


@login_required
def cursos_alumno(request, id):
	current_user = request.user
	materia = Materia.objects.all()
	curso = Cursos.objects.all()
	
	context = {

		"id_al": current_user.id,
		"m":materia,
		"id": int(id),

	}
	
	return render(request,"cursos_alumno.html",context)

@login_required
def archivos(request, id):

	current_user = request.user
	materia = Materia.objects.all()

	context = {

		"m":materia,
		"id": int(id),
		
	}
	
	return render(request,"archivos_curso.html", context)

@login_required
def archivos_del_curso(request, id):

	current_user = request.user
	arch = Archivo.objects.all()

	context = {

		"arch":arch,
		"id": int(id),
		
	}
	
	return render(request,"archivos_de_curso.html", context)