import pygame
import sys
import random

# ------------------------
# Datos de ejemplo (puedes cargar 100)
# ------------------------
ejercicios = [
    {"es": "Oración copulativa: Une ideas con nexos como 'y' o 'e'.",
     "en": "Copulative sentence: It links ideas with connectors like 'and' or 'e'."},
    {"es": "Oración adversativa: Expresa oposición o contraste.",
     "en": "Adversative sentence: It expresses opposition or contrast."},
    {"es": "Oración causal: Explica la causa de algo.",
     "en": "Causal sentence: It explains the cause of something."},
    {"es": "Oración condicional: Expresa una condición.",
     "en": "Conditional sentence: It expresses a condition."},
    {"es": "Oración concesiva: Expresa una dificultad sin impedir la acción.",
     "en": "Concessive sentence: It expresses a difficulty without preventing the action."},
]

# ------------------------
# Inicializar pygame
# ------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aprender Oraciones Compuestas - Pygame")

# Fuente
FONT = pygame.font.SysFont("Arial", 26)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 120, 200)

# ------------------------
# Variables de estado
# ------------------------
modo = "menu"  # "menu", "estudio", "juego"
texto_input = ""
mensaje = ""
puntaje = 0
indice = 0
ejercicio_actual = random.choice(ejercicios)

# ------------------------
# Funciones auxiliares
# ------------------------
def draw_text(surface, text, x, y, color=BLACK):
    label = FONT.render(text, True, color)
    surface.blit(label, (x, y))

def mostrar_menu():
    screen.fill(WHITE)
    draw_text(screen, "Selecciona un modo:", 300, 150, BLUE)
    draw_text(screen, "1. Modo Estudio (sin puntaje)", 220, 250)
    draw_text(screen, "2. Modo Gamificado (con puntaje)", 220, 300)
    draw_text(screen, "Presiona ESC para salir", 220, 400)

def mostrar_ejercicio():
    screen.fill(WHITE)
    draw_text(screen, "Traduce al inglés:", 50, 50, BLUE)
    draw_text(screen, ejercicio_actual["es"], 50, 100, BLACK)

    pygame.draw.rect(screen, GRAY, (50, 200, 700, 40))
    draw_text(screen, texto_input, 60, 205, BLACK)

    draw_text(screen, mensaje, 50, 300, BLUE)

    if modo == "juego":
        draw_text(screen, f"Puntaje: {puntaje}", 600, 50, BLACK)

    draw_text(screen, "ENTER: Comprobar | N: Siguiente | ESC: Salir", 50, 500, BLACK)

# ------------------------
# Bucle principal
# ------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if modo == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    modo = "estudio"
                    texto_input = ""
                    mensaje = ""
                elif event.key == pygame.K_2:
                    modo = "juego"
                    puntaje = 0
                    texto_input = ""
                    mensaje = ""
                elif event.key == pygame.K_ESCAPE:
                    running = False

        else:  # modo estudio o juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if texto_input.strip().lower() == ejercicio_actual["en"].lower():
                        mensaje = "✅ Correcto!"
                        if modo == "juego":
                            puntaje += 1
                    else:
                        mensaje = f"❌ Incorrecto. Respuesta: {ejercicio_actual['en']}"
                elif event.key == pygame.K_BACKSPACE:
                    texto_input = texto_input[:-1]
                elif event.key == pygame.K_n:  # siguiente
                    ejercicio_actual = random.choice(ejercicios)
                    texto_input = ""
                    mensaje = ""
                elif event.key == pygame.K_ESCAPE:
                    modo = "menu"
                else:
                    texto_input += event.unicode

    if modo == "menu":
        mostrar_menu()
    else:
        mostrar_ejercicio()

    pygame.display.flip()

pygame.quit()
sys.exit()
