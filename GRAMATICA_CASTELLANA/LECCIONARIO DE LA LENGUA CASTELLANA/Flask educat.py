from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Datos iniciales de ejemplo (puedes expandirlos por nivel y tema)
ejercicios = {
    "basico": [
        {"pregunta": "¿Cuál es la forma correcta?", "opciones": ["votar", "botar"], "respuesta": "votar"},
        {"pregunta": "Selecciona la palabra con B:", "opciones": ["baca", "vaca"], "respuesta": "baca"}
    ],
    "intermedio": [
        {"pregunta": "Completa: El libro ___ interesante.", "opciones": ["es", "esta"], "respuesta": "es"}
    ],
    "avanzado": [
        {"pregunta": "¿Cuál es una oración compuesta?", "opciones": ["Juan lee.", "Juan lee y escribe."], "respuesta": "Juan lee y escribe."}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ejercicios/<nivel>')
def get_ejercicios(nivel):
    return jsonify(ejercicios.get(nivel, []))

@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('static', 'service-worker.js')

if __name__ == '__main__':
    app.run(debug=True)
