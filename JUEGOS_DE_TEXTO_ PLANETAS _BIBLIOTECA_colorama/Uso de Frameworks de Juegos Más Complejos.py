import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Texto con Pygame")
font = pygame.font.Font(None, 36)
text = font.render("Bienvenido a la aventura!", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (200, 300))
    pygame.display.flip()
