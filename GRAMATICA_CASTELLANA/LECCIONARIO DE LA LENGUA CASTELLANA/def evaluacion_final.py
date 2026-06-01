def evaluacion_final():
    return {
        'estructura': '''
        <div class="evaluacion-final">
            <h2>🏆 Evaluación Final del Dominio del Castellano</h2>
            
            <div class="informacion-evaluacion">
                <div class="requisito">
                    <div class="icono">📚</div>
                    <h4>Requisito para la Medalla Dorada</h4>
                    <p>Obtener al menos 85% en esta evaluación</p>
                </div>
                
                <div class="detalles">
                    <div class="dato">
                        <div class="valor">100</div>
                        <div class="etiqueta">Lecciones completadas</div>
                    </div>
                    <div class="dato">
                        <div class="valor">500+</div>
                        <div class="etiqueta">Ejercicios resueltos</div>
                    </div>
                    <div class="dato">
                        <div class="valor">2000+</div>
                        <div class="etiqueta">Puntos de XP</div>
                    </div>
                </div>
            </div>
            
            <div class="secciones-evaluacion">
                <div class="seccion">
                    <h3>Parte 1: Conocimientos Fundamentales (30%)</h3>
                    <ul>
                        <li>Gramática avanzada</li>
                        <li>Ortografía compleja</li>
                        <li>Morfosintaxis</li>
                        <li>25 preguntas - 20 minutos</li>
                    </ul>
                </div>
                
                <div class="seccion">
                    <h3>Parte 2: Expresión Escrita (40%)</h3>
                    <ul>
                        <li>Ensayo argumentativo</li>
                        <li>Corrección de textos</li>
                        <li>Creación literaria</li>
                        <li>1 hora</li>
                    </ul>
                </div>
                
                <div class="seccion">
                    <h3>Parte 3: Análisis Crítico (30%)</h3>
                    <ul>
                        <li>Comentario de texto</li>
                        <li>Detección de falacias</li>
                        <li>Análisis discursivo</li>
                        <li>45 minutos</li>
                    </ul>
                </div>
            </div>
            
            <div class="preparacion-recomendada">
                <h3>Preparación Recomendada:</h3>
                <ol>
                    <li>Revisar las lecciones 10, 50 y 90</li>
                    <li>Practicar con simulacros cronometrados</li>
                    <li>Consultar tu cuaderno de logros</li>
                </ol>
            </div>
        </div>
        ''',
        'simulador': {
            'modo': 'cronometrado',
            'duracion_total': 125,  # minutos
            'preguntas': [
                {
                    'tipo': 'seleccion_multiple',
                    'pregunta': 'Identifique la oración con error de concordancia:',
                    'opciones': [
                        'Las personas que asistieron al evento recibieron un obsequio',
                        'Cada uno de los estudiantes presentaron sus trabajos',
                        'El grupo de investigadores publicó sus hallazgos'
                    ],
                    'respuesta': 1,
                    'explicacion': '"Cada uno" es singular, requiere "presentó"'
                },
                {
                    'tipo': 'correccion_texto',
                    'texto': 'El libro que me recomendastes es excelente, aunque es un poco complicado de leerlo',
                    'errores': 3,
                    'solucion': 'El libro que me recomendaste es excelente, aunque es un poco complicado de leer'
                },
                {
                    'tipo': 'analisis_texto',
                    'texto': '"La educación no es preparación para la vida; la educación es la vida misma." - John Dewey',
                    'preguntas': [
                        'Identifique la figura retórica principal',
                        'Explique la tesis del autor en sus propias palabras',
                        'Relacione con un principio pedagógico actual'
                    ]
                }
            ],
            'ensayo': {
                'temas': [
                    "El impacto de la inteligencia artificial en la escritura creativa",
                    "La evolución del español en la era digital",
                    "La importancia de preservar las variedades dialectales"
                ],
                'rúbrica': {
                    'coherencia': 25,
                    'profundidad': 30,
                    'correccion': 20,
                    'originalidad': 25
                }
            }
        },
        'sistema_medalla': {
            'requisitos': [
                'Completar 100 lecciones',
                'Obtener ≥85% en evaluación final',
                'Tener ≥1800 XP',
                'Entregar proyecto final'
            ],
            'beneficios': [
                'Certificado con validez académica',
                'Acceso a comunidad de excelencia',
                'Reconocimiento en ceremonia virtual',
                'Insignia digital verificable en blockchain'
            ],
            'ceremonia': {
                'elementos': [
                    'Discurso del rector virtual',
                    'Presentación de méritos',
                    'Entrega virtual de medalla',
                    'Fotos con avatar académico',
                    'Diploma descargable'
                ]
            }
        }
    }
