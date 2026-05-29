import pygame
import sys
import json
import os
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego 'Entonces' y Equivalentes")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
LIGHT_GRAY = (200, 200, 200)
GREEN = (0, 150, 0)
RED = (200, 0, 0)

# Fuentes
font = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Archivo de datos
FILE_NAME = "ejemplos_entonces.json"

EJEMPLOS = [
    {
        "id": 1,
        "es": "Si no hay pan, entonces compremos galletas.",
        "en": "If there's no bread, then let's buy cookies.",
        "fr": "S'il n'y a pas de pain, alors achetons des biscuits."
    },
    {
        "id": 2,
        "es": "Él era muy feliz entonces.",
        "en": "He was very happy then.",
        "fr": "Il était très heureux alors."
    },
    {
        "id": 3,
        "es": "Ya que llegas tarde, entonces no te esperaré.",
        "en": "Since you're late, then I won't wait for you.",
        "fr": "Puisque tu es en retard, alors je ne t'attendrai pas."
    },
    {
        "id": 4,
        "es": "Si es de día, entonces hay sol.",
        "en": "If it's daytime, then there is sun.",
        "fr": "S'il fait jour, alors il y a du soleil."
    },
    {
        "id": 5,
        "es": "No estudié, por lo tanto, fallé el examen.",
        "en": "I didn't study, therefore, I failed the exam.",
        "fr": "Je n'ai pas étudié, par conséquent, j'ai échoué à l'examen."
    },
    {
        "id": 6,
        "es": "Había una vez un rey. Entonces, el dragón llegó.",
        "en": "Once upon a time there was a king. Then, the dragon arrived.",
        "fr": "Il était une fois un roi. Alors, le dragon arriva."
    },
    {
        "id": 7,
        "es": "Si la puerta está abierta, entonces entra.",
        "en": "If the door is open, then come in.",
        "fr": "Si la porte est ouverte, alors entre."
    },
    {
        "id": 8,
        "es": "Me gradué en el 2010. En aquel entonces, no había smartphones.",
        "en": "I graduated in 2010. Back then, there were no smartphones.",
        "fr": "J'ai obtenu mon diplôme en 2010. À cette époque, il n'y avait pas de smartphones."
    },
    {
        "id": 9,
        "es": "No tengo dinero, así que no puedo ir.",
        "en": "I have no money, so I can't go.",
        "fr": "Je n'ai pas d'argent, donc je ne peux pas y aller."
    },
    {
        "id": 10,
        "es": "Si te duele, entonces ve al médico.",
        "en": "If it hurts, then go to the doctor.",
        "fr": "Si tu as mal, alors va chez le médecin."
    },
    {
        "id": 11,
        "es": "Éramos niños, entonces la vida era simple.",
        "en": "We were children, then life was simple.",
        "fr": "Nous étions des enfants, alors la vie était simple."
    },
    {
        "id": 12,
        "es": "Si el tráfico es denso, entonces llegaremos tarde.",
        "en": "If the traffic is heavy, then we will be late.",
        "fr": "Si la circulation est dense, alors nous serons en retard."
    },
    {
        "id": 13,
        "es": "El motor falló, por lo tanto, el avión aterrizó de emergencia.",
        "en": "The engine failed, therefore, the plane made an emergency landing.",
        "fr": "Le moteur est tombé en panne, par conséquent, l'avion a atterri en urgence."
    },
    {
        "id": 14,
        "es": "Si el tren no llega, entonces buscaré un taxi.",
        "en": "If the train doesn't arrive, then I'll look for a taxi.",
        "fr": "Si le train n'arrive pas, alors je chercherai un taxi."
    },
    {
        "id": 15,
        "es": "Ya que no contestas, entonces asumo que estás de acuerdo.",
        "en": "Since you don't answer, then I assume you agree.",
        "fr": "Puisque tu ne réponds pas, alors je suppose que tu es d'accord."
    },
    {
        "id": 16,
        "es": "La primera vez que te vi, entonces me enamoré.",
        "en": "The first time I saw you, then I fell in love.",
        "fr": "La première fois que je t'ai vue, alors je suis tombé amoureux."
    },
    {
        "id": 17,
        "es": "Él era solo un niño, en ese entonces.",
        "en": "He was just a child, at that time.",
        "fr": "Il n'était qu'un enfant, à ce moment-là."
    },
    {
        "id": 18,
        "es": "Si necesitas ayuda, entonces llama.",
        "en": "If you need help, then call.",
        "fr": "Si tu as besoin d'aide, alors appelle."
    },
    {
        "id": 19,
        "es": "Está lloviendo, por consiguiente, el partido se cancela.",
        "en": "It's raining, consequently, the game is canceled.",
        "fr": "Il pleut, par conséquent, le match est annulé."
    },
    {
        "id": 20,
        "es": "Él llegó, y entonces todos se callaron.",
        "en": "He arrived, and then everyone went silent.",
        "fr": "Il est arrivé, et alors tout le monde s'est tu."
    }
]

# Funciones de utilidad para manejar datos
def cargar_ejemplos():
    """Carga los ejemplos desde un archivo JSON o usa los ejemplos iniciales."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Guarda los ejemplos iniciales si el archivo no existe
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(EJEMPLOS, f, indent=4, ensure_ascii=False)
        return EJEMPLOS

# Cargar los ejemplos al inicio
ejemplos_data = cargar_ejemplos()

# --- Clases para la interfaz gráfica ---
class Button:
    def __init__(self, text, x, y, width, height, color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
                return True
        return False

class TextInput:
    def __init__(self, x, y, width, height, placeholder="", text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text_color = BLACK
        self.text = text
        self.placeholder = placeholder
        self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        
        if self.active:
            pygame.draw.rect(surface, BLUE, self.rect, 2)
        else:
            pygame.draw.rect(surface, BLACK, self.rect, 2)

        if self.text:
            text_surf = font_small.render(self.text, True, self.text_color)
            surface.blit(text_surf, (self.rect.x + 5, self.rect.y + 5))
        else:
            placeholder_surf = font_small.render(self.placeholder, True, (150, 150, 150))
            surface.blit(placeholder_surf, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return self.active

# --- Lógica de las pantallas del juego ---

def menu_screen():
    buttons = [
        Button("Practicar", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 50, BLUE, WHITE, lambda: main_game("practice")),
        Button("Ver Ejemplos", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50, BLUE, WHITE, lambda: main_game("view")),
        Button("Salir", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50, RED, WHITE, sys.exit)
    ]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                if button.handle_event(event):
                    return
        
        screen.fill(LIGHT_GRAY)
        title_text = font.render("Juego 'Entonces'", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_text, title_rect)

        for button in buttons:
            button.draw(screen)
        
        pygame.display.flip()

def practice_screen():
    global ejemplos_data
    current_ejemplo = random.choice(ejemplos_data)
    
    es_text = font.render(f"Español: {current_ejemplo['es']}", True, BLACK)
    
    en_input = TextInput(50, 200, SCREEN_WIDTH - 100, 50, placeholder="Traducción en inglés")
    fr_input = TextInput(50, 300, SCREEN_WIDTH - 100, 50, placeholder="Traducción en francés")
    
    result_text = ""
    result_color = BLACK

    back_button = Button("Volver", 50, 500, 100, 40, RED, WHITE, lambda: main_game("menu"))
    next_button = Button("Siguiente", SCREEN_WIDTH - 150, 500, 100, 40, GREEN, WHITE, lambda: main_game("practice"))
    check_button = Button("Revisar", SCREEN_WIDTH // 2 - 50, 500, 100, 40, BLUE, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            back_button.handle_event(event)
            next_button.handle_event(event)
            check_button.handle_event(event)
            
            en_input.handle_event(event)
            fr_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if check_button.rect.collidepoint(event.pos):
                    if en_input.text.lower().strip() == current_ejemplo['en'].lower().strip() and \
                       fr_input.text.lower().strip() == current_ejemplo['fr'].lower().strip():
                        result_text = "¡Correcto!"
                        result_color = GREEN
                    else:
                        result_text = f"Incorrecto. Correcto:\nInglés: {current_ejemplo['en']}\nFrancés: {current_ejemplo['fr']}"
                        result_color = RED

        screen.fill(LIGHT_GRAY)
        
        # Título de la pantalla
        title_text = font.render("Practicar Ejemplos", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_rect)
        
        screen.blit(es_text, (50, 120))
        en_input.draw(screen)
        fr_input.draw(screen)

        result_lines = result_text.split('\n')
        for i, line in enumerate(result_lines):
            text_surface = font_small.render(line, True, result_color)
            screen.blit(text_surface, (50, 380 + i * 25))

        back_button.draw(screen)
        next_button.draw(screen)
        check_button.draw(screen)

        pygame.display.flip()

def view_screen():
    back_button = Button("Volver", 50, 50, 100, 40, BLUE, WHITE, lambda: main_game("menu"))
    
    # Renderizar todos los textos para el scroll
    ejemplos_surfaces = []
    y_offset = 0
    for ejemplo in ejemplos_data:
        text_lines = [
            f"ID: {ejemplo['id']}",
            f"Español: {ejemplo['es']}",
            f"Inglés: {ejemplo['en']}",
            f"Francés: {ejemplo['fr']}",
            "-" * 40
        ]
        for line in text_lines:
            ejemplos_surfaces.append(font_small.render(line, True, BLACK))
        y_offset += len(text_lines) * 25

    scroll_y = 0
    scroll_speed = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: # Scroll up
                    scroll_y = min(scroll_y + scroll_speed, 0)
                if event.button == 5: # Scroll down
                    scroll_y = max(scroll_y - scroll_speed, SCREEN_HEIGHT - y_offset)
                if back_button.handle_event(event):
                    return
        
        screen.fill(LIGHT_GRAY)
        
        title_text = font.render("Lista de Ejemplos", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(title_text, title_rect)
        
        # Contenedor para la lista
        container_rect = pygame.Rect(50, 80, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 160)
        pygame.draw.rect(screen, WHITE, container_rect)
        pygame.draw.rect(screen, BLACK, container_rect, 2)
        
        # Dibuja los textos dentro del contenedor con scroll
        for i, surf in enumerate(ejemplos_surfaces):
            y_pos = 90 + i * 25 + scroll_y
            if y_pos > container_rect.top and y_pos < container_rect.bottom:
                screen.blit(surf, (container_rect.x + 10, y_pos))
        
        back_button.draw(screen)
        pygame.display.flip()

def main_game(screen_name):
    """Función para manejar las pantallas del juego."""
    while True:
        if screen_name == "menu":
            menu_screen()
        elif screen_name == "practice":
            practice_screen()
        elif screen_name == "view":
            view_screen()
        
        # Si la pantalla cambia, la función se vuelve a llamar con la nueva pantalla
        # Esto es una forma simple de manejar las transiciones.
        break

if __name__ == "__main__":
    main_game("menu")
