from django.db import models

class Archivo(models.Model):
        nombre = models.CharField(max_length= 50, default='Sin titulo')
        file = models.FileField(upload_to='archivos/')      
        curso_id = models.IntegerField()
        des = models.CharField(max_length= 100, default='Sin descripción')

       
        def __str__(self):
        	return "{}".format(self.nombre)

