import pygame
import random
import sys

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Who's That? – Interrogative Quiz")
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (220, 220, 220)

# Preguntas
questions = [
    {
        "pista": "¿Es él un maestro?",
        "options": ["Is he a teacher?", "Is she a teacher?", "Are they teachers?"],
        "correct": "Is he a teacher?"
    },
    {
        "pista": "¿Son ellos tus amigos?",
        "options": ["Are they your friends?", "Is he your friend?", "Is she your friend?"],
        "correct": "Are they your friends?"
    },
    {
        "pista": "¿Es ella una esperanza para la familia?",
        "options": ["Is she a hope for the family?", "Is she a hero?", "Is she a sister?"],
        "correct": "Is she a hope for the family?"
    },
    {
        "pista": "¿Es ella tu hermana?",
        "options": ["Is she your sister?", "Is he your sister?", "Are they your sisters?"],
        "correct": "Is she your sister?"
    }
]

score = 0
current_question = random.choice(questions)

def draw_text(text, x, y, color=BLACK):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 10, rect.y + 10)

def next_question():
    global current_question
    current_question = random.choice(questions)

def main():
    global score
    running = True
    selected = None

    while running:
        screen.fill(WHITE)
        draw_text("🎯 Pista:", 50, 50)
        draw_text(current_question["pista"], 150, 50)

        buttons = []
        for i, option in enumerate(current_question["options"]):
            rect = pygame.Rect(100, 150 + i * 100, 600, 60)
            draw_button(option, rect, GRAY)
            buttons.append((rect, option))

        draw_text(f"Puntuación: {score}", 600, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, option in buttons:
                    if rect.collidepoint(event.pos):
                        if option == current_question["correct"]:
                            score += 10
                        else:
                            score -= 5
                        next_question()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
