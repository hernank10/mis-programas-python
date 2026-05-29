# -*- coding: utf-8 -*-
#
# Aplicación de Kivy para practicar conectores en inglés y español.
#
# Este programa presenta ejercicios de traducción bidireccional
# entre ambos idiomas, usando una interfaz gráfica amigable.

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class BilingualConnectorsApp(App):
    """
    Clase principal de la aplicación de ejercicios de conectores.
    Gestiona la lógica de la aplicación y la interfaz de usuario.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Diccionario de ejercicios del inglés al español
        self.english_to_spanish = {
            1: ("He is happy because he passed the exam.", "Él está feliz porque pasó el examen."),
            2: ("You can eat an apple or you can eat an orange.", "Puedes comer una manzana o puedes comer una naranja."),
            3: ("The man who called me is my brother.", "El hombre que me llamó es mi hermano."),
            4: ("I will call you when I get home.", "Te llamaré cuando llegue a casa."),
            5: ("Although he is rich, he is unhappy.", "Aunque es rico, es infeliz."),
            6: ("The car, which is old, works well.", "El coche, que es viejo, funciona bien."),
            7: ("He studied a lot; however, he did not pass.", "Él estudió mucho; sin embargo, no pasó."),
            8: ("I was tired; therefore, I went to sleep.", "Estaba cansado; por lo tanto, fui a dormir."),
            9: ("Both my mother and my father work here.", "Ambos mi madre y mi padre trabajan aquí."),
            10: ("We stayed home since it was raining.", "Nos quedamos en casa ya que estaba lloviendo.")
        }
        
        # Diccionario de ejercicios del español al inglés
        self.spanish_to_english = {
            1: ("Me gusta el café, pero a ella le gusta el té.", "I like coffee, but she likes tea."),
            2: ("Si estudias, pasarás el examen.", "If you study, you will pass the exam."),
            3: ("El libro, que es azul, es nuevo.", "The book, which is blue, is new."),
            4: ("La casa que compramos es grande.", "The house that we bought is big."),
            5: ("Ni mi hermano ni mi hermana están aquí.", "Neither my brother nor my sister is here."),
            6: ("Estudio para que pueda pasar.", "I study so that I can pass."),
            7: ("La persona a quien le hablé es mi jefa.", "The person to whom I spoke is my boss."),
            8: ("Se comporta como si fuera el jefe.", "He acts as if he is the boss."),
            9: ("El perro que vive en la casa de al lado es ruidoso.", "The dog that lives next door is loud."),
            10: ("Puedes sentarte donde quieras.", "You can sit wherever you want.")
        }
        
        # Estado de la aplicación
        self.language_mode = 'es_to_en' # 'es_to_en' para español a inglés, 'en_to_es' para inglés a español
        self.current_exercise = None
        self.correct_answer = ""
        self.exercise_number = 0

    def build(self):
        """
        Método para construir la interfaz de usuario de la aplicación.
        """
        # Configuración inicial de la ventana
        Window.clearcolor = (0.96, 0.94, 0.88, 1)  # Color arena claro
        
        # Layout principal de la aplicación
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Botón para cambiar el idioma
        self.lang_button = Button(text="Cambiar a Inglés → Español", 
                                  size_hint_y=0.1, font_size='18sp',
                                  background_color=(0.4, 0.29, 0.17, 1),
                                  color=(1, 1, 1, 1))
        self.lang_button.bind(on_press=self.toggle_language)
        
        # Título de la aplicación
        self.title_label = Label(text="Reto de Conectores",
                                 font_size='24sp', bold=True, color=(0.2, 0.2, 0.2, 1),
                                 size_hint_y=0.2)
        
        # Etiqueta para el número y tipo de ejercicio
        self.exercise_label = Label(text="", font_size='18sp', color=(0.4, 0.4, 0.4, 1),
                                    size_hint_y=0.1)
        
        # Etiqueta para la pregunta del ejercicio
        self.question_label = Label(text="", font_size='16sp', color=(0.3, 0.3, 0.3, 1),
                                    size_hint_y=0.2)
                                    
        # Campo de texto para la respuesta del usuario
        self.answer_input = TextInput(multiline=False, font_size='16sp', size_hint_y=0.1)
        
        # Botón para comprobar la respuesta
        check_button = Button(text="Comprobar", background_color=(0.27, 0.52, 0.43, 1), 
                              color=(1, 1, 1, 1), size_hint_y=0.1, font_size='18sp')
        check_button.bind(on_press=self.check_answer)
        
        # Etiqueta para mostrar la retroalimentación
        self.feedback_label = Label(text="", font_size='18sp', bold=True, size_hint_y=0.1)
        
        # Botón para pasar al siguiente ejercicio
        next_button = Button(text="Siguiente Ejecicio", background_color=(0.4, 0.29, 0.17, 1),
                             color=(1, 1, 1, 1), size_hint_y=0.1, font_size='18sp')
        next_button.bind(on_press=self.next_exercise)
        
        # Añadir todos los widgets al layout principal
        main_layout.add_widget(self.lang_button)
        main_layout.add_widget(self.title_label)
        main_layout.add_widget(self.exercise_label)
        main_layout.add_widget(self.question_label)
        main_layout.add_widget(self.answer_input)
        main_layout.add_widget(check_button)
        main_layout.add_widget(self.feedback_label)
        main_layout.add_widget(next_button)

        self.next_exercise()
        return main_layout

    def toggle_language(self, instance):
        """
        Cambia el modo de idioma de la aplicación.
        """
        if self.language_mode == 'es_to_en':
            self.language_mode = 'en_to_es'
            self.lang_button.text = "Switch to Spanish → English"
            self.title_label.text = "Connectors Challenge"
            self.exercise_label.text = "English → Spanish"
            instance.parent.children[2].text = "Check" # Boton comprobar
            instance.parent.children[0].text = "Next Exercise" # Boton Siguiente
        else:
            self.language_mode = 'es_to_en'
            self.lang_button.text = "Cambiar a Inglés → Español"
            self.title_label.text = "Reto de Conectores"
            self.exercise_label.text = "Español → Inglés"
            instance.parent.children[2].text = "Comprobar"
            instance.parent.children[0].text = "Siguiente Ejercicio"
            
        self.next_exercise()

    def next_exercise(self, instance=None):
        """
        Selecciona y muestra un nuevo ejercicio.
        """
        self.answer_input.text = ""
        self.feedback_label.text = ""
        self.feedback_label.color = (0.3, 0.3, 0.3, 1)

        if self.language_mode == 'es_to_en':
            self.exercise_label.text = "Español → Inglés"
            self.exercise_number = random.choice(list(self.spanish_to_english.keys()))
            question, answer = self.spanish_to_english[self.exercise_number]
            self.question_label.text = question
            self.correct_answer = answer
        else:
            self.exercise_label.text = "English → Spanish"
            self.exercise_number = random.choice(list(self.english_to_spanish.keys()))
            question, answer = self.english_to_spanish[self.exercise_number]
            self.question_label.text = question
            self.correct_answer = answer

    def check_answer(self, instance):
        """
        Verifica la respuesta del usuario y muestra la retroalimentación.
        """
        user_response = self.answer_input.text.strip().lower()
        correct_response = self.correct_answer.strip().lower()

        if user_response == correct_response:
            if self.language_mode == 'es_to_en':
                self.feedback_label.text = "¡Correcto! ¡Excelente trabajo!"
            else:
                self.feedback_label.text = "Correct! Excellent work!"
            self.feedback_label.color = (0.27, 0.52, 0.43, 1)  # Verde hoja
        else:
            if self.language_mode == 'es_to_en':
                self.feedback_label.text = f"Incorrecto. La respuesta era: '{self.correct_answer}'"
            else:
                self.feedback_label.text = f"Incorrect. The correct answer was: '{self.correct_answer}'"
            self.feedback_label.color = (0.7, 0.1, 0.1, 1)  # Rojo ladrillo

if __name__ == "__main__":
    BilingualConnectorsApp().run()
