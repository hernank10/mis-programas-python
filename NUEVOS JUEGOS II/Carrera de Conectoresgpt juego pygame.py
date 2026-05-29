import pygame
import random
import sys

pygame.init()

# Configuración pantalla
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏁 Carrera de Conectores")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (50, 100, 200)

# Fuente
FONT = pygame.font.SysFont("Arial", 28)

# Datos de ejercicios
ejercicios = [
    {"texto": "No salió a jugar ___ estaba lloviendo.", "correcto": "porque", "opciones": ["porque", "pero"]},
    {"texto": "Estudia mucho ___ quiere aprobar el examen.", "correcto": "ya que", "opciones": ["ya que", "sin embargo"]},
    {"texto": "Llegó tarde ___ el tráfico estaba pesado.", "correcto": "porque", "opciones": ["porque", "aunque"]},
    {"texto": "Le gusta leer ___ no tiene mucho tiempo.", "correcto": "pero", "opciones": ["pero", "por lo tanto"]},
    {"texto": "Está cansado ___ no durmió bien.", "correcto": "porque", "opciones": ["porque", "sin embargo"]},
]

# Jugador
player = pygame.Rect(350, 500, 40, 40)
player_speed = 5
score = 0
exercise_index = 0
clock = pygame.time.Clock()

def draw_game(ejercicio, opcion1, opcion2):
    WIN.fill(WHITE)
    
    # Dibujar texto
    text = FONT.render(ejercicio, True, BLACK)
    WIN.blit(text, (50, 50))
    
    # Opciones en bifurcación
    pygame.draw.rect(WIN, BLUE, (150, 300, 200, 100))
    pygame.draw.rect(WIN, BLUE, (450, 300, 200, 100))
    
    text1 = FONT.render(opcion1, True, WHITE)
    text2 = FONT.render(opcion2, True, WHITE)
    
    WIN.blit(text1, (200, 340))
    WIN.blit(text2, (500, 340))
    
    # Dibujar jugador
    pygame.draw.rect(WIN, RED, player)
    
    # Dibujar puntaje
    score_text = FONT.render(f"Puntaje: {score}", True, BLACK)
    WIN.blit(score_text, (600, 20))
    
    pygame.display.update()

def main():
    global exercise_index, score, player_speed
    
    run = True
    while run:
        clock.tick(30)
        ejercicio = ejercicios[exercise_index]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            if ejercicio["opciones"][0] == ejercicio["correcto"]:
                score += 10
                player_speed += 2
            else:
                score -= 5
                player_speed = max(3, player_speed - 1)
            exercise_index = (exercise_index + 1) % len(ejercicios)
        
        if keys[pygame.K_RIGHT]:
            if ejercicio["opciones"][1] == ejercicio["correcto"]:
                score += 10
                player_speed += 2
            else:
                score -= 5
                player_speed = max(3, player_speed - 1)
            exercise_index = (exercise_index + 1) % len(ejercicios)
        
        # Movimiento automático del jugador
        player.y -= player_speed
        if player.y < 100:
            player.y = 500  # reinicia posición para siguiente ronda
        
        draw_game(ejercicio["texto"], ejercicio["opciones"][0], ejercicio["opciones"][1])
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
