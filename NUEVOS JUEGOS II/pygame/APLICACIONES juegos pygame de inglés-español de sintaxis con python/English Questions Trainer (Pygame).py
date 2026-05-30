import pygame
import random
import sys

# === Inicialización ===
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Questions Trainer (Pygame)")

# === Colores ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (178, 34, 34)
BLUE = (70, 130, 180)
BROWN = (139, 69, 19)

# === Fuente ===
font = pygame.font.SysFont("Arial", 28)

# === Banco de ejercicios (ejemplo reducido) ===
exercises = [
    {"spanish": "¿Cómo te llamas?", "english": ["What is your name?", "What's your name?"]},
    {"spanish": "¿Dónde vives?", "english": ["Where do you live?"]},
    {"spanish": "¿Qué hora es?", "english": ["What time is it?"]},
]

# === Variables de juego ===
score = 0
current = None
user_text = ""
message = "Presiona [N] para nuevo ejercicio / Press [N] for new exercise"

# === Funciones ===
def new_exercise():
    global current, user_text, message
    current = random.choice(exercises)
    user_text = ""
    message = f"Traduce al inglés: {current['spanish']}"

def check_answer():
    global score, message
    if not current:
        return
    if user_text.strip() in current["english"]:
        score += 1
        message = "✅ Correcto / Correct!"
    else:
        correct = " | ".join(current["english"])
        message = f"❌ Incorrecto. Respuesta: {correct}"

# === Bucle principal ===
running = True
while running:
    screen.fill((240, 230, 200))  # Fondo color arena

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Escribir en el cuadro de texto
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter → comprobar
                check_answer()
            elif event.key == pygame.K_n:  # N → nuevo ejercicio
                new_exercise()
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    # Mostrar puntaje
    score_label = font.render(f"Puntaje / Score: {score}", True, GREEN)
    screen.blit(score_label, (20, 20))

    # Mostrar mensaje / pregunta
    question_label = font.render(message, True, BROWN)
    screen.blit(question_label, (20, 100))

    # Caja de texto
    pygame.draw.rect(screen, WHITE, (20, 200, 760, 40))
    input_surface = font.render(user_text, True, BLACK)
    screen.blit(input_surface, (30, 205))

    # Instrucciones
    instr = font.render("Escribe y presiona [Enter] / Write and press [Enter]", True, BLUE)
    screen.blit(instr, (20, 300))

    instr2 = font.render("Presiona [N] para nuevo ejercicio", True, BLUE)
    screen.blit(instr2, (20, 340))

    pygame.display.flip()

pygame.quit()
sys.exit()
