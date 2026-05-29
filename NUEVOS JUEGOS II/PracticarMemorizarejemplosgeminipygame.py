import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Syntax Quest: Simple vs. Compound Sentences")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
TRANSPARENT_BLACK = (0, 0, 0, 150)
RAINBOW_COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]

# Fonts
font_title = pygame.font.Font("font/LilitaOne-Regular.ttf", 60)
font_subtitle = pygame.font.Font("font/LilitaOne-Regular.ttf", 36)
font_text = pygame.font.Font("font/LilitaOne-Regular.ttf", 24)
font_emoji = pygame.font.Font("font/LilitaOne-Regular.ttf", 36)

# --- Game Data ---
THEORY = {
    "simple": {
        "title": "Oración Simple 🧐",
        "text": "Una oración simple contiene un solo sujeto y un solo predicado. Expresa una sola idea completa.",
        "examples": [
            "El perro 🐕 ladra.",
            "María 👩‍🦱 cocina la cena."
        ],
        "syntax_emojis": [
            {"es": "Sujeto 👤 + Predicado 🗣️", "en": "Subject 👤 + Predicate 🗣️"}
        ]
    },
    "compound": {
        "title": "Oración Compuesta 🧩",
        "text": "Una oración compuesta contiene dos o más oraciones simples, unidas por una conjunción o un signo de puntuación.",
        "examples": [
            "José 🧑‍🦱 estudia 📚 y Ana 👩‍🦱 lee 📖.",
            "Llovió 🌧️, pero salimos a caminar 🚶‍♂️."
        ],
        "syntax_emojis": [
            {"es": "Oración 1️⃣ + Conjunción 🔗 + Oración 2️⃣", "en": "Sentence 1️⃣ + Conjunction 🔗 + Sentence 2️⃣"}
        ]
    }
}

PRACTICE_EXERCISES = [
    {"sentence": "El sol calienta ☀️ y la luna enfría ❄️.", "type": "compound", "emojis": "🧩"},
    {"sentence": "El gato 🐱 durmió en la silla.", "type": "simple", "emojis": "🧐"},
    {"sentence": "Juan lee un libro 📖, pero yo prefiero ver películas 🎬.", "type": "compound", "emojis": "🧩"},
    {"sentence": "Mi hermana 👩‍🦱 canta 🎤 bien.", "type": "simple", "emojis": "🧐"},
    {"sentence": "Compramos manzanas 🍏 y peras 🍐.", "type": "compound", "emojis": "🧩"},
    {"sentence": "El pájaro 🐦 canta felizmente.", "type": "simple", "emojis": "🧐"},
    {"sentence": "El tren 🚂 llegó tarde y el autobús 🚌 no vino.", "type": "compound", "emojis": "🧩"},
    {"sentence": "Los niños 👧👦 juegan en el parque 🌳.", "type": "simple", "emojis": "🧐"},
    {"sentence": "Estudié 🤓 toda la noche, por lo tanto, estoy cansado 😴.", "type": "compound", "emojis": "🧩"},
    {"sentence": "Ella baila 💃 muy bien.", "type": "simple", "emojis": "🧐"},
    {"sentence": "Ella corre 🏃‍♀️ y él camina 🚶‍♂️.", "type": "compound", "emojis": "🧩"},
    {"sentence": "El chef 👨‍🍳 prepara un pastel 🍰.", "type": "simple", "emojis": "🧐"},
    {"sentence": "La nieve 🌨️ cubrió las montañas y el hielo 🧊 congeló el río.", "type": "compound", "emojis": "🧩"},
    {"sentence": "El avión ✈️ voló alto.", "type": "simple", "emojis": "🧐"},
    {"sentence": "La computadora 💻 falló, así que la reinicié 🔄.", "type": "compound", "emojis": "🧩"},
    {"sentence": "El agua 💧 fluye por el río.", "type": "simple", "emojis": "🧐"},
    {"sentence": "Ella tiene un perro 🐶 y su hermano tiene un gato 🐱.", "type": "compound", "emojis": "🧩"},
    {"sentence": "Las flores 🌻 crecen en el jardín.", "type": "simple", "emojis": "🧐"},
    {"sentence": "La película 🎞️ era larga, pero me gustó mucho.", "type": "compound", "emojis": "🧩"},
    {"sentence": "Los estudiantes 👩‍🎓👨‍🎓 estudian para el examen.", "type": "simple", "emojis": "🧐"}
]

# --- Custom Classes ---

class RainbowButton:
    def __init__(self, text, x, y, width, height, action=None, emoji="🌟"):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.base_color = BLUE
        self.hover_color = tuple(min(255, c + 50) for c in self.base_color)
        self.current_color = self.base_color
        self.hovered = False
        self.emoji = font_emoji.render(emoji, True, WHITE)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        hovered_now = self.rect.collidepoint(mouse_pos)

        if hovered_now and not self.hovered:
            self.hovered = True
            self.start_time = time.time()
        elif not hovered_now and self.hovered:
            self.hovered = False

        if self.hovered:
            # Animate rainbow colors
            t = (time.time() - self.start_time) * 4
            color_index = int(t % len(RAINBOW_COLORS))
            self.current_color = RAINBOW_COLORS[color_index]
        else:
            self.current_color = self.base_color

        # Draw glassmorphism background
        s = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        s.fill(TRANSPARENT_BLACK)
        pygame.draw.rect(s, self.current_color, s.get_rect(), border_radius=15)
        s.set_alpha(150)
        surface.blit(s, self.rect)
        pygame.draw.rect(surface, self.current_color, self.rect, 2, border_radius=15)

        # Draw text and emoji
        text_surf = font_subtitle.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

        emoji_pos = (self.rect.x + 20, self.rect.y + self.rect.height // 2 - self.emoji.get_height() // 2)
        surface.blit(self.emoji, emoji_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
                return True
        return False

class Particle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.emoji = font_emoji.render(emoji, True, WHITE)
        self.velocity = random.uniform(1, 3)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        self.life = 255

    def update(self):
        self.y += self.velocity
        self.life -= 2

    def draw(self, surface):
        if self.life > 0:
            s = self.emoji.copy()
            s.set_alpha(self.life)
            rotated_s = pygame.transform.rotate(s, self.angle)
            self.angle += self.rotation_speed
            surface.blit(rotated_s, (self.x, self.y))

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.last_scene = None
    
    def add_scene(self, name, scene_obj):
        self.scenes[name] = scene_obj
    
    def set_scene(self, name):
        self.last_scene = self.current_scene
        self.current_scene = self.scenes[name]

    def run(self):
        self.current_scene.run()

# --- Scenes ---

class Scene:
    def __init__(self, scene_manager):
        self.manager = scene_manager
        self.particles = []
        self.background_color = [30, 30, 30]

    def handle_events(self, events):
        pass

    def update(self):
        # Update particles
        self.particles = [p for p in self.particles if p.life > 0]
        for p in self.particles:
            p.update()

    def draw(self, screen):
        # Draw dynamic background
        for x in range(SCREEN_WIDTH):
            r = int(self.background_color[0] + (x / SCREEN_WIDTH) * 20)
            g = int(self.background_color[1] + (x / SCREEN_WIDTH) * 20)
            b = int(self.background_color[2] + (x / SCREEN_WIDTH) * 20)
            pygame.draw.line(screen, (r,g,b), (x, 0), (x, SCREEN_HEIGHT))

        # Draw particles
        for p in self.particles:
            p.draw(screen)

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            self.handle_events(events)
            self.update()
            self.draw(screen)
            pygame.display.flip()

            if not running:
                pygame.quit()
                sys.exit()

class MenuScene(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.buttons = [
            RainbowButton("Teoría Simple 🧐", SCREEN_WIDTH // 2 - 200, 250, 400, 60, lambda: self.manager.set_scene("simple_theory"), "🧐"),
            RainbowButton("Teoría Compuesta 🧩", SCREEN_WIDTH // 2 - 200, 350, 400, 60, lambda: self.manager.set_scene("compound_theory"), "🧩"),
            RainbowButton("Practicar 🧠", SCREEN_WIDTH // 2 - 200, 450, 400, 60, lambda: self.manager.set_scene("practice"), "🧠"),
            RainbowButton("Salir 🚪", SCREEN_WIDTH // 2 - 200, 550, 400, 60, lambda: pygame.quit() or sys.exit(), "🚪")
        ]

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def draw(self, screen):
        super().draw(screen)
        title_text = font_title.render("Syntax Quest", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_text, title_rect)
        
        for button in self.buttons:
            button.draw(screen)

class TheoryScene(Scene):
    def __init__(self, scene_manager, theory_data):
        super().__init__(scene_manager)
        self.theory_data = theory_data
        self.back_button = RainbowButton("Volver 🔙", 30, 30, 150, 50, lambda: self.manager.set_scene("menu"), "🔙")

    def handle_events(self, events):
        for event in events:
            self.back_button.handle_event(event)
            if random.random() < 0.05:
                self.particles.append(Particle(random.randint(0, SCREEN_WIDTH), 0, random.choice(["💡", "✍️", "🧠", "✨"])))

    def draw(self, screen):
        super().draw(screen)
        
        # Glassmorphism container for text
        s = pygame.Surface((SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150), pygame.SRCALPHA)
        s.fill(TRANSPARENT_BLACK)
        pygame.draw.rect(s, GRAY, s.get_rect(), 2, border_radius=20)
        screen.blit(s, (50, 100))
        
        # Title
        title_text = font_subtitle.render(self.theory_data["title"], True, WHITE)
        screen.blit(title_text, (80, 120))
        
        # Main text
        text_lines = self.theory_data["text"].split()
        current_line = ""
        y_pos = 180
        for word in text_lines:
            if font_text.render(current_line + " " + word, True, WHITE).get_width() > SCREEN_WIDTH - 200:
                text_surf = font_text.render(current_line, True, WHITE)
                screen.blit(text_surf, (80, y_pos))
                y_pos += 30
                current_line = word
            else:
                current_line += " " + word
        text_surf = font_text.render(current_line, True, WHITE)
        screen.blit(text_surf, (80, y_pos))

        # Examples
        y_pos += 50
        text_surf = font_subtitle.render("Ejemplos:", True, WHITE)
        screen.blit(text_surf, (80, y_pos))
        for example in self.theory_data["examples"]:
            y_pos += 30
            text_surf = font_text.render(example, True, WHITE)
            screen.blit(text_surf, (100, y_pos))

        # Syntax Emojis
        y_pos += 50
        text_surf = font_subtitle.render("Sintaxis:", True, WHITE)
        screen.blit(text_surf, (80, y_pos))
        for syntax in self.theory_data["syntax_emojis"]:
            y_pos += 30
            es_text = font_text.render("ES: " + syntax["es"], True, WHITE)
            en_text = font_text.render("EN: " + syntax["en"], True, WHITE)
            screen.blit(es_text, (100, y_pos))
            screen.blit(en_text, (100, y_pos + 30))

        self.back_button.draw(screen)

class PracticeScene(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.exercises = PRACTICE_EXERCISES.copy()
        random.shuffle(self.exercises)
        self.current_exercise_index = 0
        self.result = ""
        self.result_color = BLACK

        self.back_button = RainbowButton("Volver 🔙", 30, 30, 150, 50, lambda: self.manager.set_scene("menu"), "🔙")
        self.simple_button = RainbowButton("Simple 🧐", SCREEN_WIDTH // 2 - 250, 300, 200, 60, lambda: self.check_answer("simple"), "🧐")
        self.compound_button = RainbowButton("Compuesta 🧩", SCREEN_WIDTH // 2 + 50, 300, 200, 60, lambda: self.check_answer("compound"), "🧩")
        self.next_button = RainbowButton("Siguiente", SCREEN_WIDTH - 200, 500, 150, 50, self.next_exercise, "➡️")
        
        self.exercise_text_surface = None
        self.load_exercise()

    def load_exercise(self):
        if self.current_exercise_index < len(self.exercises):
            exercise = self.exercises[self.current_exercise_index]
            self.exercise_text_surface = font_subtitle.render(exercise["sentence"], True, BLACK)
            self.result = ""
        else:
            self.manager.set_scene("results")

    def check_answer(self, user_choice):
        correct_answer = self.exercises[self.current_exercise_index]["type"]
        if user_choice == correct_answer:
            self.result = "¡Correcto! ✅"
            self.result_color = GREEN
            self.particles.append(Particle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "✅"))
        else:
            self.result = "Incorrecto. ❌"
            self.result_color = RED
            self.particles.append(Particle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "❌"))
            
    def next_exercise(self):
        self.current_exercise_index += 1
        self.load_exercise()
    
    def handle_events(self, events):
        for event in events:
            self.back_button.handle_event(event)
            self.simple_button.handle_event(event)
            self.compound_button.handle_event(event)
            self.next_button.handle_event(event)
            if random.random() < 0.1:
                self.particles.append(Particle(random.randint(0, SCREEN_WIDTH), 0, random.choice(["🧐", "🧩", "🤔", "❓"])))

    def draw(self, screen):
        super().draw(screen)
        
        # Glassmorphism container for text
        s = pygame.Surface((SCREEN_WIDTH - 100, 200), pygame.SRCALPHA)
        s.fill(TRANSPARENT_BLACK)
        pygame.draw.rect(s, GRAY, s.get_rect(), 2, border_radius=20)
        screen.blit(s, (50, 100))
        
        if self.exercise_text_surface:
            text_rect = self.exercise_text_surface.get_rect(center=(SCREEN_WIDTH // 2, 180))
            screen.blit(self.exercise_text_surface, text_rect)
        
        result_text = font_title.render(self.result, True, self.result_color)
        result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        screen.blit(result_text, result_rect)

        self.back_button.draw(screen)
        self.simple_button.draw(screen)
        self.compound_button.draw(screen)
        self.next_button.draw(screen)

class Game:
    def __init__(self):
        self.manager = SceneManager()
        self.manager.add_scene("menu", MenuScene(self.manager))
        self.manager.add_scene("simple_theory", TheoryScene(self.manager, THEORY["simple"]))
        self.manager.add_scene("compound_theory", TheoryScene(self.manager, THEORY["compound"]))
        self.manager.add_scene("practice", PracticeScene(self.manager))
        self.manager.set_scene("menu")

    def run(self):
        self.manager.run()

if __name__ == "__main__":
    game = Game()
    game.run()
