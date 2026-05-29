# modulo9_aventura.py
import pygame
import sys
import random

pygame.init()

# --- Configuración ---
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Módulo 9 - Aventura gramatical")

# --- Colores ---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 150, 255)
ROJO = (220, 50, 50)
VERDE = (50, 200, 100)
MORADO = (180, 50, 220)

# --- Fuente ---
fuente = pygame.font.SysFont("arial", 28, bold=True)

# --- Personaje ---
jugador = pygame.Rect(100, 100, 40, 40)
velocidad = 5

# --- Objeto interactivo (Libro 📘) ---
libro = pygame.Rect(400, 300, 40, 40)

# --- Banco de preguntas ---
preguntas = [
    {"en": "I am happy", "opciones": ["Yo estoy feliz", "Tú eres feliz", "Ella está feliz"], "respuesta": "Yo estoy feliz"},
    {"en": "She is my friend", "opciones": ["Ella es mi amiga", "Ella es feliz", "Ella juega fútbol"], "respuesta": "Ella es mi amiga"},
    {"en": "We are students", "opciones": ["Nosotros somos estudiantes", "Nosotros estamos en casa", "Ellos son estudiantes"], "respuesta": "Nosotros somos estudiantes"}
]

# --- Sistema de partículas (✨) ---
particulas = []
def crear_particulas(x, y):
    for _ in range(20):
        particulas.append([x, y, random.randint(2, 5), random.choice([AZUL, MORADO, VERDE]), random.uniform(-2, 2), random.uniform(-2, 2)])

def dibujar_particulas():
    for p in particulas[:]:
        pygame.draw.circle(pantalla, p[3], (int(p[0]), int(p[1])), p[2])
        p[0] += p[4]
        p[1] += p[5]
        p[2] -= 0.05
        if p[2] <= 0:
            particulas.remove(p)

# --- Estado ---
en_quiz = False
pregunta_actual = None
botones = []
mensaje_feedback = ""

# --- Botón ---
class Boton:
    def __init__(self, texto, x, y, w, h, color):
        self.texto = texto
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect, border_radius=12)
        render = fuente.render(self.texto, True, BLANCO)
        superficie.blit(render, (self.rect.x + 10, self.rect.y + 10))

    def es_click(self, pos):
        return self.rect.collidepoint(pos)

# --- Nueva pregunta ---
def nueva_pregunta():
    global pregunta_actual, botones, mensaje_feedback
    mensaje_feedback = ""
    pregunta_actual = random.choice(preguntas)
    opciones = pregunta_actual["opciones"][:]
    random.shuffle(opciones)
    botones = []
    y = 300
    for op in opciones:
        botones.append(Boton(op, 200, y, 400, 50, MORADO))
        y += 70

# --- Bucle principal ---
clock = pygame.time.Clock()
puntaje = 0

while True:
    pantalla.fill((30, 30, 60))  # fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if en_quiz:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for btn in botones:
                    if btn.es_click(pos):
                        if btn.texto == pregunta_actual["respuesta"]:
                            puntaje += 1
                            mensaje_feedback = "✅ ¡Correcto!"
                            crear_particulas(ANCHO//2, ALTO//2)
                            nueva_pregunta()
                        else:
                            mensaje_feedback = "❌ Incorrecto"
                            btn.color = ROJO
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    keys = pygame.key.get_pressed()
    if not en_quiz:
        if keys[pygame.K_LEFT]:
            jugador.x -= velocidad
        if keys[pygame.K_RIGHT]:
            jugador.x += velocidad
        if keys[pygame.K_UP]:
            jugador.y -= velocidad
        if keys[pygame.K_DOWN]:
            jugador.y += velocidad

    # Colisión con el libro 📘
    if jugador.colliderect(libro) and not en_quiz:
        en_quiz = True
        nueva_pregunta()

    # Dibujar mapa
    pygame.draw.rect(pantalla, VERDE, jugador)  # jugador
    pygame.draw.rect(pantalla, AZUL, libro)     # libro

    # Dibujar quiz
    if en_quiz:
        pygame.draw.rect(pantalla, (0, 0, 0, 128), (100, 100, 600, 400), border_radius=20)
        pregunta_render = fuente.render(f"Traduce: {pregunta_actual['en']}", True, BLANCO)
        pantalla.blit(pregunta_render, (150, 150))
        for btn in botones:
            btn.dibujar(pantalla)
        if mensaje_feedback:
            feedback_render = fuente.render(mensaje_feedback, True, BLANCO)
            pantalla.blit(feedback_render, (300, 500))

    # Dibujar puntaje
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto_puntaje, (20, 20))

    # Dibujar partículas
    dibujar_particulas()

    pygame.display.flip()
    clock.tick(30)
