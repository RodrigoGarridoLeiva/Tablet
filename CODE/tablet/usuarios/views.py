from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Perfil, Alumno, Docente
from .forms import  Registro_Form,Perfil_Form, Alumno_Form, Docente_Form
from django.urls import reverse_lazy
import threading
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


def Usuarios_in_Grupos(usuario_id): #Revisar
	users=User.objects.get(id=usuario_id)
	tutores=Group.objects.get(name='Tutores')
	personal=Group.objects.get(name='Personal')
	disponible=Group.objects.get(name='Disponible')

	if users.perfil.rol=='TUTOR':
		tutores.user_set.add(users)
	else:
		if users.perfil.rol=='PERSONAL':
			personal.user_set.add(users)
			disponible.user_set.add(users)


def Set_password(usuario_id): #Se queda
	nombre=[]
	apellido=[]
	tel=[]
	clave=[]
	user=User.objects.get(id=usuario_id)
	perfil=Perfil.objects.get(id=usuario_id)
	nombre=user.first_name
	apellido=user.last_name
	tel=perfil.tel
	clave.append(nombre[:2])
	clave.append(apellido[:3])
	user.set_password(clave[0].lower()+clave[1].lower())
	user.save()


	
       	


def PerfilView(request,perfil): #Se queda?
	tutor=None
	paciente=None
	personal=None
	usuario=User.objects.get(id=perfil)
	perfile=Perfil.objects.get(id=perfil)
	if perfile.rol=='TUTOR':
		tutor=Tutor.objects.get(id_perfil=perfil)
		paciente=Paciente.objects.get(id_tutor=tutor.id)
	if perfile.rol=='PERSONAL':
		personal=Personal.objects.get(id_perfil=perfil)
	
	context={
		"usuario":usuario,
		"perfil":perfile,
		"tutor":tutor,
		"personal":personal,
		"paciente":paciente
	}

	return render(request,'perfil.html',context)



def perfil_edit(request,usuario_id): #Se queda
    usuario=Perfil.objects.get(usuario_id=usuario_id)
    if request.method=='GET':
        form=Perfil_Form(instance=usuario)
    else:
        form=Perfil_Form(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            Usuarios_in_Grupos(usuario_id)
            Set_password(usuario_id)
        if usuario.rol=='ALUMNO':
        	return redirect(Alumno_view,usuario.id)
        if usuario.rol=='DOCENTE':
        	return redirect(Docente_view,usuario.id)     
    return render(request,'perfil_form.html',{'form':form})	


def Registro_View(request): #Se queda
	if request.method=='POST':
		form1=Registro_Form(request.POST)
		user_name=request.POST.get('username')
				
		

		if form1.is_valid():

				form1.save()
				usuarios=User.objects.last()
				usuario_id=usuarios.id
				return redirect(perfil_edit,usuario_id)
		else:
			messages.error(request,"El nombre de usuario ya existe, porfavor elije otro")

	else:
		form1 = Registro_Form()
		
	return render(request,'registro.html',{'form1':form1})
			
		

def Alumno_view(request,perfil): #Se queda
	
	if request.method=='POST':
		form1=Alumno_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

		return HttpResponseRedirect(reverse('home_l')) #Redirect to login
	else:
		form1 = Alumno_Form()
		
	return render(request,'alumno_form.html',{'form1':form1, 'perfil':perfil})





def Docente_view(request,perfil):
	if request.method=='POST':
		form=Docente_Form(request.POST,request.FILES)
		
		if form.is_valid():
			form.save()
	
		return HttpResponseRedirect(reverse('home_d')) #Redirect to login
	else:
		form = Docente_Form()
		
	return render(request,'personal_form.html',{'form':form,'perfil':perfil})


@login_required
def Perfil_admin(request):
	current_user = request.user
	cont = Llamar.objects.count()
	query = 0

	if cont > 0:
		query = get_object_or_404(Llamar)

	context={
	"user":current_user,
	"q":query,
	"cont":cont,
	}

	return render(request,"perfil_admin.html",context)



@login_required
def contraseña_perfil_edit(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect(contraseña_perfil_edit)
		else:
			messages.error(request, 'Porfavor introduzca contraseña correcta')
			return redirect(contraseña_perfil_edit)
			
	else:
		form = PasswordChangeForm(request.user)

		return render(request,'contra_perfil_edit.html',{'form': form})




