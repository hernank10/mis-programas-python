import pygame
import random
import sys
import time

# Inicialización
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Who's That? – Interrogative Challenge")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Colores
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GREEN, RED, GRAY, ORANGE = (0, 200, 0), (200, 0, 0), (220, 220, 220), (255, 165, 0)

# Sonidos
correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")

# Logros
achievements = {
    "Pronoun Prodigy": False,
    "Role Master": False,
    "Abstract Ace": False
}

# Preguntas por nivel
questions_by_level = {
    1: [
        {"pista": "¿Es él un doctor?", "options": ["Is he a doctor?", "Is she a doctor?", "Are they doctors?"], "correct": "Is he a doctor?"},
        {"pista": "¿Es ella una profesora?", "options": ["Is she a teacher?", "Is he a teacher?", "Are they teachers?"], "correct": "Is she a teacher?"}
    ],
    2: [
        {"pista": "¿Es ella tu hermana?", "options": ["Is she your sister?", "Is he your sister?", "Are they your sisters?"], "correct": "Is she your sister?"},
        {"pista": "¿Son ellos colombianos?", "options": ["Are they Colombian?", "Is she Colombian?", "Is he Colombian?"], "correct": "Are they Colombian?"}
    ],
    3: [
        {"pista": "¿Es ella una esperanza para la familia?", "options": ["Is she a hope for the family?", "Is she a hero?", "Is she a sister?"], "correct": "Is she a hope for the family?"},
        {"pista": "¿Es él un desarrollador de software?", "options": ["Is he a software developer?", "Is she a software developer?", "Are they developers?"], "correct": "Is he a software developer?"}
    ]
}

# Estadísticas
stats = {"respondidas": 0, "aciertos": 0, "errores": 0, "puntaje": 0}

# Funciones auxiliares
def draw_text(text, x, y, color=BLACK):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 10, rect.y + 10)

def show_rules():
    screen.fill(WHITE)
    draw_text("📘 Reglas del juego", 50, 50)
    draw_text("Usa preguntas interrogativas para identificar personas:", 50, 100)
    draw_text("Ej: Is he a teacher? / Are they doctors? / Is she your sister?", 50, 140)
    draw_text("Presiona cualquier tecla para volver al menú.", 50, 200)
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

def show_feedback(correct):
    color = GREEN if correct else RED
    sound = correct_sound if correct else wrong_sound
    sound.play()
    screen.fill(color)
    draw_text("✅ Correcto!" if correct else "❌ Incorrecto!", 300, 250, WHITE)
    pygame.display.flip()
    pygame.time.delay(1000)

def check_achievement(level, aciertos, tiempo_promedio):
    if level == 1 and aciertos == 2:
        achievements["Pronoun Prodigy"] = True
    elif level == 2 and aciertos >= 2:
        achievements["Role Master"] = True
    elif level == 3 and tiempo_promedio <= 8:
        achievements["Abstract Ace"] = True

def show_stats():
    screen.fill(WHITE)
    draw_text("📊 Estadísticas finales", 50, 50)
    draw_text(f"Preguntas respondidas: {stats['respondidas']}", 50, 100)
    draw_text(f"Aciertos: {stats['aciertos']}", 50, 140)
    draw_text(f"Errores: {stats['errores']}", 50, 180)
    draw_text(f"Puntaje total: {stats['puntaje']}", 50, 220)
    draw_text("🏆 Logros desbloqueados:", 50, 280)
    y = 320
    for logro, estado in achievements.items():
        if estado:
            draw_text(f"✔ {logro}", 70, y, ORANGE)
            y += 40
    draw_text("Presiona cualquier tecla para salir.", 50, y + 20)
    pygame.display.flip()
    wait_for_key()

def play_level(level, tiempo_limite):
    preguntas = questions_by_level[level]
    aciertos = 0
    tiempos = []

    for pregunta in preguntas:
        start_time = time.time()
        screen.fill(WHITE)
        draw_text(f"🎯 Pista: {pregunta['pista']}", 50, 50)
        buttons = []
        for i, option in enumerate(pregunta["options"]):
            rect = pygame.Rect(100, 150 + i * 100, 600, 60)
            draw_button(option, rect, GRAY)
            buttons.append((rect, option))
        pygame.display.flip()

        answered = False
        while not answered and time.time() - start_time < tiempo_limite:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, option in buttons:
                        if rect.collidepoint(event.pos):
                            tiempo = time.time() - start_time
                            tiempos.append(tiempo)
                            stats["respondidas"] += 1
                            if option == pregunta["correct"]:
                                stats["aciertos"] += 1
                                stats["puntaje"] += 10
                                aciertos += 1
                                show_feedback(True)
                            else:
                                stats["errores"] += 1
                                stats["puntaje"] -= 5
                                show_feedback(False)
                            answered = True
        if not answered:
            stats["errores"] += 1
            stats["puntaje"] -= 5
            show_feedback(False)

    tiempo_promedio = sum(tiempos) / len(tiempos) if tiempos else 99
    check_achievement(level, aciertos, tiempo_promedio)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("🎮 Who’s That? – Interrogative Challenge", 150, 50)
        draw_text("1. Jugar", 150, 150)
        draw_text("2. Reglas", 150, 200)
        draw_text("3. Salir", 150, 250)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_level(1, 15)
                    play_level(2, 12)
                    play_level(3, 8)
                    show_stats()
                elif event.key == pygame.K_2:
                    show_rules()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

# Ejecutar juego
if __name__ == "__main__":
    main_menu()
