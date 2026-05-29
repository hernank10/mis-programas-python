# Django adaptation of the Flask app

# 1. Set up Django project and app:
#    django-admin startproject lengua_project
#    cd lengua_project
#    python manage.py startapp ejercicios

# 2. Replace the contents of views.py in the 'ejercicios' app with:

from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import os

EJERCICIOS = [
    {"titulo": "Forme los femeninos de una serie de sustantivos.", "ejemplo": "Ej: el león → la leona", "modelo": "el doctor → la doctora"},
    {"titulo": "Separe sujeto y predicado.", "ejemplo": "Ej: El niño juega en el parque → sujeto: El niño / predicado: juega en el parque", "modelo": "Mi hermana cocina galletas → sujeto: Mi hermana / predicado: cocina galletas"},
    {"titulo": "Escriba la familia de palabras del sustantivo 'flor'.", "ejemplo": "Ej: flor, florero, florista, florido", "modelo": "flor, floral, florecer, floreado"},
    {"titulo": "Determine cuántos fonemas y cuántas letras tienen las palabras de la serie.", "ejemplo": "Ej: casa → 4 letras, 4 fonemas", "modelo": "niño → 4 letras, 4 fonemas"},
    {"titulo": "Señale los complementos del sujeto.", "ejemplo": "Ej: El gato negro de mi vecina → núcleo: gato / complementos: negro, de mi vecina", "modelo": "La niña rubia con trenzas → núcleo: niña / complementos: rubia, con trenzas"},
    {"titulo": "Señale la función de los siguientes grupos.", "ejemplo": "Ej: en el jardín → complemento circunstancial de lugar", "modelo": "por la tarde → complemento circunstancial de tiempo"},
    {"titulo": "Forme el plural de los siguientes grupos sustantivos.", "ejemplo": "Ej: el árbol frondoso → los árboles frondosos", "modelo": "la casa blanca → las casas blancas"},
    {"titulo": "Extraiga los sustantivos abstractos.", "ejemplo": "Ej: La alegría, la bondad, la tristeza", "modelo": "La inteligencia, la amistad, la justicia"},
    {"titulo": "Enuncie la regla de los verbos terminados en '-bir'.", "ejemplo": "Ej: Se escriben con 'b' todos los verbos terminados en '-bir', excepto hervir, servir y vivir", "modelo": "Los verbos en '-bir' llevan 'b', salvo excepciones como hervir, servir y vivir"},
    {"titulo": "Señale los núcleos de los grupos subrayados.", "ejemplo": "Ej: El coche rojo → núcleo: coche", "modelo": "Los niños alegres → núcleo: niños"},
    {"titulo": "Extraiga del texto los adjetivos relacionales.", "ejemplo": "Ej: escolar, laboral, presidencial", "modelo": "infantil, cultural, profesional"},
    {"titulo": "De la siguiente lista de adjetivos y verbos derive sustantivos abstractos.", "ejemplo": "Ej: feliz → felicidad; crear → creación", "modelo": "generoso → generosidad; leer → lectura"},
    {"titulo": "Identifique los adverbios y clasifíquelos.", "ejemplo": "Ej: rápidamente → modo; allí → lugar; hoy → tiempo", "modelo": "cuidadosamente → modo; lejos → lugar; entonces → tiempo"}
]

RESPUESTAS_PATH = os.path.join(os.path.dirname(__file__), 'respuestas_ejercicios.json')

def cargar_respuestas():
    if os.path.exists(RESPUESTAS_PATH):
        with open(RESPUESTAS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_respuestas(respuestas):
    with open(RESPUESTAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(respuestas[:100], f, indent=4, ensure_ascii=False)

def index(request):
    return render(request, 'ejercicios/index.html', {"ejercicios": enumerate(EJERCICIOS)})

def ejercicio(request, idx):
    ejercicio = EJERCICIOS[idx]
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta:
            respuestas = cargar_respuestas()
            respuestas.append({"titulo": ejercicio['titulo'], "respuesta": respuesta})
            guardar_respuestas(respuestas)
            return redirect('index')
    return render(request, 'ejercicios/ejercicio.html', {"ejercicio": ejercicio, "idx": idx})

def ver_respuestas(request):
    respuestas = cargar_respuestas()
    return render(request, 'ejercicios/respuestas.html', {"respuestas": respuestas})

# 3. Create templates: index.html, ejercicio.html, respuestas.html inside ejercicios/templates/ejercicios/
#    Use the Flask HTML as base and adapt to Django template syntax.

# 4. Add URL patterns in ejercicios/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ejercicio/<int:idx>/', views.ejercicio, name='ejercicio'),
    path('respuestas/', views.ver_respuestas, name='respuestas'),
]

# 5. Include these URLs in the project's urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ejercicios.urls')),
]
