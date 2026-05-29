import os
import random

class EnglishPractice:
    def __init__(self):
        self.level = None
        self.score = 0
        self.total_questions = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("PRACTICANDO IDENTIFICACIÓN DE PERSONAS EN INGLÉS")
            print("=" * 50)
            print("1. Reglas y ejemplos")
            print("2. Ejercicios de nivel básico (to be)")
            print("3. Ejercicios de nivel intermedio (do/does)")
            print("4. Ejercicios de nivel avanzado (wh- questions)")
            print("5. Ejercicios de nivel experto (what...like vs how)")
            print("6. Diálogo completo (práctica integrada)")
            print("7. Salir")
            print("=" * 50)
            
            choice = input("Selecciona una opción (1-7): ")
            
            if choice == "1":
                self.show_rules()
            elif choice == "2":
                self.practice_basic()
            elif choice == "3":
                self.practice_intermediate()
            elif choice == "4":
                self.practice_advanced()
            elif choice == "5":
                self.practice_expert()
            elif choice == "6":
                self.practice_dialogue()
            elif choice == "7":
                print("¡Gracias por practicar! Hasta pronto.")
                break
            else:
                input("Opción no válida. Presiona Enter para continuar...")
    
    def show_rules(self):
        self.clear_screen()
        print("=" * 50)
        print("REGLAS Y EJEMPLOS")
        print("=" * 50)
        print("\n1. PREGUNTAS CON 'TO BE':")
        print("   Estructura: [Verbo To Be] + [Sujeto] + [Complemento]?")
        print("   Ejemplo: 'Are you the teacher?' → ¿Eres el profesor?")
        
        print("\n2. PREGUNTAS CON 'DO/DOES':")
        print("   Estructura: [Do/Does] + [Sujeto] + [Verbo] + [Complemento]?")
        print("   Ejemplo: 'Do you have a brother?' → ¿Tienes un hermano?")
        
        print("\n3. PREGUNTAS CON PRONOMBRES INTERROGATIVOS:")
        print("   Estructura: [Wh-] + [Auxiliar] + [Sujeto] + [Verbo] + [Complemento]?")
        print("   Ejemplo: 'Where does she work?' → ¿Dónde trabaja ella?")
        
        print("\n4. DIFERENCIA ENTRE 'WHAT...LIKE' Y 'HOW':")
        print("   'What + be + like?' → Pregunta por personalidad")
        print("   'How + be?' → Pregunta por estado de salud")
        print("   'What + do/does + look like?' → Pregunta por apariencia física")
        
        input("\nPresiona Enter para volver al menú...")
    
    def check_answer(self, user_answer, correct_answers):
        user_normalized = user_answer.strip().lower()
        correct_normalized = [answer.strip().lower() for answer in correct_answers]
        
        if user_normalized in correct_normalized:
            print("¡Correcto! ✓")
            self.score += 1
            return True
        else:
            print(f"Incorrecto. La respuesta correcta es: '{correct_answers[0]}' ✗")
            return False
    
    def practice_basic(self):
        self.clear_screen()
        print("EJERCICIOS BÁSICOS: PREGUNTAS CON 'TO BE'")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Ella es la nueva estudiante?",
                "answers": ["Is she the new student?"]
            },
            {
                "question": "¿Ellos son de México?",
                "answers": ["Are they from Mexico?"]
            },
            {
                "question": "¿Tú eres el hermano de Ana?",
                "answers": ["Are you Ana's brother?", "Are you the brother of Ana?"]
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_intermediate(self):
        self.clear_screen()
        print("EJERCICIOS INTERMEDIOS: PREGUNTAS CON 'DO/DOES'")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Tú tienes un perro?",
                "answers": ["Do you have a dog?"]
            },
            {
                "question": "¿Él trabaja en una oficina?",
                "answers": ["Does he work in an office?"]
            },
            {
                "question": "¿Ellos estudian inglés?",
                "answers": ["Do they study English?"]
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_advanced(self):
        self.clear_screen()
        print("EJERCICIOS AVANZADOS: PREGUNTAS CON PRONOMBRES INTERROGATIVOS")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Dónde trabaja tu madre?",
                "answers": ["Where does your mother work?"]
            },
            {
                "question": "¿Qué es él? / ¿A qué se dedica?",
                "answers": ["What does he do?"]
            },
            {
                "question": "¿Quién es ese hombre?",
                "answers": ["Who is that man?"]
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_expert(self):
        self.clear_screen()
        print("EJERCICIOS EXPERTO: 'WHAT...LIKE' VS 'HOW'")
        print("=" * 50)
        
        questions = [
            {
                "question": "Pregunta por la personalidad de tu jefe: ¿Cómo es tu jefe?",
                "answers": ["What is your boss like?"]
            },
            {
                "question": "Pregunta por el estado de salud de tu jefe: ¿Cómo está tu jefe?",
                "answers": ["How is your boss?"]
            },
            {
                "question": "Pregunta por la apariencia física de tu hermana: ¿Cómo es tu hermana físicamente?",
                "answers": ["What does your sister look like?"]
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_dialogue(self):
        self.clear_screen()
        print("DIÁLOGO COMPLETO: PRÁCTICA INTEGRADA")
        print("=" * 50)
        print("Contexto: Le estás presentando a tu amigo Marco a tu compañera de clase, Sarah.")
        print("Ella le hace preguntas. Completa las preguntas en inglés.\n")
        
        dialogue_questions = [
            {
                "question": "¿De dónde eres?",
                "answers": ["Where are you from?"]
            },
            {
                "question": "¿A qué te dedicas?",
                "answers": ["What do you do?"]
            },
            {
                "question": "¿Dónde trabajas?",
                "answers": ["Where do you work?"]
            },
            {
                "question": "¿Y cómo es tu hermano? (personalidad)",
                "answers": ["What is your brother like?"]
            }
        ]
        
        self.score = 0
        self.total_questions = len(dialogue_questions)
        
        for i, q in enumerate(dialogue_questions, 1):
            print(f"\nPregunta {i}: {q['question']}")
            user_answer = input("Tu respuesta: ")
            self.check_answer(user_answer, q['answers'])
        
        print(f"\nResultado: {self.score}/{self.total_questions} correctas")
        input("\nPresiona Enter para continuar...")
    
    def run_exercise(self, questions):
        self.score = 0
        self.total_questions = len(questions)
        random.shuffle(questions)
        
        for i, q in enumerate(questions, 1):
            print(f"\nPregunta {i}: {q['question']}")
            user_answer = input("Tu respuesta: ")
            self.check_answer(user_answer, q['answers'])
        
        print(f"\nResultado: {self.score}/{self.total_questions} correctas")
        input("\nPresiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    practice = EnglishPractice()
    practice.show_menu()
