from django import forms
from django.contrib.auth.forms import UserCreationForm
from cursos.models import Cursos, Materia, ListaAlumno


class Cursos_Form(forms.ModelForm):
	class Meta:
		model = Cursos

		fields=['nombre',
				'id_docente',
				'id_unico']

class Materia_Form(forms.ModelForm):
	class Meta:
		model = Materia

		fields=['nombre',
				'id_curso']


class Lista_Form(forms.ModelForm):
	class Meta:
		model = ListaAlumno

		fields=['id_curso',
				'id_alumno']