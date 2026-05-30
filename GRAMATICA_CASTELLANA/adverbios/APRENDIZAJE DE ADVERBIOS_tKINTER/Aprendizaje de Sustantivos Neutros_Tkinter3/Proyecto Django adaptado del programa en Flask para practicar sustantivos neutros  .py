# Proyecto Django adaptado del programa en Flask para practicar sustantivos neutros

# Pasos básicos:
# 1. Crear un nuevo proyecto Django: django-admin startproject sustantivos
# 2. Crear una nueva app: python manage.py startapp ejercicios
# 3. Agregar 'ejercicios' al INSTALLED_APPS en settings.py
# 4. Crear las vistas, modelos y templates

# Este archivo representa una vista principal del programa en Django

# archivo: ejercicios/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json
import os

# Cargar ejemplos base
EJEMPLOS_BASE = [
    {"texto": "Esto me parece injusto.", "categoria": "Demostrativo neutro"},
    {"texto": "Eso no tiene sentido alguno.", "categoria": "Demostrativo neutro"},
    {"texto": "Aquello fue un momento inolvidable.", "categoria": "Demostrativo neutro"},
    {"texto": "Ello no justifica su comportamiento.", "categoria": "Demostrativo neutro"},
    {"texto": "Lo importante es participar.", "categoria": "Demostrativo neutro"},
    {"texto": "Cantar me relaja por las noches.", "categoria": "Infinitivo sustantivado"},
    {"texto": "El comer saludable mejora la salud.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Saber esperar también es sabiduría.", "categoria": "Infinitivo sustantivado"},
    {"texto": "Mucho se dijo, pero poco se hizo.", "categoria": "Cantidad"},
    {"texto": "Nada puede detenernos ahora.", "categoria": "Concepto general"},
    {"texto": "El vivir con miedo no es vivir.", "categoria": "Construcción con artículo"},
]

ARCHIVO_EJEMPLOS = os.path.join(os.path.dirname(__file__), 'usuario_ejemplos.json')

def cargar_ejemplos_usuario():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_ejemplo_usuario(nuevo):
    ejemplos = cargar_ejemplos_usuario()
    if len(ejemplos) < 100:
        ejemplos.append(nuevo)
        with open(ARCHIVO_EJEMPLOS, 'w', encoding='utf-8') as f:
            json.dump(ejemplos, f, ensure_ascii=False, indent=4)

# Vistas principales
def index(request):
    return render(request, 'index.html')

def diapositiva(request):
    return render(request, 'diapositiva.html')

def practicar(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria', '').strip().lower()
        oracion = request.POST.get('oracion', '')
        actual = json.loads(request.POST.get('ejemplo_json'))
        correcto = categoria == actual['categoria'].lower()
        return render(request, 'resultado.html', {
            'correcto': correcto,
            'oracion': oracion,
        })
    else:
        ejemplo = random.choice(EJEMPLOS_BASE)
        return render(request, 'practicar.html', {
            'ejemplo': ejemplo,
            'ejemplo_json': json.dumps(ejemplo)
        })

def cuestionario(request):
    if request.method == 'POST':
        total = int(request.POST.get('total', 0))
        puntaje = 0
        for i in range(total):
            user_respuesta = request.POST.get(f'respuesta{i}', '').strip().lower()
            correct_categoria = request.POST.get(f'categoria{i}', '').lower()
            if user_respuesta == correct_categoria:
                puntaje += 1
        return render(request, 'cuestionario_resultado.html', {
            'puntaje': puntaje,
            'total': total
        })
    else:
        seleccionados = random.sample(EJEMPLOS_BASE, min(5, len(EJEMPLOS_BASE)))
        return render(request, 'cuestionario.html', {
            'ejemplos': seleccionados
        })

def agregar(request):
    mensaje = ''
    if request.method == 'POST':
        texto = request.POST.get('texto')
        categoria = request.POST.get('categoria')
        guardar_ejemplo_usuario({"texto": texto, "categoria": categoria})
        mensaje = "Ejemplo agregado correctamente."
    return render(request, 'agregar.html', { 'mensaje': mensaje })

def ver(request):
    ejemplos = cargar_ejemplos_usuario()
    return render(request, 'ver.html', { 'ejemplos': ejemplos })
