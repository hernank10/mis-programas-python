import pygame
import math
import sys

pygame.init()

# Configuración pantalla
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏰 Defiende la Gramática")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 200, 0)

FONT = pygame.font.SysFont("Arial", 20)

# Datos de enemigos (oraciones incorrectas)
enemigos = [
    {"texto": "Comiendo en el parque.", "tipo": "sujeto"},
    {"texto": "Los niño juega en la calle.", "tipo": "verbo"},
    {"texto": "Salió tarde, sin embargo estaba cansado.", "tipo": "conector"},
    {"texto": "Cuando llegó.", "tipo": "sujeto"},
    {"texto": "Estudia mucho, y pasa examen.", "tipo": "conector"},
]

# Clase enemigo
class Enemigo:
    def __init__(self, x, y, texto, tipo):
        self.x = x
        self.y = y
        self.texto = texto
        self.tipo = tipo
        self.health = 100
        self.speed = 1
    
    def move(self):
        self.x += self.speed  # Avanza hacia la derecha
    
    def draw(self):
        pygame.draw.rect(WIN, RED, (self.x, self.y, 80, 40))
        txt = FONT.render(self.texto, True, WHITE)
        WIN.blit(txt, (self.x + 5, self.y + 5))

# Clase torre
class Torre:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
    
    def draw(self):
        color = GREEN if self.tipo == "sujeto" else BLUE if self.tipo == "verbo" else YELLOW
        pygame.draw.circle(WIN, color, (self.x, self.y), 25)
        txt = FONT.render(self.tipo[0].upper(), True, BLACK)
        WIN.blit(txt, (self.x - 8, self.y - 10))
    
    def atacar(self, enemigos):
        for e in enemigos:
            if e.tipo == self.tipo and abs(self.x - e.x) < 120 and abs(self.y - e.y) < 100:
                e.health -= 5
                regla = FONT.render("Regla aplicada", True, BLACK)
                WIN.blit(regla, (self.x - 20, self.y - 40))

def main():
    clock = pygame.time.Clock()
    run = True
    
    # Crear enemigos en fila
    enemigos_activos = [Enemigo(0, 100 + i*80, e["texto"], e["tipo"]) for i, e in enumerate(enemigos)]
    torres = [Torre(400, 150, "sujeto"), Torre(400, 300, "verbo"), Torre(400, 450, "conector")]
    
    while run:
        clock.tick(30)
        WIN.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Dibujar y mover enemigos
        for e in enemigos_activos[:]:
            e.move()
            e.draw()
            if e.health <= 0:
                enemigos_activos.remove(e)
        
        # Dibujar y activar torres
        for t in torres:
            t.draw()
            t.atacar(enemigos_activos)
        
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
