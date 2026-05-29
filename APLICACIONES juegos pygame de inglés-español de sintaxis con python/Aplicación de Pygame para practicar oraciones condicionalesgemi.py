# -*- coding: utf-8 -*-
#
# Aplicación de Pygame para practicar oraciones condicionales.
#
# Este programa presenta ejercicios de traducción bidireccional
# entre ambos idiomas, usando una interfaz gráfica dinámica.

import pygame
import random

class ConditionalSentencesGame:
    """
    Clase principal del juego de oraciones condicionales.
    Gestiona la lógica del juego y el bucle principal de Pygame.
    """
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        pygame.display.set_caption("Juego de Oraciones Condicionales")

        # Configuración de la ventana
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Colores de la paleta
        self.color_bg = (255, 255, 255)         # Blanco
        self.color_button_en = (66, 133, 244)   # Azul de Google
        self.color_button_es = (219, 68, 55)    # Rojo de Google
        self.color_correct = (52, 168, 83)      # Verde de Google
        self.color_incorrect = (251, 188, 5)    # Amarillo de Google
        self.color_text_dark = (50, 50, 50)     # Gris oscuro
        self.color_input_bg = (240, 240, 240)   # Gris claro para el input

        # Fuentes
        self.font_title = pygame.font.Font(None, 48)
        self.font_label = pygame.font.Font(None, 32)
        self.font_question = pygame.font.Font(None, 24)
        self.font_input = pygame.font.Font(None, 24)

        # Diccionario de ejercicios bilingües de oraciones condicionales
        # Formato: (tipo, oración incompleta, respuesta correcta)
        self.english_conditionals = {
            1: ("If it rains, we ____ (not go) to the park.", "will not go"),
            2: ("If I were rich, I ____ (travel) the world.", "would travel"),
            3: ("If you had studied, you ____ (pass) the test.", "would have passed"),
            4: ("If she arrives late, she ____ (miss) the beginning.", "will miss"),
            5: ("I would have gone if you ____ (call) me.", "had called"),
            6: ("They would buy a new car if they ____ (have) more money.", "had"),
            7: ("If the sun shines, we ____ (play) outside.", "will play"),
            8: ("If he had known, he ____ (tell) us.", "would have told"),
        }
        self.spanish_conditionals = {
            1: ("Si hace sol, ____ (ir) a la playa.", "iremos"),
            2: ("Si yo fuera tú, ____ (decirle) la verdad.", "le diría"),
            3: ("Si hubieras llegado antes, ____ (ver) la película.", "habrías visto"),
            4: ("Si estudias, ____ (aprobar) el examen.", "aprobarás"),
            5: ("Si yo tuviera dinero, ____ (comprar) una casa.", "compraría"),
            6: ("Si hubiera sabido la respuesta, ____ (responder) la pregunta.", "habría respondido"),
            7: ("Si me ayudas, te ____ (dar) un regalo.", "daré"),
            8: ("Si él fuera más rápido, ____ (ganar) la carrera.", "ganaría"),
        }
        
        # Estado del juego
        self.running = True
        self.language_mode = 'en'  # 'en' para inglés, 'es' para español
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = self.color_text_dark
        self.current_question = ""
        self.correct_answer = ""
        self.current_language_button = self.color_button_es
        self.current_check_button = self.color_button_en
        self.current_next_button = self.color_button_en

        # Rectángulos de los elementos de la UI
        self.lang_button_rect = pygame.Rect(50, 50, 250, 50)
        self.input_rect = pygame.Rect(100, 350, 600, 50)
        self.check_button_rect = pygame.Rect(100, 420, 280, 50)
        self.next_button_rect = pygame.Rect(420, 420, 280, 50)

        self.next_exercise()

    def run(self):
        """
        Bucle principal del juego. Maneja eventos y dibuja la interfaz.
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
        title_text = "Juego de Oraciones Condicionales" if self.language_mode == 'es' else "Conditional Sentences Game"
        self.draw_text(title_text, self.font_title, self.color_text_dark, self.screen_width // 2, 100)

        # Etiqueta de ejercicio
        exercise_label_text = "Español → Inglés" if self.language_mode == 'en' else "Inglés → Español"
        self.draw_text(exercise_label_text, self.font_label, self.color_text_dark, self.screen_width // 2, 180)

        # Pregunta
        self.draw_text(self.current_question, self.font_question, self.color_text_dark, self.screen_width // 2, 250)

        # Botón de idioma
        lang_button_text = "Cambiar a Español 🇪🇸" if self.language_mode == 'en' else "Switch to English 🇺🇸"
        self.draw_button(self.lang_button_rect, lang_button_text, self.current_language_button)

        # Caja de texto (input)
        pygame.draw.rect(self.screen, self.color_input_bg, self.input_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.color_text_dark, self.input_rect, 2, border_radius=10)
        input_surface = self.font_input.render(self.user_input, True, self.color_text_dark)
        self.screen.blit(input_surface, (self.input_rect.x + 10, self.input_rect.y + 15))

        # Botón de Comprobar
        check_text = "Comprobar ✅" if self.language_mode == 'es' else "Check ✅"
        self.draw_button(self.check_button_rect, check_text, self.current_check_button)

        # Botón de Siguiente
        next_text = "Siguiente ➡️" if self.language_mode == 'es' else "Next ➡️"
        self.draw_button(self.next_button_rect, next_text, self.current_next_button)

        # Retroalimentación
        self.draw_text(self.feedback, self.font_label, self.feedback_color, self.screen_width // 2, 500)

    def draw_button(self, rect, text, color):
        """
        Dibuja un botón con texto centrado.
        """
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
        self.language_mode = 'es' if self.language_mode == 'en' else 'en'
        self.next_exercise()

    def next_exercise(self):
        """
        Selecciona y muestra un nuevo ejercicio.
        """
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = self.color_text_dark

        if self.language_mode == 'en':
            question, answer = random.choice(list(self.english_conditionals.values()))
            self.current_question = question
            self.correct_answer = answer
        else:
            question, answer = random.choice(list(self.spanish_conditionals.values()))
            self.current_question = question
            self.correct_answer = answer

    def check_answer(self):
        """
        Verifica la respuesta del usuario y muestra la retroalimentación.
        """
        user_response = self.user_input.strip().lower()
        correct_response = self.correct_answer.strip().lower()

        if user_response == correct_response:
            self.feedback = "¡Correcto! ✨"
            self.feedback_color = self.color_correct
        else:
            self.feedback = f"Incorrecto. La respuesta era: '{self.correct_answer}' 😔"
            self.feedback_color = self.color_incorrect

if __name__ == "__main__":
    app = ConditionalSentencesGame()
    app.run()
