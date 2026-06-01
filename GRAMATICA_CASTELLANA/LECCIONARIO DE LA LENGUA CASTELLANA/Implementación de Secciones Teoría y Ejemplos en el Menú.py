# Actualización en app.py
@app.route('/leccion/<int:leccion_id>')
def ver_leccion(leccion_id):
    usuario = Usuario.query.get(session['usuario_id'])
    leccion = Leccion.query.get(leccion_id)
    
    # Verificar progreso secuencial
    if leccion_id > usuario.progreso + 1:
        return redirect(url_for('ver_leccion', leccion_id=usuario.progreso + 1))
    
    # Obtener contenido estructurado
    contenido = {
        'teoria': leccion.contenido,
        'ejemplos': obtener_ejemplos(leccion_id),
        'ejercicios': eval(leccion.ejercicios) if leccion.ejercicios else []
    }
    
    return render_template('leccion.html', 
                          leccion=leccion, 
                          usuario=usuario,
                          contenido=contenido)

def obtener_ejemplos(leccion_id):
    """Genera ejemplos contextualizados según el nivel"""
    nivel = min(leccion_id // 10 + 1, 10)
    
    if nivel <= 3:  # Primaria básica
        return [
            {"tipo": "simple", "texto": "El niño juega en el parque."},
            {"tipo": "comparativo", "texto": "Comparación correcta: 'más alto que' vs incorrecta: 'más alto de'"}
        ]
    elif nivel <= 6:  # Primaria avanzada
        return [
            {"tipo": "estructura", "texto": "Sujeto + Verbo + Complemento: 'La profesora explica la lección'"},
            {"tipo": "error_comun", "texto": "Haber vs A ver: 'Vamos a ver una película' (correcto)"}
        ]
    else:  # Secundaria y Bachillerato
        return [
            {"tipo": "academico", "texto": "En ensayos: 'Se evidencia que...' en lugar de 'Yo pienso que...'"},
            {"tipo": "complejo", "texto": "Uso del subjuntivo: 'Es necesario que estudies más'"},
            {"tipo": "literario", "texto": "Metáfora: 'El tiempo es oro'"}
        ]

# Actualización en templates/leccion.html
<div class="leccion-container">
    <h1>{{ leccion.titulo }}</h1>
    
    <!-- Menú de secciones -->
    <nav class="menu-secciones">
        <button class="btn-seccion active" data-seccion="teoria">📚 Teoría</button>
        <button class="btn-seccion" data-seccion="ejemplos">💡 Ejemplos</button>
        <button class="btn-seccion" data-seccion="ejercicios">✏️ Ejercicios</button>
    </nav>
    
    <!-- Contenido de Teoría -->
    <div id="seccion-teoria" class="seccion-contenido activa">
        <div class="teoria-content">
            {{ contenido.teoria|safe }}
        </div>
        <div class="consejo-didactico">
            <strong>Consejo de aprendizaje:</strong> 
            <p>{{ obtener_consejo(leccion.id) }}</p>
        </div>
    </div>
    
    <!-- Contenido de Ejemplos -->
    <div id="seccion-ejemplos" class="seccion-contenido">
        <h3>Ejemplos Prácticos</h3>
        <div class="ejemplos-container">
            {% for ejemplo in contenido.ejemplos %}
            <div class="ejemplo-card">
                <div class="ejemplo-header">
                    <span class="tipo-ejemplo">{{ ejemplo.tipo|replace('_', ' ')|title }}</span>
                </div>
                <div class="ejemplo-body">
                    {{ ejemplo.texto }}
                </div>
                <div class="ejemplo-analisis">
                    <button class="btn-analizar">🔍 Analizar estructura</button>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="crea-tu-ejemplo">
            <h4>Crea tu propio ejemplo:</h4>
            <textarea class="ejemplo-usuario" placeholder="Escribe aquí un ejemplo aplicando la regla..."></textarea>
            <button class="btn-verificar">✓ Verificar</button>
        </div>
    </div>
    
    <!-- Contenido de Ejercicios (existente) -->
    <div id="seccion-ejercicios" class="seccion-contenido">
        <!-- ... código previo de ejercicios ... -->
    </div>
    
    <!-- Navegación -->
    <div class="leccion-navigation">
        <!-- ... botones de navegación ... -->
    </div>
</div>

# Función de apoyo para consejos didácticos
def obtener_consejo(leccion_id):
    consejos = {
        1: "Recuerda que las vocales son la base de todas las palabras.",
        15: "Presta atención a la acentuación en palabras interrogativas: ¿Cómo? ¿Qué?",
        50: "Para dominar B/V, piensa en palabras relacionadas: 'biblioteca' → libro → con B",
        75: "El subjuntivo expresa deseos o posibilidades, no hechos concretos.",
        99: "Revisa siempre la concordancia sujeto-verbo en tus textos."
    }
    return consejos.get(leccion_id, "Practica estos conceptos con ejercicios diarios.")
