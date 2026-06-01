def generar_leccion_3grado():
    return {
        'teoria': '''
        <div class="leccion-grado3">
            <h2>¡Descubriendo las Sílabas!</h2>
            
            <div class="concepto-central">
                <div class="definicion">
                    <p>Una <strong>sílaba</strong> es un grupo de sonidos que pronunciamos juntos.</p>
                    <p>Cada sílaba tiene una <span class="destacado">vocal fuerte</span>.</p>
                </div>
                <div class="ejemplo-visual">
                    <div class="palabra-desglosada">
                        <div class="silaba destacada">CA</div>
                        <div class="silaba">SA</div>
                    </div>
                    <div class="separador">=</div>
                    <div class="palabra">CASA</div>
                    <div class="contador">2 sílabas</div>
                </div>
            </div>
            
            <h3>El Acento y la Tilde</h3>
            <div class="explicacion-acento">
                <div class="tarjeta-acento">
                    <div class="titulo-tarjeta">Sílaba tónica</div>
                    <div class="contenido-tarjeta">La sílaba que suena más fuerte</div>
                    <div class="ejemplo-tarjeta">ca<span class="tonica">SA</span></div>
                </div>
                
                <div class="tarjeta-acento">
                    <div class="titulo-tarjeta">Tilde</div>
                    <div class="contenido-tarjeta">Rayita sobre la vocal (´)</div>
                    <div class="ejemplo-tarjeta">can<span class="tonica">CIÓN</span></div>
                </div>
            </div>
            
            <div class="regla-importante">
                <h4>¡Regla de Oro!</h4>
                <p>Las palabras agudas llevan tilde cuando terminan en <strong>N</strong>, <strong>S</strong> o <strong>vocal</strong>:</p>
                <p>cam<i>ión</i> - rat<i>ón</i> - beb<i>é</i></p>
            </div>
        </div>
        ''',
        'ejemplos': [
            {
                'tipo': 'desglose_silabas', 
                'texto': 'Helicóptero = He-li-cóp-te-ro (5 sílabas)',
                'analisis': 'Sílaba tónica: "cóp"'
            },
            {
                'tipo': 'comparacion', 
                'texto': 'Casa (sin tilde) vs Canción (con tilde)',
                'analisis': 'Canción termina en N → lleva tilde'
            },
            {
                'tipo': 'error_comun', 
                'texto': 'Incorrecto: "arbol" → Correcto: "árbol"',
                'analisis': 'Árbol es palabra grave que NO termina en N/S/vocal'
            }
        ],
        'ejercicios': [
            {
                'pregunta': '¿Cuántas sílabas tiene "elefante"?',
                'opciones': ['3 sílabas', '4 sílabas', '5 sílabas'],
                'respuesta': 1,
                'tipo': 'seleccion_simple'
            },
            {
                'pregunta': 'Selecciona las palabras agudas que llevan tilde',
                'opciones': ['camión', 'pared', 'sofá', 'reloj', 'mandarín'],
                'respuesta': [0, 2],
                'tipo': 'seleccion_multiple',
                'explicacion': 'Camión y sofá terminan en N y vocal respectivamente'
            },
            {
                'pregunta': 'Separa en sílabas y marca la tónica:',
                'palabras': ['árbol', 'mesa', 'república', 'balón'],
                'tipo': 'separacion_silabas'
            },
            {
                'pregunta': 'Arrastra las palabras a su categoría correcta:',
                'categorias': ['Agudas con tilde', 'Agudas sin tilde', 'Graves'],
                'palabras': ['canción', 'pared', 'azúcar', 'reloj', 'sofá', 'árbol'],
                'solucion': {
                    'Agudas con tilde': ['canción', 'sofá'],
                    'Agudas sin tilde': ['reloj'],
                    'Graves': ['pared', 'azúcar', 'árbol']
                },
                'tipo': 'clasificacion'
            }
        ],
        'actividad_especial': {
            'titulo': 'Cazador de Sílabas Tónicas',
            'instrucciones': 'Escucha las palabras y marca la sílaba tónica',
            'palabras': ['teléfono', 'computadora', 'lápiz', 'ventana'],
            'tipo': 'audio_interactivo'
        }
    }
