import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# --- Configuración de la Pantalla ---
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cazador de Verbos")

# --- Colores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (150, 150, 150)
LIGHT_BLUE = (173, 216, 230)

# --- Fuentes ---
font_title = pygame.font.Font(None, 72)
font_text = pygame.font.Font(None, 48)
font_score = pygame.font.Font(None, 60)

# --- Sonidos ---
pygame.mixer.init()
try:
    sound_correct = pygame.mixer.Sound("sounds/correct.wav")
    sound_incorrect = pygame.mixer.Sound("sounds/incorrect.wav")
except pygame.error as e:
    print(f"Error al cargar los sonidos: {e}")
    sound_correct = None
    sound_incorrect = None

# --- Datos del Juego: 20 Ejercicios ---
EJERCICIOS = [
    {"sentence": "Los niños juegan en el parque.", "verbs": ["juegan"]},
    {"sentence": "Mi hermana cocina un pastel delicioso.", "verbs": ["cocina"]},
    {"sentence": "El sol sale por la mañana.", "verbs": ["sale"]},
    {"sentence": "Yo leo un libro cada noche.", "verbs": ["leo"]},
    {"sentence": "El gato persigue al ratón velozmente.", "verbs": ["persigue"]},
    {"sentence": "Ellos viajaron a la playa el verano pasado.", "verbs": ["viajaron"]},
    {"sentence": "La computadora se apagó de repente.", "verbs": ["apagó"]},
    {"sentence": "Las flores crecen en el jardín.", "verbs": ["crecen"]},
    {"sentence": "Tú escribes una carta a tu abuela.", "verbs": ["escribes"]},
    {"sentence": "El perro duerme tranquilamente en su cama.", "verbs": ["duerme"]},
    {"sentence": "El avión voló sobre las nubes.", "verbs": ["voló"]},
    {"sentence": "Nosotros aprendemos un nuevo idioma.", "verbs": ["aprendemos"]},
    {"sentence": "Ellas bailan en la fiesta.", "verbs": ["bailan"]},
    {"sentence": "El chef prepara una cena especial.", "verbs": ["prepara"]},
    {"sentence": "Los estudiantes estudian para el examen.", "verbs": ["estudian"]},
    {"sentence": "El río fluye hacia el mar.", "verbs": ["fluye"]},
    {"sentence": "El cartero entrega las cartas.", "verbs": ["entrega"]},
    {"sentence": "Yo bebo un vaso de agua.", "verbs": ["bebo"]},
    {"sentence": "El niño corre muy rápido.", "verbs": ["corre"]},
    {"sentence": "Los músicos tocan sus instrumentos.", "verbs": ["tocan"]}
]

# --- Clase para las Palabras ---
class Word:
    def __init__(self, text, x, y, speed, is_verb):
        self.text = text
        self.surf = font_text.render(self.text, True, BLACK)
        self.rect = self.surf.get_rect(center=(x, y))
        self.speed = speed
        self.is_verb = is_verb
        self.is_caught = False

    def update(self):
        self.rect.x -= self.speed

    def draw(self, surface):
        if not self.is_caught:
            surface.blit(self.surf, self.rect)

# --- Funciones de Escenas ---
def main_menu():
    while True:
        screen.fill(LIGHT_BLUE)
        
        # Título
        title_surf = font_title.render("Cazador de Verbos", True, BLACK)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)

        # Botón de inicio
        start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 70)
        pygame.draw.rect(screen, GREEN, start_button_rect, border_radius=15)
        start_text = font_text.render("Comenzar", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button_rect.center)
        screen.blit(start_text, start_text_rect)

        # Eventos del menú
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game_loop()

        pygame.display.flip()

def game_loop():
    score = 0
    total_verbs_caught = 0
    total_verbs_possible = 0
    
    current_exercise_index = 0
    
    running = True
    while running and current_exercise_index < len(EJERCICIOS):
        exercise = EJERCICIOS[current_exercise_index]
        words_data = exercise["sentence"].split()
        verbs_in_sentence = exercise["verbs"]
        
        words = []
        x_pos = SCREEN_WIDTH
        
        for word_text in words_data:
            is_verb = word_text.lower() in verbs_in_sentence
            words.append(Word(word_text, x_pos, SCREEN_HEIGHT // 2, random.randint(1, 3), is_verb))
            x_pos += font_text.size(word_text)[0] + 50
        
        total_verbs_possible += len(verbs_in_sentence)
        
        sentence_running = True
        while sentence_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sentence_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for word in words:
                        if word.rect.collidepoint(event.pos) and not word.is_caught:
                            if word.is_verb:
                                word.is_caught = True
                                score += 1
                                total_verbs_caught += 1
                                if sound_correct:
                                    sound_correct.play()
                            else:
                                score -= 1
                                if sound_incorrect:
                                    sound_incorrect.play()

            screen.fill(LIGHT_BLUE)
            
            # Actualizar y dibujar las palabras
            active_words = [word for word in words if not word.is_caught and word.rect.right > 0]
            
            for word in active_words:
                word.update()
                word.draw(screen)

            # Mostrar el puntaje
            score_text = font_text.render(f"Puntaje: {score}", True, BLACK)
            screen.blit(score_text, (20, 20))
            
            # Verificar si la oración ha terminado
            if not active_words:
                sentence_running = False

            pygame.display.flip()
            pygame.time.Clock().tick(60)
            
        current_exercise_index += 1
        pygame.time.wait(2000) # Pausa de 2 segundos entre oraciones

    # Pantalla de resultados
    results_screen(score, total_verbs_caught, total_verbs_possible)

def results_screen(score, caught, possible):
    while True:
        screen.fill(LIGHT_BLUE)
        
        # Título de resultados
        title_surf = font_score.render("Resultados", True, BLACK)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surf, title_rect)
        
        # Puntaje final
        score_surf = font_text.render(f"Puntaje final: {score}", True, BLACK)
        score_rect = score_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(score_surf, score_rect)
        
        # Resumen de verbos
        summary_surf = font_text.render(f"Verbos cazados: {caught} de {possible}", True, BLACK)
        summary_rect = summary_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(summary_surf, summary_rect)

        # Botón para volver al menú
        back_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100, 300, 70)
        pygame.draw.rect(screen, GRAY, back_button_rect, border_radius=15)
        back_text = font_text.render("Volver al Menú", True, WHITE)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)

        # Eventos de la pantalla de resultados
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    main_menu()

        pygame.display.flip()

# Iniciar el juego
if __name__ == "__main__":
    main_menu()
