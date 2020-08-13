from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




class Cursos(models.Model):
	id_unico = models.IntegerField()
	nombre = models.CharField(null=False,max_length=20)
	id_docente = models.IntegerField()


class Materia(models.Model):
	id_curso = models.IntegerField()
	nombre = models.CharField(null=False,max_length=20)


class ListaAlumno(models.Model):
	id_curso = models.IntegerField()
	id_alumno = models.IntegerField()

