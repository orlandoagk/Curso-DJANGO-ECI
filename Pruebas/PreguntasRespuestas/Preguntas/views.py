from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Pregunta,Respuesta
from django.template import loader

def mostrarPreguntas(request):
	preguntas = Pregunta.objects.all()
	return render(request,'mostrarPreguntas.html',{'preguntas':preguntas})

def mostrarRespuestas(request,pregunta_id):
	pregunta = get_object_or_404(Pregunta,pk=pregunta_id)
	respuestas = Respuesta.objects.all().filter(preguntaPerteneciente=pregunta)
	return render(request,'mostrarRespuestas.html',{'respuestas':respuestas,'pregunta':pregunta})