import pygame
import random
import sys
import time

# ------------------------
# Datos de oraciones
# ------------------------
pares = [
    ("El gato duerme en el sillón.", "Simple"),
    ("María lee un libro y Juan escucha música.", "Coordinada copulativa"),
    ("No fui al cine porque estaba cansado.", "Subordinada causal"),
    ("Llegamos temprano, pero la tienda estaba cerrada.", "Coordinada adversativa"),
    ("El sol brilla intensamente.", "Simple"),
    ("Si estudias, aprobarás.", "Subordinada condicional"),
    ("Pedro canta mientras su hermano toca la guitarra.", "Coordinada distributiva"),
    ("Llueve mucho; los niños no salen a jugar.", "Yuxtapuesta"),
    ("Ana escribe cartas a su abuela.", "Simple"),
    ("Aunque estaba cansado, siguió trabajando.", "Subordinada concesiva"),
]

# Crear cartas (duplicadas como oraciones y clasificaciones)
cartas = []
for oracion, tipo in pares:
    cartas.append(("Oración", oracion))
    cartas.append(("Clasificación", tipo))

# ------------------------
# Configuración pygame
# ------------------------
pygame.init()
ANCHO, ALTO = 1000, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🃏 Memotest Sintáctico 🧠")

FUENTE = pygame.font.SysFont("arial", 20, bold=True)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (100, 149, 237)
VERDE = (50, 205, 50)
ROJO = (220, 20, 60)
GRIS = (200, 200, 200)

# Barajar cartas
random.shuffle(cartas)

# ------------------------
# Parámetros de cartas
# ------------------------
COLS, FILAS = 5, 4  # 20 cartas
CARD_W, CARD_H = 180, 100
ESPACIO = 20
offset_x = (ANCHO - (COLS * (CARD_W + ESPACIO))) // 2
offset_y = 80

# Estado de las cartas
rects = []
descubiertas = [False] * len(cartas)
seleccionadas = []
pares_encontrados = 0

# Crear rectángulos para las cartas
for fila in range(FILAS):
    for col in range(COLS):
        x = offset_x + col * (CARD_W + ESPACIO)
        y = offset_y + fila * (CARD_H + ESPACIO)
        rects.append(pygame.Rect(x, y, CARD_W, CARD_H))

# ------------------------
# Función para dibujar
# ------------------------
def dibujar():
    pantalla.fill((240, 248, 255))
    titulo = FUENTE.render("🃏 Memotest Sintáctico - Encuentra pares oración + clasificación", True, NEGRO)
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 20))

    for i, rect in enumerate(rects):
        if descubiertas[i] or i in seleccionadas:
            # Mostrar texto de la carta
            pygame.draw.rect(pantalla, VERDE, rect, border_radius=10)
            texto = FUENTE.render(cartas[i][1], True, NEGRO)
            pantalla.blit(texto, (rect.x + 10, rect.y + rect.height//2 - 10))
        else:
            # Carta oculta
            pygame.draw.rect(pantalla, AZUL, rect, border_radius=10)
            signo = FUENTE.render("❓", True, BLANCO)
            pantalla.blit(signo, (rect.centerx - 10, rect.centery - 10))

    pygame.display.flip()

# ------------------------
# Bucle principal
# ------------------------
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    dibujar()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos = pygame.mouse.get_pos()
            for i, rect in enumerate(rects):
                if rect.collidepoint(pos) and i not in seleccionadas and not descubiertas[i]:
                    seleccionadas.append(i)
                    if len(seleccionadas) == 2:
                        # Esperar un poco para mostrar ambas
                        dibujar()
                        pygame.time.delay(1000)

                        i1, i2 = seleccionadas
                        c1, c2 = cartas[i1], cartas[i2]

                        # Verificar par válido
                        if c1[0] != c2[0] and (
                            c1[1] == c2[1] or (c1[0] == "Oración" and c2[0] == "Clasificación") or (c2[0] == "Oración" and c1[0] == "Clasificación")
                        ):
                            descubiertas[i1] = True
                            descubiertas[i2] = True
                            pares_encontrados += 1
                        seleccionadas = []

    # Verificar fin de juego
    if pares_encontrados == len(pares):
        pantalla.fill(BLANCO)
        msg = FUENTE.render("🎉 ¡Felicidades! Has encontrado todos los pares. 🧠", True, ROJO)
        pantalla.blit(msg, (ANCHO//2 - msg.get_width()//2, ALTO//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        ejecutando = False

    reloj.tick(30)
