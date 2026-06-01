from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de conocimiento de reglas gramaticales (estructura ampliable)
REGLAS = {
    'verbos': {
        'titulo': '⚡ La Aventura de los Verbos',
        'contenido': '''
        <p>Los verbos son guerreros que cambian su armadura según el tiempo:</p>
        <ul>
            <li><strong>Presente:</strong> Yo <mark>como</mark>, tú <mark>comes</mark></li>
            <li><strong>Pasado:</strong> Yo <mark>comí</mark>, tú <mark>comiste</mark></li>
            <li><strong>Futuro:</strong> Yo <mark>comeré</mark>, tú <mark>comerás</mark></li>
        </ul>
        <div class="gamification">
            <span class="badge bg-warning">Nivel 1</span>
            <div class="progress mt-2">
                <div class="progress-bar" style="width: 30%">XP: 30/100</div>
            </div>
        </div>
        '''
    },
    'acentos': {
        'titulo': '🎯 La Misión de los Acentos',
        'contenido': '''
        <p>Los acentos son faros que guían la pronunciación:</p>
        <ul>
            <li>Agudas: terminan en <mark>n</mark>, <mark>s</mark> o vocal (cam<strong>ión</strong>)</li>
            <li>Llanas: terminan en consonante ≠ n/s (ár<strong>bol</strong>)</li>
            <li>Esdrújulas: siempre llevan tilde (mág<strong>i</strong>co)</li>
        </ul>
        '''
    }
}

# Sistema de gamificación
logros = {
    'explorador': False,
    'gramatico': False
}

@app.route('/')
def home():
    """Página principal con navegación gamificada"""
    return render_template('index.html', modulos=REGLAS.keys())

@app.route('/modulo/<nombre_modulo>')
def modulo(nombre_modulo):
    """Página interactiva para cada regla gramatical"""
    contenido = REGLAS.get(nombre_modulo, {})
    if not contenido:
        return "Módulo no encontrado", 404
    return render_template('modulo.html', **contenido)

@app.route('/quiz/<tema>')
def cuestionario(tema):
    """Generador dinámico de quizzes"""
    preguntas = {
        'verbos': [
            {
                'pregunta': '¿Qué verbo está en futuro?',
                'opciones': ['Canté', 'Canto', 'Cantaré'],
                'respuesta': 2
            }
        ],
        'acentos': [
            {
                'pregunta': '¿Qué palabra es esdrújula?',
                'opciones': ['Casa', 'Árbol', 'Música'],
                'respuesta': 2
            }
        ]
    }
    return jsonify(random.sample(preguntas.get(tema, []), min(3, len(preguntas.get(tema, []))))

@app.route('/completar_mision', methods=['POST'])
def mision_completada():
    """Sistema de recompensas"""
    usuario = request.json.get('usuario')
    modulo = request.json.get('modulo')
    
    # Lógica de gamificación (ejemplo)
    if modulo == 'verbos':
        logros['explorador'] = True
        return jsonify({
            'nuevo_logro': 'Explorador de Verbos',
            'insignia': '🏅'
        })
    
    return jsonify({'estado': 'progreso_actualizado'})

if __name__ == '__main__':
    app.run(debug=True)
