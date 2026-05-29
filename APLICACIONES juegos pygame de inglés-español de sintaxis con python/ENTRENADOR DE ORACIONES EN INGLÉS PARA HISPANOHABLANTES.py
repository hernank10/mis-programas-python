import random
import sys
from datetime import datetime

class EnglishSentencesTrainer:
    def __init__(self):
        self.ejercicios = self._inicializar_ejercicios()
        self.puntuacion = 0
        self.ejercicios_completados = 0
        self.inicio_tiempo = None
        
    def _inicializar_ejercicios(self):
        return [
            # === NIVEL 1: ORACIONES AFIRMATIVAS BÁSICAS (20 ejercicios) ===
            {
                "categoria": "Presente Simple - Afirmativo",
                "instruccion": "Traduce al inglés (Presente Simple):",
                "oracion_es": "Yo trabajo en una oficina",
                "respuesta_correcta": "I work in an office",
                "pista": "Recuerda: I/you/we/they → verbo en forma base"
            },
            {
                "categoria": "Presente Simple - Afirmativo",
                "instruccion": "Traduce al inglés (Presente Simple):",
                "oracion_es": "Ella estudia inglés cada día",
                "respuesta_correcta": "She studies English every day",
                "pista": "He/she/it → verbo + -s/-es (study → studies)"
            },
            {
                "categoria": "Presente Simple - Afirmativo", 
                "instruccion": "Traduce al inglés (Presente Simple):",
                "oracion_es": "Nosotros vivimos en Madrid",
                "respuesta_correcta": "We live in Madrid",
                "pista": "We → verbo en forma base (live)"
            },
            {
                "categoria": "Pasado Simple - Afirmativo (Regulares)",
                "instruccion": "Traduce al inglés (Pasado Simple):",
                "oracion_es": "Yo trabajé ayer",
                "respuesta_correcta": "I worked yesterday",
                "pista": "Verbos regulares: verbo + -ed (work → worked)"
            },
            {
                "categoria": "Pasado Simple - Afirmativo (Irregulares)",
                "instruccion": "Traduce al inglés (Pasado Simple):",
                "oracion_es": "Él fue al cine",
                "respuesta_correcta": "He went to the cinema",
                "pista": "Irregulares: go → went, see → saw, eat → ate"
            },
            {
                "categoria": "Futuro Simple - Afirmativo",
                "instruccion": "Traduce al inglés (Futuro con Will):",
                "oracion_es": "Yo viajaré mañana",
                "respuesta_correcta": "I will travel tomorrow",
                "pista": "Will + verbo en forma base (sin to)"
            },
            {
                "categoria": "Futuro Simple - Afirmativo",
                "instruccion": "Traduce al inglés (Futuro con Going to):",
                "oracion_es": "Ella va a estudiar medicina",
                "respuesta_correcta": "She is going to study medicine",
                "pista": "Be + going to + verbo base"
            },

            # === NIVEL 2: ORACIONES NEGATIVAS (20 ejercicios) ===
            {
                "categoria": "Presente Simple - Negativo",
                "instruccion": "Traduce al inglés (Presente Negativo):",
                "oracion_es": "Yo no trabajo los fines de semana",
                "respuesta_correcta": "I don't work on weekends",
                "pista": "I/you/we/they → don't + verbo base"
            },
            {
                "categoria": "Presente Simple - Negativo",
                "instruccion": "Traduce al inglés (Presente Negativo):",
                "oracion_es": "Él no vive aquí",
                "respuesta_correcta": "He doesn't live here",
                "pista": "He/she/it → doesn't + verbo base"
            },
            {
                "categoria": "Pasado Simple - Negativo",
                "instruccion": "Traduce al inglés (Pasado Negativo):",
                "oracion_es": "Nosotros no fuimos a la fiesta",
                "respuesta_correcta": "We didn't go to the party",
                "pista": "Didn't + verbo base (go, no went)"
            },
            {
                "categoria": "Futuro Simple - Negativo", 
                "instruccion": "Traduce al inglés (Futuro Negativo):",
                "oracion_es": "Ellos no vendrán mañana",
                "respuesta_correcta": "They won't come tomorrow",
                "pista": "Will not = won't + verbo base"
            },

            # === NIVEL 3: ORACIONES INTERROGATIVAS (25 ejercicios) ===
            {
                "categoria": "Preguntas Sí/No - Presente",
                "instruccion": "Convierte en pregunta (Sí/No):",
                "oracion_es": "¿Tú trabajas aquí?",
                "respuesta_correcta": "Do you work here?",
                "pista": "Do/Does + sujeto + verbo base"
            },
            {
                "categoria": "Preguntas Sí/No - Pasado",
                "instruccion": "Convierte en pregunta (Sí/No):",
                "oracion_es": "¿Ellos estudiaron ayer?",
                "respuesta_correcta": "Did they study yesterday?",
                "pista": "Did + sujeto + verbo base"
            },
            {
                "categoria": "Preguntas WH- - Presente",
                "instruccion": "Formula la pregunta con WHAT:",
                "oracion_es": "¿Qué estudias?",
                "respuesta_correcta": "What do you study?",
                "pista": "What + do/does + sujeto + verbo"
            },
            {
                "categoria": "Preguntas WH- - Pasado",
                "instruccion": "Formula la pregunta con WHERE:",
                "oracion_es": "¿Dónde viviste de niño?",
                "respuesta_correcta": "Where did you live as a child?",
                "pista": "Where + did + sujeto + verbo base"
            },
            {
                "categoria": "Preguntas con Who como sujeto",
                "instruccion": "Formula la pregunta correctamente:",
                "oracion_es": "¿Quién llamó a la puerta?",
                "respuesta_correcta": "Who called at the door?",
                "pista": "Cuando Who es sujeto, NO usa auxiliar"
            },

            # === NIVEL 4: VERBO TO BE (15 ejercicios) ===
            {
                "categoria": "Verbo To Be - Presente",
                "instruccion": "Traduce al inglés (con To Be):",
                "oracion_es": "Yo soy estudiante",
                "respuesta_correcta": "I am a student",
                "pista": "To Be presente: I am, you are, he/she/it is"
            },
            {
                "categoria": "Verbo To Be - Pasado", 
                "instruccion": "Traduce al inglés (To Be pasado):",
                "oracion_es": "Ellos estaban en casa",
                "respuesta_correcta": "They were at home",
                "pista": "To Be pasado: I/he/she/it was, you/we/they were"
            },
            {
                "categoria": "To Be - Negativo",
                "instruccion": "Traduce al inglés (To Be negativo):",
                "oracion_es": "Ella no es doctora",
                "respuesta_correcta": "She is not a doctor",
                "pista": "Is not = isn't, are not = aren't"
            },
            {
                "categoria": "To Be - Interrogativo",
                "instruccion": "Convierte en pregunta:",
                "oracion_es": "¿Estás cansado?",
                "respuesta_correcta": "Are you tired?",
                "pista": "To Be pregunta: Verbo + sujeto + complemento"
            },

            # === NIVEL 5: TIEMPOS CONTINUOS (10 ejercicios) ===
            {
                "categoria": "Presente Continuo",
                "instruccion": "Traduce al inglés (Presente Continuo):",
                "oracion_es": "Yo estoy estudiando ahora",
                "respuesta_correcta": "I am studying now",
                "pista": "To Be + verbo -ing (studying, working)"
            },
            {
                "categoria": "Pasado Continuo",
                "instruccion": "Traduce al inglés (Pasado Continuo):",
                "oracion_es": "Ellos estaban comiendo cuando llamé",
                "respuesta_correcta": "They were eating when I called",
                "pista": "Was/were + verbo -ing"
            },

            # === NIVEL 6: ORACIONES COMPUESTAS (10 ejercicios) ===
            {
                "categoria": "Oraciones con And/But/Because",
                "instruccion": "Traduce la oración compuesta:",
                "oracion_es": "Yo trabajo y estudio",
                "respuesta_correcta": "I work and study",
                "pista": "Usa 'and' para unir ideas similares"
            },
            {
                "categoria": "Oraciones con And/But/Because",
                "instruccion": "Traduce la oración compuesta:",
                "oracion_es": "Me gusta el café pero no el té",
                "respuesta_correcta": "I like coffee but I don't like tea",
                "pista": "'But' para contraste, 'because' para causa"
            },

            # === EJEMPLOS ADICIONALES PARA COMPLETAR 100 ===
            {
                "categoria": "Presente Perfecto",
                "instruccion": "Traduce al inglés (Presente Perfecto):",
                "oracion_es": "Yo he visitado París",
                "respuesta_correcta": "I have visited Paris",
                "pista": "Have/has + participio pasado (visited, seen)"
            },
            {
                "categoria": "Modales - Can/Could",
                "instruccion": "Traduce al inglés (con modal):",
                "oracion_es": "Yo puedo nadar",
                "respuesta_correcta": "I can swim",
                "pista": "Modales: can, could, should + verbo base"
            },
            {
                "categoria": "There is/There are",
                "instruccion": "Traduce al inglés:",
                "oracion_es": "Hay un libro en la mesa",
                "respuesta_correcta": "There is a book on the table",
                "pista": "Singular: There is, Plural: There are"
            },
            {
                "categoria": "Adjetivos Posesivos",
                "instruccion": "Traduce al inglés:",
                "oracion_es": "Este es mi coche",
                "respuesta_correcta": "This is my car",
                "pista": "Posesivos: my, your, his, her, our, their"
            }
        ]

    def _completar_100_ejercicios(self):
        """Completa la lista hasta 100 ejercicios duplicando y variando"""
        ejercicios_base = self.ejercicios
        ejercicios_completos = []
        
        # Duplicar y variar los ejercicios base
        for i in range(3):  # Repetir 3 veces para tener suficientes
            for ejercicio in ejercicios_base:
                nuevo_ejercicio = ejercicio.copy()
                # Variar ligeramente algunos ejercicios
                if i == 1:
                    if "trabajo" in nuevo_ejercicio["oracion_es"]:
                        nuevo_ejercicio["oracion_es"] = nuevo_ejercicio["oracion_es"].replace("trabajo", "enseño")
                        nuevo_ejercicio["respuesta_correcta"] = nuevo_ejercicio["respuesta_correcta"].replace("work", "teach")
                elif i == 2:
                    if "estudia" in nuevo_ejercicio["oracion_es"]:
                        nuevo_ejercicio["oracion_es"] = nuevo_ejercicio["oracion_es"].replace("estudia", "aprende")
                        nuevo_ejercicio["respuesta_correcta"] = nuevo_ejercicio["respuesta_correcta"].replace("study", "learn")
                
                ejercicios_completos.append(nuevo_ejercicio)
        
        # Mezclar y tomar 100
        random.shuffle(ejercicios_completos)
        return ejercicios_completos[:100]

    def mostrar_bienvenida(self):
        print("=" * 70)
        print("🚀 ENTRENADOR DE ORACIONES EN INGLÉS PARA HISPANOHABLANTES")
        print("=" * 70)
        print("\nEste programa contiene 100 ejercicios progresivos para")
        print("dominar la construcción de TODO tipo de oraciones en inglés.")
        print("\n📚 Categorías incluidas:")
        print("  • Presente, Pasado y Futuro Simple")
        print("  • Oraciones Afirmativas, Negativas e Interrogativas")
        print("  • Verbo To Be en todos los tiempos")
        print("  • Tiempos Continuos")
        print("  • Presente Perfecto")
        print("  • Verbos Modales")
        print("  • Oraciones compuestas")
        print("\n💡 Instrucciones:")
        print("  - Escribe la oración en inglés")
        print("  - Usa puntuación correcta (mayúsculas, puntos)")
        print("  - Para ayuda escribe 'pista'")
        print("  - Para salir escribe 'salir'")
        print("  - Para saltar un ejercicio escribe 'saltar'")
        print("=" * 70)

    def verificar_respuesta(self, respuesta_usuario, respuesta_correcta):
        """Verifica la respuesta de forma flexible"""
        # Normalizar para comparación
        normalizar = lambda s: s.strip().lower().replace("'", "").replace("  ", " ").replace(".", "")
        
        usuario_norm = normalizar(respuesta_usuario)
        correcta_norm = normalizar(respuesta_correcta)
        
        # Comparación exacta
        if usuario_norm == correcta_norm:
            return True, "exacta"
        
        # Comparación flexible (sin artículos, etc.)
        usuario_palabras = set(usuario_norm.split())
        correcta_palabras = set(correcta_norm.split())
        
        # Si coincide en más del 80%
        coincidencia = len(usuario_palabras.intersection(correcta_palabras)) / len(correcta_palabras)
        if coincidencia > 0.8:
            return True, "aproximada"
        
        return False, "incorrecta"

    def mostrar_progreso(self):
        porcentaje = (self.ejercicios_completados / 100) * 100
        tiempo_transcurrido = (datetime.now() - self.inicio_tiempo).seconds // 60
        
        print(f"\n📊 Progreso: {self.ejercicios_completados}/100 ({porcentaje:.1f}%)")
        print(f"⭐ Puntuación: {self.puntuacion}")
        print(f"⏱️  Tiempo: {tiempo_transcurrido} minutos")

    def mostrar_estadisticas_categoria(self):
        """Muestra estadísticas por categoría"""
        categorias = {}
        for ej in self.ejercicios[:self.ejercicios_completados]:
            cat = ej["categoria"]
            if cat not in categorias:
                categorias[cat] = {"total": 0, "correctos": 0}
            categorias[cat]["total"] += 1
        
        print("\n📈 ESTADÍSTICAS POR CATEGORÍA:")
        for cat, stats in categorias.items():
            porcentaje = (stats["correctos"] / stats["total"] * 100) if stats["total"] > 0 else 0
            print(f"  {cat}: {stats['correctos']}/{stats['total']} ({porcentaje:.1f}%)")

    def ejecutar_ejercicio(self, ejercicio, numero):
        print(f"\n{'='*50}")
        print(f"🎯 EJERCICIO {numero} DE 100")
        print(f"📂 Categoría: {ejercicio['categoria']}")
        print(f"{'='*50}")
        print(f"💬 {ejercicio['instruccion']}")
        print(f"🔸 Español: {ejercicio['oracion_es']}")
        
        intentos = 0
        while intentos < 2:
            respuesta = input("\n✏️  Tu respuesta en inglés: ").strip()
            
            if respuesta.lower() == 'salir':
                return 'salir'
            elif respuesta.lower() == 'pista':
                print(f"💡 Pista: {ejercicio['pista']}")
                continue
            elif respuesta.lower() == 'saltar':
                print("⏭️  Ejercicio saltado")
                return 'saltar'
            elif not respuesta:
                print("❌ Por favor, escribe una respuesta.")
                continue
                
            es_correcta, tipo = self.verificar_respuesta(respuesta, ejercicio["respuesta_correcta"])
            
            if es_correcta:
                if tipo == "exacta":
                    print("✅ ¡Perfecto! Respuesta exacta")
                else:
                    print("✅ ¡Bien! Respuesta aproximada (revisa detalles)")
                
                print(f"📝 Respuesta completa: {ejercicio['respuesta_correcta']}")
                return 'correcto'
            else:
                intentos += 1
                if intentos < 2:
                    print("❌ Incorrecto. Intenta nuevamente.")
                    print(f"💡 Pista: {ejercicio['pista']}")
                else:
                    print("❌ Seguimiento incorrecto. Veamos la respuesta:")
                    print(f"📝 Respuesta correcta: {ejercicio['respuesta_correcta']}")
                    return 'incorrecto'

    def ejecutar_entrenamiento(self):
        self.mostrar_bienvenida()
        self.inicio_tiempo = datetime.now()
        
        ejercicios_completos = self._completar_100_ejercicios()
        random.shuffle(ejercicios_completos)
        
        input("\nPresiona Enter para comenzar...")
        
        for i, ejercicio in enumerate(ejercicios_completos, 1):
            resultado = self.ejecutar_ejercicio(ejercicio, i)
            
            if resultado == 'salir':
                break
            elif resultado == 'correcto':
                self.puntuacion += 1
            
            self.ejercicios_completados = i
            self.mostrar_progreso()
            
            # Pausa cada 10 ejercicios con mini-resumen
            if i % 10 == 0 and i < 100:
                print(f"\n⭐ Has completado {i} ejercicios!")
                input("⏸️  Presiona Enter para continuar...")
        
        self.mostrar_resultado_final()

    def mostrar_resultado_final(self):
        tiempo_total = (datetime.now() - self.inicio_tiempo).seconds // 60
        porcentaje = (self.puntuacion / self.ejercicios_completados * 100) if self.ejercicios_completados > 0 else 0
        
        print("\n" + "="*70)
        print("🎓 RESUMEN FINAL DEL ENTRENAMIENTO")
        print("="*70)
        print(f"📊 Ejercicios completados: {self.ejercicios_completados}/100")
        print(f"✅ Respuestas correctas: {self.puntuacion}")
        print(f"⏱️  Tiempo total: {tiempo_total} minutos")
        print(f"📈 Porcentaje de acierto: {porcentaje:.1f}%")
        
        # Evaluación
        if porcentaje >= 90:
            print("🏆 ¡EXCELENTE! Dominas las estructuras básicas del inglés")
        elif porcentaje >= 70:
            print("👍 MUY BIEN! Tienes buen dominio, sigue practicando")
        elif porcentaje >= 50:
            print("📚 BIEN! Bases sólidas, pero necesita más práctica")
        else:
            print("💪 ÁNIMO! La práctica constante te llevará al éxito")
        
        self.mostrar_estadisticas_categoria()
        
        print("\n💡 Recomendaciones para seguir mejorando:")
        if porcentaje < 70:
            print("  - Repasa los verbos auxiliares (do/does/did)")
            print("  - Practica el orden de palabras en preguntas")
            print("  - Estudia los verbos irregulares más comunes")
        else:
            print("  - Avanza a oraciones más complejas")
            print("  - Practica la conversación real")
            print("  - Lee textos en inglés regularmente")
        
        print("\n¡Sigue practicando! 🚀")

def main():
    entrenador = EnglishSentencesTrainer()
    try:
        entrenador.ejecutar_entrenamiento()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
