import random
import os # Para limpiar la consola

# --- Datos de la Lección ---

# Enum-like structure for QuestionType
class QuestionType:
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_THE_BLANK = "fill_in_the_blank"
    TRANSFORMATION = "transformation"
    RULE_EXAMPLE = "rule_example"

lesson10_questions = [
    {
        "id": "L10Q1",
        "text": "___ si lo entiendes. (expresión para pedir que alguien compruebe)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "A ver",
        "feedback_explanation": "'A ver' (preposición 'a' + verbo 'ver') se usa para pedir que se vea o se compruebe algo, o como exclamación de expectación."
    },
    {
        "id": "L10Q2",
        "text": "Va a ___ mucha gente en la fiesta. (verbo auxiliar de existencia)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "'Haber' (verbo) se usa para indicar existencia (hay, había, habrá) o como auxiliar en tiempos compuestos (ha hecho, hemos comido)."
    },
    {
        "id": "L10Q3",
        "text": "Elije: [A ver/Haber] si llegamos a tiempo. (Escribe la opción correcta)",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A ver", "Haber"],
        "correct_answer": "A ver",
        "feedback_explanation": "'A ver' se usa para expresar expectación o para comprobar algo."
    },
    {
        "id": "L10Q4",
        "text": "Debe ___ estudiado más. (verbo auxiliar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "En este caso, 'haber' funciona como un verbo auxiliar en una perífrasis verbal ('deber de haber + participio')."
    },
    {
        "id": "L10Q5",
        "text": "Vamos a ___ la película que te dije.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "ver",
        "feedback_explanation": "Aunque la frase usa 'a', la palabra que falta es el verbo 'ver'. La confusión es común con 'a ver'."
    }
]

# Mapeo de la única lección que vamos a usar en este ejemplo
all_lessons = {
    10: {"title": "Uso de \"A ver\" vs. \"Haber\" 🧐", "questions": lesson10_questions}
}

# --- Lógica del Programa (LessonManager) ---
class LessonManager:
    def __init__(self):
        self.current_lesson_num = None
        self.current_lesson = None
        self.shuffled_questions = []
        self.current_question_index = 0
        self.score = 0
        self.total_possible_score = 0
        self.user_answer = ""

    def start_lesson(self, lesson_number):
        if lesson_number in all_lessons:
            self.current_lesson_num = lesson_number
            self.current_lesson = all_lessons[lesson_number]
            self.shuffled_questions = random.sample(self.current_lesson["questions"], len(self.current_lesson["questions"]))
            self.current_question_index = 0
            self.score = 0
            self.total_possible_score = len(self.shuffled_questions) * 10
            self.user_answer = ""
            self.clear_console()
            print(f"\n--- Lección '{self.current_lesson['title']}' Iniciada ---\n")
            return True
        print(f"Error: La lección {lesson_number} no existe.")
        return False

    def get_current_question(self):
        if self.shuffled_questions and self.current_question_index < len(self.shuffled_questions):
            return self.shuffled_questions[self.current_question_index]
        return None

    def check_answer(self, user_input):
        question = self.get_current_question()
        if not question:
            return False, "Error: No hay pregunta cargada."

        self.user_answer = user_input.strip()

        is_correct = False
        user_input_normalized = self.user_answer.lower()
        correct_answer_normalized = question["correct_answer"].lower()

        is_correct = (user_input_normalized == correct_answer_normalized)

        if is_correct:
            self.score += 10
            print(f"\n¡Correcto! ✅")
        else:
            print(f"\nIncorrecto. ❌")
            print(f"   La respuesta correcta es: '{question['correct_answer']}'")
        print(f"   Explicación: {question['feedback_explanation']}")
        print(f"   Puntuación actual: {self.score}\n")

        return is_correct, question["feedback_explanation"]

    def move_to_next_question(self):
        self.current_question_index += 1
        self.user_answer = ""
        return self.current_question_index < len(self.shuffled_questions)

    def get_lesson_title(self):
        return self.current_lesson["title"] if self.current_lesson else "Lección Desconocida"

    def get_current_question_number(self):
        return self.current_question_index + 1

    def get_total_questions(self):
        return len(self.shuffled_questions)

    def clear_console(self):
        # Para Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # Para macOS y Linux
        else:
            _ = os.system('clear')

# --- Función Principal para la Interacción en Consola ---

def run_console_app():
    lesson_manager = LessonManager()
    
    print("--- Bienvenido a la Aplicación de Lecciones de Castellano (Consola) ---")
    print("Vamos a iniciar la lección: Uso de 'A ver' vs. 'Haber'")
    input("Presiona Enter para comenzar...")

    lesson_manager.start_lesson(10) # Inicia la lección 10

    while True:
        current_question = lesson_manager.get_current_question()
        if not current_question:
            # Todas las preguntas han sido respondidas
            break 
        
        lesson_manager.clear_console()
        print(f"--- Lección: {lesson_manager.get_lesson_title()} ---")
        print(f"Pregunta {lesson_manager.get_current_question_number()} de {lesson_manager.get_total_questions()}")
        print(f"\n{current_question['text']}\n")

        user_input = input("Tu respuesta: ").strip()

        if not user_input:
            print("No has ingresado nada. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...")
            continue # Vuelve a mostrar la misma pregunta

        lesson_manager.check_answer(user_input)
        
        if lesson_manager.get_current_question_number() < lesson_manager.get_total_questions():
            input("Presiona Enter para la siguiente pregunta...")
        else:
            input("Has terminado las preguntas. Presiona Enter para ver tus resultados finales...")
        
    # Mostrar resultados finales
    lesson_manager.clear_console()
    final_score = lesson_manager.score
    total_possible = lesson_manager.total_possible_score
    percentage = (final_score / total_possible) * 100 if total_possible > 0 else 0

    print(f"\n--- Resultados Finales de la Lección '{lesson_manager.get_lesson_title()}' ---")
    print(f"Tu puntuación final: {final_score} de {total_possible} puntos.")
    print(f"Porcentaje: {percentage:.0f}%")

    if percentage == 100:
        print("\n¡Felicidades! ¡Has dominado esta lección a la perfección! ⭐⭐⭐")
    elif percentage >= 70:
        print("\n¡Muy bien! Estás dominando las reglas. ¡Sigue así! 👍")
    else:
        print("\n¡Buen intento! Repasa las reglas y vuelve a intentarlo. ¡La práctica te hará un experto! 💪")
    
    print("\n--- Lección Finalizada ---")
    input("Presiona Enter para salir.")


# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    run_console_app()
