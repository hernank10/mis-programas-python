# Estructura básica para una app Django que implementa las funcionalidades

# 1. Crear el proyecto y la app:
# django-admin startproject sintaxis_project
# cd sintaxis_project
# python manage.py startapp ejercicios

# 2. Agregar 'ejercicios' al INSTALLED_APPS en settings.py

# 3. Código de views.py en la app 'ejercicios'
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

EJEMPLOS = [
    ("El hombre honrado", "adjetivo"),
    ("La dama duende", "adjetivo"),
    ("Las orillas del Maipo", "complemento"),
    ("La sin par Dulcinea", "complemento"),
    ("Aquel gran bulto que allí se ve", "proposición"),
    ("La persona a quien vimos ayer en el paseo", "proposición"),
    ("La campiña por donde transitábamos", "proposición")
]

DIAPO_TEXTO = {
    "adjetivo": ["El hombre honrado", "La dama duende"],
    "complemento": ["Las orillas del Maipo", "La sin par Dulcinea"],
    "proposición": ["Aquel gran bulto que allí se ve", "La persona a quien vimos ayer en el paseo"]
}

CREADAS = []

def index(request):
    ejemplo = random.choice(EJEMPLOS)
    request.session['ejemplo_actual'] = ejemplo
    return render(request, 'index.html', {'ejemplo': ejemplo[0]})

def clasificar(request):
    if request.method == 'POST':
        seleccion = request.POST.get('tipo')
        actual = request.session.get('ejemplo_actual')
        correcto = actual[1]
        resultado = "Correcto" if seleccion == correcto else f"Incorrecto, era: {correcto}"
        return render(request, 'resultado.html', {'resultado': resultado})
    return redirect('index')

def diapositiva(request):
    return render(request, 'diapositiva.html', {'diapositiva': DIAPO_TEXTO})

def crear(request):
    if request.method == 'POST':
        texto = request.POST.get('oracion')
        tipo = request.POST.get('tipo')
        if texto:
            CREADAS.append((texto, tipo))
            return render(request, 'creadas.html', {'creadas': CREADAS})
    return render(request, 'crear.html')

def creadas(request):
    return render(request, 'creadas.html', {'creadas': CREADAS})

# 4. Crear urls.py en la app ejercicios
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clasificar/', views.clasificar, name='clasificar'),
    path('diapositiva/', views.diapositiva, name='diapositiva'),
    path('crear/', views.crear, name='crear'),
    path('creadas/', views.creadas, name='creadas')
]

# 5. Incluir estas urls en el urls.py del proyecto principal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ejercicios.urls')),
]

# 6. Crear las plantillas HTML correspondientes (index.html, resultado.html, diapositiva.html, crear.html, creadas.html) en la carpeta templates de la app.
# Cada plantilla debe tener formularios para enviar datos y mostrar resultados, similar al ejemplo en Flask.

# ¿Deseas que también genere el contenido de las plantillas HTML?
