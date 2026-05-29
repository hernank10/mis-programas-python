import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Colores inspirados en la naturaleza
GREEN = (34, 139, 34)   # Bosque
BLUE = (70, 130, 180)   # Cielo
BROWN = (139, 69, 19)   # Tierra
YELLOW = (255, 215, 0)  # Sol
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)

# Configuración pantalla
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Bilingüe: Oraciones Condicionales")

# Fuente
font = pygame.font.SysFont("arial", 28)

# Ejercicios condicionales (simplificado)
exercises = [
    {"q": "If it rains, we ___ at home. (First conditional)", 
     "options": ["stay", "stayed", "would stay", "had stayed"], 
     "a": "stay", "emoji": "😀"},
    {"q": "Si llueve, nosotros ___ en casa. (Primer condicional)", 
     "options": ["quedamos", "quedaremos", "quedábamos", "hubiéramos quedado"], 
     "a": "quedaremos", "emoji": "😀"},
    {"q": "If I were you, I ___ more. (Second conditional)", 
     "options": ["study", "studied", "would study", "had studied"], 
     "a": "would study", "emoji": "🤔"},
    {"q": "Si yo fuera tú, ___ más. (Segundo condicional)", 
     "options": ["estudio", "estudiaría", "estudié", "hubiera estudiado"], 
     "a": "estudiaría", "emoji": "🤔"},
]

# Estado del juego
current_exercise = 0
feedback = ""
score = 0

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def draw_button(text, x, y, w, h, color, option):
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=12)
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + 10, y + 10))
    return pygame.Rect(x, y, w, h), option

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    # Obtener ejercicio actual
    exercise = exercises[current_exercise]
    draw_text(f"Pregunta {current_exercise+1}/{len(exercises)}", 50, 30, BLUE)
    draw_text(exercise["q"], 50, 80, BROWN)

    # Dibujar botones de opciones
    buttons = []
    y_offset = 150
    colors = [GREEN, BLUE, YELLOW, BROWN]
    for i, opt in enumerate(exercise["options"]):
        rect, option = draw_button(opt, 100, y_offset, 300, 50, colors[i % len(colors)], opt)
        buttons.append((rect, option))
        y_offset += 70

    # Mostrar retroalimentación
    if feedback:
        draw_text(feedback, 500, 200, RED if "Incorrecto" in feedback else GREEN)

    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for rect, option in buttons:
                if rect.collidepoint(mouse_pos):
                    if option == exercise["a"]:
                        feedback = f"✔ Correcto {exercise['emoji']}"
                        score += 1
                    else:
                        feedback = f"❌ Incorrecto {exercise['emoji']}"
                    pygame.time.delay(800)
                    current_exercise = (current_exercise + 1) % len(exercises)
                    feedback = ""

    # Mostrar puntaje
    draw_text(f"Puntaje: {score}", 700, 30, BLACK)

    pygame.display.flip()

pygame.quit()
sys.exit()
