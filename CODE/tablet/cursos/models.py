from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




class Cursos(models.Model):
	nombre = models.CharField(null=False,max_length=20)
	id_docente = models.IntegerField()

	def __str__(self):
		return str(self.usuario.username)


class Materia(models.Model):
	id_curso = models.IntegerField()
	nombre = models.CharField(null=False,max_length=20)


class ListaAlumno(models.Model):
	id_curso = models.IntegerField()
	id_alumno = models.IntegerField()

