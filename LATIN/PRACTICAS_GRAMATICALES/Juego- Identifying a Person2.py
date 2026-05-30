import pygame
import random
import sys

pygame.init()

# --- Colores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)

# --- Ventana ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego: Identifying a Person")

# --- Fuentes ---
font_big = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 28)

# --- Preguntas por nivel ---
questions = {
    1: [
        ("Is she María?", "yes"),
        ("Is he a teacher?", "yes"),
        ("Is she Pedro?", "no"),
    ],
    2: [
        ("Is he Colombian?", "yes"),
        ("Is she your sister?", "no"),
        ("Is he Mexican?", "no"),
    ],
    3: [
        ("Are they doctors?", "yes"),
        ("Is she your mother?", "yes"),
        ("Is he Juan?", "no"),
    ]
}

# --- Variables de juego ---
level = 1
score = 0
current_question = None
game_state = "menu"  # menu, reglas, juego, fin


def draw_text(text, font, color, x, y, center=True):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)


def show_menu():
    screen.fill(WHITE)
    draw_text("Juego: Identifying a Person", font_big, BLUE, WIDTH//2, 100)
    draw_text("1. Jugar", font_small, BLACK, WIDTH//2, 250)
    draw_text("2. Reglas", font_small, BLACK, WIDTH//2, 300)
    draw_text("3. Salir", font_small, BLACK, WIDTH//2, 350)


def show_rules():
    screen.fill(WHITE)
    draw_text("Reglas del juego:", font_big, BLUE, WIDTH//2, 60)
    reglas = [
        "1. Responde preguntas de identificación (nombre, profesión, nacionalidad).",
        "2. Usa 'yes' o 'no' según corresponda.",
        "3. Ganas 10 puntos si aciertas, pierdes 5 si fallas.",
        "4. Avanza de nivel con 3 respuestas correctas.",
    ]
    y = 150
    for r in reglas:
        draw_text(r, font_small, BLACK, 50, y, center=False)
        y += 50
    draw_text("Presiona [ESC] para volver", font_small, RED, WIDTH//2, 500)


def get_question():
    return random.choice(questions[level])


def show_game():
    global current_question
    screen.fill(WHITE)
    if not current_question:
        current_question = get_question()
    draw_text(f"Nivel: {level}", font_small, BLACK, 100, 40, center=False)
    draw_text(f"Puntaje: {score}", font_small, BLACK, 600, 40, center=False)
    draw_text("Pregunta:", font_small, BLUE, WIDTH//2, 200)
    draw_text(current_question[0], font_big, BLACK, WIDTH//2, 300)
    draw_text("Responde: Y = Yes   N = No", font_small, GREEN, WIDTH//2, 450)


def show_end():
    screen.fill(WHITE)
    draw_text("¡Juego terminado!", font_big, BLUE, WIDTH//2, 150)
    draw_text(f"Puntaje final: {score}", font_small, BLACK, WIDTH//2, 250)
    draw_text("Presiona ESC para salir", font_small, RED, WIDTH//2, 400)


# --- Bucle principal ---
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- Teclas ---
        if event.type == pygame.KEYDOWN:
            if game_state == "menu":
                if event.key == pygame.K_1:
                    game_state = "juego"
                elif event.key == pygame.K_2:
                    game_state = "reglas"
                elif event.key == pygame.K_3:
                    running = False

            elif game_state == "reglas":
                if event.key == pygame.K_ESCAPE:
                    game_state = "menu"

            elif game_state == "juego":
                if event.key == pygame.K_y:
                    if current_question[1] == "yes":
                        score += 10
                        level = min(3, level + 1)
                    else:
                        score -= 5
                    current_question = None
                elif event.key == pygame.K_n:
                    if current_question[1] == "no":
                        score += 10
                        level = min(3, level + 1)
                    else:
                        score -= 5
                    current_question = None

            elif game_state == "fin":
                if event.key == pygame.K_ESCAPE:
                    running = False

    # --- Mostrar pantallas ---
    if game_state == "menu":
        show_menu()
    elif game_state == "reglas":
        show_rules()
    elif game_state == "juego":
        show_game()
    elif game_state == "fin":
        show_end()

    pygame.display.flip()

pygame.quit()
sys.exit()
