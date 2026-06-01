from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_educativa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///espanol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    progreso = db.Column(db.Integer, default=0)  # Lección actual
    puntuacion = db.Column(db.Integer, default=0)
    medalla_dorada = db.Column(db.Boolean, default=False)

class Leccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    ejercicios = db.Column(db.Text)  # JSON con ejercicios
    nivel_dificultad = db.Column(db.Integer, default=1)

class EvaluacionFinal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    puntuacion = db.Column(db.Integer)
    aprobado = db.Column(db.Boolean)

# Crear base de datos al iniciar (solo en desarrollo)
@app.before_first_request
def crear_db():
    db.create_all()
    # Crear lecciones si no existen
    if Leccion.query.count() == 0:
        for i in range(1, 101):
            nueva_leccion = Leccion(
                titulo=f"Lección {i}: {obtener_titulo_por_numero(i)}",
                contenido=generar_contenido_leccion(i),
                ejercicios=generar_ejercicios(i),
                nivel_dificultad=min(i//10 + 1, 10)
            db.session.add(nueva_leccion)
        db.session.commit()

def obtener_titulo_por_numero(num):
    temas = {
        1: "El Abecedario y Vocales",
        10: "Acentuación Básica",
        20: "Los Verbos Regulares",
        30: "Pretérito Perfecto",
        40: "Subjuntivo Presente",
        50: "Ortografía de B/V",
        60: "Usos de G/J",
        70: "Puntuación Avanzada",
        80: "Reglas de la R/RR",
        90: "Concordancias Complejas",
        99: "Repaso Final",
        100: "Evaluación Final"
    }
    return temas.get(num, f"Reglas Gramaticales Nivel {num}")

def generar_contenido_leccion(num):
    # Contenido educativo estructurado por niveles
    if num <= 10:
        return f"<h3>Fundamentos del Castellano</h3><p>Lección introductoria sobre {obtener_titulo_por_numero(num)}...</p>"
    elif num <= 50:
        return f"<h3>Gramática Intermedia</h3><p>Profundizando en {obtener_titulo_por_numero(num)} con ejemplos prácticos...</p>"
    else:
        return f"<h3>Dominio del Idioma</h3><p>Lección avanzada sobre {obtener_titulo_por_numero(num)} para preparación universitaria...</p>"

def generar_ejercicios(num):
    # Generar ejercicios según nivel de dificultad
    ejercicios = []
    for i in range(3 + (num//20)):  # Más ejercicios en lecciones avanzadas
        ejercicios.append({
            'pregunta': f"Ejercicio {i+1} sobre {obtener_titulo_por_numero(num)}",
            'opciones': random.sample(["Opción Correcta", "Incorrecta 1", "Incorrecta 2", "Incorrecta 3"], 4),
            'respuesta': 0
        })
    return str(ejercicios)

# Rutas principales
@app.route('/')
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('registro'))
    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('inicio.html', usuario=usuario, lecciones=Leccion.query.all())

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nuevo_usuario = Usuario(nombre=request.form['nombre'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        session['usuario_id'] = nuevo_usuario.id
        return redirect(url_for('inicio'))
    return render_template('registro.html')

@app.route('/leccion/<int:leccion_id>')
def ver_leccion(leccion_id):
    usuario = Usuario.query.get(session['usuario_id'])
    leccion = Leccion.query.get(leccion_id)
    
    # Verificar progreso secuencial
    if leccion_id > usuario.progreso + 1:
        return redirect(url_for('ver_leccion', leccion_id=usuario.progreso + 1))
    
    return render_template('leccion.html', leccion=leccion, usuario=usuario)

@app.route('/completar_leccion/<int:leccion_id>', methods=['POST'])
def completar_leccion(leccion_id):
    usuario = Usuario.query.get(session['usuario_id'])
    
    # Actualizar progreso
    if leccion_id == usuario.progreso + 1:
        usuario.progreso = leccion_id
        usuario.puntuacion += 10  # 10 puntos por lección completada
        
        # Recompensas especiales cada 10 lecciones
        if leccion_id % 10 == 0:
            usuario.puntuacion += 50  # Bonus por hito
        
        db.session.commit()
    
    # Redirigir a siguiente lección o evaluación final
    if leccion_id < 100:
        return redirect(url_for('ver_leccion', leccion_id=leccion_id + 1))
    else:
        return redirect(url_for('evaluacion_final'))

@app.route('/evaluacion_final')
def evaluacion_final():
    usuario = Usuario.query.get(session['usuario_id'])
    if usuario.progreso < 100:
        return redirect(url_for('ver_leccion', leccion_id=usuario.progreso + 1))
    
    # Generar examen final con preguntas de todas las lecciones
    preguntas = []
    for leccion in Leccion.query.filter(Leccion.id < 100).order_by(db.func.random()).limit(50):
        ejercicios = eval(leccion.ejercicios)
        preguntas.append(random.choice(ejercicios))
    
    return render_template('evaluacion.html', preguntas=preguntas)

@app.route('/entregar_evaluacion', methods=['POST'])
def entregar_evaluacion():
    usuario = Usuario.query.get(session['usuario_id'])
    respuestas = request.form
    correctas = 0
    total = len(respuestas)
    
    # Calcular puntuación
    for pregunta_id, respuesta in respuestas.items():
        leccion_id = int(pregunta_id.split('_')[1])
        leccion = Leccion.query.get(leccion_id)
        ejercicios = eval(leccion.ejercicios)
        ejercicio = ejercicios[int(pregunta_id.split('_')[2])]
        
        if int(respuesta) == ejercicio['respuesta']:
            correctas += 1
    
    porcentaje = (correctas / total) * 100
    
    # Guardar resultados
    evaluacion = EvaluacionFinal(
        usuario_id=usuario.id,
        puntuacion=porcentaje,
        aprobado=porcentaje >= 85
    )
    db.session.add(evaluacion)
    
    # Otorgar medalla dorada si aprueba
    if porcentaje >= 85:
        usuario.medalla_dorada = True
        usuario.puntuacion += 1000  # Gran premio
    
    db.session.commit()
    
    return render_template('resultado_evaluacion.html', 
                          porcentaje=porcentaje, 
                          aprobado=porcentaje >= 85,
                          usuario=usuario)

@app.route('/perfil')
def perfil():
    usuario = Usuario.query.get(session['usuario_id'])
    medallas = []
    
    # Medallas por hitos
    if usuario.progreso >= 10:
        medallas.append({'nombre': 'Bronce', 'icono': '🥉'})
    if usuario.progreso >= 50:
        medallas.append({'nombre': 'Plata', 'icono': '🥈'})
    if usuario.medalla_dorada:
        medallas.append({'nombre': 'ORO', 'icono': '🥇', 'especial': True})
    
    return render_template('perfil.html', usuario=usuario, medallas=medallas)

if __name__ == '__main__':
    app.run(debug=True)
