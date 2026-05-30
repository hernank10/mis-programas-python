import pygame
import sys
import random
import math
from pygame import gfxdraw

# Inicializar Pygame
pygame.init()
pygame.font.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 PyGame Edu-Emoticons: Aprendizaje de Sintaxis Bilingüe")

# Colores vibrantes
COLORS = {
    'background': [(30, 10, 40), (60, 20, 80)],
    'rainbow': [(255, 50, 50), (255, 150, 50), (255, 255, 50), 
                (50, 255, 50), (50, 150, 255), (150, 50, 255)],
    'glass': (255, 255, 255, 80),
    'text': (240, 240, 240)
}

# Fuentes
title_font = pygame.font.SysFont('comicsans', 60, bold=True)
main_font = pygame.font.SysFont('comicsans', 32)
button_font = pygame.font.SysFont('comicsans', 28)

# Emoticones para sintaxis
EMOTICONS = {
    'python': ['🐍', '⚡', '🔧', '💻', '🚀'],
    'english': ['🇺🇸', '📚', '✏️', '🎓', '🔤'],
    'spanish': ['🇪🇸', '📖', '🖊️', '🎯', '🔡'],
    'success': ['✅', '🎉', '🌟', '💫', '🔥'],
    'error': ['❌', '💥', '⚠️', '🔴', '🚫']
}

# Base de datos de sintaxis bilingüe
SYNTAX_QUESTIONS = [
    {
        'python': 'for i in range(5):',
        'english': 'Loop through numbers 0 to 4',
        'spanish': 'Iterar por números del 0 al 4',
        'explanation': 'Bucle for en Python'
    },
    {
        'python': 'if x > 10:',
        'english': 'Conditional if x is greater than 10',
        'spanish': 'Condicional si x es mayor que 10',
        'explanation': 'Estructura condicional'
    },
    {
        'python': 'def function_name():',
        'english': 'Define a new function',
        'spanish': 'Definir una nueva función',
        'explanation': 'Declaración de función'
    },
    {
        'python': 'lista = [1, 2, 3]',
        'english': 'Create a list with elements',
        'spanish': 'Crear lista con elementos',
        'explanation': 'Inicialización de lista'
    },
    {
        'python': 'print("Hello World")',
        'english': 'Display text on screen',
        'spanish': 'Mostrar texto en pantalla',
        'explanation': 'Función de impresión'
    }
]

class RainbowButton:
    def __init__(self, x, y, width, height, text, emoticon='🎮'):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoticon = emoticon
        self.hovered = False
        self.clicked = False
        self.rainbow_offset = 0
        self.pulse = 0
        self.pulse_direction = 1
        
    def draw(self, surface):
        # Efecto de pulsación
        self.pulse += 0.1 * self.pulse_direction
        if self.pulse > 5 or self.pulse < 0:
            self.pulse_direction *= -1
            
        # Efecto rainbow animado
        self.rainbow_offset = (self.rainbow_offset + 1) % 360
        
        # Color base con efecto hover
        if self.hovered:
            color_index = int((self.rainbow_offset / 60) % len(COLORS['rainbow']))
            base_color = COLORS['rainbow'][color_index]
            glow_color = tuple(min(c + 50, 255) for c in base_color)
        else:
            base_color = (100, 100, 200)
            glow_color = (150, 150, 255)
            
        # Dibujar efecto de glow
        for i in range(5, 0, -1):
            glow_rect = self.rect.inflate(i * 4, i * 4)
            alpha = 50 - i * 10
            glow_surface = pygame.Surface(glow_rect.size, pygame.SRCALPHA)
            pygame.draw.rect(glow_surface, (*glow_color, alpha), 
                           glow_surface.get_rect(), border_radius=20)
            surface.blit(glow_surface, glow_rect)
        
        # Dibujar botón principal
        button_color = tuple(min(c + int(self.pulse * 10), 255) for c in base_color)
        pygame.draw.rect(surface, button_color, self.rect, border_radius=15)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 3, border_radius=15)
        
        # Texto y emoticono
        text_surf = button_font.render(f"{self.emoticon} {self.text} {self.emoticon}", 
                                     True, COLORS['text'])
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def update(self, mouse_pos, mouse_click):
        self.hovered = self.rect.collidepoint(mouse_pos)
        self.clicked = self.hovered and mouse_click
        return self.clicked

class EmoticonParticle:
    def __init__(self, x, y, emoticon_type='success'):
        self.x = x
        self.y = y
        self.emoticon = random.choice(EMOTICONS[emoticon_type])
        self.size = random.randint(20, 40)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-5, -2)
        self.rotation = 0
        self.rotation_speed = random.uniform(-5, 5)
        self.life = 100
        self.alpha = 255
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += 0.1  # Gravedad
        self.rotation += self.rotation_speed
        self.life -= 1
        self.alpha = int(255 * (self.life / 100))
        return self.life > 0
        
    def draw(self, surface):
        font = pygame.font.SysFont('segoeuiemoji', self.size)
        text_surf = font.render(self.emoticon, True, (255, 255, 255))
        text_surf = pygame.transform.rotate(text_surf, self.rotation)
        
        # Aplicar alpha
        text_surf.set_alpha(self.alpha)
        text_rect = text_surf.get_rect(center=(self.x, self.y))
        surface.blit(text_surf, text_rect)

class SyntaxCard:
    def __init__(self, x, y, question_data):
        self.rect = pygame.Rect(x, y, 350, 200)
        self.question_data = question_data
        self.revealed = False
        self.wobble = 0
        
    def draw(self, surface):
        # Efecto de wobble
        self.wobble += 0.1
        wobble_offset = math.sin(self.wobble) * 3
        
        # Fondo glassmorphism
        glass_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(glass_surface, (*COLORS['glass'][:3], 120), 
                        glass_surface.get_rect(), border_radius=20)
        pygame.draw.rect(glass_surface, (255, 255, 255, 100), 
                        glass_surface.get_rect(), 2, border_radius=20)
        
        surface.blit(glass_surface, (self.rect.x, self.rect.y + wobble_offset))
        
        # Contenido
        y_offset = self.rect.y + 20 + wobble_offset
        
        # Python code
        code_font = pygame.font.SysFont('consolas', 24)
        code_text = code_font.render(self.question_data['python'], True, (50, 255, 150))
        surface.blit(code_text, (self.rect.x + 20, y_offset))
        
        if self.revealed:
            # Explicación en inglés y español
            y_offset += 40
            eng_text = main_font.render(f"🇺🇸 {self.question_data['english']}", True, (200, 200, 255))
            surface.blit(eng_text, (self.rect.x + 20, y_offset))
            
            y_offset += 35
            esp_text = main_font.render(f"🇪🇸 {self.question_data['spanish']}", True, (200, 255, 200))
            surface.blit(esp_text, (self.rect.x + 20, y_offset))
            
            y_offset += 35
            exp_text = main_font.render(f"💡 {self.question_data['explanation']}", True, (255, 255, 150))
            surface.blit(exp_text, (self.rect.x + 20, y_offset))
        else:
            # Botón para revelar
            hint_text = main_font.render("🎯 Click para revelar sintaxis", True, (255, 200, 100))
            surface.blit(hint_text, (self.rect.x + 20, y_offset + 60))
            
    def check_click(self, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos) and mouse_click:
            self.revealed = True
            return True
        return False

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.particles = []
        self.cards = []
        self.buttons = []
        self.score = 0
        self.level = 1
        self.background_offset = 0
        
        # Crear botones
        self.buttons.append(RainbowButton(450, 600, 300, 60, "Nueva Pregunta", "🔄"))
        self.buttons.append(RainbowButton(450, 680, 300, 60, "Quiz Rápido", "⚡"))
        
        # Crear cartas iniciales
        self.create_cards()
        
    def create_cards(self):
        self.cards = []
        x_positions = [100, 500, 800]
        random.shuffle(SYNTAX_QUESTIONS)
        
        for i, question in enumerate(SYNTAX_QUESTIONS[:3]):
            self.cards.append(SyntaxCard(x_positions[i], 200, question))
    
    def create_particles(self, x, y, count=10, type='success'):
        for _ in range(count):
            self.particles.append(EmoticonParticle(x, y, type))
    
    def draw_animated_background(self):
        # Fondo con gradiente animado
        self.background_offset = (self.background_offset + 0.5) % HEIGHT
        
        for y in range(0, HEIGHT * 2, 5):
            color_progress = (y + self.background_offset) % HEIGHT / HEIGHT
            r = int(COLORS['background'][0][0] + 
                   (COLORS['background'][1][0] - COLORS['background'][0][0]) * color_progress)
            g = int(COLORS['background'][0][1] + 
                   (COLORS['background'][1][1] - COLORS['background'][0][1]) * color_progress)
            b = int(COLORS['background'][0][2] + 
                   (COLORS['background'][1][2] - COLORS['background'][0][2]) * color_progress)
            
            pygame.draw.line(screen, (r, g, b), (0, y - self.background_offset), 
                           (WIDTH, y - self.background_offset))
        
        # Estrellas decorativas
        for i in range(50):
            x = (i * 123) % WIDTH
            y = (i * 79) % HEIGHT
            size = math.sin(pygame.time.get_ticks() * 0.001 + i) * 2 + 1
            pygame.draw.circle(screen, (255, 255, 200), (x, y), size)
    
    def draw_glass_panel(self):
        # Panel superior glassmorphism
        glass_surface = pygame.Surface((WIDTH, 120), pygame.SRCALPHA)
        pygame.draw.rect(glass_surface, (*COLORS['glass'][:3], 100), 
                        glass_surface.get_rect(), border_radius=0)
        
        # Borde superior brillante
        pygame.draw.line(glass_surface, (255, 255, 255, 150), (0, 0), (WIDTH, 0), 3)
        
        screen.blit(glass_surface, (0, 0))
        
        # Título y puntuación
        title_text = title_font.render("🎮 PyGame Edu-Emoticons 🐍", True, COLORS['text'])
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
        
        score_text = main_font.render(f"Puntuación: {self.score} 🌟 | Nivel: {self.level} 🚀", 
                                    True, (255, 255, 150))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 80))
    
    def run(self):
        running = True
        
        while running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Dibujar fondo animado
            self.draw_animated_background()
            
            # Actualizar y dibujar partículas
            self.particles = [p for p in self.particles if p.update()]
            for particle in self.particles:
                particle.draw(screen)
            
            # Dibujar panel superior
            self.draw_glass_panel()
            
            # Actualizar y dibujar cartas
            for card in self.cards:
                if card.check_click(mouse_pos, mouse_click):
                    self.create_particles(card.rect.centerx, card.rect.centery, 15, 'success')
                    self.score += 10
                
                card.draw(screen)
            
            # Actualizar y dibujar botones
            for button in self.buttons:
                if button.update(mouse_pos, mouse_click):
                    if button.text == "Nueva Pregunta":
                        self.create_cards()
                        self.create_particles(button.rect.centerx, button.rect.centery, 20, 'python')
                    elif button.text == "Quiz Rápido":
                        self.level += 1
                        self.create_particles(button.rect.centerx, button.rect.centery, 25, 'english')
                
                button.draw(screen)
            
            # Efectos de emoticones flotantes ocasionales
            if random.random() < 0.02:
                x = random.randint(0, WIDTH)
                self.create_particles(x, HEIGHT + 50, 5, random.choice(['python', 'english', 'spanish']))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.run()
