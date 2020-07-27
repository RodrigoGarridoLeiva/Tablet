from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Perfil(models.Model):
	usuario = models.OneToOneField(User,on_delete=models.CASCADE)
	rol = models.CharField(null=False,max_length=20)
	tel = models.CharField(null=False, max_length=20)

	def __str__(self):
		return str(self.usuario.username)


class Alumno(models.Model):
	id_perfil = models.ForeignKey(Perfil, default=None,on_delete=models.CASCADE)
	rut = models.CharField( null=False,max_length=15)
	
	def __str__(self):
		return str(self.id_perfil.usuario.username)
		

class Docente(models.Model):
	id_perfil = models.ForeignKey(Perfil, default=None,on_delete=models.CASCADE)
	rut = rut = models.CharField(null=False,max_length=15)


	def __str__(self):
		return str(self.id_perfil.usuario.username)



@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()





