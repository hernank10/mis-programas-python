<!-- numeros/templates/numeros/practice.html -->
{% extends 'numeros/base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="card">
        <div class="card-header">
            Práctica {{ current_index|add:1 }} de {{ total }}
            <div class="progress">
                <div class="progress-bar" style="width: {{ progress }}%"></div>
            </div>
        </div>
        
        <div class="card-body">
            <h5 class="card-title">{{ example.phrase }}</h5>
            <form method="post">
                {% csrf_token %}
                <input type="text" name="answer" class="form-control" required>
                <button type="submit" class="btn btn-primary mt-3">Comprobar</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}

numeros/
├── migrations/
├── templates/
│   ├── numeros/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── theory.html
│   │   ├── practice.html
│   │   ├── quiz.html
│   │   ├── example_form.html
│   │   └── examples_list.html
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
└── views.py


Sistema de modelos ORM con persistencia en base de datos

Autenticación de usuarios integrada

Panel de administración personalizable

Sistema de migraciones para cambios en esquema

Paginación automática en listados

Sistema de sesiones robusto

Arquitectura escalable MVT

Configuración para producción (DEBUG=False, allowed_hosts, etc.)

Comandos para configurar:

bash
django-admin startproject numerales
cd numerales
python manage.py startapp numeros
Cargar datos iniciales:

bash
python manage.py loaddata initial_data.json

Este sistema incluye todas las funcionalidades solicitadas y puede escalarse para:

Añadir usuarios personalizados

Implementar rankings globales

Crear aulas virtuales

Exportar/importar datos

Integrar API REST

Para desplegar en producción:

Configurar base de datos PostgreSQL

Configurar static files con WhiteNoise

Usar Gunicorn + Nginx

Implementar sistema de caché

Configurar HTTPS
