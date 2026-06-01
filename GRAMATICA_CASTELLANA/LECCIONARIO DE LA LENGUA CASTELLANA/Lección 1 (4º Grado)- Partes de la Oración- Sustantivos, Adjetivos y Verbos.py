def generar_leccion_4grado():
    return {
        'teoria': '''
        <div class="leccion-grado4">
            <h2>¡Explorando las Partes de la Oración!</h2>
            
            <div class="categorias-gramaticales">
                <div class="categoria-card" data-categoria="sustantivo">
                    <div class="categoria-icono">📦</div>
                    <h3>Sustantivos</h3>
                    <p>Nombran personas, animales, cosas o ideas</p>
                    <div class="ejemplos-categoria">
                        <span>niño</span>
                        <span>ciudad</span>
                        <span>libertad</span>
                    </div>
                </div>
                
                <div class="categoria-card" data-categoria="adjetivo">
                    <div class="categoria-icono">🎨</div>
                    <h3>Adjetivos</h3>
                    <p>Describen características de los sustantivos</p>
                    <div class="ejemplos-categoria">
                        <span>alto</span>
                        <span>azul</span>
                        <span>interesante</span>
                    </div>
                </div>
                
                <div class="categoria-card" data-categoria="verbo">
                    <div class="categoria-icono">⚡</div>
                    <h3>Verbos</h3>
                    <p>Expresan acciones, estados o procesos</p>
                    <div class="ejemplos-categoria">
                        <span>correr</span>
                        <span>pensar</span>
                        <span>existir</span>
                    </div>
                </div>
            </div>
            
            <div class="analizador-oraciones">
                <h3>Análisis de Oraciones</h3>
                <div class="oracion-ejemplo">
                    "El rápido zorro marrón salta sobre el perro perezoso"
                </div>
                <div class="desglose-gramatical">
                    <div class="palabra" data-tipo="articulo">El</div>
                    <div class="palabra" data-tipo="adjetivo">rápido</div>
                    <div class="palabra" data-tipo="sustantivo">zorro</div>
                    <div class="palabra" data-tipo="adjetivo">marrón</div>
                    <div class="palabra" data-tipo="verbo">salta</div>
                    <div class="palabra" data-tipo="preposicion">sobre</div>
                    <div class="palabra" data-tipo="articulo">el</div>
                    <div class="palabra" data-tipo="sustantivo">perro</div>
                    <div class="palabra" data-tipo="adjetivo">perezoso</div>
                </div>
            </div>
            
            <div class="reglas-avanzadas">
                <h4>¡Secretos de los Adjetivos!</h4>
                <ul>
                    <li>Concuerdan en género y número con el sustantivo</li>
                    <li>Pueden ser calificativos, demostrativos o posesivos</li>
                    <li>Su posición cambia el énfasis: "casa grande" vs "gran casa"</li>
                </ul>
            </div>
        </div>
        ''',
        'ejemplos': [
            {
                'tipo': 'analisis_oracion', 
                'texto': 'Las inteligentes estudiantes leen libros fascinantes',
                'desglose': [
                    {'palabra': 'Las', 'tipo': 'artículo'},
                    {'palabra': 'inteligentes', 'tipo': 'adjetivo'},
                    {'palabra': 'estudiantes', 'tipo': 'sustantivo'},
                    {'palabra': 'leen', 'tipo': 'verbo'},
                    {'palabra': 'libros', 'tipo': 'sustantivo'},
                    {'palabra': 'fascinantes', 'tipo': 'adjetivo'}
                ]
            },
            {
                'tipo': 'comparacion', 
                'texto': 'Sustantivo concreto vs abstracto: mesa (concreto) vs amor (abstracto)',
                'analisis': 'Los sustantivos abstractos nombran ideas o sentimientos'
            },
            {
                'tipo': 'transformacion', 
                'texto': 'Transformar con adjetivos: casa → casa grande → casa enorme',
                'analisis': 'Los adjetivos añaden información específica'
            }
        ],
        'ejercicios': [
            {
                'pregunta': 'Identifica el verbo en la oración: "Los pájaros cantan al amanecer"',
                'opciones': ['Los', 'pájaros', 'cantan', 'amanecer'],
                'respuesta': 2,
                'tipo': 'seleccion_simple'
            },
            {
                'pregunta': 'Clasifica estas palabras:',
                'palabras': ['correr', 'feliz', 'montaña', 'rápidamente', 'bello'],
                'categorias': ['Sustantivo', 'Adjetivo', 'Verbo', 'Adverbio'],
                'solucion': {
                    'Sustantivo': ['montaña'],
                    'Adjetivo': ['feliz', 'bello'],
                    'Verbo': ['correr'],
                    'Adverbio': ['rápidamente']
                },
                'tipo': 'clasificacion'
            },
            {
                'pregunta': 'Completa la oración con el adjetivo adecuado:',
                'oracion': 'El _____ gato cazó un ratón _____',
                'opciones': {
                    'primer_espacio': ['negro', 'negra', 'negros'],
                    'segundo_espacio': ['pequeña', 'pequeño', 'pequeños']
                },
                'respuesta': ['negro', 'pequeño'],
                'tipo': 'completar_oracion'
            },
            {
                'pregunta': 'Crea una oración usando:',
                'elementos': [
                    {'tipo': 'sustantivo', 'palabra': 'científico'},
                    {'tipo': 'adjetivo', 'palabra': 'brillante'},
                    {'tipo': 'verbo', 'palabra': 'descubrir'}
                ],
                'tipo': 'creacion_oracion'
            }
        ],
        'actividad_especial': {
            'titulo': 'Cazador de Categorías Gramaticales',
            'instrucciones': 'Analiza párrafos reales e identifica las partes de la oración',
            'textos': [
                "La luna llena iluminaba el cielo nocturno con su luz plateada.",
                "Los valientes exploradores atravesaron la densa selva en busca de antiguas ruinas."
            ],
            'tipo': 'analisis_textual'
        }
    }
