import pygame
import random
import sys
import math

pygame.init()

# --- Configuración de pantalla ---
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Sintaxis Bilingüe - Octavo Grado")

# --- Colores (gradientes de la naturaleza + glassmorphism) ---
COLORS = [
    (255, 99, 71),    # Tomato
    (135, 206, 235),  # SkyBlue
    (60, 179, 113),   # MediumSeaGreen
    (238, 130, 238),  # Violet
    (255, 215, 0)     # Gold
]
WHITE = (255, 255, 255)

# --- Fuente ---
font = pygame.font.SysFont("Arial", 28, bold=True)

# --- Preguntas de sintaxis bilingüe (Octavo grado) ---
questions = [
    {"es": "Aunque estaba cansado, terminó su tarea.",
     "en": "Although he was tired, he finished his homework."},
    {"es": "Si estudias, aprobarás el examen.",
     "en": "If you study, you will pass the exam."},
    {"es": "No salió porque estaba lloviendo.",
     "en": "He didn’t go out because it was raining."},
    {"es": "Trabajó duro para que pudiera ahorrar dinero.",
     "en": "He worked hard so that he could save money."},
    {"es": "Aunque es joven, entiende mucho.",
     "en": "Although he is young, he understands a lot."}
]

# --- Clase RainbowButton ---
class RainbowButton:
    def __init__(self, x, y, w, h, text, emoji):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.emoji = emoji
        self.color_shift = 0

    def draw(self, screen):
        # Degradado arcoíris animado
        self.color_shift = (self.color_shift + 1) % 360
        color = pygame.Color(0)
        color.hsva = (self.color_shift, 100, 100, 100)

        # Efecto glassmorphism
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        s.fill((color.r, color.g, color.b, 180))
        screen.blit(s, (self.rect.x, self.rect.y))

        # Texto + emoji
        text_surf = font.render(f"{self.emoji} {self.text}", True, WHITE)
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# --- Sistema de partículas con emoticones ---
class Particle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.emoji = emoji
        self.speed = random.uniform(1, 3)
        self.angle = random.uniform(0, math.pi * 2)
        self.rotation = random.randint(0, 360)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.rotation += 5
        if self.y > HEIGHT + 20:
            self.y = -20

    def draw(self, screen):
        text_surf = font.render(self.emoji, True, WHITE)
        rotated = pygame.transform.rotate(text_surf, self.rotation)
        screen.blit(rotated, (self.x, self.y))

# --- Inicializar botones y partículas ---
buttons = [
    RainbowButton(100, 450, 300, 60, "Ver respuesta", "💡"),
    RainbowButton(500, 450, 300, 60, "Siguiente", "➡️")
]

particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.choice(["😊", "📚", "✨"])) for _ in range(20)]

# --- Variables de juego ---
current_question = 0
show_answer = False

# --- Bucle principal ---
running = True
while running:
    screen.fill((30, 30, 60))

    # Fondo degradado animado
    for y in range(HEIGHT):
        r = 30 + int(20 * math.sin(pygame.time.get_ticks() / 1000 + y / 50))
        g = 60 + int(20 * math.cos(pygame.time.get_ticks() / 1200 + y / 60))
        b = 90
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

    # Mostrar pregunta
    q = questions[current_question]
    es_text = font.render("ES: " + q["es"], True, WHITE)
    en_text = font.render("EN: " + ("???" if not show_answer else q["en"]), True, WHITE)
    screen.blit(es_text, (50, 100))
    screen.blit(en_text, (50, 160))

    # Dibujar botones
    for btn in buttons:
        btn.draw(screen)

    # Dibujar partículas
    for p in particles:
        p.move()
        p.draw(screen)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if buttons[0].is_clicked(pos):  # Ver respuesta
                show_answer = True
            elif buttons[1].is_clicked(pos):  # Siguiente
                current_question = (current_question + 1) % len(questions)
                show_answer = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
