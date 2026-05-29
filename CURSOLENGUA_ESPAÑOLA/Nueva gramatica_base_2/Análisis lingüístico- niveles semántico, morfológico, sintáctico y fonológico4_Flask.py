#linguistic-flask/
#├── app.py
#├── templates/
#│   ├── base.html
#│   ├── index.html
#│   ├── semantico.html
#│   ├── morfologico.html
#│   ├── sintactico.html
#│   └── fonologico.html
#└── static/
#    └── styles.css
# 4. static/styles.css (Estilos Básicos)
from flask import Flask, render_template, request, flash
from eng_to_ipa import convert as eng_to_ipa
import subprocess

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Análisis Semántico-Categorial
def analizar_semantico(texto):
    categorias = {
        'sustantivos': [],
        'verbos': [],
        'adjetivos': []
    }
    
    # Implementación básica (mejorar con NLTK/Spacy)
    for palabra in texto.split():
        if palabra.endswith(('ción', 'dad', 'ez')):
            categorias['sustantivos'].append(palabra)
        elif palabra.endswith(('ar', 'er', 'ir')):
            categorias['verbos'].append(palabra)
        elif palabra.endswith(('oso', 'al', 'ivo')):
            categorias['adjetivos'].append(palabra)
    
    return categorias

# Análisis Morfológico
def analizar_morfologia(palabra):
    resultados = {
        'raiz': palabra[:3],  # Implementación básica
        'morfemas': [],
        'derivaciones': []
    }
    
    if len(palabra) > 4:
        resultados['derivaciones'].append(f"{palabra} → {palabra}oso")
    
    return resultados

# Rutas Principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/semantico', methods=['GET', 'POST'])
def semantico():
    if request.method == 'POST':
        texto = request.form['texto']
        if not texto.strip():
            flash("¡Ingrese un texto para analizar!", "error")
            return render_template('semantico.html')
        
        resultado = analizar_semantico(texto)
        return render_template('semantico.html', resultado=resultado)
    
    return render_template('semantico.html')

@app.route('/morfologico', methods=['GET', 'POST'])
def morfologico():
    if request.method == 'POST':
        palabra = request.form['palabra']
        if not palabra.strip():
            flash("¡Ingrese una palabra!", "error")
            return render_template('morfologico.html')
        
        resultado = analizar_morfologia(palabra)
        return render_template('morfologico.html', resultado=resultado)
    
    return render_template('morfologico.html')

@app.route('/fonologico', methods=['GET', 'POST'])
def fonologico():
    if request.method == 'POST':
        texto = request.form['texto']
        if not texto.strip():
            flash("¡Ingrese un texto!", "error")
            return render_template('fonologico.html')
        
        # Conversión a IPA (inglés)
        ipa = eng_to_ipa(texto)
        return render_template('fonologico.html', ipa=ipa, texto=texto)
    
    return render_template('fonologico.html')

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Análisis Lingüístico</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <h1>Análisis Multinivel</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/semantico">Semántico</a>
            <a href="/morfologico">Morfológico</a>
            <a href="/fonologico">Fonológico</a>
        </nav>
    </header>
    
    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>Sistema de Análisis Lingüístico - © 2024</p>
    </footer>
</body>
</html>

{% extends "base.html" %}

{% block content %}
    <h2>Análisis Semántico-Categorial</h2>
    <form method="POST">
        <textarea name="texto" placeholder="Ingrese texto para análisis..." rows="4"></textarea>
        <button type="submit">Analizar</button>
    </form>
    
    {% if resultado %}
    <div class="resultados">
        <h3>Resultados:</h3>
        <div class="categoria">
            <h4>Sustantivos</h4>
            <ul>
                {% for palabra in resultado.sustantivos %}
                <li>{{ palabra }}</li>
                {% endfor %}
            </ul>
        </div>
        <!-- Repetir para verbos y adjetivos -->
    </div>
    {% endif %}
{% endblock %}

body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

nav {
    margin: 20px 0;
    padding: 10px;
    background: #f0f0f0;
}

.flash {
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
}

.flash.error {
    background: #ffebee;
    color: #b71c1c;
}

textarea {
    width: 100%;
    margin: 10px 0;
}

.resultados {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #ddd;
}
