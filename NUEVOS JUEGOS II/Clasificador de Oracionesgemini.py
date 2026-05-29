import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# --- Configuración de la Pantalla ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clasificador de Oraciones")

# --- Colores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
LIGHT_GRAY = (220, 220, 220)

# --- Fuentes ---
font_title = pygame.font.Font(None, 72)
font_text = pygame.font.Font(None, 36)
font_box = pygame.font.Font(None, 48)

# --- Sonidos ---
pygame.mixer.init()
try:
    sound_correct = pygame.mixer.Sound("sounds/correct.wav")
    sound_incorrect = pygame.mixer.Sound("sounds/incorrect.wav")
except pygame.error as e:
    print(f"Error al cargar los sonidos: {e}. Asegúrate de tener los archivos 'correct.wav' e 'incorrect.wav' en la carpeta 'sounds'.")
    sound_correct = None
    sound_incorrect = None

# --- Datos del Juego: 20 Ejercicios ---
EJERCICIOS = [
    {"sentence": "El cielo es azul.", "type": "Declarativa"},
    {"sentence": "¿Qué hora es?", "type": "Interrogativa"},
    {"sentence": "¡Qué día tan hermoso!", "type": "Exclamativa"},
    {"sentence": "Por favor, cierra la puerta.", "type": "Imperativa"},
    {"sentence": "Los perros ladran fuerte.", "type": "Declarativa"},
    {"sentence": "¿Dónde está mi mochila?", "type": "Interrogativa"},
    {"sentence": "¡Cuidado con el escalón!", "type": "Exclamativa"},
    {"sentence": "Ayuda a tu hermano.", "type": "Imperativa"},
    {"sentence": "La capital de Francia es París.", "type": "Declarativa"},
    {"sentence": "¿Cuándo comienza la clase?", "type": "Interrogativa"},
    {"sentence": "¡Me encanta el helado!", "type": "Exclamativa"},
    {"sentence": "No corras por el pasillo.", "type": "Imperativa"},
    {"sentence": "Mi padre lee el periódico.", "type": "Declarativa"},
    {"sentence": "¿Cómo te llamas?", "type": "Interrogativa"},
    {"sentence": "¡Qué golazo!", "type": "Exclamativa"},
    {"sentence": "Lava tus manos.", "type": "Imperativa"},
    {"sentence": "La película empieza a las ocho.", "type": "Declarativa"},
    {"sentence": "¿Por qué lloras?", "type": "Interrogativa"},
    {"sentence": "¡Qué alegría verte!", "type": "Exclamativa"},
    {"sentence": "Prende la luz, por favor.", "type": "Imperativa"}
]

# --- Clases para la interfaz de usuario ---
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, current_color, self.rect, border_radius=10)
        text_surf = font_text.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

class Box:
    def __init__(self, text, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        text_surf = font_box.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_collision(self, item_rect):
        return self.rect.colliderect(item_rect)

# --- Clase para las Oraciones ---
class Sentence:
    def __init__(self, text, sentence_type):
        self.text = text
        self.type = sentence_type
        self.surf = font_text.render(self.text, True, BLACK)
        self.rect = self.surf.get_rect(center=(random.randint(150, SCREEN_WIDTH - 150), 50))
        self.is_dragging = False
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.surf, self.rect)
        if self.is_dragging:
            pygame.draw.rect(surface, BLUE, self.rect, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.is_dragging = True
            self.rect_offset_x = self.rect.x - event.pos[0]
            self.rect_offset_y = self.rect.y - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP and self.is_dragging:
            self.is_dragging = False
            return True # Retorna True si se suelta el mouse

    def drag(self, mouse_pos):
        if self.is_dragging:
            self.rect.x = mouse_pos[0] + self.rect_offset_x
            self.rect.y = mouse_pos[1] + self.rect_offset_y

# --- Funciones de Escenas ---
def main_menu():
    while True:
        screen.fill(LIGHT_GRAY)
        
        title_surf = font_title.render("Clasificador de Oraciones", True, BLACK)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)

        start_button = Button("Comenzar", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 70, GREEN, (0, 255, 0), game_loop)
        exit_button = Button("Salir", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100, 300, 70, RED, (255, 0, 0), sys.exit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            start_button.handle_event(event)
            exit_button.handle_event(event)

        start_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()

def game_loop():
    score = 0
    errors = 0
    
    boxes = [
        Box("Declarativa", 50, SCREEN_HEIGHT - 150, 200, 100, BLUE),
        Box("Interrogativa", 275, SCREEN_HEIGHT - 150, 200, 100, GREEN),
        Box("Exclamativa", 500, SCREEN_HEIGHT - 150, 200, 100, ORANGE),
        Box("Imperativa", 725, SCREEN_HEIGHT - 150, 200, 100, PURPLE)
    ]
    
    exercises_shuffled = EJERCICIOS.copy()
    random.shuffle(exercises_shuffled)
    
    current_sentence = None
    
    running = True
    while running:
        if not current_sentence:
            if not exercises_shuffled:
                break # No más ejercicios
            exercise = exercises_shuffled.pop(0)
            current_sentence = Sentence(exercise["sentence"], exercise["type"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if current_sentence and current_sentence.handle_event(event):
                # Se soltó el mouse
                is_correct = False
                for box in boxes:
                    if box.check_collision(current_sentence.rect):
                        if box.text == current_sentence.type:
                            score += 1
                            if sound_correct: sound_correct.play()
                            is_correct = True
                            break
                if is_correct:
                    current_sentence = None
                else:
                    errors += 1
                    if sound_incorrect: sound_incorrect.play()
                    # Regresa a la posición inicial
                    current_sentence.rect.center = (random.randint(150, SCREEN_WIDTH - 150), 50)

        # Actualizar
        if current_sentence and not current_sentence.is_dragging:
            current_sentence.update()

        # Si se arrastra la oración
        if current_sentence and current_sentence.is_dragging:
            current_sentence.drag(pygame.mouse.get_pos())
        
        # Dibujar
        screen.fill(LIGHT_GRAY)
        
        score_surf = font_text.render(f"Aciertos: {score} | Errores: {errors}", True, BLACK)
        screen.blit(score_surf, (10, 10))

        for box in boxes:
            box.draw(screen)

        if current_sentence:
            current_sentence.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    results_screen(score, errors)

def results_screen(score, errors):
    while True:
        screen.fill(LIGHT_GRAY)
        
        title_surf = font_title.render("Fin del Juego", True, BLACK)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)
        
        final_score_surf = font_text.render(f"Puntaje Final: {score}", True, BLACK)
        final_score_rect = final_score_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(final_score_surf, final_score_rect)

        errors_surf = font_text.render(f"Errores: {errors}", True, BLACK)
        errors_rect = errors_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(errors_surf, errors_rect)

        back_button = Button("Volver al Menú", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100, 300, 70, BLUE, (0, 0, 255), main_menu)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            back_button.handle_event(event)

        pygame.display.flip()

# Iniciar el juego
if __name__ == "__main__":
    main_menu()
