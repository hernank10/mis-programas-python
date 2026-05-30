import os
import random

class EnglishCourse:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.total_questions = 0
        self.completed_levels = set()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_menu(self):
        while True:
            self.clear_screen()
            print("=" * 60)
            print("CURSO DE IDENTIFICACIÓN DE PERSONAS EN INGLÉS")
            print("=" * 60)
            print("1. Reglas y ejemplos completos")
            print("\n--- NIVELES PRINCIPALES ---")
            print("2. Nivel 1: Pronombres + Verbo To Be (Básico)")
            print("3. Nivel 2: To Be + Sustantivos Comunes (Intermedio)")
            print("4. Nivel 3: To Be + Sustantivos Compuestos (Avanzado)")
            print("\n--- MÓDULOS COMPLEMENTARIOS ---")
            print("5. Preguntas con Do/Does")
            print("6. Preguntas con Wh- Questions")
            print("7. What...like vs How")
            print("8. Diálogos contextualizados")
            print("9. Progreso y estadísticas")
            print("10. Salir")
            print("=" * 60)
            
            choice = input("Selecciona una opción (1-10): ")
            
            if choice == "1":
                self.show_rules()
            elif choice == "2":
                self.practice_level1()
            elif choice == "3":
                self.practice_level2()
            elif choice == "4":
                self.practice_level3()
            elif choice == "5":
                self.practice_do_does()
            elif choice == "6":
                self.practice_wh_questions()
            elif choice == "7":
                self.practice_like_vs_how()
            elif choice == "8":
                self.practice_dialogues()
            elif choice == "9":
                self.show_progress()
            elif choice == "10":
                print("¡Gracias por usar el curso! Hasta pronto.")
                break
            else:
                input("Opción no válida. Presiona Enter para continuar...")
    
    def show_rules(self):
        self.clear_screen()
        print("=" * 60)
        print("REGLAS Y EJEMPLOS COMPLETOS")
        print("=" * 60)
        
        print("\n1. ESTRUCTURA BÁSICA CON 'TO BE':")
        print("   Forma afirmativa: Sujeto + am/is/are + complemento")
        print("   Forma interrogativa: Am/Is/Are + sujeto + complemento?")
        print("   Ejemplos:")
        print("   - He is tall → Is he tall?")
        print("   - They are students → Are they students?")
        
        print("\n2. USO DE ARTÍCULOS CON SUSTANTIVOS:")
        print("   Regla: Usamos 'a/an' con sustantivos singulares contables en afirmaciones")
        print("   Excepción: No usamos artículo cuando hablamos en general o con profesiones")
        print("   Ejemplos:")
        print("   - She is a doctor (correcto)")
        print("   - She is doctor (incorrecto)")
        print("   - They are doctors (correcto)")
        
        print("\n3. SUSTANTIVOS COMPUESTOS:")
        print("   Regla: En inglés, los adjetivos y modificadores van antes del sustantivo")
        print("   Ejemplo:")
        print("   - Él es un desarrollador de software → He is a software developer")
        
        print("\n4. PREGUNTAS CON 'DO/DOES':")
        print("   Estructura: Do/Does + sujeto + verbo + complemento?")
        print("   Ejemplo: Does she work here?")
        
        print("\n5. PREGUNTAS CON WH- WORDS:")
        print("   Estructura: Wh- word + do/does + sujeto + verbo + complemento?")
        print("   Ejemplo: Where does she work?")
        
        input("\nPresiona Enter para volver al menú...")
    
    def check_answer(self, user_answer, correct_answers, explanation=None):
        user_normalized = user_answer.strip().lower()
        correct_normalized = [answer.strip().lower() for answer in correct_answers]
        
        if user_normalized in correct_normalized:
            print("¡Correcto! ✓")
            if explanation:
                print(f"   Explicación: {explanation}")
            self.score += 1
            return True
        else:
            print(f"Incorrecto. ✗")
            print(f"   La respuesta correcta es: '{correct_answers[0]}'")
            if explanation:
                print(f"   Explicación: {explanation}")
            return False
    
    def practice_level1(self):
        self.clear_screen()
        print("NIVEL 1: PRONOMBRES + VERBO TO BE (BÁSICO)")
        print("=" * 50)
        print("Objetivo: Dominar la estructura básica con pronombres personales.")
        print()
        
        questions = [
            {
                "question": "¿Él es alto?",
                "answers": ["Is he tall?", "Is he tall"],
                "explanation": "Usamos 'is' con he/she/it, y la estructura interrogativa invierte el orden: Is + he + adjective?"
            },
            {
                "question": "¿Ellos son estudiantes?",
                "answers": ["Are they students?", "Are they students"],
                "explanation": "Usamos 'are' con they/we/you, y la estructura interrogativa invierte el orden: Are + they + noun?"
            },
            {
                "question": "¿Tú eres mexicano?",
                "answers": ["Are you Mexican?", "Are you Mexican"],
                "explanation": "Usamos 'are' con you, y los adjetivos de nacionalidad no llevan artículo."
            },
            {
                "question": "¿Ella es de España?",
                "answers": ["Is she from Spain?", "Is she from Spain"],
                "explanation": "Para preguntar por origen, usamos 'from + país'. La estructura es: Is + she + from + country?"
            },
            {
                "question": "¿Nosotros somos amigos?",
                "answers": ["Are we friends?", "Are we friends"],
                "explanation": "Usamos 'are' con we, y los sustantivos plurales no llevan artículo."
            }
        ]
        
        result = self.run_exercise(questions)
        if result:
            self.completed_levels.add(1)
    
    def practice_level2(self):
        self.clear_screen()
        print("NIVEL 2: TO BE + SUSTANTIVOS COMUNES (INTERMEDIO)")
        print("=" * 50)
        print("Objetivo: Aprender a usar artículos y posesivos con sustantivos comunes.")
        print()
        
        questions = [
            {
                "question": "¿Él es un doctor?",
                "answers": ["Is he a doctor?", "Is he a doctor"],
                "explanation": "Los sustantivos singulares contables (doctor) necesitan artículo indefinido (a/an)."
            },
            {
                "question": "¿Ella es mi hermana?",
                "answers": ["Is she my sister?", "Is she my sister"],
                "explanation": "Los adjetivos posesivos (my, your, his, her) van antes del sustantivo."
            },
            {
                "question": "¿Ellos son nuestros padres?",
                "answers": ["Are they our parents?", "Are they our parents"],
                "explanation": "Parentesco en plural (parents) no lleva artículo. 'Our' es el posesivo para we."
            },
            {
                "question": "¿Tú eres el profesor?",
                "answers": ["Are you the teacher?", "Are you the teacher"],
                "explanation": "Usamos 'the' cuando nos referimos a algo específico o único."
            },
            {
                "question": "¿Ella es una buena estudiante?",
                "answers": ["Is she a good student?", "Is she a good student"],
                "explanation": "Los adjetivos (good) van antes del sustantivo (student)."
            }
        ]
        
        result = self.run_exercise(questions)
        if result:
            self.completed_levels.add(2)
    
    def practice_level3(self):
        self.clear_screen()
        print("NIVEL 3: TO BE + SUSTANTIVOS COMPUESTOS (AVANZADO)")
        print("=" * 50)
        print("Objetivo: Dominar estructuras complejas con sustantivos compuestos y abstractos.")
        print()
        
        questions = [
            {
                "question": "¿Él es un desarrollador de software?",
                "answers": ["Is he a software developer?", "Is he a software developer"],
                "explanation": "En inglés, los modificadores van antes del sustantivo: 'software developer', no 'developer of software'."
            },
            {
                "question": "¿Ella es la gerente de recursos humanos?",
                "answers": ["Is she the human resources manager?", "Is she the HR manager"],
                "explanation": "Los sustantivos compuestos se forman con adjetivos + sustantivo: 'human resources manager'."
            },
            {
                "question": "¿Ellos son los dueños de la empresa?",
                "answers": ["Are they the company owners?", "Are they the owners of the company?"],
                "explanation": "Podemos usar el genitivo sajón (company's owners) o la estructura con of (owners of the company)."
            },
            {
                "question": "¿Él es una persona de confianza?",
                "answers": ["Is he a trustworthy person?", "Is he a reliable person?"],
                "explanation": "En inglés, preferimos usar un adjetivo compuesto (trustworthy) antes que una frase preposicional."
            },
            {
                "question": "¿Ella es una esperanza para la familia?",
                "answers": ["Is she a hope for the family?", "Is she hope for the family?"],
                "explanation": "Aunque 'hope' es abstracto, en este contexto contable lleva artículo: 'a hope'."
            }
        ]
        
        result = self.run_exercise(questions)
        if result:
            self.completed_levels.add(3)
    
    def practice_do_does(self):
        self.clear_screen()
        print("MÓDULO COMPLEMENTARIO: PREGUNTAS CON DO/DOES")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Tú trabajas aquí?",
                "answers": ["Do you work here?", "Do you work here"],
                "explanation": "Para verbos diferentes a 'to be', usamos 'do/does' + sujeto + verbo en infinitivo."
            },
            {
                "question": "¿Él estudia inglés?",
                "answers": ["Does he study English?", "Does he study English"],
                "explanation": "Para tercera persona singular (he/she/it), usamos 'does' y el verbo pierde la -s."
            },
            {
                "question": "¿Ellos viven en esta ciudad?",
                "answers": ["Do they live in this city?", "Do they live in this city"],
                "explanation": "Para plural (they/we/you), usamos 'do' y el verbo en infinitivo."
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_wh_questions(self):
        self.clear_screen()
        print("MÓDULO COMPLEMENTARIO: PREGUNTAS CON WH- WORDS")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Dónde trabaja ella?",
                "answers": ["Where does she work?", "Where does she work"],
                "explanation": "Las wh- questions siguen la estructura: Wh- word + do/does + sujeto + verbo."
            },
            {
                "question": "¿Qué estudian ellos?",
                "answers": ["What do they study?", "What do they study"],
                "explanation": "'What' pregunta por cosas o actividades. Estructura: What + do + sujeto + verbo."
            },
            {
                "question": "¿Quién es tu jefe?",
                "answers": ["Who is your boss?", "Who is your boss"],
                "explanation": "Cuando 'who' es el sujeto de la pregunta, no necesita auxiliar: Who + verbo + complemento."
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_like_vs_how(self):
        self.clear_screen()
        print("MÓDULO COMPLEMENTARIO: WHAT...LIKE VS HOW")
        print("=" * 50)
        
        questions = [
            {
                "question": "¿Cómo es tu hermana? (personalidad)",
                "answers": ["What is your sister like?", "What's your sister like"],
                "explanation": "Usamos 'What...like?' para preguntar por características permanentes (personalidad, apariencia general)."
            },
            {
                "question": "¿Cómo está tu hermana? (estado actual)",
                "answers": ["How is your sister?", "How's your sister"],
                "explanation": "Usamos 'How?' para preguntar por estados temporales (salud, estado de ánimo actual)."
            },
            {
                "question": "¿Cómo se ve tu hermana? (apariencia física)",
                "answers": ["What does your sister look like?", "What does your sister look like"],
                "explanation": "Usamos 'What...look like?' específicamente para apariencia física."
            }
        ]
        
        self.run_exercise(questions)
    
    def practice_dialogues(self):
        self.clear_screen()
        print("DIÁLOGOS CONTEXTUALIZADOS")
        print("=" * 50)
        print("Practica con situaciones reales de conversación.")
        print()
        
        dialogues = [
            {
                "context": "Estás en una fiesta y conoces a alguien nuevo.",
                "questions": [
                    {
                        "question": "¿Eres amigo de María?",
                        "answers": ["Are you Maria's friend?", "Are you a friend of Maria?"]
                    },
                    {
                        "question": "¿Qué haces? (¿A qué te dedicas?)",
                        "answers": ["What do you do?", "What is your job?"]
                    },
                    {
                        "question": "¿Eres de aquí?",
                        "answers": ["Are you from here?", "Are you from this city?"]
                    }
                ]
            },
            {
                "context": "Estás en tu primer día de trabajo.",
                "questions": [
                    {
                        "question": "¿Eres el nuevo gerente?",
                        "answers": ["Are you the new manager?", "Are you the new manager"]
                    },
                    {
                        "question": "¿Dónde está la sala de reuniones?",
                        "answers": ["Where is the meeting room?", "Where's the meeting room?"]
                    },
                    {
                        "question": "¿Quién es tu jefe?",
                        "answers": ["Who is your boss?", "Who's your boss?"]
                    }
                ]
            }
        ]
        
        for dialogue in dialogues:
            print(f"Contexto: {dialogue['context']}")
            print("-" * 30)
            
            for q in dialogue["questions"]:
                print(f"Pregunta: {q['question']}")
                user_answer = input("Tu respuesta: ")
                self.check_answer(user_answer, q["answers"])
                print()
            
            input("Presiona Enter para continuar al siguiente diálogo...")
            print()
    
    def show_progress(self):
        self.clear_screen()
        print("PROGRESO Y ESTADÍSTICAS")
        print("=" * 50)
        
        print("Niveles completados:")
        for i in range(1, 4):
            status = "✓" if i in self.completed_levels else "✗"
            print(f"  Nivel {i}: {status}")
        
        print(f"\nPuntuación total: {self.score}")
        
        if len(self.completed_levels) == 3:
            print("\n¡Felicidades! Has completado todos los niveles principales.")
        elif len(self.completed_levels) > 0:
            print(f"\n¡Buen trabajo! Has completado {len(self.completed_levels)} de 3 niveles.")
        else:
            print("\nAún no has completado ningún nivel. ¡Anímate a empezar!")
        
        input("\nPresiona Enter para volver al menú...")
    
    def run_exercise(self, questions):
        self.score = 0
        self.total_questions = len(questions)
        random.shuffle(questions)
        
        for i, q in enumerate(questions, 1):
            print(f"Pregunta {i}: {q['question']}")
            user_answer = input("Tu respuesta: ")
            self.check_answer(user_answer, q.get("answers", []), q.get("explanation"))
            print()
        
        print(f"Resultado: {self.score}/{self.total_questions} correctas")
        
        if self.score / self.total_questions >= 0.7:
            print("¡Excelente trabajo! Puedes avanzar al siguiente nivel.")
            input("Presiona Enter para continuar...")
            return True
        else:
            print("Necesitas practicar más este nivel.")
            retry = input("¿Quieres intentarlo de nuevo? (s/n): ").lower()
            if retry == "s":
                return self.run_exercise(questions)
            else:
                input("Presiona Enter para volver al menú...")
                return False

# Ejecutar el programa
if __name__ == "__main__":
    course = EnglishCourse()
    course.show_menu()
