import pygame
import sys
import random

# Inicializar pygame
pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Sustantivos - Aprende Jugando")
font = pygame.font.SysFont("Arial", 28)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Datos: Tipos de sustantivos + ejercicios
ejercicios = [
    {"oracion": "El _____ es un planeta del sistema solar.", "respuesta": "Marte", "tipo": "Propio"},
    {"oracion": "El _____ es un animal doméstico muy común.", "respuesta": "perro", "tipo": "Común"},
    {"oracion": "Me gusta leer un buen _____ antes de dormir.", "respuesta": "libro", "tipo": "Concreto"},
    {"oracion": "La _____ es necesaria para vivir.", "respuesta": "esperanza", "tipo": "Abstracto"},
    {"oracion": "El _____ se utiliza para transportar mercancías.", "respuesta": "camión", "tipo": "Concreto"},
    {"oracion": "La ciudad de _____ es la capital de Francia.", "respuesta": "París", "tipo": "Propio"},
    {"oracion": "El _____ del salón explicó la lección.", "respuesta": "profesor", "tipo": "Común"},
    {"oracion": "La _____ es un valor muy importante.", "respuesta": "honestidad", "tipo": "Abstracto"},
]

# Variables de juego
input_text = ""
score = 0
index = 0
feedback = ""
running = True

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Bucle principal
while running:
    screen.fill(WHITE)

    # Mostrar enunciado
    if index < len(ejercicios):
        ejercicio = ejercicios[index]
        draw_text(f"Oración: {ejercicio['oracion']}", 50, 100)
        draw_text(f"Tipo de sustantivo esperado: {ejercicio['tipo']}", 50, 150)
        draw_text("Tu respuesta: " + input_text, 50, 250)
    else:
        draw_text("¡Has completado todos los ejercicios!", 200, 200, BLUE)
        draw_text(f"Puntaje final: {score}/{len(ejercicios)}", 200, 300, GREEN)

    # Feedback
    draw_text(feedback, 50, 350, RED if "Incorrecto" in feedback else GREEN)

    # Puntaje
    draw_text(f"Puntaje: {score}", 700, 20, BLUE)

    pygame.display.flip()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter
                if index < len(ejercicios):
                    if input_text.strip().lower() == ejercicios[index]["respuesta"].lower():
                        feedback = "¡Correcto!"
                        score += 1
                    else:
                        feedback = f"Incorrecto. Era: {ejercicios[index]['respuesta']}"
                    index += 1
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

pygame.quit()
sys.exit()
