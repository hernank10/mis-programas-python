import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Sentence Practice")

# Fuentes y colores
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BLUE = (0, 100, 255)

# Lista de retos
challenges = [
    "Write a sentence with the word 'school'.",
    "Write a sentence with the word 'friend'.",
    "Write a sentence with the word 'book'.",
    "Write a sentence with the word 'music'.",
    "Write a sentence with the word 'computer'."
]

challenge_index = 0
user_input = ""
feedback = ""
score = 0

def check_sentence(sentence, keyword):
    """Valida que la oración sea correcta según reglas básicas"""
    if not sentence:
        return False, "The sentence is empty."
    if not sentence[0].isupper():
        return False, "The sentence must start with a capital letter."
    if not sentence.endswith("."):
        return False, "The sentence must end with a period."
    if keyword.lower() not in sentence.lower():
        return False, f"The sentence must include the word '{keyword}'."
    return True, "Correct!"

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    win.fill(WHITE)

    # Mostrar reto
    challenge = challenges[challenge_index]
    keyword = challenge.split("'")[1]  # palabra obligatoria
    text = big_font.render(challenge, True, BLUE)
    win.blit(text, (50, 50))

    # Mostrar lo que el usuario escribe
    input_text = font.render("Your sentence: " + user_input, True, BLACK)
    win.blit(input_text, (50, 150))

    # Mostrar retroalimentación
    feedback_text = font.render(feedback, True, GREEN if "Correct" in feedback else RED)
    win.blit(feedback_text, (50, 220))

    # Mostrar puntaje
    score_text = font.render(f"Score: {score}", True, BLACK)
    win.blit(score_text, (650, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Verificar respuesta
                correct, message = check_sentence(user_input.strip(), keyword)
                feedback = message
                if correct:
                    score += 1
                    challenge_index = (challenge_index + 1) % len(challenges)
                user_input = ""

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
