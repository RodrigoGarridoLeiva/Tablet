from django.db import models

class Anuncios(models.Model):
	id_curso = models.IntegerField()
	titulo = models.CharField(null=False,max_length=50)
	des = models.CharField(null=False,max_length=400)
	
