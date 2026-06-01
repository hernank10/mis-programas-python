import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
import random

# Establecer la versión mínima de Kivy
kivy.require('2.0.0')

# --- Datos de la Lección (Solo la Lección 10 para simplificar) ---

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
        "text": "Elije: [A ver/Haber] si llegamos a tiempo.",
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
        "correct_answer": "ver", # Aquí el "a" ya está implícito en la frase
        "feedback_explanation": "Aunque la frase usa 'a', la palabra que falta es el verbo 'ver'. La confusión es común con 'a ver'."
    }
    # Solo 5 preguntas para mantener el ejemplo conciso
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
            # Usamos list(questions) para copiar y luego barajar, si no queremos modificar el original
            self.shuffled_questions = random.sample(self.current_lesson["questions"], len(self.current_lesson["questions"]))
            self.current_question_index = 0
            self.score = 0
            self.total_possible_score = len(self.shuffled_questions) * 10
            self.user_answer = ""
            print(f"\n--- Lección '{self.current_lesson['title']}' Iniciada ---")
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
        # Normalizar para comparación (quitar corchetes, dividir opciones si es MULTIPLE_CHOICE en texto)
        question_text_normalized = question["text"].lower()
        user_input_normalized = self.user_answer.lower()

        if question["type"] == QuestionType.MULTIPLE_CHOICE:
            # Para MULTIPLE_CHOICE en este formato simplificado, la respuesta del usuario debe coincidir con una de las opciones correctas
            # Si el texto de la pregunta tiene [Opcion1/Opcion2], el usuario debe escribir la opción correcta.
            is_correct = (user_input_normalized == question["correct_answer"].lower())
            if not is_correct and user_input_normalized in [o.lower() for o in question["options"]]:
                # El usuario eligió una opción pero no la correcta.
                pass # El feedback_explanation ya manejará esto
        elif question["type"] == QuestionType.FILL_IN_THE_BLANK or \
             question["type"] == QuestionType.TRANSFORMATION:
            is_correct = (user_input_normalized == question["correct_answer"].lower())
        elif question["type"] == QuestionType.RULE_EXAMPLE:
            if "example_check_func" in question and callable(question["example_check_func"]):
                is_correct = question["example_check_func"](self.user_answer)
            else:
                is_correct = (user_input_normalized == question["correct_answer"].lower())

        if is_correct:
            self.score += 10
            print(f"¡Correcto! ✅ Puntuación: {self.score}")
        else:
            print(f"Incorrecto. ❌ La respuesta correcta es: '{question['correct_answer']}'")
            print(f"   Explicación: {question['feedback_explanation']}")

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

# --- Kivy UI y Lógica de Interacción ---

class SimpleLessonApp(App):
    # Propiedades para actualizar la UI desde Python
    current_question_text = StringProperty("Presiona 'Iniciar Lección' para comenzar.")
    question_number_display = StringProperty("")
    status_message = StringProperty("Esperando...")

    lesson_manager = ObjectProperty(LessonManager()) # Instancia del gestor de lecciones

    def build(self):
        self.title = 'Kivy Consola: Lección de Castellano'

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título de la Aplicación
        main_layout.add_widget(Label(text="Kivy Consola: Lección de \"A ver\" vs. \"Haber\"",
                                     font_size='26sp', size_hint_y=0.15))

        # Indicador de Pregunta
        self.question_number_label = Label(text=self.question_number_display,
                                           font_size='18sp', size_hint_y=0.05)
        main_layout.add_widget(self.question_number_label)

        # Texto de la Pregunta
        self.question_label = Label(text=self.current_question_text,
                                    font_size='22sp', halign='center', valign='middle',
                                    text_size=(self.root.width - 40, None) if self.root else (Window.width - 40, None),
                                    size_hint_y=0.3)
        main_layout.add_widget(self.question_label)

        # Campo de Entrada para la Respuesta
        self.answer_input = TextInput(hint_text="Escribe tu respuesta aquí...",
                                      multiline=False, size_hint_y=0.1)
        # Enlazar la validación del texto (cuando se presiona Enter)
        self.answer_input.bind(on_text_validate=self.submit_answer)
        main_layout.add_widget(self.answer_input)

        # Botones de Acción
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.submit_button = Button(text="Comprobar", background_color=(0.2, 0.6, 0.2, 1))
        self.submit_button.bind(on_release=self.submit_answer)
        button_layout.add_widget(self.submit_button)

        self.next_button = Button(text="Siguiente >>", background_color=(0.2, 0.2, 0.8, 1), disabled=True)
        self.next_button.bind(on_release=self.go_to_next_question)
        button_layout.add_widget(self.next_button)
        main_layout.add_widget(button_layout)

        # Etiqueta de Estado/Mensajes
        self.status_label = Label(text=self.status_message,
                                  font_size='16sp', size_hint_y=0.1)
        main_layout.add_widget(self.status_label)

        # Botón para iniciar la lección
        self.start_lesson_button = Button(text="Iniciar Lección \"A ver\" vs. \"Haber\"",
                                          size_hint_y=0.1, background_color=(0.8, 0.5, 0.2, 1))
        self.start_lesson_button.bind(on_release=lambda x: self.start_lesson(10))
        main_layout.add_widget(self.start_lesson_button)

        # Botón para salir
        exit_button = Button(text="Salir", size_hint_y=0.1, background_color=(0.8, 0.2, 0.2, 1))
        exit_button.bind(on_release=self.stop)
        main_layout.add_widget(exit_button)
        
        # Enlazar propiedades para que los Labels se actualicen
        self.bind(current_question_text=self.question_label.setter('text'),
                  question_number_display=self.question_number_label.setter('text'),
                  status_message=self.status_label.setter('text'))

        print("--- Aplicación Kivy de Lección de Castellano Iniciada ---")
        return main_layout

    def start_lesson(self, lesson_num):
        if self.lesson_manager.start_lesson(lesson_num):
            self.start_lesson_button.disabled = True
            self.start_lesson_button.opacity = 0 # Ocultar botón de inicio
            self.update_question_display()
            self.answer_input.focus = True # Poner el foco en el campo de entrada
            self.next_button.disabled = True # Desactivar 'Siguiente' al inicio
            self.submit_button.disabled = False # Activar 'Comprobar'
            self.status_message = "Responde la pregunta."
        else:
            self.status_message = "No se pudo iniciar la lección."

    def update_question_display(self):
        question = self.lesson_manager.get_current_question()
        if question:
            self.current_question_text = f"[{self.lesson_manager.get_current_question_number()}/{self.lesson_manager.get_total_questions()}] " + question["text"]
            self.question_number_display = f"Pregunta {self.lesson_manager.get_current_question_number()} de {self.lesson_manager.get_total_questions()}"
            self.answer_input.text = "" # Limpiar el campo de entrada
            self.next_button.disabled = True # Desactivar hasta comprobar
            self.submit_button.disabled = False # Activar Comprobar
            self.status_message = "Ingresa tu respuesta."
            self.answer_input.focus = True
            print(f"\n--- Pregunta {self.lesson_manager.get_current_question_number()} ---")
            print(self.current_question_text)
        else:
            self.show_results()

    def submit_answer(self, instance):
        user_input = self.answer_input.text
        if not user_input.strip():
            self.status_message = "¡Por favor, ingresa una respuesta!"
            print("AVISO: El campo de respuesta está vacío.")
            return

        is_correct, feedback_exp = self.lesson_manager.check_answer(user_input)

        if is_correct:
            self.status_message = "¡Correcto! ✅"
            print("Resultado: Correcto!")
        else:
            self.status_message = "Incorrecto. ❌"
            print("Resultado: Incorrecto.")
            
        print(f"   Tu respuesta: '{user_input}'")
        print(f"   Explicación: {feedback_exp}")
        print(f"   Puntuación actual: {self.lesson_manager.score}")

        self.submit_button.disabled = True # Desactivar Comprobar
        self.next_button.disabled = False # Activar Siguiente

    def go_to_next_question(self, instance):
        if self.lesson_manager.move_to_next_question():
            self.update_question_display()
        else:
            self.show_results()

    def show_results(self):
        final_score = self.lesson_manager.score
        total_possible = self.lesson_manager.total_possible_score
        percentage = (final_score / total_possible) * 100 if total_possible > 0 else 0

        result_message = f"--- Lección Terminada ---"
        result_message += f"\nTu puntuación final: {final_score} / {total_possible}"
        result_message += f"\nPorcentaje: {percentage:.0f}%"

        ui_message = f"Lección terminada!\nPuntuación: {final_score}/{total_possible}\nPorcentaje: {percentage:.0f}%"
        
        if percentage == 100:
            result_message += "\n¡Felicidades! ¡Has dominado esta lección! ⭐⭐⭐"
            ui_message += "\n¡Felicidades!"
        elif percentage >= 70:
            result_message += "\n¡Muy bien! Estás dominando las reglas. 👍"
            ui_message += "\n¡Muy bien!"
        else:
            result_message += "\n¡Buen intento! Repasa y vuelve a intentarlo. 💪"
            ui_message += "\n¡Buen intento!"

        print(result_message)
        self.current_question_text = "Lección Completada."
        self.question_number_display = ""
        self.status_message = ui_message
        
        self.submit_button.disabled = True
        self.next_button.disabled = True
        self.answer_input.disabled = True # Desactivar input al finalizar
        self.start_lesson_button.text = "Volver a Inicio / Otra Lección"
        self.start_lesson_button.opacity = 1
        self.start_lesson_button.disabled = False


    def on_stop(self):
        print("--- Aplicación Kivy Detenida ---")

if __name__ == '__main__':
    SimpleLessonApp().run()
