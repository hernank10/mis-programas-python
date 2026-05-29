import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# --- Configuración de la Pantalla ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Constructor de Frases")

# --- Colores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (50, 50, 50)

# --- Fuentes ---
font_title = pygame.font.Font(None, 72)
font_text = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

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
    {"sentence": "El perro persigue al gato."},
    {"sentence": "Mi mamá cocina un pastel."},
    {"sentence": "El sol calienta la tierra."},
    {"sentence": "Los niños juegan en el parque."},
    {"sentence": "Ella lee un libro cada noche."},
    {"sentence": "Nosotros vivimos en una ciudad grande."},
    {"sentence": "La luna brilla en la noche."},
    {"sentence": "Ellos compran frutas en el mercado."},
    {"sentence": "El profesor explica la lección."},
    {"sentence": "Yo escribo una carta a mi amigo."},
    {"sentence": "El tren llega a la estación."},
    {"sentence": "La flor crece en el jardín."},
    {"sentence": "El avión vuela sobre las montañas."},
    {"sentence": "El coche corre muy rápido."},
    {"sentence": "Las estrellas brillan en el cielo."},
    {"sentence": "Tú comes una manzana roja."},
    {"sentence": "La computadora tiene un virus."},
    {"sentence": "El estudiante estudia para su examen."},
    {"sentence": "Mi abuela prepara la cena."},
    {"sentence": "El agua fluye por el río."}
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

class WordButton:
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, font_text.size(text)[0] + 20, 50)
        self.is_used = False

    def draw(self, surface):
        if not self.is_used:
            pygame.draw.rect(surface, DARK_GRAY, self.rect, border_radius=10)
            text_surf = font_text.render(self.text, True, WHITE)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    def handle_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and not self.is_used:
            self.is_used = True
            return self.text
        return None

# --- Funciones de Escenas ---
def main_menu():
    while True:
        screen.fill(LIGHT_GRAY)

        title_surf = font_title.render("Constructor de Frases", True, BLACK)
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
    exercise_index = 0
    
    selected_words = []
    
    def load_exercise():
        nonlocal selected_words, exercise_index
        if exercise_index >= len(EJERCICIOS):
            return False
        
        sentence_text = EJERCICIOS[exercise_index]["sentence"]
        words_list = sentence_text.split()
        random.shuffle(words_list)
        
        selected_words = []
        word_buttons = []
        x_start = (SCREEN_WIDTH - (len(words_list) * 150)) // 2 # Ajustar para centrar
        
        for i, word in enumerate(words_list):
            word_buttons.append(WordButton(word, x_start + i * 150, SCREEN_HEIGHT - 150))
        
        return word_buttons
        
    word_buttons = load_exercise()
    if not word_buttons:
        results_screen(score)
        
    def verify_answer():
        nonlocal score, exercise_index, word_buttons
        
        correct_sentence = EJERCICIOS[exercise_index]["sentence"]
        user_sentence = " ".join(selected_words)
        
        if user_sentence == correct_sentence:
            score += 1
            if sound_correct:
                sound_correct.play()
            
            # Pasar al siguiente ejercicio
            exercise_index += 1
            word_buttons = load_exercise()
            
            if not word_buttons:
                return "finish"
            
            return "correct"
        else:
            if sound_incorrect:
                sound_incorrect.play()
            selected_words.clear()
            for button in word_buttons:
                button.is_used = False
            return "incorrect"
            
    def reset_words():
        nonlocal selected_words
        selected_words.clear()
        for button in word_buttons:
            button.is_used = False
            
    # Botones de control
    verify_button = Button("Verificar", SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 50, 150, 60, GREEN, (0, 255, 0), verify_answer)
    reset_button = Button("Reiniciar", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50, 150, 60, RED, (255, 0, 0), reset_words)
    
    running = True
    while running:
        if word_buttons is False: # El juego ha terminado
            running = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Comprobar si se hizo clic en una palabra
                for button in word_buttons:
                    clicked_word = button.handle_click(event.pos)
                    if clicked_word:
                        selected_words.append(clicked_word)
                        break
                
                # Comprobar si se hizo clic en un botón de control
                verify_button.handle_event(event)
                reset_button.handle_event(event)
        
        screen.fill(LIGHT_GRAY)
        
        # Área de construcción de la oración
        pygame.draw.rect(screen, WHITE, (50, 100, SCREEN_WIDTH - 100, 100), border_radius=15)
        
        # Mostrar las palabras seleccionadas
        x_pos_word = 60
        for word in selected_words:
            word_surf = font_text.render(word, True, BLACK)
            screen.blit(word_surf, (x_pos_word, 135))
            x_pos_word += word_surf.get_width() + 10
            
        # Dibujar las palabras desordenadas
        for button in word_buttons:
            button.draw(screen)

        # Dibujar botones de control
        verify_button.draw(screen)
        reset_button.draw(screen)
        
        # Mostrar el puntaje
        score_surf = font_text.render(f"Puntaje: {score}", True, BLACK)
        screen.blit(score_surf, (10, 10))
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    results_screen(score)

def results_screen(score):
    while True:
        screen.fill(LIGHT_GRAY)

        title_surf = font_title.render("Fin del Juego", True, BLACK)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)

        final_score_surf = font_text.render(f"Puntaje final: {score} de {len(EJERCICIOS)}", True, BLACK)
        final_score_rect = final_score_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(final_score_surf, final_score_rect)
        
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
