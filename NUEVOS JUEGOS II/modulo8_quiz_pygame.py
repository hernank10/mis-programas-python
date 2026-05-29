# modulo8_quiz_pygame.py
import pygame
import random
import sys

pygame.init()

# --- Configuración de pantalla ---
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Módulo 8 - Quiz Bilingüe")

# --- Colores ---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
RUBI = (224, 17, 95)
AZUL = (0, 120, 255)

# --- Fuentes ---
fuente = pygame.font.SysFont("arial", 32, bold=True)

# --- Banco de preguntas ---
preguntas = [
    {"en": "I am happy", "es": "Yo estoy feliz"},
    {"en": "She is my friend", "es": "Ella es mi amiga"},
    {"en": "We are students", "es": "Nosotros somos estudiantes"},
    {"en": "They play soccer", "es": "Ellos juegan fútbol"},
    {"en": "You are reading", "es": "Tú estás leyendo"}
]

# --- Sistema de partículas (estrellas) ---
class Particula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = random.randint(2, 5)
        self.color = random.choice([(255, 255, 0), (255, 200, 50), (255, 255, 200)])
        self.vel_y = random.uniform(1, 3)

    def mover(self):
        self.y += self.vel_y

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), self.radio)

# --- Botón interactivo ---
class Boton:
    def __init__(self, texto, x, y, w, h, color):
        self.texto = texto
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect, border_radius=12)
        texto_render = fuente.render(self.texto, True, BLANCO)
        superficie.blit(texto_render, (self.rect.x + 20, self.rect.y + 10))

    def es_click(self, pos):
        return self.rect.collidepoint(pos)

# --- Juego principal ---
def juego():
    puntaje = 0
    particulas = []
    reloj = pygame.time.Clock()
    pregunta_actual = None
    botones = []

    def nueva_pregunta():
        nonlocal pregunta_actual, botones
        pregunta_actual = random.choice(preguntas)
        opciones = [pregunta_actual["es"]]
        while len(opciones) < 3:
            distractor = random.choice(preguntas)["es"]
            if distractor not in opciones:
                opciones.append(distractor)
        random.shuffle(opciones)

        botones = []
        y = 300
        for op in opciones:
            btn = Boton(op, 200, y, 400, 60, RUBI)
            botones.append(btn)
            y += 80

    nueva_pregunta()

    en_juego = True
    while en_juego:
        pantalla.fill((30, 30, 60))  # fondo oscuro azul

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_juego = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for btn in botones:
                    if btn.es_click(pos):
                        if btn.texto == pregunta_actual["es"]:
                            puntaje += 1
                            for _ in range(20):  # generar partículas
                                particulas.append(Particula(*pos))
                            nueva_pregunta()
                        else:
                            # Feedback visual rojo
                            btn.color = ROJO

        # Dibujar pregunta
        texto_preg = fuente.render(f"Traduce al español: {pregunta_actual['en']}", True, BLANCO)
        pantalla.blit(texto_preg, (100, 150))

        # Dibujar botones
        for btn in botones:
            btn.dibujar(pantalla)

        # Dibujar puntaje
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, AZUL)
        pantalla.blit(texto_puntaje, (20, 20))

        # Dibujar partículas
        for p in particulas[:]:
            p.mover()
            p.dibujar(pantalla)
            if p.y > ALTO:
                particulas.remove(p)

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    juego()
