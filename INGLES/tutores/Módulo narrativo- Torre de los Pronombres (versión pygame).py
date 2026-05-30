import pygame
import sys
import random

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La Torre de los Pronombres")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Colores
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GRAY, GREEN, RED = (200, 200, 200), (0, 180, 0), (180, 0, 0)

# Datos de personajes
personajes = [
    {
        "nombre": "Sir He",
        "descripcion": "Un caballero con capa azul y espada dorada.",
        "pista": "Es un doctor.",
        "respuesta_correcta": "Is he a doctor?",
        "opciones": ["Is he a doctor?", "Is she a doctor?", "Are they doctors?"]
    },
    {
        "nombre": "Lady She",
        "descripcion": "Una reina con corona de plata.",
        "pista": "Es una profesora.",
        "respuesta_correcta": "Is she a teacher?",
        "opciones": ["Is he a teacher?", "Is she a teacher?", "Are they teachers?"]
    },
    {
        "nombre": "The Twins",
        "descripcion": "Dos figuras idénticas con túnicas verdes.",
        "pista": "Son músicos.",
        "respuesta_correcta": "Are they musicians?",
        "opciones": ["Is he a musician?", "Is she a musician?", "Are they musicians?"]
    }
]

# Estadísticas
puntaje = 0
actual = 0

def draw_text(text, x, y, color=BLACK):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 10, rect.y + 10)

def mostrar_pregunta(personaje):
    screen.fill(WHITE)
    draw_text(f"🧙 {personaje['nombre']}", 50, 40)
    draw_text(personaje["descripcion"], 50, 80)
    draw_text(f"🎯 Pista: {personaje['pista']}", 50, 120)
    draw_text(f"Puntaje: {puntaje}", 600, 20)

    botones = []
    for i, opcion in enumerate(personaje["opciones"]):
        rect = pygame.Rect(100, 200 + i * 100, 600, 60)
        draw_button(opcion, rect, GRAY)
        botones.append((rect, opcion))
    return botones

def mostrar_feedback(correcto, personaje):
    screen.fill(GREEN if correcto else RED)
    mensaje = "✅ ¡Correcto!" if correcto else "❌ Incorrecto"
    draw_text(mensaje, 300, 250, WHITE)
    draw_text(f"Regla: {personaje['respuesta_correcta']}", 200, 300, WHITE)
    pygame.display.flip()
    pygame.time.delay(1500)

def juego():
    global puntaje, actual
    running = True
    while running and actual < len(personajes):
        personaje = personajes[actual]
        botones = mostrar_pregunta(personaje)
        pygame.display.flip()

        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, opcion in botones:
                        if rect.collidepoint(event.pos):
                            correcto = opcion == personaje["respuesta_correcta"]
                            puntaje += 10 if correcto else -5
                            mostrar_feedback(correcto, personaje)
                            actual += 1
                            esperando = False
        clock.tick(30)

    # Pantalla final
    screen.fill(WHITE)
    draw_text("🎉 Misión completada", 250, 200)
    draw_text(f"🏆 Puntaje final: {puntaje}", 250, 250)
    draw_text("Presiona cualquier tecla para salir", 250, 300)
    pygame.display.flip()
    esperar_tecla()

def esperar_tecla():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

# Ejecutar juego
if __name__ == "__main__":
    juego()
