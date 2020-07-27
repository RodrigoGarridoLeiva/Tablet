from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil , Alumno, Docente
from django.contrib.auth.models import User


class Registro_Form(UserCreationForm):
	first_name = forms.CharField(max_length=140, required = True)
	last_name = forms.CharField(max_length=140, required=False)
	email = forms.EmailField(required=True)
	 

	class Meta:
		model = User

		fields = [
			 'username',
			 'email',
			 'first_name',
			 'last_name',
			 'password1',
			 'password2'
			 ]


	
     






class Perfil_Form(forms.ModelForm):
	class Meta:
		ROL=(
			('PERSONAL','Docente'),
			('TUTOR','Tutor'),
			('ALUMNO','Alumno'))

		model = Perfil

		fields=['rol']

		widgets={
		
		'rol':forms.Select(choices=ROL,attrs={'class':'form-control'}),
		}



class Alumno_Form(forms.ModelForm):
	class Meta:

		model = Alumno

		fields=['id_perfil',
				'rut']

		widgets={
				'rut':forms.TextInput(attrs={'class':'form-control',"id":"rut", "required oninput":"checkRut(this)", "maxlength":"10"})
		}

class Docente_Form(forms.ModelForm):
	class Meta:

		model = Docente

		fields =['id_perfil','rut']

		widgets ={
		'rut':forms.TextInput(attrs={'class':'form-control',"id":"rut", "required oninput":"checkRut(this)", "maxlength":"10"})
		}