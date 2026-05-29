# juego_entonces_pygame.py
import pygame
import random
import sys

pygame.init()

# ---------------- CONFIGURACIÓN ----------------
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
BLUE = (50, 100, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego: Practicar 'entonces'")

font = pygame.font.SysFont("Arial", 24)

# ---------------- 20 EJEMPLOS ----------------
EXAMPLES = [
    {"spanish": "Terminé de leer el libro; entonces me fui a dormir.",
     "english": "I finished reading the book; then I went to sleep.",
     "category": "temporal"},
    {"spanish": "Se hizo de noche; entonces encendieron las luces.",
     "english": "It got dark; then they turned on the lights.",
     "category": "temporal"},
    {"spanish": "Estaba enfermo; entonces no salió de casa.",
     "english": "He was sick; then he didn’t leave home.",
     "category": "temporal"},
    {"spanish": "El tren se retrasó; entonces perdimos la conexión.",
     "english": "The train was late; then we missed the connection.",
     "category": "temporal"},
    {"spanish": "Salimos del cine; entonces empezó a llover.",
     "english": "We left the cinema; then it started to rain.",
     "category": "temporal"},
    {"spanish": "No apagaste el horno; entonces la comida se quemó.",
     "english": "You didn’t turn off the oven; so the food got burnt.",
     "category": "consecuencial"},
    {"spanish": "No llegó el autobús; entonces tuvimos que caminar.",
     "english": "The bus didn’t come; so we had to walk.",
     "category": "consecuencial"},
    {"spanish": "Estaba cansado; entonces no quiso salir.",
     "english": "He was tired; so he didn’t want to go out.",
     "category": "consecuencial"},
    {"spanish": "Olvidaste la llave; entonces no pudimos entrar.",
     "english": "You forgot the key; so we couldn’t get in.",
     "category": "consecuencial"},
    {"spanish": "No estudió; entonces reprobó el examen.",
     "english": "He didn’t study; so he failed the exam.",
     "category": "consecuencial"},
    {"spanish": "Entonces… ¿qué opinas de esta idea?",
     "english": "So… what do you think of this idea?",
     "category": "discursivo"},
    {"spanish": "Entonces, como decía, la reunión será mañana.",
     "english": "So, as I was saying, the meeting will be tomorrow.",
     "category": "discursivo"},
    {"spanish": "Entonces, sigamos con el siguiente punto.",
     "english": "So, let’s move on to the next point.",
     "category": "discursivo"},
    {"spanish": "Entonces, ¿quieres venir con nosotros?",
     "english": "So, do you want to come with us?",
     "category": "discursivo"},
    {"spanish": "Entonces, ¿qué hacemos ahora?",
     "english": "So, what do we do now?",
     "category": "discursivo"},
    {"spanish": "Se cansó mucho; entonces decidió descansar.",
     "english": "He got very tired; then he decided to rest.",
     "category": "temporal"},
    {"spanish": "Me quedé sin dinero; entonces pedí ayuda.",
     "english": "I ran out of money; so I asked for help.",
     "category": "consecuencial"},
    {"spanish": "Perdimos el mapa; entonces nos perdimos.",
     "english": "We lost the map; so we got lost.",
     "category": "consecuencial"},
    {"spanish": "Estaba lloviendo; entonces cogí un paraguas.",
     "english": "It was raining; then I took an umbrella.",
     "category": "temporal"},
    {"spanish": "Entonces, volvamos al tema principal.",
     "english": "So, let’s get back to the main topic.",
     "category": "discursivo"}
]

# ---------------- VARIABLES ----------------
score = 0
current_example = random.choice(EXAMPLES)
user_text = ""
feedback = ""

# ---------------- FUNCIONES ----------------
def draw_text(surface, text, x, y, color=BLACK):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        label = font.render(line, True, color)
        surface.blit(label, (x, y + i * 30))

def new_question():
    global current_example, user_text, feedback
    current_example = random.choice(EXAMPLES)
    user_text = ""
    feedback = ""

# ---------------- LOOP PRINCIPAL ----------------
running = True
while running:
    screen.fill(WHITE)

    # Mostrar la frase en español
    draw_text(screen, f"Traduce al inglés:", 50, 50)
    draw_text(screen, current_example["spanish"], 50, 100, BLUE)

    # Mostrar entrada del usuario
    pygame.draw.rect(screen, (220, 220, 220), (50, 200, 700, 40))
    draw_text(screen, user_text, 60, 210)

    # Mostrar retroalimentación
    draw_text(screen, feedback, 50, 300, GREEN if "✅" in feedback else RED)

    # Mostrar puntaje
    draw_text(screen, f"Puntaje: {score}", 600, 20, BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_text.strip().lower() == current_example["english"].lower():
                    feedback = "✅ ¡Correcto!"
                    score += 1
                else:
                    feedback = f"❌ Incorrecto. Respuesta: {current_example['english']}"
                new_question()
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()

pygame.quit()
sys.exit()
