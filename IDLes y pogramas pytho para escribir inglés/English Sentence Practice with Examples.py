import pygame
import sys
import random

pygame.init()

# Pantalla
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Sentence Practice with Examples")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 100, 255)
GREEN = (0, 180, 0)
RED = (200, 0, 0)

# Fuente
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 36)

# Lista de retos: (palabra, ejemplo)
challenges = [
    ("school", "I go to school every day."),
    ("friend", "My friend is very kind."),
    ("book", "I am reading a book."),
    ("music", "She likes classical music."),
    ("computer", "He is using a computer."),
    ("because", "I stayed home because it was raining."),
    ("and", "I like coffee and tea."),
    ("but", "I wanted to go, but I was tired."),
    ("dog", "The dog is barking loudly."),
    ("sun", "The sun is shining in the sky."),
    # ... agregar hasta 50 retos
]

random.shuffle(challenges)

# Variables del juego
current_challenge = 0
user_text = ""
score = 0
modo_gamificado = True  # True = puntaje, False = solo práctica

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    if current_challenge < len(challenges):
        palabra, ejemplo = challenges[current_challenge]

        draw_text(f"Challenge {current_challenge+1}/{len(challenges)}", 50, 20, BLUE)
        draw_text(f"Word to use: '{palabra}'", 50, 70)
        draw_text(f"Example: {ejemplo}", 50, 120)

        # Entrada de usuario
        pygame.draw.rect(screen, GRAY, (50, 200, 800, 50))
        draw_text("Your sentence: " + user_text, 60, 210)

        # Puntaje
        draw_text(f"Score: {score}", 700, 20, BLUE)
    else:
        draw_text("🎉 Finished all challenges!", 250, 250, BLUE)
        draw_text(f"Final Score: {score}/{len(challenges)}", 300, 300, GREEN)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if current_challenge < len(challenges):
                    # Validación básica si estamos en modo gamificado
                    if modo_gamificado:
                        palabras = user_text.strip().split()
                        if len(palabras) >= 3 and palabra.lower() in user_text.lower():
                            score += 1
                    current_challenge += 1
                    user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
