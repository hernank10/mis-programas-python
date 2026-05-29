import pygame
import sys
import random
import math
import time
from pygame import gfxdraw

# Inicializar Pygame
pygame.init()
pygame.font.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Grammar Adventure - Aventura Gramatical")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (25, 25, 40)

# Fuentes
title_font = pygame.font.SysFont('comicsansms', 60)
button_font = pygame.font.SysFont('comicsansms', 28)
game_font = pygame.font.SysFont('comicsansms', 32)
feedback_font = pygame.font.SysFont('comicsansms', 24)

# Emoticonos para partículas
EMOTICONS = ["🎯", "🧩", "📊", "✏️", "🧱", "🏎️", "🛡️", "⭐", "🎉", "💫", "🔥", "💖", "🌟", "💎", "🚀"]
SYNTAX_EMOTICONS = ["📝", "🔤", "📚", "💬", "🎓", "🏆", "💡", "✅", "❌", "⚡"]

# Clase para botones arcoíris
class RainbowButton:
    def __init__(self, x, y, width, height, text, emoticon="", action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoticon = emoticon
        self.action = action
        self.hovered = False
        self.clicked = False
        self.hover_time = 0
        self.rainbow_offset = 0
        self.particles = []
        
    def draw(self, surface):
        # Efecto arcoíris animado
        self.rainbow_offset = (self.rainbow_offset + 1) % 360
        
        # Colores del arcoíris
        rainbow_colors = []
        for i in range(7):
            hue = (self.rainbow_offset + i * 30) % 360
            color = self.hsv_to_rgb(hue, 1, 1)
            rainbow_colors.append(color)
        
        # Dibujar fondo del botón con efecto arcoíris
        if self.hovered:
            # Efecto de hover más intenso
            for i in range(7):
                color = rainbow_colors[i]
                rect = pygame.Rect(
                    self.rect.x + i * 2, 
                    self.rect.y + i * 2, 
                    self.rect.width - i * 4, 
                    self.rect.height - i * 4
                )
                pygame.draw.rect(surface, color, rect, border_radius=15)
        else:
            # Efecto normal
            for i in range(5):
                color = rainbow_colors[i]
                rect = pygame.Rect(
                    self.rect.x + i, 
                    self.rect.y + i, 
                    self.rect.width - i * 2, 
                    self.rect.height - i * 2
                )
                pygame.draw.rect(surface, color, rect, border_radius=15)
        
        # Dibujar texto y emoticono
        text_color = WHITE if not self.hovered else (255, 255, 200)
        text_surface = button_font.render(f"{self.emoticon} {self.text}", True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
        # Efecto de partículas en hover
        if self.hovered and random.random() < 0.3:
            self.create_particle()
        
        # Actualizar y dibujar partículas
        for particle in self.particles[:]:
            particle['y'] += particle['speed']
            particle['life'] -= 1
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
            else:
                # Dibujar partícula como emoticono
                emoticon_surface = game_font.render(particle['emoticon'], True, particle['color'])
                surface.blit(emoticon_surface, (particle['x'], particle['y']))
    
    def create_particle(self):
        particle = {
            'x': random.randint(self.rect.left, self.rect.right),
            'y': self.rect.top,
            'speed': random.uniform(1, 3),
            'life': random.randint(20, 40),
            'emoticon': random.choice(EMOTICONS),
            'color': self.hsv_to_rgb(random.randint(0, 360), 1, 1)
        }
        self.particles.append(particle)
    
    def hsv_to_rgb(self, h, s, v):
        h = h / 360.0
        if s == 0.0: v*=255; return (v, v, v)
        i = int(h*6.)
        f = (h*6.)-i
        p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f))))
        v = int(255*v)
        i %= 6
        if i == 0: return (v, t, p)
        if i == 1: return (q, v, p)
        if i == 2: return (p, v, t)
        if i == 3: return (p, q, v)
        if i == 4: return (t, p, v)
        if i == 5: return (v, p, q)
    
    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        was_hovered = self.hovered
        self.hovered = self.rect.collidepoint(mouse_pos)
        
        if self.hovered and not was_hovered:
            self.hover_time = pygame.time.get_ticks()
        
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.hovered:
                    self.clicked = True
                    if self.action:
                        self.action()
                    return True
        return False

# Clase para el sistema de partículas de fondo
class ParticleSystem:
    def __init__(self):
        self.particles = []
        self.max_particles = 50
        
    def add_particle(self):
        if len(self.particles) < self.max_particles:
            particle = {
                'x': random.randint(0, WIDTH),
                'y': random.randint(-100, -10),
                'speed': random.uniform(1, 4),
                'size': random.randint(20, 40),
                'emoticon': random.choice(SYNTAX_EMOTICONS),
                'color': (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255)),
                'rotation': random.uniform(0, 360),
                'rotation_speed': random.uniform(-2, 2)
            }
            self.particles.append(particle)
    
    def update(self):
        # Añadir nuevas partículas aleatoriamente
        if random.random() < 0.1:
            self.add_particle()
        
        # Actualizar partículas existentes
        for particle in self.particles[:]:
            particle['y'] += particle['speed']
            particle['rotation'] += particle['rotation_speed']
            
            # Si la partícula sale de la pantalla, eliminarla
            if particle['y'] > HEIGHT + 50:
                self.particles.remove(particle)
    
    def draw(self, surface):
        for particle in self.particles:
            # Crear superficie para el emoticono rotado
            emoticon_surface = game_font.render(particle['emoticon'], True, particle['color'])
            rotated_surface = pygame.transform.rotate(emoticon_surface, particle['rotation'])
            rect = rotated_surface.get_rect(center=(particle['x'], particle['y']))
            surface.blit(rotated_surface, rect)

# Clase para efectos de transición
class Transition:
    def __init__(self):
        self.active = False
        self.progress = 0
        self.duration = 30  # frames
        self.type = "fade"  # fade, slide, etc.
    
    def start(self, transition_type="fade"):
        self.active = True
        self.progress = 0
        self.type = transition_type
    
    def update(self):
        if self.active:
            self.progress += 1
            if self.progress >= self.duration:
                self.active = False
                return True
        return False
    
    def draw(self, surface):
        if self.active and self.type == "fade":
            alpha = min(255, (self.progress / self.duration) * 255)
            fade_surface = pygame.Surface((WIDTH, HEIGHT))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(alpha)
            surface.blit(fade_surface, (0, 0))

# Clase para el juego de gramática base
class GrammarGame:
    def __init__(self, name, emoticon):
        self.name = name
        self.emoticon = emoticon
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.feedback = ""
        self.feedback_timer = 0
        self.correct_sound = pygame.mixer.Sound()  # Podrías cargar sonidos reales
        self.incorrect_sound = pygame.mixer.Sound()
        
    def load_questions(self):
        # Este método debe ser sobrescrito por cada juego específico
        pass
    
    def display_question(self, surface):
        # Este método debe ser sobrescrito por cada juego específico
        pass
    
    def check_answer(self, answer):
        # Este método debe ser sobrescrito por cada juego específico
        pass
    
    def show_feedback(self, surface, message, is_correct):
        self.feedback = message
        self.feedback_timer = 60  # Mostrar por 60 frames (2 segundos aprox.)
        
        # Posición para el feedback
        x, y = WIDTH // 2, HEIGHT - 100
        
        # Fondo del feedback con efecto glassmorphism
        feedback_bg = pygame.Surface((600, 60), pygame.SRCALPHA)
        feedback_bg.fill((255, 255, 255, 100))  # Fondo semi-transparente
        surface.blit(feedback_bg, (x - 300, y - 30))
        
        # Texto del feedback
        color = (0, 200, 0) if is_correct else (200, 0, 0)
        emoticon = "✅" if is_correct else "❌"
        feedback_text = feedback_font.render(f"{emoticon} {message}", True, color)
        surface.blit(feedback_text, (x - feedback_text.get_width() // 2, y - feedback_text.get_height() // 2))
        
        # Efecto de partículas para feedback
        if is_correct:
            for _ in range(5):
                self.create_feedback_particle(x, y, is_correct)
    
    def create_feedback_particle(self, x, y, is_correct):
        # Crear partículas de celebración
        pass
    
    def update(self):
        if self.feedback_timer > 0:
            self.feedback_timer -= 1

# Juego específico: Cazador de Sujeto y Predicado
class SubjectPredicateGame(GrammarGame):
    def __init__(self):
        super().__init__("Cazador de Sujeto y Predicado", "🎯")
        self.load_questions()
        self.user_subject = ""
        self.user_predicate = ""
        self.input_active = "subject"  # "subject" or "predicate"
        self.answer_buttons = []
        
    def load_questions(self):
        self.questions = [
            {
                "sentence": "El niño juega en el parque",
                "subject": "El niño",
                "predicate": "juega en el parque",
                "bilingual": "The boy plays in the park"
            },
            {
                "sentence": "María estudia matemáticas en la biblioteca",
                "subject": "María",
                "predicate": "estudia matemáticas en la biblioteca",
                "bilingual": "Maria studies math at the library"
            },
            {
                "sentence": "Los pájaros cantan hermosamente por la mañana",
                "subject": "Los pájaros",
                "predicate": "cantan hermosamente por la mañana",
                "bilingual": "The birds sing beautifully in the morning"
            }
        ]
    
    def display_question(self, surface):
        if self.current_question >= len(self.questions):
            self.show_results(surface)
            return
            
        question = self.questions[self.current_question]
        
        # Título del juego
        title = title_font.render(f"{self.emoticon} {self.name}", True, WHITE)
        surface.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Oración a analizar
        sentence_text = game_font.render(question["sentence"], True, (200, 200, 255))
        surface.blit(sentence_text, (WIDTH // 2 - sentence_text.get_width() // 2, 150))
        
        # Versión bilingüe
        bilingual_text = feedback_font.render(question["bilingual"], True, (150, 200, 255))
        surface.blit(bilingual_text, (WIDTH // 2 - bilingual_text.get_width() // 2, 200))
        
        # Instrucciones
        instructions = feedback_font.render("Identifica el sujeto y el predicado:", True, WHITE)
        surface.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, 250))
        
        # Área de entrada para sujeto
        subject_label = game_font.render("Sujeto / Subject:", True, WHITE)
        surface.blit(subject_label, (WIDTH // 2 - 300, 320))
        
        # Dibujar caja de texto para sujeto
        subject_rect = pygame.Rect(WIDTH // 2 - 300, 360, 600, 50)
        pygame.draw.rect(surface, (100, 100, 150), subject_rect, border_radius=10)
        if self.input_active == "subject":
            pygame.draw.rect(surface, (150, 150, 200), subject_rect, 3, border_radius=10)
        
        subject_input = game_font.render(self.user_subject, True, WHITE)
        surface.blit(subject_input, (subject_rect.x + 10, subject_rect.y + 10))
        
        # Área de entrada para predicado
        predicate_label = game_font.render("Predicado / Predicate:", True, WHITE)
        surface.blit(predicate_label, (WIDTH // 2 - 300, 450))
        
        # Dibujar caja de texto para predicado
        predicate_rect = pygame.Rect(WIDTH // 2 - 300, 490, 600, 50)
        pygame.draw.rect(surface, (100, 100, 150), predicate_rect, border_radius=10)
        if self.input_active == "predicate":
            pygame.draw.rect(surface, (150, 150, 200), predicate_rect, 3, border_radius=10)
        
        predicate_input = game_font.render(self.user_predicate, True, WHITE)
        surface.blit(predicate_input, (predicate_rect.x + 10, predicate_rect.y + 10))
        
        # Botón de verificación
        verify_button = RainbowButton(WIDTH // 2 - 100, 580, 200, 60, "Verificar", "✅", self.verify_answer)
        verify_button.draw(surface)
        
        # Mostrar feedback si existe
        if self.feedback_timer > 0:
            self.show_feedback(surface, self.feedback, "correcto" in self.feedback.lower())
    
    def verify_answer(self):
        question = self.questions[self.current_question]
        subject_correct = self.user_subject.strip().lower() == question["subject"].lower()
        predicate_correct = self.user_predicate.strip().lower() == question["predicate"].lower()
        
        if subject_correct and predicate_correct:
            self.score += 10
            self.show_feedback(screen, "¡Correcto! 🎉 Both subject and predicate are right!", True)
            self.current_question += 1
            self.user_subject = ""
            self.user_predicate = ""
        else:
            errors = []
            if not subject_correct:
                errors.append("subject")
            if not predicate_correct:
                errors.append("predicate")
            
            error_msg = f"Incorrect. Check your {', '.join(errors)}. Try again! ❌"
            self.show_feedback(screen, error_msg, False)
    
    def show_results(self, surface):
        # Pantalla de resultados
        result_bg = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        result_bg.fill((0, 0, 0, 200))
        surface.blit(result_bg, (0, 0))
        
        # Título de resultados
        result_title = title_font.render("🎉 ¡Juego Completado!", True, WHITE)
        surface.blit(result_title, (WIDTH // 2 - result_title.get_width() // 2, 200))
        
        # Puntuación
        score_text = game_font.render(f"Puntuación: {self.score}/{len(self.questions)*10}", True, WHITE)
        surface.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 300))
        
        # Botón para volver al menú
        menu_button = RainbowButton(WIDTH // 2 - 150, 400, 300, 70, "Volver al Menú", "🏠", self.return_to_menu)
        menu_button.draw(surface)
    
    def return_to_menu(self):
        global current_game, current_screen
        current_screen = "menu"
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.input_active == "subject":
                    if event.key == pygame.K_RETURN:
                        self.input_active = "predicate"
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_subject = self.user_subject[:-1]
                    else:
                        self.user_subject += event.unicode
                
                elif self.input_active == "predicate":
                    if event.key == pygame.K_RETURN:
                        self.verify_answer()
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_predicate = self.user_predicate[:-1]
                    else:
                        self.user_predicate += event.unicode
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Cambiar entre campos de entrada al hacer clic
                mouse_pos = pygame.mouse.get_pos()
                subject_rect = pygame.Rect(WIDTH // 2 - 300, 360, 600, 50)
                predicate_rect = pygame.Rect(WIDTH // 2 - 300, 490, 600, 50)
                
                if subject_rect.collidepoint(mouse_pos):
                    self.input_active = "subject"
                elif predicate_rect.collidepoint(mouse_pos):
                    self.input_active = "predicate"

# Clase para el menú principal
class MainMenu:
    def __init__(self):
        self.buttons = []
        self.particle_system = ParticleSystem()
        self.background_offset = 0
        self.setup_buttons()
    
    def setup_buttons(self):
        button_width, button_height = 400, 80
        start_x = WIDTH // 2 - button_width // 2
        start_y = 200
        spacing = 20
        
        games = [
            ("🎯 Cazador de Sujeto y Predicado", "sujeto_predicado"),
            ("🧩 Puzzle de la Oración", "puzzle_oracion"),
            ("📊 Clasifica la Oración", "clasifica_oracion"),
            ("✏️ Corrector de Oraciones", "corrector_oraciones"),
            ("🧱 Construye tu Propia Oración", "construye_oracion"),
            ("🏎️ Carrera de Conectores", "carrera_conectores"),
            ("🛡️ Defiende la Gramática", "defensa_gramatica")
        ]
        
        for i, (text, game_id) in enumerate(games):
            y_pos = start_y + i * (button_height + spacing)
            button = RainbowButton(start_x, y_pos, button_width, button_height, text, "", 
                                  lambda g=game_id: self.start_game(g))
            self.buttons.append(button)
    
    def start_game(self, game_id):
        global current_game, current_screen
        current_screen = "game"
        
        if game_id == "sujeto_predicado":
            current_game = SubjectPredicateGame()
        # Aquí agregarías los otros juegos
    
    def draw(self, surface):
        # Fondo animado con gradientes
        self.background_offset = (self.background_offset + 0.5) % HEIGHT
        
        for y in range(0, HEIGHT, 10):
            # Crear un gradiente que se desplace
            color_value = int(128 + 127 * math.sin((y + self.background_offset) * 0.01))
            color = (25, 25, color_value)
            pygame.draw.rect(surface, color, (0, y, WIDTH, 10))
        
        # Dibujar partículas de fondo
        self.particle_system.update()
        self.particle_system.draw(surface)
        
        # Título principal
        title = title_font.render("🎮 Grammar Adventure", True, WHITE)
        subtitle = game_font.render("Aventura Gramatical Bilingüe", True, (200, 200, 255))
        
        surface.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
        surface.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 150))
        
        # Dibujar botones
        for button in self.buttons:
            button.draw(surface)
        
        # Pie de página con emoticonos
        footer = feedback_font.render("✨ Aprende gramática español-inglés de forma divertida! ✨", True, WHITE)
        surface.blit(footer, (WIDTH // 2 - footer.get_width() // 2, HEIGHT - 50))
    
    def update(self, events):
        for button in self.buttons:
            button.update(events)
        
        self.particle_system.update()

# Variables globales
current_screen = "menu"
current_game = None
transition = Transition()
main_menu = MainMenu()

# Bucle principal del juego
clock = pygame.time.Clock()
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if current_screen == "game":
                    current_screen = "menu"
    
    # Limpiar pantalla
    screen.fill(BACKGROUND)
    
    # Actualizar y dibujar según la pantalla actual
    if current_screen == "menu":
        main_menu.update(events)
        main_menu.draw(screen)
    elif current_screen == "game" and current_game:
        if isinstance(current_game, GrammarGame):
            current_game.display_question(screen)
            if hasattr(current_game, 'handle_events'):
                current_game.handle_events(events)
    
    # Actualizar y dibujar transición si está activa
    if transition.update():
        # La transición ha terminado
        pass
    transition.draw(screen)
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
