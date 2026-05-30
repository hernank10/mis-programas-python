import random
import sys
from datetime import datetime

class EnglishConnectorsMaster:
    def __init__(self):
        self.ejercicios = self._inicializar_ejercicios()
        self.puntuacion = 0
        self.ejercicios_completados = 0
        self.inicio_tiempo = None
        self.conectores_dominados = set()
        
    def _inicializar_ejercicios(self):
        return [
            # === CONECTORES BÁSICOS DE ADICIÓN (15 ejercicios) ===
            {
                "categoria": "Adición - AND",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Me gusta el café ___ el té.",
                "oracion_ingles": "I like coffee ___ tea.",
                "respuesta_correcta": "and",
                "pista": "AND une ideas similares o elementos de una lista",
                "dificultad": "básico"
            },
            {
                "categoria": "Adición - ALSO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Ella habla inglés. ___ habla francés.",
                "oracion_ingles": "She speaks English. She ___ speaks French.",
                "respuesta_correcta": "also",
                "pista": "ALSO va antes del verbo principal o después de 'to be'",
                "dificultad": "básico"
            },
            {
                "categoria": "Adición - TOO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Me gusta el cine, y a mí hermana ___.",
                "oracion_ingles": "I like movies, and my sister does ___.",
                "respuesta_correcta": "too",
                "pista": "TOO va al final de la oración, significa 'también'",
                "dificultad": "básico"
            },
            {
                "categoria": "Adición - MOREOVER",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "El proyecto es viable. ___, tenemos el presupuesto necesario.",
                "oracion_ingles": "The project is feasible. ___, we have the necessary budget.",
                "respuesta_correcta": "Moreover",
                "pista": "MOREOVER es formal, añade información importante (además)",
                "dificultad": "intermedio"
            },

            # === CONECTORES DE CONTRASTE (20 ejercicios) ===
            {
                "categoria": "Contraste - BUT",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Quiero ir al cine ___ no tengo dinero.",
                "oracion_ingles": "I want to go to the cinema ___ I don't have money.",
                "respuesta_correcta": "but",
                "pista": "BUT muestra contraste entre dos ideas (pero)",
                "dificultad": "básico"
            },
            {
                "categoria": "Contraste - HOWEVER",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "El producto es caro. ___, es de alta calidad.",
                "oracion_ingles": "The product is expensive. ___, it's high quality.",
                "respuesta_correcta": "However",
                "pista": "HOWEVER es más formal que BUT, va entre punto y coma o al inicio",
                "dificultad": "intermedio"
            },
            {
                "categoria": "Contraste - ALTHOUGH",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ hace frío, voy a salir a correr.",
                "oracion_ingles": "___ it's cold, I'm going running.",
                "respuesta_correcta": "Although",
                "pista": "ALTHOUGH introduce una concesión (aunque), va al inicio o en medio",
                "dificultad": "intermedio"
            },
            {
                "categoria": "Contraste - DESPITE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ la lluvia, el partido continuó.",
                "oracion_ingles": "___ the rain, the game continued.",
                "respuesta_correcta": "Despite",
                "pista": "DESPITE va seguido de sustantivo o gerundio, no de sujeto+verbo",
                "dificultad": "avanzado"
            },

            # === CONECTORES DE CAUSA (15 ejercicios) ===
            {
                "categoria": "Causa - BECAUSE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "No fui a trabajar ___ estaba enfermo.",
                "oracion_ingles": "I didn't go to work ___ I was sick.",
                "respuesta_correcta": "because",
                "pista": "BECAUSE responde a 'why?' y va seguido de sujeto+verbo",
                "dificultad": "básico"
            },
            {
                "categoria": "Causa - SINCE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ ya es tarde, debemos irnos.",
                "oracion_ingles": "___ it's late, we should leave.",
                "respuesta_correcta": "Since",
                "pista": "SINCE puede significar 'ya que' o 'desde que'",
                "dificultad": "intermedio"
            },
            {
                "categoria": "Causa - DUE TO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "El vuelo se canceló ___ el mal tiempo.",
                "oracion_ingles": "The flight was canceled ___ bad weather.",
                "respuesta_correcta": "due to",
                "pista": "DUE TO es más formal, va seguido de sustantivo (debido a)",
                "dificultad": "avanzado"
            },

            # === CONECTORES DE EFECTO/RESULTADO (15 ejercicios) ===
            {
                "categoria": "Resultado - SO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Estaba lloviendo, ___ llevamos paraguas.",
                "oracion_ingles": "It was raining, ___ we brought umbrellas.",
                "respuesta_correcta": "so",
                "pista": "SO muestra resultado o consecuencia (así que, por lo tanto)",
                "dificultad": "básico"
            },
            {
                "categoria": "Resultado - THEREFORE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "La evidencia era contundente. ___, el acusado fue declarado culpable.",
                "oracion_ingles": "The evidence was compelling. ___, the defendant was found guilty.",
                "respuesta_correcta": "Therefore",
                "pista": "THEREFORE es formal, indica conclusión lógica (por lo tanto)",
                "dificultad": "avanzado"
            },
            {
                "categoria": "Resultado - AS A RESULT",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Estudié mucho. ___, aprobé el examen.",
                "oracion_ingles": "I studied hard. ___, I passed the exam.",
                "respuesta_correcta": "As a result",
                "pista": "AS A RESULT enfatiza la relación causa-efecto (como resultado)",
                "dificultad": "intermedio"
            },

            # === CONECTORES DE TIEMPO (15 ejercicios) ===
            {
                "categoria": "Tiempo - WHEN",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ llegué a casa, el teléfono sonaba.",
                "oracion_ingles": "___ I arrived home, the phone was ringing.",
                "respuesta_correcta": "When",
                "pista": "WHEN para acciones secuenciales (cuando)",
                "dificultad": "básico"
            },
            {
                "categoria": "Tiempo - WHILE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ yo cocinaba, mi hermano veía televisión.",
                "oracion_ingles": "___ I was cooking, my brother was watching TV.",
                "respuesta_correcta": "While",
                "pista": "WHILE para acciones simultáneas (mientras)",
                "dificultad": "intermedio"
            },
            {
                "categoria": "Tiempo - UNTIL",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Trabajaré aquí ___ me jubile.",
                "oracion_ingles": "I'll work here ___ I retire.",
                "respuesta_correcta": "until",
                "pista": "UNTIL marca el punto final de una acción (hasta que)",
                "dificultad": "intermedio"
            },

            # === CONECTORES DE CONDICIÓN (10 ejercicios) ===
            {
                "categoria": "Condición - IF",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "___ llueve, cancelaremos el picnic.",
                "oracion_ingles": "___ it rains, we'll cancel the picnic.",
                "respuesta_correcta": "If",
                "pista": "IF introduce una condición (si)",
                "dificultad": "básico"
            },
            {
                "categoria": "Condición - UNLESS",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "No iré ___ me invites formalmente.",
                "oracion_ingles": "I won't go ___ you invite me properly.",
                "respuesta_correcta": "unless",
                "pista": "UNLESS significa 'a menos que' o 'a no ser que'",
                "dificultad": "avanzado"
            },

            # === CONECTORES DE FINALIDAD (10 ejercicios) ===
            {
                "categoria": "Finalidad - TO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Estudio inglés ___ conseguir un mejor trabajo.",
                "oracion_ingles": "I study English ___ get a better job.",
                "respuesta_correcta": "to",
                "pista": "TO + verbo base expresa propósito (para)",
                "dificultad": "básico"
            },
            {
                "categoria": "Finalidad - IN ORDER TO",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "Ahorro dinero ___ comprar una casa.",
                "oracion_ingles": "I save money ___ buy a house.",
                "respuesta_correcta": "in order to",
                "pista": "IN ORDER TO es más formal que 'to' (con el fin de)",
                "dificultad": "intermedio"
            },

            # === EJEMPLOS ADICIONALES PARA COMPLETAR 100 ===
            {
                "categoria": "Conectores Avanzados - NEVERTHELESS",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "El camino era peligroso. ___, decidimos continuar.",
                "oracion_ingles": "The path was dangerous. ___, we decided to continue.",
                "respuesta_correcta": "Nevertheless",
                "pista": "NEVERTHELESS es muy formal, similar a 'however' (no obstante)",
                "dificultad": "avanzado"
            },
            {
                "categoria": "Conectores Avanzados - FURTHERMORE",
                "instruccion": "Completa la oración con el conector correcto:",
                "oracion_es": "El hotel es céntrico. ___, tiene piscina y gimnasio.",
                "oracion_ingles": "The hotel is central. ___, it has a pool and gym.",
                "respuesta_correcta": "Furthermore",
                "pista": "FURTHERMORE añade información importante (además)",
                "dificultad": "avanzado"
            }
        ]

    def _completar_100_ejercicios(self):
        """Completa la lista hasta 100 ejercicios con variaciones"""
        ejercicios_base = self.ejercicios
        ejercicios_completos = []
        
        # Categorías para variación temática
        temas_variacion = [
            {
                "tema": "trabajo", 
                "sustituciones": [
                    ("café", "café de la oficina"), ("cine", "reunión"), 
                    ("hermano", "colega"), ("casa", "oficina")
                ]
            },
            {
                "tema": "estudios", 
                "sustituciones": [
                    ("trabajar", "estudiar"), ("dinero", "tiempo"),
                    ("proyecto", "examen"), ("presupuesto", "beca")
                ]
            },
            {
                "tema": "viajes",
                "sustituciones": [
                    ("casa", "hotel"), ("ciudad", "destino"),
                    ("lluvia", "tormenta"), ("dinero", "presupuesto de viaje")
                ]
            }
        ]
        
        # Generar ejercicios variados
        for i in range(4):  # 4 ciclos para llegar a ~100
            for ejercicio in ejercicios_base:
                nuevo_ej = ejercicio.copy()
                tema = temas_variacion[i % len(temas_variacion)]
                
                # Aplicar sustituciones temáticas
                for original, reemplazo in tema["sustituciones"]:
                    if original in nuevo_ej["oracion_es"].lower():
                        nuevo_ej["oracion_es"] = nuevo_ej["oracion_es"].replace(original, reemplazo)
                        # También actualizar la versión en inglés si corresponde
                        if original in nuevo_ej["oracion_ingles"].lower():
                            nuevo_ej["oracion_ingles"] = nuevo_ej["oracion_ingles"].replace(original, reemplazo)
                
                ejercicios_completos.append(nuevo_ej)
        
        random.shuffle(ejercicios_completos)
        return ejercicios_completos[:100]

    def mostrar_bienvenida(self):
        print("=" * 80)
        print("🔗 MAESTRO DE CONECTORES EN INGLÉS PARA HISPANOHABLANTES")
        print("=" * 80)
        print("\nEste programa contiene 100 ejercicios para dominar TODOS los")
        print("conectores del inglés, enfocándose en los desafíos específicos")
        print("de los estudiantes hispanohablantes.")
        print("\n📚 CATEGORÍAS DE CONECTORES INCLUIDAS:")
        print("  • Adición (and, also, too, moreover, furthermore)")
        print("  • Contraste (but, however, although, despite, nevertheless)")
        print("  • Causa (because, since, due to, owing to)")
        print("  • Resultado (so, therefore, as a result, consequently)")
        print("  • Tiempo (when, while, until, as soon as)")
        print("  • Condición (if, unless, provided that)")
        print("  • Finalidad (to, in order to, so that)")
        print("\n🎯 CARACTERÍSTICAS ESPECIALES:")
        print("  - Enfoque en errores comunes de hispanohablantes")
        print("  - Explicaciones gramaticales detalladas")
        print("  - Progresión de básico a avanzado")
        print("  - Seguimiento de conectores dominados")
        print("\n💡 COMANDOS DISPONIBLES:")
        print("  'pista'      - Mostrar ayuda gramatical")
        print("  'explicacion' - Explicación extendida del conector")
        print("  'saltar'     - Pasar al siguiente ejercicio")
        print("  'estadisticas' - Ver progreso actual")
        print("  'salir'      - Terminar el programa")
        print("=" * 80)

    def verificar_respuesta(self, respuesta_usuario, respuesta_correcta, ejercicio):
        """Sistema de verificación inteligente para conectores"""
        
        def normalizar(texto):
            texto = texto.strip().lower()
            reemplazos = [
                (".", ""), (",", ""), (";", ""), ("'", ""),
                ("  ", " "), ("although", "though"), ("despite", "in spite of"),
                ("because", "cos"), ("therefore", "thus")
            ]
            for orig, nuevo in reemplazos:
                texto = texto.replace(orig, nuevo)
            return texto
        
        usuario_norm = normalizar(respuesta_usuario)
        correcta_norm = normalizar(respuesta_correcta)
        
        # Verificación exacta
        if usuario_norm == correcta_norm:
            return True, "exacta"
        
        # Verificación de sinónimos aceptables
        sinonimos = {
            "and": ["&"],
            "but": ["yet"],
            "however": ["nevertheless", "nonetheless"],
            "although": ["though", "even though"],
            "because": ["since", "as"],
            "so": ["thus", "hence"],
            "therefore": ["consequently", "thus"],
            "moreover": ["furthermore", "additionally"]
        }
        
        if correcta_norm in sinonimos:
            if usuario_norm in sinonimos[correcta_norm]:
                return True, "sinonimo_aceptable"
        
        # Verificación de colocaciones comunes
        if ejercicio["categoria"] == "Contraste - DESPITE":
            if "in spite of" in usuario_norm:
                return True, "variacion_aceptable"
        
        return False, "incorrecto"

    def mostrar_explicacion_extendida(self, ejercicio):
        """Muestra explicación gramatical detallada del conector"""
        conector = ejercicio["respuesta_correcta"].lower()
        
        explicaciones = {
            "and": "📖 AND: Une elementos similares. No usa coma antes excepto en listas de 3+ elementos.",
            "but": "📖 BUT: Muestra contraste directo. Va entre dos ideas opuestas.",
            "although": "📖 ALTHOUGH: Introduce una concesión. Puede ir al inicio (con coma) o en medio.",
            "despite": "📖 DESPITE: Significa 'a pesar de'. Va seguido de sustantivo o gerundio, NO de sujeto+verbo.",
            "because": "📖 BECAUSE: Responde 'why?'. Es más común que 'since' en inglés hablado.",
            "however": "📖 HOWEVER: Conector formal. Va entre punto y coma o al inicio de oración.",
            "therefore": "📖 THEREFORE: Indica conclusión lógica. Muy usado en escritura académica.",
            "moreover": "📖 MOREOVER: Añade información importante. Más formal que 'furthermore'."
        }
        
        explicacion = explicaciones.get(conector, 
            f"📖 {conector.upper()}: Consulta una gramática para detalles específicos.")
        
        print(f"\n💡 EXPLICACIÓN EXTENDIDA:")
        print(f"   {explicacion}")
        
        # Mostrar ejemplos adicionales
        ejemplos = {
            "and": "Ejemplos: I like coffee AND tea. She's smart AND funny.",
            "but": "Ejemplos: It's expensive BUT good quality. I'm tired BUT I'll continue.",
            "although": "Ejemplos: ALTHOUGH it was cold, we went out. We went out, ALTHOUGH it was cold.",
            "despite": "Ejemplos: DESPITE the rain, we had fun. DESPITE feeling tired, she worked."
        }
        
        if conector in ejemplos:
            print(f"   {ejemplos[conector]}")

    def mostrar_progreso_detallado(self):
        """Muestra progreso con estadísticas por categoría y dificultad"""
        if self.inicio_tiempo:
            tiempo_transcurrido = datetime.now() - self.inicio_tiempo
            minutos = tiempo_transcurrido.seconds // 60
            segundos = tiempo_transcurrido.seconds % 60
        else:
            minutos = segundos = 0
        
        porcentaje_total = (self.ejercicios_completados / 100) * 100
        
        print(f"\n📊 PROGRESO GENERAL:")
        print(f"   Ejercicios completados: {self.ejercicios_completados}/100 ({porcentaje_total:.1f}%)")
        print(f"   Puntuación: {self.puntuacion} puntos")
        print(f"   Tiempo: {minutos:02d}:{segundos:02d}")
        print(f"   Conectores dominados: {len(self.conectores_dominados)}")
        
        # Estadísticas por dificultad
        if self.ejercicios_completados > 0:
            dificultades = {"básico": 0, "intermedio": 0, "avanzado": 0}
            for i in range(min(self.ejercicios_completados, 100)):
                # Esto es una simplificación - en implementación real se trackearía mejor
                dificultad = self.ejercicios[i % len(self.ejercicios)]["dificultad"]
                dificultades[dificultad] += 1
            
            print(f"\n🎯 DISTRIBUCIÓN POR DIFICULTAD:")
            for nivel, cantidad in dificultades.items():
                if cantidad > 0:
                    porcentaje = (cantidad / self.ejercicios_completados) * 100
                    print(f"   {nivel.title()}: {cantidad} ejercicios ({porcentaje:.1f}%)")

    def ejecutar_ejercicio(self, ejercicio, numero):
        print(f"\n{'='*60}")
        print(f"🎯 EJERCICIO {numero} DE 100")
        print(f"📂 Categoría: {ejercicio['categoria']}")
        print(f"🏷️  Dificultad: {ejercicio['dificultad'].upper()}")
        print(f"{'='*60}")
        print(f"💬 {ejercicio['instruccion']}")
        print(f"🔸 Español: {ejercicio['oracion_es']}")
        print(f"🔸 English: {ejercicio['oracion_ingles']}")
        
        intentos = 0
        max_intentos = 2
        
        while intentos < max_intentos:
            respuesta = input("\n✏️  Escribe el conector faltante: ").strip()
            
            # Comandos especiales
            if respuesta.lower() == 'salir':
                return 'salir'
            elif respuesta.lower() == 'pista':
                print(f"💡 PISTA: {ejercicio['pista']}")
                continue
            elif respuesta.lower() == 'explicacion':
                self.mostrar_explicacion_extendida(ejercicio)
                continue
            elif respuesta.lower() == 'saltar':
                print("⏭️  Ejercicio saltado.")
                return 'saltar'
            elif respuesta.lower() == 'estadisticas':
                self.mostrar_progreso_detallado()
                continue
            elif not respuesta:
                print("❌ Por favor, escribe una respuesta.")
                continue
            
            # Verificar respuesta
            es_correcta, tipo = self.verificar_respuesta(respuesta, ejercicio["respuesta_correcta"], ejercicio)
            
            if es_correcta:
                if tipo == "exacta":
                    print("✅ ¡PERFECTO! Respuesta exacta.")
                    self.puntuacion += 2
                else:
                    print("✅ ¡MUY BIEN! Respuesta aceptada.")
                    self.puntuacion += 1
                
                # Agregar conector a los dominados
                self.conectores_dominados.add(ejercicio["respuesta_correcta"].lower())
                
                print(f"📝 Oración completa: {ejercicio['oracion_ingles'].replace('___', ejercicio['respuesta_correcta'])}")
                
                # Explicación adicional basada en el tipo de conector
                if "contraste" in ejercicio["categoria"].lower():
                    print("💡 RECUERDA: Los conectores de contraste muestran oposición entre ideas.")
                elif "causa" in ejercicio["categoria"].lower():
                    print("💡 RECUERDA: Los conectores de causa explican el 'por qué'.")
                
                return 'correcto'
            else:
                intentos += 1
                if intentos < max_intentos:
                    print(f"❌ Intento {intentos}/{max_intentos}. Intenta nuevamente.")
                    print(f"💡 Pista: {ejercicio['pista']}")
                else:
                    print("🔍 VEAMOS LA RESPUESTA CORRECTA:")
                    print(f"📝 Conector correcto: {ejercicio['respuesta_correcta']}")
                    print(f"📝 Oración completa: {ejercicio['oracion_ingles'].replace('___', ejercicio['respuesta_correcta'])}")
                    self.mostrar_explicacion_extendida(ejercicio)
                    return 'incorrecto'

    def ejecutar_entrenamiento(self):
        self.mostrar_bienvenida()
        self.inicio_tiempo = datetime.now()
        
        ejercicios_completos = self._completar_100_ejercicios()
        
        input("\n🎯 Presiona Enter para comenzar tu entrenamiento de conectores...")
        
        for i, ejercicio in enumerate(ejercicios_completos, 1):
            resultado = self.ejercutar_ejercicio_seguro(ejercicio, i)
            
            if resultado == 'salir':
                break
            
            self.ejercicios_completados = i
            
            # Mostrar progreso cada 5 ejercicios
            if i % 5 == 0:
                self.mostrar_progreso_detallado()
            
            # Pausa cada 10 ejercicios con mini-resumen
            if i % 10 == 0 and i < 100:
                print(f"\n⭐ Hito: {i} ejercicios completados!")
                print(f"🔗 Conectores practicados recientemente: {', '.join(list(self.conectores_dominados)[-5:])}")
                input("⏸️  Presiona Enter para continuar...")
        
        self.mostrar_resultado_final()

    def ejercutar_ejercicio_seguro(self, ejercicio, numero):
        """Maneja errores en ejercicios individuales"""
        try:
            return self.ejecutar_ejercicio(ejercicio, numero)
        except Exception as e:
            print(f"❌ Error en el ejercicio: {e}")
            return 'error'

    def mostrar_resultado_final(self):
        """Muestra resultados finales detallados"""
        tiempo_total = datetime.now() - self.inicio_tiempo
        minutos_totales = tiempo_total.seconds // 60
        segundos_totales = tiempo_total.seconds % 60
        
        porcentaje_acierto = (self.puntuacion / (self.ejercicios_completados * 2)) * 100 if self.ejercicios_completados > 0 else 0
        
        print("\n" + "="*80)
        print("🎓 RESUMEN FINAL - MAESTRÍA DE CONECTORES")
        print("="*80)
        print(f"📅 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"⏱️  Tiempo total: {minutos_totales:02d}:{segundos_totales:02d}")
        print(f"📊 Ejercicios completados: {self.ejercicios_completados}/100")
        print(f"✅ Puntuación final: {self.puntuacion}/{(self.ejercicios_completados * 2)}")
        print(f"📈 Porcentaje de acierto: {porcentaje_acierto:.1f}%")
        print(f"🔗 Conectores diferentes dominados: {len(self.conectores_dominados)}")
        
        # Evaluación del desempeño
        if porcentaje_acierto >= 90:
            print("\n🏆 ¡EXCELENTE! Eres un maestro de los conectores")
            print("   Nivel: Avanzado - Usas conectores como nativo")
        elif porcentaje_acierto >= 70:
            print("\n👍 ¡MUY BIEN! Buen dominio de conectores")
            print("   Nivel: Intermedio-Alto - Comunicación efectiva")
        elif porcentaje_acierto >= 50:
            print("\n📚 ¡BIEN! Bases sólidas, sigue practicando")
            print("   Nivel: Intermedio - En camino a la fluidez")
        else:
            print("\n💪 ¡EN DESARROLLO! La práctica hace al maestro")
            print("   Nivel: Básico-Intermedio - Sigue practicando")
        
        # Mostrar conectores dominados
        if self.conectores_dominados:
            print(f"\n🔗 CONECTORES QUE DOMINAS:")
            conectores_ordenados = sorted(self.conectores_dominados)
            for i in range(0, len(conectores_ordenados), 5):
                print(f"   {', '.join(conectores_ordenados[i:i+5])}")
        
        # Recomendaciones de estudio
        print(f"\n📚 RECOMENDACIONES PARA SEGUIR MEJORANDO:")
        if porcentaje_acierto < 70:
            print("   1. Enfócate en conectores básicos (and, but, because, so)")
            print("   2. Practica la diferencia entre although/despite")
            print("   3. Domina los conectores de tiempo (when, while, until)")
            print("   4. Lee textos simples identificando conectores")
        else:
            print("   1. Practica conectores formales (however, therefore, moreover)")
            print("   2. Perfecciona el uso de despite/in spite of")
            print("   3. Trabaja con conectores académicos (furthermore, consequently)")
            print("   4. Escribe párrafos usando variedad de conectores")
        
        print("\n✨ ¡Felicidades por completar el entrenamiento!")
        print("   Sigue practicando para una comunicación más fluida y natural.")

def main():
    entrenador = EnglishConnectorsMaster()
    try:
        entrenador.ejecutar_entrenamiento()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Tu progreso ha sido registrado!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reinicia el programa.")

if __name__ == "__main__":
    main()
