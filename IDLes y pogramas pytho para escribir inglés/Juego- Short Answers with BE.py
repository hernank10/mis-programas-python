import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego: Short Answers with BE")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (200, 200, 200)

# Fuente
font = pygame.font.SysFont("Arial", 32)

# Preguntas y respuestas (affirmative / negative)
questions = [
    ("Is she a teacher?", "Yes, she is.", "No, she isn’t."),
    ("Are they brothers?", "Yes, they are.", "No, they aren’t."),
    ("Is it a dog?", "Yes, it is.", "No, it isn’t."),
    ("Am I late?", "Yes, you are.", "No, you aren’t."),
    ("Are we friends?", "Yes, we are.", "No, we aren’t."),
    ("Is he at school?", "Yes, he is.", "No, he isn’t.")
]

# Escoger pregunta actual
def new_question():
    q, yes, no = random.choice(questions)
    correct = random.choice([yes, no])  # aleatoriamente la correcta
    return q, yes, no, correct

question, yes_ans, no_ans, correct_ans = new_question()
score = 0

# Función para dibujar botones
def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + 10, y + 10))

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    # Mostrar pregunta
    question_text = font.render(question, True, BLACK)
    screen.blit(question_text, (50, 50))

    # Botones de respuesta
    draw_button(yes_ans, 150, 200, 500, 50, GRAY)
    draw_button(no_ans, 150, 300, 500, 50, GRAY)

    # Mostrar puntaje
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (50, 400))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Si elige YES
            if 150 <= x <= 650 and 200 <= y <= 250:
                if yes_ans == correct_ans:
                    score += 1
                else:
                    score -= 1
                question, yes_ans, no_ans, correct_ans = new_question()

            # Si elige NO
            if 150 <= x <= 650 and 300 <= y <= 350:
                if no_ans == correct_ans:
                    score += 1
                else:
                    score -= 1
                question, yes_ans, no_ans, correct_ans = new_question()

    pygame.display.update()
