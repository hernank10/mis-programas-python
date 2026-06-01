def generar_leccion_5grado():
    return {
        'teoria': '''
        <div class="leccion-grado5">
            <h2>¡Descubriendo los Modos Verbales!</h2>
            
            <div class="modos-verbales">
                <div class="modo-card" data-modo="indicativo">
                    <div class="modo-icono">📌</div>
                    <h3>Indicativo</h3>
                    <p>Expresa hechos reales y objetivos</p>
                    <div class="ejemplo-modales">
                        <p>"Estudio español"</p>
                        <p>"Hace sol"</p>
                    </div>
                </div>
                
                <div class="modo-card" data-modo="subjuntivo">
                    <div class="modo-icono">❓</div>
                    <h3>Subjuntivo</h3>
                    <p>Expresa deseos, dudas o posibilidades</p>
                    <div class="ejemplo-modales">
                        <p>"Espero que estudies"</p>
                        <p>"Quizás venga"</p>
                    </div>
                </div>
                
                <div class="modo-card" data-modo="imperativo">
                    <div class="modo-icono">❗</div>
                    <h3>Imperativo</h3>
                    <p>Expresa órdenes o peticiones</p>
                    <div class="ejemplo-modales">
                        <p>"Estudia ahora"</p>
                        <p>"Por favor, ven"</p>
                    </div>
                </div>
            </div>
            
            <div class="tabla-conjugacion">
                <h3>Conjugación del Verbo "Amar"</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Persona</th>
                            <th>Indicativo Presente</th>
                            <th>Subjuntivo Presente</th>
                            <th>Imperativo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Yo</td>
                            <td>amo</td>
                            <td>ame</td>
                            <td>-</td>
                        </tr>
                        <tr>
                            <td>Tú</td>
                            <td>amas</td>
                            <td>ames</td>
                            <td>¡ama!</td>
                        </tr>
                        <tr>
                            <td>Él/Ella</td>
                            <td>ama</td>
                            <td>ame</td>
                            <td>-</td>
                        </tr>
                        <tr>
                            <td>Nosotros</td>
                            <td>amamos</td>
                            <td>amemos</td>
                            <td>¡amemos!</td>
                        </tr>
                        <tr>
                            <td>Vosotros</td>
                            <td>amáis</td>
                            <td>améis</td>
                            <td>¡amad!</td>
                        </tr>
                        <tr>
                            <td>Ellos</td>
                            <td>aman</td>
                            <td>amen</td>
                            <td>-</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="reglas-avanzadas">
                <h4>¡Uso Clave del Subjuntivo!</h4>
                <ul>
                    <li>Después de verbos de deseo: <em>Quiero que vengas</em></li>
                    <li>Con expresiones de duda: <em>Dudo que sepa</em></li>
                    <li>Para dar consejos: <em>Es mejor que estudies</em></li>
                    <li>Con "ojalá": <em>Ojalá llueva</em></li>
                </ul>
            </div>
            
            <div class="diferencia-modos">
                <h3>Comparación Fundamental</h3>
                <div class="comparacion">
                    <div class="indicativo">
                        <p><strong>Indicativo:</strong> Hechos comprobables</p>
                        <p>"Sé que <u>estás</u> aquí"</p>
                    </div>
                    <div class="subjuntivo">
                        <p><strong>Subjuntivo:</strong> Posibilidades</p>
                        <p>"No creo que <u>estés</u> aquí"</p>
                    </div>
                </div>
            </div>
        </div>
        ''',
        'ejemplos': [
            {
                'tipo': 'analisis_modos', 
                'texto': '"Es necesario que estudies" (subjuntivo) vs "Estudias todos los días" (indicativo)',
                'analisis': 'El subjuntivo expresa necesidad, el indicativo describe un hecho'
            },
            {
                'tipo': 'transformacion', 
                'texto': 'Transformar indicativo a imperativo: "Tú comes" → "¡Come!"',
                'analisis': 'El imperativo elimina el sujeto y cambia la conjugación'
            },
            {
                'tipo': 'error_comun', 
                'texto': 'Incorrecto: "Espero que tú vienes" → Correcto: "Espero que tú vengas"',
                'analisis': 'Después de "espero que" siempre se usa subjuntivo'
            }
        ],
        'ejercicios': [
            {
                'pregunta': 'Identifica el modo verbal en: "Quizás llueva mañana"',
                'opciones': ['Indicativo', 'Subjuntivo', 'Imperativo'],
                'respuesta': 1,
                'tipo': 'seleccion_simple'
            },
            {
                'pregunta': 'Conjuga en subjuntivo presente: "Yo (estudiar)"',
                'respuesta_correcta': 'estudie',
                'tipo': 'respuesta_corta'
            },
            {
                'pregunta': 'Transforma al imperativo: "Tú debes hacer la tarea"',
                'respuesta_correcta': '¡Haz la tarea!',
                'tipo': 'transformacion'
            },
            {
                'pregunta': 'Completa con el modo adecuado: "Dudo que él _____ (saber) la respuesta"',
                'opciones': ['sabe', 'sepa', 'sabría'],
                'respuesta': 1,
                'explicacion': 'Después de "dudo que" se usa subjuntivo'
            },
            {
                'pregunta': 'Crea una oración usando imperativo y otra usando subjuntivo',
                'elementos': [
                    {'modo': 'imperativo', 'verbo': 'leer'},
                    {'modo': 'subjuntivo', 'expresion': 'es importante que'}
                ],
                'tipo': 'creacion_oraciones'
            }
        ],
        'actividad_especial': {
            'titulo': 'Detective de Modos Verbales',
            'instrucciones': 'Analiza textos reales e identifica los modos verbales',
            'textos': [
                "Es fundamental que los estudiantes comprendan los modos verbales. ¡Estudiad con atención!",
                "Ojalá tengamos buen clima mañana. Si hace sol, iremos al parque."
            ],
            'tipo': 'analisis_textual'
        }
    }
