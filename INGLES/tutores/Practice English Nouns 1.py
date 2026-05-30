import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Practice English Nouns")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (100, 149, 237)
ROJO = (220, 20, 60)

# Fuente
fuente = pygame.font.SysFont("arial", 28)

# Ejercicios: (oración, respuesta correcta)
ejercicios = [
    ("The _____ is barking loudly. (dog/cat/car)", "dog"),
    ("I bought a new _____. (book/apple/sky)", "book"),
    ("The _____ is shining in the sky. (sun/tree/pen)", "sun"),
    ("My _____ is very kind. (teacher/door/shoe)", "teacher"),
    ("We saw a big _____ in the forest. (elephant/desk/ball)", "elephant"),
    ("He put the milk in the _____. (fridge/car/bird)", "fridge"),
    ("I like to play the _____. (guitar/banana/table)", "guitar"),
    ("The _____ is full of stars. (sky/cat/book)", "sky"),
    ("She has a red _____. (dress/ball/house)", "dress"),
    ("The _____ is flying in the sky. (bird/pen/door)", "bird"),
]

random.shuffle(ejercicios)

# Variables de juego
indice = 0
respuesta_usuario = ""
puntaje = 0
mostrar_resultado = False

# Bucle principal
clock = pygame.time.Clock()
ejecutando = True
while ejecutando:
    pantalla.fill(BLANCO)

    # Mostrar puntaje
    texto_puntaje = fuente.render(f"Score: {puntaje}", True, AZUL)
    pantalla.blit(texto_puntaje, (10, 10))

    if indice < len(ejercicios):
        oracion, respuesta_correcta = ejercicios[indice]

        # Mostrar oración
        texto_oracion = fuente.render(oracion, True, NEGRO)
        pantalla.blit(texto_oracion, (50, 150))

        # Mostrar lo que escribe el usuario
        texto_input = fuente.render("Your answer: " + respuesta_usuario, True, ROJO)
        pantalla.blit(texto_input, (50, 250))

        if mostrar_resultado:
            if respuesta_usuario.lower() == respuesta_correcta.lower():
                texto_feedback = fuente.render("✅ Correct!", True, (0, 180, 0))
            else:
                texto_feedback = fuente.render(f"❌ Wrong! Correct answer: {respuesta_correcta}", True, (200, 0, 0))
            pantalla.blit(texto_feedback, (50, 350))
    else:
        # Fin del juego
        texto_final = fuente.render(f"Game Over! Final Score: {puntaje}/{len(ejercicios)}", True, AZUL)
        pantalla.blit(texto_final, (150, 250))

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if indice < len(ejercicios):
                    if respuesta_usuario.lower() == respuesta_correcta.lower():
                        puntaje += 1
                    mostrar_resultado = True
                    pygame.time.delay(1000)
                    indice += 1
                    respuesta_usuario = ""
                    mostrar_resultado = False
            elif evento.key == pygame.K_BACKSPACE:
                respuesta_usuario = respuesta_usuario[:-1]
            else:
                respuesta_usuario += evento.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
