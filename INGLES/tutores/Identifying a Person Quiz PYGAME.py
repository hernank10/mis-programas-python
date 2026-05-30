import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Identifying a Person Quiz")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

# Fuente
font = pygame.font.SysFont("arial", 28)

# Preguntas y respuestas
questions = [
    {
        "question": "Is she María?",
        "options": ["Yes, she is.", "No, she aren’t.", "Yes, he is."],
        "answer": "Yes, she is."
    },
    {
        "question": "Is he a teacher?",
        "options": ["Yes, she is.", "Yes, he is.", "No, they aren’t."],
        "answer": "Yes, he is."
    },
    {
        "question": "Are they doctors?",
        "options": ["Yes, they are.", "No, he isn’t.", "Yes, she is."],
        "answer": "Yes, they are."
    },
    {
        "question": "Is she your sister?",
        "options": ["Yes, she is.", "No, she isn’t.", "Yes, they are."],
        "answer": "Yes, she is."
    },
    {
        "question": "Is he Colombian?",
        "options": ["Yes, he is.", "No, she isn’t.", "Yes, it is."],
        "answer": "Yes, he is."
    }
]

# Variables del juego
score = 0
question_index = 0
game_over = False

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def show_question():
    global question_index
    q = questions[question_index]
    draw_text(f"Q: {q['question']}", 50, 50, BLUE)

    for i, option in enumerate(q["options"]):
        pygame.draw.rect(screen, GREEN if not game_over else RED, (50, 150 + i*100, 700, 60))
        draw_text(option, 60, 160 + i*100, WHITE)

def check_answer(pos):
    global score, question_index, game_over
    q = questions[question_index]
    for i, option in enumerate(q["options"]):
        rect = pygame.Rect(50, 150 + i*100, 700, 60)
        if rect.collidepoint(pos):
            if option == q["answer"]:
                score += 1
            question_index += 1
            if question_index >= len(questions):
                game_over = True
            break

def show_game_over():
    draw_text("Game Over!", 300, 200, RED)
    draw_text(f"Final Score: {score}/{len(questions)}", 300, 300, BLUE)

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    if not game_over:
        show_question()
        draw_text(f"Score: {score}", 650, 20, BLACK)
    else:
        show_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            check_answer(event.pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
