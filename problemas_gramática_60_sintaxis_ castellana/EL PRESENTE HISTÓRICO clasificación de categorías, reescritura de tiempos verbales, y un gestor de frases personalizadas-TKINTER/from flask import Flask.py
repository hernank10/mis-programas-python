# app.py
from flask import Flask, render_template, request, session, redirect, url_for
import json
import random
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Cargar datos
def cargar_ejemplos(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

EJEMPLOS_BASE = cargar_ejemplos('ejemplos_base.json')
EJEMPLOS_USUARIO = cargar_ejemplos('ejemplos_usuario.json')

def guardar_ejemplos():
    with open('ejemplos_usuario.json', 'w', encoding='utf-8') as f:
        json.dump(EJEMPLOS_USUARIO, f, ensure_ascii=False)

# Rutas principales
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/practicar')
def practicar():
    session['ejemplos_practica'] = EJEMPLOS_BASE + EJEMPLOS_USUARIO
    session['indice_practica'] = 0
    session['aciertos'] = 0
    return redirect(url_for('mostrar_ejemplo'))

@app.route('/ejemplo')
def mostrar_ejemplo():
    indice = session.get('indice_practica', 0)
    ejemplos = session.get('ejemplos_practica', [])
    
    if indice >= len(ejemplos):
        return render_template('resultado_practica.html', 
                            total=len(ejemplos),
                            aciertos=session['aciertos'])
    
    ejemplo = ejemplos[indice]
    return render_template('practica.html', 
                         ejemplo=ejemplo,
                         indice=indice+1,
                         total=len(ejemplos))

@app.route('/verificar', methods=['POST'])
def verificar():
    respuesta = request.form.get('respuesta', '').strip()
    indice = session['indice_practica']
    ejemplos = session['ejemplos_practica']
    
    correcto = (respuesta.lower() == ejemplos[indice]['respuesta'].lower())
    if correcto:
        session['aciertos'] += 1
    
    session['indice_practica'] += 1
    return json.dumps({
        'correcto': correcto,
        'respuesta_correcta': ejemplos[indice]['respuesta']
    })

@app.route('/conceptos')
def conceptos():
    return render_template('conceptos.html')

@app.route('/cuestionario')
def cuestionario():
    session['preguntas'] = random.sample(EJEMPLOS_BASE + EJEMPLOS_USUARIO, 10)
    session['indice_pregunta'] = 0
    session['puntuacion'] = 0
    return redirect(url_for('mostrar_pregunta'))

@app.route('/pregunta')
def mostrar_pregunta():
    indice = session.get('indice_pregunta', 0)
    if indice >= len(session['preguntas']):
        return render_template('resultado_cuestionario.html', 
                            puntuacion=session['puntuacion'])
    
    pregunta = session['preguntas'][indice]
    return render_template('cuestionario.html', 
                        pregunta=pregunta,
                        numero=indice+1)

@app.route('/verificar_categoria', methods=['POST'])
def verificar_categoria():
    categoria = request.form.get('categoria')
    indice = session['indice_pregunta']
    pregunta = session['preguntas'][indice]
    
    correcto = (categoria == pregunta['categoria'])
    if correcto:
        session['puntuacion'] += 1
    
    session['indice_pregunta'] += 1
    return json.dumps({
        'correcto': correcto,
        'categoria_correcta': pregunta['categoria'].capitalize()
    })

@app.route('/gestionar', methods=['GET', 'POST'])
def gestionar():
    if request.method == 'POST':
        nuevo = {
            'frase': request.form['frase'],
            'respuesta': request.form['respuesta'],
            'categoria': request.form['categoria']
        }
        EJEMPLOS_USUARIO.append(nuevo)
        guardar_ejemplos()
        return redirect(url_for('gestionar'))
    
    return render_template('gestion.html', ejemplos=EJEMPLOS_USUARIO)

if __name__ == '__main__':
    app.run(debug=True)
