linguistic_django/
├── linguistic_app/
│   ├── migrations/
│   ├── templatetags/
│   │   └── linguistic_filters.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   └── linguistic/
│       ├── index.html
│       ├── semantico.html
│       ├── morfologico.html
│       ├── sintactico.html
│       └── fonologico.html
├── static/
│   └── css/
│       └── styles.css
└── manage.py

from django.db import models

class Analisis(models.Model):
    TIPOS = (
        ('SEM', 'Semántico'),
        ('MOR', 'Morfológico'),
        ('FON', 'Fonológico'),
    )
    tipo = models.CharField(max_length=3, choices=TIPOS)
    texto = models.TextField()
    resultado = models.JSONField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.texto[:20]}"


    from django import forms

class AnalisisSemanticoForm(forms.Form):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Ingrese texto para análisis semántico...'
        }),
        label=''
    )

class AnalisisMorfologicoForm(forms.Form):
    palabra = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: correr'
        }),
        label='Palabra a analizar'
    )



from django.shortcuts import render
from django.contrib import messages
from .forms import AnalisisSemanticoForm, AnalisisMorfologicoForm
from .models import Analisis
from eng_to_ipa import convert as eng_to_ipa

def analisis_semantico(request):
    if request.method == 'POST':
        form = AnalisisSemanticoForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            resultado = {
                'sustantivos': [pal for pal in texto.split() 
                              if pal.endswith(('ción', 'dad', 'ez'))],
                'verbos': [pal for pal in texto.split() 
                         if pal.endswith(('ar', 'er', 'ir'))],
                'adjetivos': [pal for pal in texto.split() 
                            if pal.endswith(('oso', 'al', 'ivo'))]
            }
            Analisis.objects.create(
                tipo='SEM',
                texto=texto,
                resultado=resultado
            )
            return render(request, 'linguistic/semantico.html', {
                'form': form,
                'resultado': resultado
            })
    else:
        form = AnalisisSemanticoForm()
    return render(request, 'linguistic/semantico.html', {'form': form})

def analisis_morfologico(request):
    resultado = None
    if request.method == 'POST':
        form = AnalisisMorfologicoForm(request.POST)
        if form.is_valid():
            palabra = form.cleaned_data['palabra']
            resultado = {
                'raiz': palabra[:3],
                'morfemas': [],
                'derivaciones': [f"{palabra} → {palabra}oso"] if len(palabra) > 4 else []
            }
            Analisis.objects.create(
                tipo='MOR',
                texto=palabra,
                resultado=resultado
            )
    else:
        form = AnalisisMorfologicoForm()
    return render(request, 'linguistic/morfologico.html', {
        'form': form,
        'resultado': resultado
    })


from django.urls import path
from . import views

urlpatterns = [
    path('semantico/', views.analisis_semantico, name='semantico'),
    path('morfologico/', views.analisis_morfologico, name='morfologico'),
    # Añadir rutas para fonológico y sintáctico
]


{% extends "base.html" %}

{% block content %}
<div class="container">
    <h2 class="my-4">Análisis Semántico</h2>
    
    <form method="post" class="mb-4">
        {% csrf_token %}
        {{ form.texto }}
        <button type="submit" class="btn btn-primary mt-2">Analizar</button>
    </form>

    {% if resultado %}
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Resultados</h5>
            
            <div class="row">
                <div class="col-md-4">
                    <h6>Sustantivos</h6>
                    <ul class="list-group">
                        {% for sust in resultado.sustantivos %}
                        <li class="list-group-item">{{ sust }}</li>
                        {% endfor %}
                    </ul>
                </div>
                <!-- Repetir para verbos y adjetivos -->
            </div>
        </div>
    </div>
    {% endif %}
</div>
{% endblock %}

from django import template

register = template.Library()

@register.filter
def formato_ipa(texto):
    # Lógica personalizada para formato fonético
    return f"/{texto}/"

