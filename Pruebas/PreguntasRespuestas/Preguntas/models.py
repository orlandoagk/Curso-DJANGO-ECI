from django.db import models

# Create your models here.
class Pregunta(models.Model):
	fechaPublicacion = models.DateTimeField('date published')
	textoPregunta = models.CharField(max_length=200)
	def __str__(self):
		return self.textoPregunta

class Respuesta(models.Model):
	preguntaPerteneciente = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	textoRespuesta = models.CharField(max_length=200)
	def __str__(self):
		return self.preguntaPerteneciente.__str__()+" "+self.textoRespuesta