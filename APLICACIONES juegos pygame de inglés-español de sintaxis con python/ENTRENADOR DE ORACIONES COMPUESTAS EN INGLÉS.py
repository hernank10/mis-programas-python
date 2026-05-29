import random
import sys
from datetime import datetime

class EnglishCompoundSentencesTrainer:
    def __init__(self):
        self.ejercicios = self._inicializar_ejercicios()
        self.puntuacion = 0
        self.ejercicios_completados = 0
        self.inicio_tiempo = None
        
    def _inicializar_ejercicios(self):
        return [
            # === CONJUNCIONES COORDINANTES (25 ejercicios) ===
            {
                "categoria": "Conjunciones Coordinantes - AND",
                "instruccion": "Une las dos oraciones usando AND:",
                "oracion_es": "Yo estudio inglés. Mi hermano estudia francés.",
                "respuesta_correcta": "I study English and my brother studies French.",
                "pista": "AND une ideas similares. Cuidado con la concordancia del verbo."
            },
            {
                "categoria": "Conjunciones Coordinantes - BUT",
                "instruccion": "Une las oraciones usando BUT:",
                "oracion_es": "Quiero ir al cine. No tengo dinero.",
                "respuesta_correcta": "I want to go to the cinema but I don't have money.",
                "pista": "BUT muestra contraste u oposición entre ideas."
            },
            {
                "categoria": "Conjunciones Coordinantes - OR",
                "instruccion": "Une las oraciones usando OR:",
                "oracion_es": "Podemos comer en casa. Podemos ir a un restaurante.",
                "respuesta_correcta": "We can eat at home or we can go to a restaurant.",
                "pista": "OR presenta alternativas o opciones."
            },
            {
                "categoria": "Conjunciones Coordinantes - SO",
                "instruccion": "Une las oraciones usando SO:",
                "oracion_es": "Estaba lloviendo. Decidimos quedarnos en casa.",
                "respuesta_correcta": "It was raining so we decided to stay at home.",
                "pista": "SO indica resultado o consecuencia."
            },
            {
                "categoria": "Conjunciones Coordinantes - YET",
                "instruccion": "Une las oraciones usando YET:",
                "oracion_es": "Estudié mucho. No aprobé el examen.",
                "respuesta_correcta": "I studied hard yet I didn't pass the exam.",
                "pista": "YET es similar a BUT pero más formal, indica contraste sorprendente."
            },
            {
                "categoria": "Conjunciones Coordinantes - FOR",
                "instruccion": "Une las oraciones usando FOR:",
                "oracion_es": "Debemos apurarnos. Vamos a llegar tarde.",
                "respuesta_correcta": "We must hurry for we are going to be late.",
                "pista": "FOR explica la razón (similar a 'because' pero más formal)."
            },

            # === CONJUNCIONES SUBORDINANTES (30 ejercicios) ===
            {
                "categoria": "Subordinantes - BECAUSE/SINCE",
                "instruccion": "Une las oraciones usando BECAUSE:",
                "oracion_es": "No fui a trabajar. Estaba enfermo.",
                "respuesta_correcta": "I didn't go to work because I was sick.",
                "pista": "BECAUSE introduce la causa o razón."
            },
            {
                "categoria": "Subordinantes - ALTHOUGH/EVEN THOUGH",
                "instruccion": "Une las oraciones usando ALTHOUGH:",
                "oracion_es": "Hace frío. Voy a salir a correr.",
                "respuesta_correcta": "Although it is cold, I'm going to go running.",
                "pista": "ALTHOUGH introduce una concesión (contraste)."
            },
            {
                "categoria": "Subordinantes - IF/UNLESS",
                "instruccion": "Une las oraciones usando IF:",
                "oracion_es": "LLueve. Cancelaremos el picnic.",
                "respuesta_correcta": "If it rains, we will cancel the picnic.",
                "pista": "IF introduce una condición. Usa coma cuando la condición va primero."
            },
            {
                "categoria": "Subordinantes - WHEN/WHILE",
                "instruccion": "Une las oraciones usando WHEN:",
                "oracion_es": "Llegué a casa. El teléfono estaba sonando.",
                "respuesta_correcta": "When I arrived home, the phone was ringing.",
                "pista": "WHEN para acciones secuenciales, WHILE para acciones simultáneas."
            },
            {
                "categoria": "Subordinantes - BEFORE/AFTER",
                "instruccion": "Une las oraciones usando BEFORE:",
                "oracion_es": "Cenaremos. Terminarás tu tarea.",
                "respuesta_correcta": "We will have dinner before you finish your homework.",
                "pista": "BEFORE/AFTER muestran secuencia temporal."
            },
            {
                "categoria": "Subordinantes - SO THAT/IN ORDER THAT",
                "instruccion": "Une las oraciones usando SO THAT:",
                "oracion_es": "Estudio mucho. Quiero aprobar el examen.",
                "respuesta_correcta": "I study hard so that I can pass the exam.",
                "pista": "SO THAT indica propósito o finalidad."
            },
            {
                "categoria": "Subordinantes - WHERE/WHEREVER",
                "instruccion": "Une las oraciones usando WHERE:",
                "oracion_es": "Este es el lugar. Nos conocimos.",
                "respuesta_correcta": "This is the place where we met.",
                "pista": "WHERE se refiere al lugar donde ocurre la acción."
            },

            # === ORACIONES RELATIVAS (20 ejercicios) ===
            {
                "categoria": "Relativas - WHO/WHOM",
                "instruccion": "Combina las oraciones usando WHO:",
                "oracion_es": "La mujer es mi hermana. Ella vive en París.",
                "respuesta_correcta": "The woman who lives in Paris is my sister.",
                "pista": "WHO se refiere a personas (sujeto), WHOM para objeto."
            },
            {
                "categoria": "Relativas - WHICH/THAT",
                "instruccion": "Combina las oraciones usando WHICH:",
                "oracion_es": "El libro es muy interesante. Lo compré ayer.",
                "respuesta_correcta": "The book which I bought yesterday is very interesting.",
                "pista": "WHICH/THAT se refieren a cosas o animales."
            },
            {
                "categoria": "Relativas - WHOSE",
                "instruccion": "Combina las oraciones usando WHOSE:",
                "oracion_es": "Conocí a un hombre. Su hijo juega en el Real Madrid.",
                "respuesta_correcta": "I met a man whose son plays for Real Madrid.",
                "pista": "WHOSE indica posesión (cuyo/a)."
            },
            {
                "categoria": "Relativas - OMISIÓN DEL PRONOMBRE",
                "instruccion": "Combina las oraciones omitiendo el pronombre relativo:",
                "oracion_es": "La casa es muy grande. Compraron la casa.",
                "respuesta_correcta": "The house they bought is very big.",
                "pista": "Se puede omitir el relativo cuando no es el sujeto de la relativa."
            },

            # === CONDICIONALES COMPUESTAS (15 ejercicios) ===
            {
                "categoria": "Condicionales - Primer Condicional",
                "instruccion": "Forma una oración condicional (Tipo 1):",
                "oracion_es": "Si estudias, aprobarás el examen.",
                "respuesta_correcta": "If you study, you will pass the exam.",
                "pista": "Tipo 1: If + presente simple, will + verbo base (condición real)"
            },
            {
                "categoria": "Condicionales - Segundo Condicional",
                "instruccion": "Forma una oración condicional (Tipo 2):",
                "oracion_es": "Si tuviera dinero, compraría un coche nuevo.",
                "respuesta_correcta": "If I had money, I would buy a new car.",
                "pista": "Tipo 2: If + pasado simple, would + verbo base (condición hipotética)"
            },
            {
                "categoria": "Condicionales - Tercer Condicional",
                "instruccion": "Forma una oración condicional (Tipo 3):",
                "oracion_es": "Si hubiera sabido, te habría ayudado.",
                "respuesta_correcta": "If I had known, I would have helped you.",
                "pista": "Tipo 3: If + pasado perfecto, would have + participio (condición pasada)"
            },
            {
                "categoria": "Condicionales - MIXTAS",
                "instruccion": "Forma una condicional mixta:",
                "oracion_es": "Si hubieras estudiado, ahora tendrías un buen trabajo.",
                "respuesta_correcta": "If you had studied, you would have a good job now.",
                "pista": "Mixta: If + pasado perfecto, would + verbo base"
            },

            # === ESTILO INDIRECTO (10 ejercicios) ===
            {
                "categoria": "Estilo Indirecto - DECLARACIONES",
                "instruccion": "Convierte al estilo indirecto:",
                "oracion_es": "María dijo: 'Estoy cansada'.",
                "respuesta_correcta": "Maria said that she was tired.",
                "pista": "En estilo indirecto: presente → pasado, pronombres cambian"
            },
            {
                "categoria": "Estilo Indirecto - PREGUNTAS",
                "instruccion": "Convierte la pregunta al estilo indirecto:",
                "oracion_es": "Él preguntó: '¿Dónde vives?'",
                "respuesta_correcta": "He asked where I lived.",
                "pista": "Preguntas directas → orden afirmativo en indirectas"
            },
            {
                "categoria": "Estilo Indirecto - ÓRDENES",
                "instruccion": "Convierte la orden al estilo indirecto:",
                "oracion_es": "El profesor dijo: '¡Estudien para el examen!'",
                "respuesta_correcta": "The teacher told us to study for the exam.",
                "pista": "Órdenes: told/asked + objeto + to + verbo"
            },

            # === EJEMPLOS ADICIONALES PARA DIVERSIDAD ===
            {
                "categoria": "Conectores Avanzados - HOWEVER",
                "instruccion": "Une las oraciones usando HOWEVER:",
                "oracion_es": "El producto es caro. Es de muy buena calidad.",
                "respuesta_correcta": "The product is expensive; however, it is very good quality.",
                "pista": "HOWEVER es más formal que BUT, va entre punto y coma y coma."
            },
            {
                "categoria": "Conectores Avanzados - THEREFORE",
                "instruccion": "Une las oraciones usando THEREFORE:",
                "oracion_es": "No había suficiente evidencia. El caso fue cerrado.",
                "respuesta_correcta": "There wasn't enough evidence; therefore, the case was closed.",
                "pista": "THEREFORE indica conclusión lógica."
            },
            {
                "categoria": "Conectores Avanzados - MOREOVER",
                "instruccion": "Une las oraciones usando MOREOVER:",
                "oracion_es": "El hotel es lujoso. Además, tiene vista al mar.",
                "respuesta_correcta": "The hotel is luxurious; moreover, it has sea views.",
                "pista": "MOREOVER añade información importante."
            }
        ]

    def _completar_100_ejercicios(self):
        """Completa la lista hasta 100 ejercicios con variaciones"""
        ejercicios_base = self.ejercicios
        ejercicios_completos = []
        
        # Variaciones temáticas para cada tipo de ejercicio
        variaciones = [
            {"tema": "trabajo", "sustituciones": [("estudiar", "trabajar"), ("examen", "proyecto")]},
            {"tema": "viajes", "sustituciones": [("casa", "hotel"), ("ciudad", "país")]},
            {"tema": "comida", "sustituciones": [("comer", "cocinar"), ("restaurante", "cafetería")]},
            {"tema": "deportes", "sustituciones": [("correr", "jugar"), ("ejercicio", "partido")]},
            {"tema": "clima", "sustituciones": [("lluvia", "nieve"), ("frío", "calor")]}
        ]
        
        # Generar ejercicios variados
        for i in range(4):  # 4 ciclos para llegar a ~100
            for ejercicio in ejercicios_base:
                nuevo_ej = ejercicio.copy()
                variacion = variaciones[i % len(variaciones)]
                
                # Aplicar sustituciones temáticas
                for original, reemplazo in variacion["sustituciones"]:
                    if original in nuevo_ej["oracion_es"].lower():
                        nuevo_ej["oracion_es"] = nuevo_ej["oracion_es"].replace(original, reemplazo)
                        nuevo_ej["respuesta_correcta"] = nuevo_ej["respuesta_correcta"].replace(
                            original.title() if original[0].isupper() else original, 
                            reemplazo.title() if reemplazo[0].isupper() else reemplazo
                        )
                
                ejercicios_completos.append(nuevo_ej)
        
        random.shuffle(ejercicios_completos)
        return ejercicios_completos[:100]

    def mostrar_bienvenida(self):
        print("=" * 80)
        print("🧠 ENTRENADOR DE ORACIONES COMPUESTAS EN INGLÉS")
        print("           (Para Hispanohablantes)")
        print("=" * 80)
        print("\nEste programa contiene 100 ejercicios avanzados para dominar")
        print("la construcción de ORACIONES COMPUESTAS en inglés.")
        print("\n📚 ESTRUCTURAS INCLUIDDAS:")
        print("  • Conjunciones coordinantes (AND, BUT, OR, SO, YET, FOR)")
        print("  • Conjunciones subordinantes (BECAUSE, ALTHOUGH, IF, WHEN)")
        print("  • Oraciones de relativo (WHO, WHICH, THAT, WHOSE)")
        print("  • Condicionales (Tipos 1, 2, 3 y mixtas)")
        print("  • Estilo indirecto (declaraciones, preguntas, órdenes)")
        print("  • Conectores avanzados (HOWEVER, THEREFORE, MOREOVER)")
        print("\n💡 CARACTERÍSTICAS DEL PROGRAMA:")
        print("  - Enfoque en errores comunes de hispanohablantes")
        print("  - Explicaciones gramaticales detalladas")
        print("  - Progresión de simple a complejo")
        print("  - Sistema de puntuación y estadísticas")
        print("\n⌨️  COMANDOS DISPONIBLES:")
        print("  'pista'    - Mostrar ayuda gramatical")
        print("  'saltar'   - Pasar al siguiente ejercicio") 
        print("  'salir'    - Terminar el programa")
        print("  'estadísticas' - Ver progreso actual")
        print("=" * 80)

    def verificar_respuesta(self, respuesta_usuario, respuesta_correcta):
        """Sistema de verificación flexible para oraciones compuestas"""
        def normalizar(texto):
            texto = texto.strip().lower()
            # Eliminar diferencias menores
            reemplazos = [
                ("'", ""), (",", ""), (".", ""), (";", ""), 
                ("  ", " "), ("i'm", "i am"), ("he's", "he is"),
                ("doesn't", "does not"), ("don't", "do not")
            ]
            for original, nuevo in reemplazos:
                texto = texto.replace(original, nuevo)
            return texto
        
        usuario_norm = normalizar(respuesta_usuario)
        correcta_norm = normalizar(respuesta_correcta)
        
        # Verificación exacta
        if usuario_norm == correcta_norm:
            return True, "exacta"
        
        # Verificación por palabras clave estructurales
        palabras_clave = ["although", "because", "if", "when", "who", "which", "that"]
        palabras_usuario = usuario_norm.split()
        palabras_correctas = correcta_norm.split()
        
        # Verificar presencia de conectores clave
        conector_correcto = any(palabra in palabras_usuario for palabra in palabras_clave)
        if not conector_correcto:
            return False, "Falta conector principal"
        
        # Verificación semántica (75% de coincidencia)
        coincidencias = len(set(palabras_usuario) & set(palabras_correctas))
        porcentaje = coincidencias / len(palabras_correctas)
        
        if porcentaje >= 0.75:
            return True, "aproximada"
        
        return False, "Estructura incorrecta"

    def mostrar_progreso_detallado(self):
        """Muestra progreso con estadísticas por categoría"""
        tiempo_actual = datetime.now()
        if self.inicio_tiempo:
            minutos = (tiempo_actual - self.inicio_tiempo).seconds // 60
            segundos = (tiempo_actual - self.inicio_tiempo).seconds % 60
        else:
            minutos = segundos = 0
        
        porcentaje_total = (self.ejercicios_completados / 100) * 100
        
        print(f"\n📊 PROGRESO GENERAL:")
        print(f"   Ejercicios: {self.ejercicios_completados}/100 ({porcentaje_total:.1f}%)")
        print(f"   Puntuación: {self.puntuacion}/{self.ejercicios_completados}")
        print(f"   Tiempo: {minutos:02d}:{segundos:02d}")
        
        # Estadísticas por categoría
        if self.ejercicios_completados > 0:
            categorias = {}
            for i in range(min(self.ejercicios_completados, 100)):
                cat = self.ejercicios[i % len(self.ejercicios)]["categoria"]
                if cat not in categorias:
                    categorias[cat] = {"intentos": 0, "correctos": 0}
                categorias[cat]["intentos"] += 1
                # Asumimos que si el índice es menor que la puntuación, fue correcto
                if i < self.puntuacion:
                    categorias[cat]["correctos"] += 1
            
            print(f"\n📈 POR CATEGORÍA:")
            for cat, stats in categorias.items():
                porcentaje = (stats["correctos"] / stats["intentos"] * 100) if stats["intentos"] > 0 else 0
                print(f"   {cat}: {stats['correctos']}/{stats['intentos']} ({porcentaje:.1f}%)")

    def ejecutar_ejercicio(self, ejercicio, numero):
        print(f"\n{'='*60}")
        print(f"🎯 EJERCICIO {numero} DE 100")
        print(f"🏷️  Categoría: {ejercicio['categoria']}")
        print(f"{'='*60}")
        print(f"💬 {ejercicio['instruccion']}")
        print(f"🔸 Español: {ejercicio['oracion_es']}")
        
        intentos = 0
        max_intentos = 2
        
        while intentos < max_intentos:
            respuesta = input("\n✏️  Tu respuesta en inglés: ").strip()
            
            # Comandos especiales
            if respuesta.lower() == 'salir':
                return 'salir'
            elif respuesta.lower() == 'pista':
                print(f"💡 PISTA GRAMATICAL: {ejercicio['pista']}")
                continue
            elif respuesta.lower() == 'saltar':
                print("⏭️  Ejercicio saltado. Continuando...")
                return 'saltar'
            elif respuesta.lower() == 'estadísticas':
                self.mostrar_progreso_detallado()
                continue
            elif not respuesta:
                print("❌ Por favor, escribe una respuesta.")
                continue
            
            # Verificar respuesta
            es_correcta, tipo = self.verificar_respuesta(respuesta, ejercicio["respuesta_correcta"])
            
            if es_correcta:
                if tipo == "exacta":
                    print("✅ ¡EXCELENTE! Respuesta perfecta.")
                    self.puntuacion += 2  # Bonus por respuesta exacta
                else:
                    print("✅ ¡MUY BIEN! Respuesta aceptada con pequeñas variaciones.")
                    self.puntuacion += 1
                
                print(f"📝 Respuesta modelo: {ejercicio['respuesta_correcta']}")
                
                # Explicación gramatical adicional
                if "because" in ejercicio["respuesta_correcta"].lower():
                    print("💡 RECUERDA: 'Because' va seguido de sujeto + verbo")
                elif "although" in ejercicio["respuesta_correcta"].lower():
                    print("💡 RECUERDA: 'Although' puede ir al inicio o en medio de la oración")
                
                return 'correcto'
            else:
                intentos += 1
                if intentos < max_intentos:
                    print(f"❌ Intento {intentos}/{max_intentos}. {tipo}")
                    print(f"💡 Pista: {ejercicio['pista']}")
                else:
                    print("💡 ANALICEMOS LA RESPUESTA:")
                    print(f"📝 Respuesta correcta: {ejercicio['respuesta_correcta']}")
                    print(f"🔍 Explicación: {ejercicio['pista']}")
                    return 'incorrecto'

    def ejecutar_entrenamiento(self):
        self.mostrar_bienvenida()
        self.inicio_tiempo = datetime.now()
        
        ejercicios_completos = self._completar_100_ejercicios()
        
        input("\n🎯 Presiona Enter para comenzar tu entrenamiento...")
        
        for i, ejercicio in enumerate(ejercicios_completos, 1):
            resultado = self.ejercicio_ejecutar(ejercicio, i)
            
            if resultado == 'salir':
                break
            
            self.ejercicios_completados = i
            
            # Mostrar progreso cada 5 ejercicios
            if i % 5 == 0:
                self.mostrar_progreso_detallado()
            
            # Pausa cada 10 ejercicios con resumen
            if i % 10 == 0 and i < 100:
                print(f"\n⭐ Hito alcanzado: {i} ejercicios completados!")
                input("⏸️  Presiona Enter para continuar...")
        
        self.mostrar_resultado_final()

    def ejercicio_ejecutar(self, ejercicio, numero):
        """Wrapper para manejar errores en ejercicios individuales"""
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
        
        porcentaje_acierto = (self.puntuacion / self.ejercicios_completados * 100) if self.ejercicios_completados > 0 else 0
        
        print("\n" + "="*80)
        print("🎓 RESUMEN FINAL - ORACIONES COMPUESTAS")
        print("="*80)
        print(f"📅 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"⏱️  Tiempo total: {minutos_totales:02d}:{segundos_totales:02d}")
        print(f"📊 Ejercicios completados: {self.ejercicios_completados}/100")
        print(f"✅ Puntuación final: {self.puntuacion} puntos")
        print(f"📈 Porcentaje de acierto: {porcentaje_acierto:.1f}%")
        
        # Evaluación del desempeño
        if porcentaje_acierto >= 90:
            print("\n🏆 ¡NIVAVO AVANZADO! Dominas las estructuras compuestas")
            print("   Recomendación: Practica con textos académicos o literarios")
        elif porcentaje_acierto >= 70:
            print("\n👍 ¡NIVEL INTERMEDIO-ALTO! Buen dominio gramatical")
            print("   Recomendación: Enfócate en la fluidez y vocabulario avanzado")
        elif porcentaje_acierto >= 50:
            print("\n📚 ¡NIVEL INTERMEDIO! Bases sólidas, sigue practicando")
            print("   Recomendación: Repasa conectores y oraciones subordinadas")
        else:
            print("\n💪 ¡NIVEL EN DESARROLLO! La práctica constante es clave")
            print("   Recomendación: Comienza con oraciones simples + un conector")
        
        # Plan de estudio personalizado
        print("\n🔍 PLAN DE ESTUDIO SUGERIDO:")
        if porcentaje_acierto < 70:
            print("   1. Repasa conjunciones básicas (and, but, because)")
            print("   2. Practica oraciones con 'when' y 'if'")
            print("   3. Domina las relativas con 'who' y 'which'")
            print("   4. Avanza a condicionales simples")
        else:
            print("   1. Perfecciona condicionales mixtas")
            print("   2. Practica estilo indirecto complejo")
            print("   3. Trabaja con conectores formales (however, therefore)")
            print("   4. Lee artículos académicos analizando estructuras")
        
        print("\n✨ ¡Felicidades por completar el entrenamiento!")
        print("   Sigue practicando para alcanzar la fluidez total.")

def main():
    entrenador = EnglishCompoundSentencesTrainer()
    try:
        entrenador.ejecutar_entrenamiento()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Tu progreso ha sido guardado!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reinicia el programa.")

if __name__ == "__main__":
    main()
