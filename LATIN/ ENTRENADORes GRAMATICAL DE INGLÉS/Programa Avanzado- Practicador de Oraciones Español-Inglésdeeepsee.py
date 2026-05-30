import os
import random

# Datos para la tabla comparativa
table_data = [
    ["Tipo", "Estructura Español", "Ejemplo Español", "Estructura Inglés", "Ejemplo Inglés"],
    ["Afirmativa", "Sujeto + Verbo + Objeto", "Ella lee libros", "Sujeto + Verbo + Objeto", "She reads books"],
    ["Negativa", "No + Verbo", "No tenemos tiempo", "Sujeto + do/does/did + not + verbo", "We do not have time"],
    ["Interrogativa Sí/No", "¿ + Verbo + Sujeto + ?", "¿Tú entiendes?", "Do/Does/Did + Sujeto + Verbo + ?", "Do you understand?"],
    ["Interrogativa WH-", "¿ + WH- + Verbo + Sujeto + ?", "¿Qué quieres tú?", "WH- + do/does/did + Sujeto + Verbo + ?", "What do you want?"],
    ["Exclamativa", "¡ + Qué/Cómo + !", "¡Qué sorpresa!", "What/How + !", "What a surprise!"]
]

# 100 ejercicios para practicar (español, inglés, tipo, dificultad)
exercises = [
    # Afirmativas (20)
    ("Él cocina pescado", "He cooks fish", "afirmativa", 1),
    ("Yo camino al parque", "I walk to the park", "afirmativa", 1),
    ("Nosotros estudiamos inglés", "We study English", "afirmativa", 1),
    ("Ella lee un libro", "She reads a book", "afirmativa", 1),
    ("Ellos juegan fútbol", "They play soccer", "afirmativa", 1),
    ("El niño corre rápido", "The boy runs fast", "afirmativa", 1),
    ("La mujer cocina bien", "The woman cooks well", "afirmativa", 1),
    ("Ustedes trabajan mucho", "You work a lot", "afirmativa", 1),
    ("Mi hermana canta bonito", "My sister sings beautifully", "afirmativa", 2),
    ("Nuestro equipo gana siempre", "Our team always wins", "afirmativa", 2),
    ("El sol brilla intensamente", "The sun shines brightly", "afirmativa", 2),
    ("Los estudiantes aprenden rápido", "The students learn quickly", "afirmativa", 2),
    ("Mi padre conduce cuidadosamente", "My father drives carefully", "afirmativa", 2),
    ("Esa empresa crece constantemente", "That company grows constantly", "afirmativa", 3),
    ("El proyecto avanza satisfactoriamente", "The project progresses satisfactorily", "afirmativa", 3),
    ("Nuestros productos mejoran continuamente", "Our products improve continuously", "afirmativa", 3),
    
    # Negativas (20)
    ("Ella no canta bien", "She does not sing well", "negativa", 1),
    ("Nosotros no jugamos fútbol", "We do not play soccer", "negativa", 1),
    ("Yo no como carne", "I do not eat meat", "negativa", 1),
    ("Ellos no estudian francés", "They do not study French", "negativa", 1),
    ("Tú no trabajas los domingos", "You do not work on Sundays", "negativa", 1),
    ("El niño no llora", "The boy does not cry", "negativa", 1),
    ("Usted no fuma", "You do not smoke", "negativa", 1),
    ("Ellas no bailan bien", "They do not dance well", "negativa", 1),
    ("Mi hermano no practica deportes", "My brother does not practice sports", "negativa", 2),
    ("Nuestro equipo no pierde nunca", "Our team never loses", "negativa", 2),
    ("Ese restaurante no abre los lunes", "That restaurant does not open on Mondays", "negativa", 2),
    ("El avión no llegó a tiempo", "The plane did not arrive on time", "negativa", 2),
    ("No entendí la pregunta", "I did not understand the question", "negativa", 2),
    ("El gobierno no aprobó la ley", "The government did not approve the law", "negativa", 3),
    ("La empresa no cumplió sus objetivos", "The company did not meet its objectives", "negativa", 3),
    
    # Interrogativas Sí/No (20)
    ("¿Ellos estudian inglés?", "Do they study English?", "interrogativa sí/no", 1),
    ("¿Tú necesitas ayuda?", "Do you need help?", "interrogativa sí/no", 1),
    ("¿Ella canta bien?", "Does she sing well?", "interrogativa sí/no", 1),
    ("¿Ustedes trabajan aquí?", "Do you work here?", "interrogativa sí/no", 1),
    ("¿El niño corre rápido?", "Does the boy run fast?", "interrogativa sí/no", 1),
    ("¿Ellos juegan fútbol?", "Do they play soccer?", "interrogativa sí/no", 1),
    ("¿Tu hermano lee mucho?", "Does your brother read a lot?", "interrogativa sí/no", 2),
    ("¿Tu familia viaja frecuentemente?", "Does your family travel frequently?", "interrogativa sí/no", 2),
    ("¿Comprendiste la lección?", "Did you understand the lesson?", "interrogativa sí/no", 2),
    ("¿Ellos terminaron el proyecto?", "Did they finish the project?", "interrogativa sí/no", 2),
    ("¿El equipo ganó el campeonato?", "Did the team win the championship?", "interrogativa sí/no", 2),
    ("¿Estudiarás medicina?", "Will you study medicine?", "interrogativa sí/no", 3),
    ("¿Habías visitado antes este lugar?", "Had you visited this place before?", "interrogativa sí/no", 3),
    
    # Interrogativas WH- (20)
    ("¿Dónde trabaja tu madre?", "Where does your mother work?", "interrogativa wh-", 1),
    ("¿Qué quieres comer?", "What do you want to eat?", "interrogativa wh-", 1),
    ("¿Cuándo llegaste?", "When did you arrive?", "interrogativa wh-", 1),
    ("¿Por qué lloras?", "Why do you cry?", "interrogativa wh-", 1),
    ("¿Cómo te llamas?", "What is your name?", "interrogativa wh-", 1),
    ("¿Dónde viven ellos?", "Where do they live?", "interrogativa wh-", 1),
    ("¿Qué estudia tu hermana?", "What does your sister study?", "interrogativa wh-", 2),
    ("¿Cuándo termina la película?", "When does the movie end?", "interrogativa wh-", 2),
    ("¿Cómo funciona esta máquina?", "How does this machine work?", "interrogativa wh-", 2),
    ("¿Por qué no viniste ayer?", "Why didn't you come yesterday?", "interrogativa wh-", 2),
    ("¿Qué habrías hecho diferente?", "What would you have done differently?", "interrogativa wh-", 3),
    ("¿Cómo podría mejorar mi pronunciación?", "How could I improve my pronunciation?", "interrogativa wh-", 3),
    
    # Exclamativas (20)
    ("¡Qué día tan horrible!", "What a horrible day!", "exclamativa", 1),
    ("¡Cómo me gusta este lugar!", "How I like this place!", "exclamativa", 1),
    ("¡Qué sorpresa!", "What a surprise!", "exclamativa", 1),
    ("¡Qué bonito!", "How beautiful!", "exclamativa", 1),
    ("¡Qué inteligente eres!", "How smart you are!", "exclamativa", 1),
    ("¡Qué rápido corres!", "How fast you run!", "exclamativa", 1),
    ("¡Qué bien cantas!", "How well you sing!", "exclamativa", 2),
    ("¡Qué increíble historia!", "What an incredible story!", "exclamativa", 2),
    ("¡Cómo has crecido!", "How you have grown!", "exclamativa", 2),
    ("¡Qué maravilloso resultado!", "What a wonderful result!", "exclamativa", 2),
    ("¡Qué desastre absoluto!", "What an absolute disaster!", "exclamativa", 3),
    ("¡Cómo podría olvidar ese momento!", "How could I forget that moment!", "exclamativa", 3),
]

def print_table():
    """Imprime la tabla comparativa con formato"""
    print("\n" + "="*120)
    print("TABLA COMPARATIVA: ESTRUCTURAS DE ORACIONES (ESPAÑOL ↔ INGLÉS)")
    print("="*120)
    
    for row in table_data:
        print(f"{row[0]:<20} | {row[1]:<25} | {row[2]:<25} | {row[3]:<25} | {row[4]:<20}")
        if row[0] == "Tipo":
            print("-"*120)

def practice_exercises():
    """Modo de práctica con 100 ejercicios y sistema de puntuación"""
    print("\n" + "="*60)
    print("MODO PRÁCTICA: TRADUCE LAS ORACIONES")
    print("="*60)
    print("Instrucciones: Traduce la oración mostrada. Escribe 'salir' para terminar.")
    print("Niveles de dificultad: 1 (★), 2 (★★), 3 (★★★)")
    print("Puntuación: +1 por respuesta correcta, +0 por incorrecta, +0.5 por casi correcta")
    print("-"*60)
    
    # Mezclar ejercicios
    random.shuffle(exercises)
    score = 0
    total = min(100, len(exercises))
    
    for i in range(total):
        esp, eng_correct, tipo, dificultad = exercises[i]
        stars = "★" * dificultad
        
        print(f"\nEjercicio {i+1}/{total} ({tipo}) Dificultad: {stars}")
        print(f"Español: {esp}")
        
        user_input = input("Tu traducción al inglés: ").strip()
        
        if user_input.lower() == 'salir':
            break
            
        # Evaluación de la respuesta
        if user_input.lower() == eng_correct.lower():
            print("✅ ¡Correcto! +1 punto")
            score += 1
        else:
            # Verificación de respuestas "casi correctas" (sin signos de puntuación o con errores menores)
            user_clean = user_input.lower().replace("?", "").replace("!", "").replace(".", "").strip()
            correct_clean = eng_correct.lower().replace("?", "").replace("!", "").replace(".", "").strip()
            
            if user_clean == correct_clean:
                print("✅ ¡Casi correcto! (+0.5 puntos) - Revisa signos de puntuación")
                score += 0.5
            else:
                print(f"❌ Incorrecto. La respuesta era: {eng_correct}")
    
    # Resultado final
    print("\n" + "="*60)
    print("RESULTADO FINAL")
    print("="*60)
    print(f"Puntuación total: {score}/{total}")
    percentage = (score / total) * 100
    print(f"Porcentaje de aciertos: {percentage:.1f}%")
    
    # Evaluación cualitativa
    if percentage >= 90:
        print("🎖️ Excelente! Dominas las estructuras gramaticales.")
    elif percentage >= 70:
        print("👍 Buen trabajo! Sigues mejorando.")
    elif percentage >= 50:
        print("👌 No está mal! Sigue practicando.")
    else:
        print("💪 Necesitas más práctica. Sigue intentándolo.")
    
    input("\nPresiona Enter para continuar...")

def main():
    """Función principal"""
    while True:
        print("\n" + "="*60)
        print("APRENDIZAJE DE ESTRUCTURAS DE ORACIONES INGLÉS/ESPAÑOL")
        print("="*60)
        print("1. Ver tabla comparativa")
        print("2. Practicar con 100 ejercicios")
        print("3. Salir")
        
        choice = input("Elige una opción (1-3): ").strip()
        
        if choice == "1":
            print_table()
            input("\nPresiona Enter para continuar...")
        elif choice == "2":
            practice_exercises()
        elif choice == "3":
            print("¡Hasta pronto! Sigue practicando.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        # Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
