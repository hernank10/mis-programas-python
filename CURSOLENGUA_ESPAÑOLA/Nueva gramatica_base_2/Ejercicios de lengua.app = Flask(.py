from flask import Flask, request, jsonify, render_template_string
import json
import os

app = Flask(__name__)

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

RESPUESTAS_PATH = 'respuestas_ejercicios.json'

def cargar_respuestas():
    if os.path.exists(RESPUESTAS_PATH):
        with open(RESPUESTAS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_respuestas(respuestas):
    with open(RESPUESTAS_PATH, 'w', encoding='utf-8') as f:
        json.dump(respuestas[:100], f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    html = '''
    <h1>Ejercicios de Lengua</h1>
    <ul>
    {% for i, e in enumerate(ejercicios) %}
        <li><a href="/ejercicio/{{ i }}">{{ e.titulo }}</a></li>
    {% endfor %}
    </ul>
    <a href="/respuestas">Ver respuestas guardadas</a>
    '''
    return render_template_string(html, ejercicios=EJERCICIOS)

@app.route('/ejercicio/<int:idx>', methods=['GET', 'POST'])
def ejercicio(idx):
    if request.method == 'POST':
        respuesta = request.form.get('respuesta')
        if respuesta:
            respuestas = cargar_respuestas()
            respuestas.append({"titulo": EJERCICIOS[idx]['titulo'], "respuesta": respuesta})
            guardar_respuestas(respuestas)
            return "Respuesta guardada. <a href='/'>Volver</a>"
    
    ej = EJERCICIOS[idx]
    html = f'''
    <h2>{ej['titulo']}</h2>
    <p><strong>Ejemplo:</strong> {ej['ejemplo']}</p>
    <p><strong>Modelo:</strong> {ej['modelo']}</p>
    <form method="post">
        <label>Escriba una respuesta similar:</label><br>
        <textarea name="respuesta" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Guardar">
    </form>
    <a href='/'>Volver</a>
    '''
    return html

@app.route('/respuestas')
def ver_respuestas():
    respuestas = cargar_respuestas()
    html = '<h2>Respuestas guardadas</h2><ul>'
    for r in respuestas:
        html += f"<li><strong>{r['titulo']}:</strong> {r['respuesta']}</li>"
    html += '</ul><a href="/">Volver</a>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
