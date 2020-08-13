from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

from usuarios.models import Docente, Alumno

@login_required
def docente_perfil(request):

	current_user = request.user
	instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"rut":instance.rut
	}
	
	return render(request,'home_perfil_docente.html',context)


@login_required
def alumno_perfil(request):

	current_user = request.user
	instance = get_object_or_404(Alumno, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"rut":instance.rut
	}
	
	return render(request,'home_perfil_alumno.html',context)



@login_required
def docente_edit(request):
	
	current_user = request.user
	docente=Docente.objects.get(id_perfil_id=current_user.id)
	if request.method=='GET':
		form1=Docente_Form(instance=docente)
	else:
		form1=Docente_Form(request.POST,instance=docente)
		if form1.is_valid():
			form1.save()
		return redirect(ver_perfil)
	return render(request,'tutor_f.html',{'form1':form1,'docente':docente})


@login_required
def docente_contraseña_edit(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect(docente_contraseña_edit)
		else:
			messages.error(request, 'Porfavor introduzca contraseña correcta')
			return redirect(docente_contraseña_edit)
			
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'docente_contra_edit.html',{'form': form})


@login_required
def alumno_contraseña_edit(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect(alumno_contraseña_edit)
		else:
			messages.error(request, 'Porfavor introduzca contraseña correcta')
			return redirect(alumno_contraseña_edit)
			
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'al_contra_edit.html',{'form': form})

