import pygame
import random
import sys
import math

pygame.init()

# Pantalla
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Sintaxis Bilingüe - Undécimo Grado")

# Fuente
font = pygame.font.SysFont("Arial", 28, bold=True)

# Colores gradiente
gradient_colors = [(255, 87, 34), (156, 39, 176), (33, 150, 243), (0, 188, 212)]

# Preguntas de sintaxis bilingüe (nivel avanzado)
questions = [
    {"es": "Identifica el tipo de oración: 'Although it was raining, we decided to go for a walk.'",
     "en": "Identify the sentence type: 'Although it was raining, we decided to go for a walk.'",
     "answer": "subordinada concesiva"},
    {"es": "Traduce al inglés: 'No salí porque estaba cansado.'",
     "en": "Translate into English: 'No salí porque estaba cansado.'",
     "answer": "I didn’t go out because I was tired."},
    {"es": "Clasifica la oración: 'I studied hard, and I passed the exam.'",
     "en": "Classify the sentence: 'I studied hard, and I passed the exam.'",
     "answer": "compuesta coordinada copulativa"},
    {"es": "Transforma en inglés académico: 'Quiero ser ingeniero para ayudar a mi comunidad.'",
     "en": "Transform into academic English: 'Quiero ser ingeniero para ayudar a mi comunidad.'",
     "answer": "I want to become an engineer in order to help my community."}
]

# Botón Arcoíris
class RainbowButton:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.hovered = False

    def draw(self, surface):
        color_shift = (pygame.time.get_ticks() // 5) % 255
        color = (abs(255 - color_shift), color_shift, 255 - color_shift // 2)
        pygame.draw.rect(surface, color, self.rect, border_radius=20)
        text_render = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_render, (self.rect.x + 20, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Partículas con emoticones
class Particle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.emoji = emoji
        self.size = random.randint(24, 36)
        self.speed = random.uniform(1, 3)
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation = random.uniform(-5, 5)

    def update(self):
        self.y += self.speed
        self.x += math.sin(self.angle) * 2
        self.angle += 0.02
        self.rotation += 0.1

    def draw(self, surface):
        emoji_surface = font.render(self.emoji, True, (255, 255, 255))
        rotated = pygame.transform.rotate(emoji_surface, self.rotation)
        surface.blit(rotated, (self.x, self.y))

# Inicializar botones
buttons = [
    RainbowButton("😀 Responder", 100, 500, 200, 60),
    RainbowButton("📖 Ver Respuesta", 350, 500, 250, 60),
    RainbowButton("➡️ Siguiente", 650, 500, 180, 60)
]

# Variables de juego
running = True
current_q = 0
particles = []
feedback = ""

# Loop principal
while running:
    screen.fill((0, 0, 0))

    # Fondo gradiente animado
    for i in range(HEIGHT):
        color = gradient_colors[(i // 150 + pygame.time.get_ticks() // 100) % len(gradient_colors)]
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

    # Pregunta
    q = questions[current_q]
    text_es = font.render("ES: " + q["es"], True, (255, 255, 255))
    text_en = font.render("EN: " + q["en"], True, (200, 255, 200))
    screen.blit(text_es, (50, 50))
    screen.blit(text_en, (50, 100))

    # Dibujar botones
    for btn in buttons:
        btn.draw(screen)

    # Dibujar partículas
    for p in particles:
        p.update()
        p.draw(screen)
    particles = [p for p in particles if p.y < HEIGHT]

    # Feedback
    if feedback:
        feedback_text = font.render(feedback, True, (255, 223, 0))
        screen.blit(feedback_text, (50, 400))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if buttons[0].is_clicked(pos):  # Responder
                feedback = "🌟 ¡Inténtalo en voz alta!"
                for _ in range(15):
                    particles.append(Particle(pos[0], pos[1], random.choice(["✨", "🎓", "📘", "😀"])))
            elif buttons[1].is_clicked(pos):  # Ver respuesta
                feedback = "✅ " + q["answer"]
            elif buttons[2].is_clicked(pos):  # Siguiente
                current_q = (current_q + 1) % len(questions)
                feedback = ""

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
