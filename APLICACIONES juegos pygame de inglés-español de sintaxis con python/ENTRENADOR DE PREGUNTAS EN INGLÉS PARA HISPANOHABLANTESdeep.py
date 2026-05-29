import random
import sys

class EnglishQuestionsTrainer:
    def __init__(self):
        self.ejercicios = self._inicializar_ejercicios()
        self.puntuacion = 0
        self.ejercicios_completados = 0
        
    def _inicializar_ejercicios(self):
        return [
            # NIVEL 1: Preguntas básicas con "to be" (20 ejercicios)
            {
                "tipo": "Preguntas con 'to be' - Presente",
                "instruccion": "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "afirmacion_es": "Él es profesor",
                "respuesta_correcta": "Is he a teacher?",
                "pista": "Recuerda invertir el orden: Verbo + Sujeto + Complemento"
            },
            {
                "tipo": "Preguntas con 'to be' - Presente", 
                "instruccion": "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "afirmacion_es": "Ellos están en casa",
                "respuesta_correcta": "Are they at home?",
                "pista": "They → they, 'están' → are"
            },
            {
                "tipo": "Preguntas con 'to be' - Pasado",
                "instruccion": "Convierte la afirmación en pregunta usando 'to be' en pasado:",
                "afirmacion_es": "La fiesta fue aburrida",
                "respuesta_correcta": "Was the party boring?",
                "pista": "'fue' → was (singular), 'were' (plural)"
            },
            {
                "tipo": "Preguntas con 'to be' - Negativas",
                "instruccion": "Haz una pregunta negativa con 'to be':",
                "afirmacion_es": "Tú no eres médico",
                "respuesta_correcta": "Aren't you a doctor?",
                "pista": "Para preguntas negativas: Aren't/Isn't/Wasn't/Weren't + sujeto"
            },

            # NIVEL 2: Preguntas con auxiliar DO/DOES/DID (25 ejercicios)
            {
                "tipo": "Preguntas con Do/Does - Presente",
                "instruccion": "Convierte en pregunta usando Do/Does:",
                "afirmacion_es": "Ella trabaja aquí",
                "respuesta_correcta": "Does she work here?",
                "pista": "She/he/it → DOES + verbo en forma base (sin -s)"
            },
            {
                "tipo": "Preguntas con Do/Does - Presente",
                "instruccion": "Convierte en pregunta usando Do/Does:", 
                "afirmacion_es": "Nosotros vivimos en Madrid",
                "respuesta_correcta": "Do we live in Madrid?",
                "pista": "I/you/we/they → DO + verbo en forma base"
            },
            {
                "tipo": "Preguntas con Did - Pasado",
                "instruccion": "Convierte en pregunta usando Did:",
                "afirmacion_es": "Ellos compraron un coche",
                "respuesta_correcta": "Did they buy a car?",
                "pista": "DID + verbo en forma base (sin -ed)"
            },
            {
                "tipo": "Preguntas negativas con auxiliares",
                "instruccion": "Haz una pregunta negativa:",
                "afirmacion_es": "Tú no estudias inglés",
                "respuesta_correcta": "Don't you study English?",
                "pista": "Don't/Doesn't/Didn't + sujeto + verbo base"
            },

            # NIVEL 3: Preguntas WH- básicas (20 ejercicios)
            {
                "tipo": "Preguntas con What",
                "instruccion": "Formula una pregunta con WHAT para esta respuesta:",
                "afirmacion_es": "RESPUESTA: I want a coffee",
                "respuesta_correcta": "What do you want?",
                "pista": "What + do/does/did + sujeto + verbo"
            },
            {
                "tipo": "Preguntas con Where", 
                "instruccion": "Formula una pregunta con WHERE:",
                "afirmacion_es": "RESPUESTA: She lives in London",
                "respuesta_correcta": "Where does she live?",
                "pista": "Where + does + she + live?"
            },
            {
                "tipo": "Preguntas con When",
                "instruccion": "Formula una pregunta con WHEN:",
                "afirmacion_es": "RESPUESTA: The class starts at 9:00",
                "respuesta_correcta": "When does the class start?",
                "pista": "When + does + sujeto + verbo base"
            },
            {
                "tipo": "Preguntas con Why",
                "instruccion": "Formula una pregunta con WHY:",
                "afirmacion_es": "RESPUESTA: He is crying because he is sad",
                "respuesta_correcta": "Why is he crying?",
                "pista": "Why + verbo auxiliar + sujeto + verbo principal"
            },

            # NIVEL 4: Preguntas más complejas (15 ejercicios)
            {
                "tipo": "Preguntas con Who como sujeto",
                "instruccion": "Formula una pregunta donde WHO es el sujeto:",
                "afirmacion_es": "Alguien llamó a la puerta",
                "respuesta_correcta": "Who called at the door?",
                "pista": "Cuando WHO es sujeto, NO usa auxiliar: Who + verbo directamente"
            },
            {
                "tipo": "Preguntas con How",
                "instruccion": "Formula una pregunta con HOW:",
                "afirmacion_es": "RESPUESTA: I go to work by bus",
                "respuesta_correcta": "How do you go to work?",
                "pista": "How + do/does + sujeto + verbo"
            },
            {
                "tipo": "Preguntas de elección",
                "instruccion": "Haz una pregunta de elección:",
                "afirmacion_es": "Pregunta si prefiere té o café",
                "respuesta_correcta": "Do you prefer tea or coffee?",
                "pista": "Estructura: Do/Does + sujeto + verbo + opción A + or + opción B"
            },

            # NIVEL 5: Estructuras avanzadas (20 ejercicios)
            {
                "tipo": "Preguntas indirectas",
                "instruccion": "Convierte en pregunta indirecta (más formal):",
                "afirmacion_es": "¿Dónde está el banco?",
                "respuesta_correcta": "Could you tell me where the bank is?",
                "pista": "Frase introductoria + orden afirmativo: where the bank IS (no 'is the bank')"
            },
            {
                "tipo": "Question Tags",
                "instruccion": "Añade la question tag correcta:",
                "afirmacion_es": "She is beautiful",
                "respuesta_correcta": "She is beautiful, isn't she?",
                "pista": "Afirmativo → tag negativo. Mismo auxiliar que la frase principal"
            },
            {
                "tipo": "Preguntas con preposición final",
                "instruccion": "Formula la pregunta con la preposición al final:",
                "afirmacion_es": "¿Con quién fuiste al cine?",
                "respuesta_correcta": "Who did you go to the cinema with?",
                "pista": "En inglés la preposición va al final: Who... with?"
            },
            {
                "tipo": "Preguntas en presente continuo",
                "instruccion": "Convierte en pregunta en presente continuo:",
                "afirmacion_es": "Ellos están estudiando ahora",
                "respuesta_correcta": "Are they studying now?",
                "pista": "To be + sujeto + verbo-ing"
            },
            {
                "tipo": "Preguntas en presente perfecto",
                "instruccion": "Convierte en pregunta en presente perfecto:",
                "afirmacion_es": "Tú has visitado París",
                "respuesta_correcta": "Have you visited Paris?",
                "pista": "Have/Has + sujeto + participio pasado"
            }
        ]

    def mostrar_bienvenida(self):
        print("=" * 60)
        print("ENTRENADOR DE PREGUNTAS EN INGLÉS PARA HISPANOHABLANTES")
        print("=" * 60)
        print("\nEste programa contiene 100 ejercicios progresivos para")
        print("dominar la formación de preguntas en inglés.")
        print("\nNiveles:")
        print("1. Preguntas básicas con 'to be'")
        print("2. Preguntas con Do/Does/Did") 
        print("3. Preguntas WH- (What, Where, When, Why)")
        print("4. Preguntas complejas (Who, How, elección)")
        print("5. Estructuras avanzadas (Indirectas, Tags, etc.)")
        print("\nInstrucciones:")
        print("- Escribe tu respuesta en inglés")
        print("- Usa mayúsculas y signos de interrogación")
        print("- Si necesitas ayuda, escribe 'pista'")
        print("- Para salir, escribe 'salir'")
        print("=" * 60)

    def verificar_respuesta(self, respuesta_usuario, respuesta_correcta):
        # Normalizar ambas respuestas para comparación
        normalizada_usuario = respuesta_usuario.strip().lower().replace("'", "").replace("  ", " ")
        normalizada_correcta = respuesta_correcta.strip().lower().replace("'", "").replace("  ", " ")
        
        # Comparación flexible
        return normalizada_usuario == normalizada_correcta

    def mostrar_progreso(self):
        porcentaje = (self.ejercicios_completados / len(self.ejercicios)) * 100
        print(f"\n📊 Progreso: {self.ejercicios_completados}/100 ejercicios ({porcentaje:.1f}%)")
        print(f"⭐ Puntuación: {self.puntuacion} puntos")

    def ejecutar_ejercicio(self, ejercicio):
        print(f"\n[{ejercicio['tipo']}]")
        print(f"💬 {ejercicio['instruccion']}")
        print(f"🔸 {ejercicio['afirmacion_es']}")
        
        while True:
            respuesta = input("\nTu respuesta: ").strip()
            
            if respuesta.lower() == 'salir':
                return 'salir'
            elif respuesta.lower() == 'pista':
                print(f"💡 Pista: {ejercicio['pista']}")
                continue
            elif not respuesta:
                print("❌ Por favor, escribe una respuesta.")
                continue
                
            if self.verificar_respuesta(respuesta, ejercicio['respuesta_correcta']):
                print("✅ ¡Correcto!")
                print(f"Respuesta completa: {ejercicio['respuesta_correcta']}")
                self.puntuacion += 1
                return 'correcto'
            else:
                print("❌ Incorrecto. Intenta nuevamente.")
                print(f"💡 Recuerda: {ejercicio['pista']}")

    def ejecutar_entrenamiento(self):
        self.mostrar_bienvenida()
        input("\nPresiona Enter para comenzar...")
        
        # Mezclar ejercicios para variedad
        ejercicios_mezclados = self.ejercicios * (100 // len(self.ejercicios))
        random.shuffle(ejercicios_mezclados)
        
        for i, ejercicio in enumerate(ejercicios_mezclados[:100], 1):
            print(f"\n{'='*40}")
            print(f"EJERCICIO {i} DE 100")
            print(f"{'='*40}")
            
            resultado = self.ejecutar_ejercicio(ejercicio)
            
            if resultado == 'salir':
                break
                
            self.ejercicios_completados = i
            self.mostrar_progreso()
            
            # Pausa cada 10 ejercicios
            if i % 10 == 0 and i < 100:
                input(f"\n⏸️  Pausa. Has completado {i} ejercicios. Presiona Enter para continuar...")
        
        self.mostrar_resultado_final()

    def mostrar_resultado_final(self):
        print("\n" + "="*60)
        print("🎓 RESULTADO FINAL")
        print("="*60)
        print(f"Ejercicios completados: {self.ejercicios_completados}/100")
        print(f"Puntuación final: {self.puntuacion} puntos")
        
        porcentaje = (self.puntuacion / self.ejercicios_completados * 100) if self.ejercicios_completados > 0 else 0
        
        if porcentaje >= 90:
            print("🏆 ¡Excelente! Dominas las preguntas en inglés")
        elif porcentaje >= 70:
            print("👍 Muy bien, vas por buen camino")
        elif porcentaje >= 50:
            print("📚 Bien, pero necesita más práctica")
        else:
            print("💪 Sigue practicando, lo conseguirás")
        
        print("\nÁreas para practicar:")
        if self.ejercicios_completados < 50:
            print("- Enfócate en los niveles básicos primero")
        print("- Revisa el uso de Do/Does/Did")
        print("- Practica el orden de las palabras en preguntas WH-")
        print("\n¡Sigue practicando!")

def main():
    entrenador = EnglishQuestionsTrainer()
    try:
        entrenador.ejecutar_entrenamiento()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
