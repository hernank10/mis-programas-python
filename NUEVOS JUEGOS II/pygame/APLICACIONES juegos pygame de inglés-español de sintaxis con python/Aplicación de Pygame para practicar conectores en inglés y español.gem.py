# -*- coding: utf-8 -*-
#
# Aplicación de Pygame para practicar conectores en inglés y español.
#
# Este programa presenta ejercicios de traducción bidireccional
# entre ambos idiomas, usando una interfaz gráfica dibujada manualmente.

import pygame
import random

class BilingualConnectorsApp:
    """
    Clase principal de la aplicación de ejercicios de conectores.
    Gestiona la lógica de la aplicación y el bucle principal de Pygame.
    """
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        pygame.display.set_caption("Reto de Conectores")

        # Configuración de la ventana
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Colores de la paleta inspirada en la naturaleza
        self.color_bg = (245, 239, 225)       # Arena claro
        self.color_button = (102, 74, 43)    # Marrón oscuro
        self.color_button_hover = (122, 94, 63) # Marrón oscuro al pasar el mouse
        self.color_correct = (68, 132, 110)   # Verde hoja
        self.color_incorrect = (178, 25, 25)  # Rojo ladrillo
        self.color_text_dark = (50, 50, 50)    # Gris oscuro
        self.color_input_border = (150, 150, 150) # Gris para el borde del input

        # Fuentes
        self.font_title = pygame.font.Font(None, 48)
        self.font_label = pygame.font.Font(None, 32)
        self.font_question = pygame.font.Font(None, 24)
        self.font_input = pygame.font.Font(None, 24)

        # Diccionario de ejercicios
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
        self.running = True
        self.language_mode = 'es_to_en'
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = self.color_text_dark
        self.current_question = ""
        self.correct_answer = ""

        # Rectángulos de los elementos de la UI
        self.lang_button_rect = pygame.Rect(50, 50, 250, 50)
        self.input_rect = pygame.Rect(100, 350, 600, 50)
        self.check_button_rect = pygame.Rect(100, 420, 280, 50)
        self.next_button_rect = pygame.Rect(420, 420, 280, 50)

        self.next_exercise()

    def run(self):
        """
        Bucle principal del programa. Maneja eventos y dibuja la interfaz.
        """
        while self.running:
            self.handle_events()
            self.draw_elements()
            pygame.display.flip()

    def handle_events(self):
        """
        Maneja los eventos del usuario, como clics del mouse y pulsaciones de teclado.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.lang_button_rect.collidepoint(event.pos):
                    self.toggle_language()
                elif self.check_button_rect.collidepoint(event.pos):
                    self.check_answer()
                elif self.next_button_rect.collidepoint(event.pos):
                    self.next_exercise()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    self.check_answer()
                else:
                    self.user_input += event.unicode

    def draw_elements(self):
        """
        Dibuja todos los elementos de la interfaz en la pantalla.
        """
        self.screen.fill(self.color_bg)

        # Título
        title_text = "Reto de Conectores" if self.language_mode == 'es_to_en' else "Connectors Challenge"
        self.draw_text(title_text, self.font_title, self.color_text_dark, self.screen_width // 2, 100)

        # Etiqueta de ejercicio
        exercise_label_text = "Español → Inglés" if self.language_mode == 'es_to_en' else "English → Spanish"
        self.draw_text(exercise_label_text, self.font_label, self.color_text_dark, self.screen_width // 2, 180)

        # Pregunta
        self.draw_text(self.current_question, self.font_question, self.color_text_dark, self.screen_width // 2, 250)

        # Botón de idioma
        self.draw_button(self.lang_button_rect, "Cambiar a Inglés → Español" if self.language_mode == 'es_to_en' else "Switch to Spanish → English")

        # Caja de texto (input)
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.color_input_border, self.input_rect, 2, border_radius=10)
        input_surface = self.font_input.render(self.user_input, True, self.color_text_dark)
        self.screen.blit(input_surface, (self.input_rect.x + 10, self.input_rect.y + 15))

        # Botón de Comprobar
        check_text = "Comprobar" if self.language_mode == 'es_to_en' else "Check"
        self.draw_button(self.check_button_rect, check_text)

        # Botón de Siguiente
        next_text = "Siguiente Ejercicio" if self.language_mode == 'es_to_en' else "Next Exercise"
        self.draw_button(self.next_button_rect, next_text)

        # Retroalimentación
        self.draw_text(self.feedback, self.font_label, self.feedback_color, self.screen_width // 2, 500)

    def draw_button(self, rect, text):
        """
        Dibuja un botón con texto centrado.
        """
        # Cambia el color si el mouse está sobre el botón
        mouse_pos = pygame.mouse.get_pos()
        color = self.color_button_hover if rect.collidepoint(mouse_pos) else self.color_button
        
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        button_text_surface = self.font_label.render(text, True, (255, 255, 255))
        text_rect = button_text_surface.get_rect(center=rect.center)
        self.screen.blit(button_text_surface, text_rect)

    def draw_text(self, text, font, color, x, y):
        """
        Dibuja un texto centrado en las coordenadas dadas.
        """
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def toggle_language(self):
        """
        Cambia el modo de idioma y reinicia el ejercicio.
        """
        self.language_mode = 'en_to_es' if self.language_mode == 'es_to_en' else 'es_to_en'
        self.next_exercise()

    def next_exercise(self):
        """
        Selecciona y muestra un nuevo ejercicio.
        """
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = self.color_text_dark

        if self.language_mode == 'es_to_en':
            question, answer = random.choice(list(self.spanish_to_english.values()))
            self.current_question = question
            self.correct_answer = answer
        else:
            question, answer = random.choice(list(self.english_to_spanish.values()))
            self.current_question = question
            self.correct_answer = answer

    def check_answer(self):
        """
        Verifica la respuesta del usuario y muestra la retroalimentación.
        """
        user_response = self.user_input.strip().lower()
        correct_response = self.correct_answer.strip().lower()

        if user_response == correct_response:
            self.feedback = "¡Correcto! ¡Excelente trabajo!" if self.language_mode == 'es_to_en' else "Correct! Excellent work!"
            self.feedback_color = self.color_correct
        else:
            self.feedback = f"Incorrecto. La respuesta era: '{self.correct_answer}'" if self.language_mode == 'es_to_en' else f"Incorrect. The correct answer was: '{self.correct_answer}'"
            self.feedback_color = self.color_incorrect

if __name__ == "__main__":
    app = BilingualConnectorsApp()
    app.run()
