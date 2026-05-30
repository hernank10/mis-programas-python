# -*- coding: utf-8 -*-
#
# Juego de Pygame para practicar sintaxis para escritores y periodistas.
#
# El juego presenta una interfaz inmersiva con botones animados,
# un sistema de partículas de emoticones y efectos de glassmorphism.

import pygame
import random
import math

# Constantes de colores
COLOR_BG = (20, 20, 30)  # Azul oscuro
COLOR_GLASS = (255, 255, 255, 60)  # Blanco transparente para glassmorphism
COLOR_TEXT_LIGHT = (240, 240, 240)  # Gris claro
COLOR_CORRECT = (52, 168, 83)
COLOR_INCORRECT = (251, 188, 5)

# Emoticones para el sistema de partículas
PARTICLE_EMOJIS = ["✍️", "📝", "💡", "✒️", "✨", "🌟", "📚"]
FEEDBACK_EMOJIS = {"correct": "✅", "incorrect": "❌", "change": "🔄"}

# Clase para representar una partícula de emoticones
class Particle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(0.5, 1.5)
        self.rotation = 0
        self.rotation_speed = random.uniform(-5, 5)
        self.emoji = emoji
        self.life = 255

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.rotation_speed
        self.life -= 2

    def draw(self, screen, font):
        if self.life > 0:
            emoji_surface = font.render(self.emoji, True, (255, 255, 255, self.life))
            
            # Rotar la partícula
            rotated_surface = pygame.transform.rotate(emoji_surface, self.rotation)
            rect = rotated_surface.get_rect(center=(self.x, self.y))
            screen.blit(rotated_surface, rect)

# Clase principal del juego
class SyntaxGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Juego de Sintaxis para Escritores ✍️")
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        # Fuentes y relojes
        self.font_title = pygame.font.Font(None, 48)
        self.font_label = pygame.font.Font(None, 32)
        self.font_question = pygame.font.Font(None, 24)
        self.font_input = pygame.font.Font(None, 24)
        self.font_emoji = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()
        self.running = True

        # Datos de las oraciones subordinadas
        self.data_es = [
            {"topic": "Concisión Periodística", "question": "Corrige la siguiente frase para un titular: 'El equipo de baloncesto, que es muy conocido en la ciudad, ganó el campeonato.'", "correct": "El conocido equipo de baloncesto ganó el campeonato."},
            {"topic": "Voz Activa", "question": "Reescribe la siguiente frase a voz activa: 'El libro fue escrito por el autor.'", "correct": "El autor escribió el libro."},
            {"topic": "Puntuación de Diálogo", "question": "Corrige la puntuación del siguiente diálogo: 'dijo la niña no quiero jugar más'", "correct": "—No quiero jugar más —dijo la niña."},
            {"topic": "Adjetivación Literaria", "question": "Mejora la siguiente frase con un adjetivo: 'La casa se veía vieja.'", "correct": "La casa se veía decrépita."},
            {"topic": "Cláusulas para Reportajes", "question": "Reduce la siguiente frase compleja: 'El reporte, que fue divulgado a pesar de la controversia, detalla las conclusiones de la investigación.'", "correct": "El reporte divulgado detalla las conclusiones de la investigación."},
        ]
        self.data_en = [
            {"topic": "Journalistic Conciseness", "question": "Fix the following headline for conciseness: 'The basketball team, which is very well known in the city, won the championship.'", "correct": "The well-known basketball team won the championship."},
            {"topic": "Active Voice", "question": "Rewrite the following sentence in active voice: 'The book was written by the author.'", "correct": "The author wrote the book."},
            {"topic": "Dialogue Punctuation", "question": "Correct the punctuation of the following dialogue: 'said the girl I do not want to play anymore'", "correct": "'I do not want to play anymore,' said the girl."},
            {"topic": "Literary Adjectives", "question": "Improve the following sentence with a more descriptive adjective: 'The house looked old.'", "correct": "The house looked decrepit."},
            {"topic": "Report Clauses", "question": "Reduce the following complex sentence: 'The report, which was released despite the controversy, details the findings of the investigation.'", "correct": "The released report details the investigation's findings."},
        ]

        # Estado del juego
        self.language_mode = 'es' # 'es' o 'en'
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = COLOR_TEXT_LIGHT
        self.current_question = {"topic": "", "question": "", "correct": ""}
        self.particles = []

        # Rectángulos de la UI
        self.lang_button_rect = pygame.Rect(50, 50, 250, 50)
        self.input_rect = pygame.Rect(100, 350, 600, 50)
        self.check_button_rect = pygame.Rect(100, 420, 280, 50)
        self.next_button_rect = pygame.Rect(420, 420, 280, 50)
        self.glass_rect = pygame.Rect(self.screen_width // 2 - 350, 200, 700, 250)
        
        # Estado de animación de fondo
        self.bg_colors = [(135, 206, 235), (255, 105, 180), (255, 255, 0)]
        self.bg_current_color_index = 0
        self.bg_next_color_index = 1
        self.bg_progress = 0

        self.next_exercise()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw_elements()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
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

    def update(self):
        # Actualizar el fondo animado
        self.bg_progress += 0.001
        if self.bg_progress >= 1:
            self.bg_progress = 0
            self.bg_current_color_index = self.bg_next_color_index
            self.bg_next_color_index = (self.bg_next_color_index + 1) % len(self.bg_colors)

        # Actualizar partículas
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.life > 0]

    def draw_elements(self):
        # Dibujar fondo de gradiente animado
        self.draw_animated_background()

        # Dibujar efecto glassmorphism
        self.draw_glassmorphism_effect()

        # Título
        title_text = "Juego de Sintaxis para Escritores y Periodistas ✍️"
        self.draw_text(title_text, self.font_title, COLOR_TEXT_LIGHT, self.screen_width // 2, 100)

        # Etiqueta de tipo de subordinada
        sub_label = f"Tema: {self.current_question['topic']}"
        self.draw_text(sub_label, self.font_label, COLOR_TEXT_LIGHT, self.screen_width // 2, 200)

        # Pregunta
        self.draw_text(self.current_question['question'], self.font_question, COLOR_TEXT_LIGHT, self.screen_width // 2, 250)

        # Botones "Rainbow"
        self.draw_rainbow_button(self.lang_button_rect, f"Cambiar a Español {FEEDBACK_EMOJIS['change']}" if self.language_mode == 'en' else f"Switch to English {FEEDBACK_EMOJIS['change']}", pygame.mouse.get_pos())
        self.draw_rainbow_button(self.check_button_rect, f"Comprobar {FEEDBACK_EMOJIS['correct']}" if self.language_mode == 'es' else f"Check {FEEDBACK_EMOJIS['correct']}", pygame.mouse.get_pos())
        self.draw_rainbow_button(self.next_button_rect, f"Siguiente {FEEDBACK_EMOJIS['incorrect']}" if self.language_mode == 'es' else f"Next {FEEDBACK_EMOJIS['incorrect']}", pygame.mouse.get_pos())
        
        # Caja de texto (input)
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_rect, border_radius=10)
        pygame.draw.rect(self.screen, COLOR_TEXT_LIGHT, self.input_rect, 2, border_radius=10)
        input_surface = self.font_input.render(self.user_input, True, COLOR_TEXT_LIGHT)
        self.screen.blit(input_surface, (self.input_rect.x + 10, self.input_rect.y + 15))

        # Retroalimentación
        self.draw_text(self.feedback, self.font_label, self.feedback_color, self.screen_width // 2, 500)

        # Dibujar partículas
        for particle in self.particles:
            particle.draw(self.screen, self.font_emoji)

    def draw_animated_background(self):
        color1 = self.bg_colors[self.bg_current_color_index]
        color2 = self.bg_colors[self.bg_next_color_index]
        interp_color = (
            int(color1[0] + (color2[0] - color1[0]) * self.bg_progress),
            int(color1[1] + (color2[1] - color1[1]) * self.bg_progress),
            int(color1[2] + (color2[2] - color1[2]) * self.bg_progress)
        )
        self.screen.fill(interp_color)
        
    def draw_glassmorphism_effect(self):
        s = pygame.Surface(self.glass_rect.size, pygame.SRCALPHA)
        s.fill(COLOR_GLASS)
        self.screen.blit(s, self.glass_rect.topleft)
        pygame.draw.rect(self.screen, (255, 255, 255, 100), self.glass_rect, 1, border_radius=20)

    def draw_rainbow_button(self, rect, text, mouse_pos):
        colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
        color_count = len(colors)
        
        # Dibujar el gradiente
        for i in range(rect.width):
            progress = i / rect.width
            color_idx1 = int(progress * (color_count - 1))
            color_idx2 = (color_idx1 + 1) % color_count
            interp = (progress * (color_count - 1)) % 1
            
            c1 = colors[color_idx1]
            c2 = colors[color_idx2]
            
            interp_color = (
                int(c1[0] + (c2[0] - c1[0]) * interp),
                int(c1[1] + (c2[1] - c1[1]) * interp),
                int(c1[2] + (c2[2] - c1[2]) * interp)
            )
            pygame.draw.line(self.screen, interp_color, (rect.x + i, rect.y), (rect.x + i, rect.y + rect.height))
        
        # Efecto de hover y pulsación
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (255, 255, 255, 50), rect, 5, border_radius=10)
        
        # Dibujar texto
        button_text_surface = self.font_label.render(text, True, COLOR_TEXT_LIGHT)
        text_rect = button_text_surface.get_rect(center=rect.center)
        self.screen.blit(button_text_surface, text_rect)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def toggle_language(self):
        self.language_mode = 'en' if self.language_mode == 'es' else 'es'
        self.next_exercise()

    def next_exercise(self):
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = COLOR_TEXT_LIGHT
        
        if self.language_mode == 'es':
            self.current_question = random.choice(self.data_es)
        else:
            self.current_question = random.choice(self.data_en)

    def create_particles(self):
        for _ in range(50):
            x = random.randint(0, self.screen_width)
            y = 0
            emoji = random.choice(PARTICLE_EMOJIS)
            self.particles.append(Particle(x, y, emoji))

    def check_answer(self):
        # Normalizar la entrada del usuario y la respuesta correcta para una verificación más flexible
        user_response_normalized = self.user_input.strip().lower()
        correct_response_normalized = self.current_question['correct'].strip().lower()
        
        if user_response_normalized == correct_response_normalized:
            self.feedback = "¡Correcto! ¡Felicidades! 🎉"
            self.feedback_color = COLOR_CORRECT
            self.create_particles()
        else:
            self.feedback = f"Incorrecto. La respuesta era: '{self.current_question['correct']}' 😔"
            self.feedback_color = COLOR_INCORRECT

if __name__ == "__main__":
    game = SyntaxGame()
    game.run()
