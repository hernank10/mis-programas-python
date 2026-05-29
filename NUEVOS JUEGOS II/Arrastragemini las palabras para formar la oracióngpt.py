import pygame
import random
import sys

pygame.init()

# Pantalla
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle de la Oración")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fuente
font = pygame.font.SysFont("arial", 28)

# Sonidos
success_sound = pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.get_init() and pygame.mixer.Sound(file=None)))
fail_sound = pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.get_init() and pygame.mixer.Sound(file=None)))

# Oraciones precargadas (20)
sentences = [
    "El perro duerme en la sala",
    "María estudia para el examen",
    "Los niños juegan en el parque",
    "Juan y Ana cantan una canción",
    "El sol brilla con intensidad",
    "Pedro corre mientras llueve",
    "El profesor explica la lección",
    "Carmen escribe una carta",
    "El río crece porque llueve mucho",
    "Laura cocina y su hermano lava los platos",
    "El avión aterriza suavemente",
    "El poeta escribe versos hermosos",
    "El mar se agita cuando hay tormenta",
    "Los estudiantes aprenden porque estudian",
    "Marcos pinta y luego descansa",
    "La luna ilumina la noche",
    "El coche se detuvo porque se dañó",
    "La maestra sonríe y los alumnos aplauden",
    "El viento sopla con fuerza",
    "El gato duerme pero el perro ladra"
]

# Barajar palabras
def shuffle_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    return words

# Clase para las fichas de palabras
class WordTile:
    def __init__(self, text, x, y):
        self.text = text
        self.image = font.render(text, True, BLACK, GRAY)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dragging = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Juego principal
def main():
    score = 0
    sentence_index = 0

    running = True
    selected_tile = None
    offset_x, offset_y = 0, 0

    # Primera oración
    current_sentence = sentences[sentence_index]
    shuffled_words = shuffle_sentence(current_sentence)

    tiles = [WordTile(word, 50 + i*120, HEIGHT//2) for i, word in enumerate(shuffled_words)]

    while running:
        screen.fill(WHITE)

        # Mostrar puntuación y oración objetivo
        score_text = font.render(f"Puntuación: {score}", True, BLACK)
        screen.blit(score_text, (20, 20))

        instr_text = font.render("Arrastra las palabras para formar la oración", True, BLACK)
        screen.blit(instr_text, (20, 60))

        # Dibujar fichas
        for tile in tiles:
            tile.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for tile in tiles:
                    if tile.rect.collidepoint(event.pos):
                        tile.dragging = True
                        selected_tile = tile
                        offset_x = tile.rect.x - event.pos[0]
                        offset_y = tile.rect.y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_tile:
                    selected_tile.dragging = False
                    selected_tile = None

                    # Verificar respuesta
                    formed_sentence = " ".join([t.text for t in sorted(tiles, key=lambda t: t.rect.x)])
                    if formed_sentence == current_sentence:
                        score += 1
                        print("✅ Correcto!")
                        #success_sound.play()
                        sentence_index += 1
                        if sentence_index < len(sentences):
                            current_sentence = sentences[sentence_index]
                            shuffled_words = shuffle_sentence(current_sentence)
                            tiles = [WordTile(word, 50 + i*120, HEIGHT//2) for i, word in enumerate(shuffled_words)]
                        else:
                            print("🎉 ¡Completaste todas las oraciones!")
                            running = False
                    else:
                        print("❌ Incorrecto")
                        #fail_sound.play()

            elif event.type == pygame.MOUSEMOTION:
                if selected_tile and selected_tile.dragging:
                    selected_tile.rect.x = event.pos[0] + offset_x
                    selected_tile.rect.y = event.pos[1] + offset_y

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
