# En app.py - Actualización de la función generar_contenido_leccion
def generar_contenido_leccion(num):
    if num == 1:  # Lección especial para 2º grado
        return {
            'teoria': '''
            <div class="leccion-grado2">
                <h2>¡Aprendiendo el Abecedario!</h2>
                <div class="abecedario-animado">
                    <div class="letra" style="background-color: #ffcccc;">A</div>
                    <div class="letra" style="background-color: #ffddcc;">B</div>
                    <div class="letra" style="background-color: #ffeedd;">C</div>
                    <div class="letra" style="background-color: #ffffcc;">D</div>
                    <div class="letra" style="background-color: #ccffcc;">E</div>
                    <!-- ... continuaría con todo el abecedario ... -->
                </div>
                
                <h3>Las Super Vocales</h3>
                <div class="vocales-container">
                    <div class="vocal-card" data-vocal="A">
                        <div class="vocal-letra">A</div>
                        <div class="vocal-ejemplo">Avión</div>
                        <div class="vocal-imagen">✈️</div>
                    </div>
                    <div class="vocal-card" data-vocal="E">
                        <div class="vocal-letra">E</div>
                        <div class="vocal-ejemplo">Elefante</div>
                        <div class="vocal-imagen">🐘</div>
                    </div>
                    <!-- ... vocales restantes ... -->
                </div>
                
                <div class="consejo-ninos">
                    <p>¡Recuerda! Las vocales son las letras <strong>más importantes</strong> 
                    porque todas las palabras las necesitan para existir.</p>
                </div>
            </div>
            ''',
            'ejemplos': [
                {
                    'tipo': 'animales', 
                    'texto': 'Perro = P + E + R + R + O (5 letras, 2 vocales)'
                },
                {
                    'tipo': 'objetos', 
                    'texto': 'Mesa = M + E + S + A (4 letras, 2 vocales)'
                },
                {
                    'tipo': 'juego', 
                    'texto': 'Palabras con A: avión, araña, amigo, árbol'
                }
            ],
            'ejercicios': [
                {
                    'pregunta': '¿Cuántas vocales tiene la palabra "SOL"?',
                    'opciones': ['1 vocal', '2 vocales', '3 vocales'],
                    'respuesta': 1,
                    'explicacion': 'SOL tiene 1 vocal: O'
                },
                {
                    'pregunta': 'Selecciona todas las vocales',
                    'opciones': ['A', 'B', 'E', 'M', 'U'],
                    'respuesta': [0, 2, 4],
                    'tipo': 'seleccion_multiple'
                },
                {
                    'pregunta': 'Une cada vocal con una palabra que comience con ella',
                    'tipo': 'arrastrar',
                    'pares': [('A', 'Avión'), ('E', 'Elefante'), ('I', 'Iglú'), 
                             ('O', 'Oso'), ('U', 'Uvas')]
                }
            ]
        }
    # ... resto de lecciones ...

# En templates/leccion.html - Sección de Ejercicios adaptada
<div id="seccion-ejercicios" class="seccion-contenido">
    <h3>¡Practiquemos Juntos!</h3>
    
    {% for ejercicio in contenido.ejercicios %}
    <div class="ejercicio-ninos">
        <p class="pregunta">{{ ejercicio.pregunta }}</p>
        
        {% if ejercicio.tipo == 'seleccion_multiple' %}
        <div class="opciones-multiselect">
            {% for opcion in ejercicio.opciones %}
            <label>
                <input type="checkbox" name="ej{{ loop.index }}" value="{{ loop.index0 }}">
                {{ opcion }}
            </label>
            {% endfor %}
        </div>
        
        {% elif ejercicio.tipo == 'arrastrar' %}
        <div class="arrastrable-container">
            <div class="opciones-arrastre">
                {% for item in ejercicio.pares %}
                <div class="item-arrastre" data-valor="{{ item.0 }}">{{ item.0 }}</div>
                {% endfor %}
            </div>
            <div class="destinos-arrastre">
                {% for item in ejercicio.pares %}
                <div class="destino" data-valor="{{ item.0 }}">{{ item.1 }}</div>
                {% endfor %}
            </div>
        </div>
        
        {% else %}
        <div class="opciones-simples">
            {% for opcion in ejercicio.opciones %}
            <button class="btn-opcion" data-respuesta="{{ loop.index0 }}">
                {{ opcion }}
            </button>
            {% endfor %}
        </div>
        {% endif %}
        
        <div class="retroalimentacion" id="fb-ej{{ loop.index }}" style="display:none;">
            {% if ejercicio.explicacion %}
            <p>💡 {{ ejercicio.explicacion }}</p>
            {% endif %}
            <div class="animacion-feedback"></div>
        </div>
    </div>
    {% endfor %}
    
    <div class="recompensa-ejercicios">
        <p>Completa todos los ejercicios para desbloquear:</p>
        <div class="medalla-pequena">🥉</div>
        <p>¡Tu primera insignia de conocimiento!</p>
    </div>
</div>
