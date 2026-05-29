import pygame
import sys
import random
import math
import json
from pygame import gfxdraw

# Inicializar Pygame
pygame.init()
pygame.font.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Syntax Master - Aprendizaje de Sintaxis Bilingüe")

# Colores vibrantes para efectos rainbow
COLORS = {
    'background': [(20, 5, 30), (40, 10, 60)],
    'rainbow': [
        (255, 0, 0), (255, 127, 0), (255, 255, 0),
        (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
    ],
    'glass': (255, 255, 255, 120),
    'success': (46, 204, 113),
    'error': (231, 76, 60),
    'warning': (241, 196, 15)
}

# Fuentes avanzadas
title_font = pygame.font.Font(None, 80)
main_font = pygame.font.Font(None, 36)
code_font = pygame.font.SysFont('consolas', 28)
button_font = pygame.font.Font(None, 32)
emoji_font = pygame.font.SysFont('segoeuiemoji', 40)

# Base de datos mejorada de sintaxis Python para preuniversitarios
SYNTAX_DATABASE = [
    {
        'id': 1,
        'python_code': 'for i in range(10):\n    print(i)',
        'english_explanation': 'Loop that prints numbers 0 through 9',
        'spanish_explanation': 'Bucle que imprime números del 0 al 9',
        'difficulty': 'beginner',
        'category': 'loops',
        'correct': True,
        'common_errors': ['for i in range(10)', 'for i in range(10): print(i)']
    },
    {
        'id': 2,
        'python_code': 'if x = 5:\n    print("five")',
        'english_explanation': 'INCORRECT: Should use == for comparison',
        'spanish_explanation': 'INCORRECTO: Debe usar == para comparación',
        'difficulty': 'beginner',
        'category': 'conditionals',
        'correct': False,
        'common_errors': []
    },
    {
        'id': 3,
        'python_code': 'def calculate_area(radius):\n    return 3.14 * radius ** 2',
        'english_explanation': 'Function to calculate circle area',
        'spanish_explanation': 'Función para calcular área del círculo',
        'difficulty': 'intermediate',
        'category': 'functions',
        'correct': True,
        'common_errors': ['def calculate_area(radius) return 3.14 * radius ** 2']
    },
    {
        'id': 4,
        'python_code': 'lista = [1, 2, 3]\nfor item in lista:\nprint(item)',
        'english_explanation': 'INCORRECT: Missing indentation after for loop',
        'spanish_explanation': 'INCORRECTO: Falta indentación después del for',
        'difficulty': 'beginner',
        'category': 'loops',
        'correct': False,
        'common_errors': []
    },
    {
        'id': 5,
        'python_code': 'class Student:\n    def __init__(self, name):\n        self.name = name',
        'english_explanation': 'Class definition with constructor',
        'spanish_explanation': 'Definición de clase con constructor',
        'difficulty': 'advanced',
        'category': 'oop',
        'correct': True,
        'common_errors': ['class Student:\n__init__(self, name):\nself.name = name']
    }
]

class RainbowButton:
    def __init__(self, x, y, width, height, text, emoticon="🎮", action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoticon = emoticon
        self.action = action
        self.hovered = False
        self.clicked = False
        self.rainbow_offset = random.randint(0, 360)
        self.pulse = 0
        self.pulse_direction = 1
        self.glow_intensity = 0
        self.particles = []
        
    def update(self, mouse_pos, mouse_click):
        self.hovered = self.rect.collidepoint(mouse_pos)
        was_clicked = self.hovered and mouse_click and not self.clicked
        self.clicked = self.hovered and mouse_click
        
        # Efectos de hover
        if self.hovered:
            self.glow_intensity = min(self.glow_intensity + 10, 100)
            self.pulse += 0.2 * self.pulse_direction
            if self.pulse > 8 or self.pulse < 0:
                self.pulse_direction *= -1
        else:
            self.glow_intensity = max(self.glow_intensity - 5, 0)
            
        # Animación rainbow
        self.rainbow_offset = (self.rainbow_offset + 2) % 360
        
        # Crear partículas al hacer hover
        if self.hovered and random.random() < 0.1:
            self.create_hover_particles()
            
        # Actualizar partículas
        self.particles = [p for p in self.particles if p.update()]
        
        return was_clicked
    
    def create_hover_particles(self):
        x = random.randint(self.rect.left, self.rect.right)
        y = self.rect.top - 10
        self.particles.append(EmoticonParticle(x, y, 'button'))
    
    def draw(self, surface):
        # Dibujar efecto de glow
        if self.glow_intensity > 0:
            for i in range(3):
                glow_rect = self.rect.inflate(i * 8 + self.glow_intensity, 
                                            i * 8 + self.glow_intensity)
                alpha = 100 - i * 30
                glow_surf = pygame.Surface(glow_rect.size, pygame.SRCALPHA)
                color_index = int((self.rainbow_offset / 60) % len(COLORS['rainbow']))
                glow_color = COLORS['rainbow'][color_index]
                
                pygame.draw.rect(glow_surf, (*glow_color, alpha), 
                               glow_surf.get_rect(), border_radius=25)
                surface.blit(glow_surf, glow_rect)
        
        # Color del botón con efecto rainbow
        color_index = int((self.rainbow_offset / 60) % len(COLORS['rainbow']))
        base_color = COLORS['rainbow'][color_index]
        
        # Efecto de pulsación
        pulse_offset = int(self.pulse)
        button_color = tuple(min(c + pulse_offset * 10, 255) for c in base_color)
        
        # Dibujar botón principal
        pygame.draw.rect(surface, button_color, self.rect, border_radius=20)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 3, border_radius=20)
        
        # Dibujar partículas
        for particle in self.particles:
            particle.draw(surface)
        
        # Texto y emoticono
        button_text = f"{self.emoticon} {self.text} {self.emoticon}"
        text_surf = button_font.render(button_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        
        # Efecto de sombra en texto
        shadow_surf = button_font.render(button_text, True, (0, 0, 0))
        surface.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
        surface.blit(text_surf, text_rect)

class EmoticonParticle:
    def __init__(self, x, y, type='success'):
        self.x = x
        self.y = y
        self.type = type
        self.emoticon = self.get_emoticon(type)
        self.size = random.randint(20, 40)
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-8, -3)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-8, 8)
        self.life = 100
        self.alpha = 255
        self.gravity = 0.2
        self.wobble = random.uniform(0, math.pi * 2)
        self.wobble_speed = random.uniform(0.05, 0.1)
        
    def get_emoticon(self, type):
        emoticon_sets = {
            'success': ['✅', '🎉', '🌟', '💫', '🔥', '✨', '💎'],
            'error': ['❌', '💥', '⚠️', '🔴', '🚫', '💔'],
            'button': ['⚡', '💠', '🔷', '🔶', '💫', '✨'],
            'code': ['🐍', '💻', '🔧', '⚙️', '📝', '🔍'],
            'language': ['🇺🇸', '🇪🇸', '🌍', '🔤', '📚']
        }
        return random.choice(emoticon_sets.get(type, ['⭐']))
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rotation += self.rotation_speed
        self.life -= 1.5
        self.alpha = int(255 * (self.life / 100))
        self.wobble += self.wobble_speed
        
        # Efecto de wobble lateral
        self.x += math.sin(self.wobble) * 0.5
        
        return self.life > 0 and self.alpha > 0
    
    def draw(self, surface):
        font = pygame.font.SysFont('segoeuiemoji', int(self.size + math.sin(pygame.time.get_ticks() * 0.01) * 2))
        text_surf = font.render(self.emoticon, True, (255, 255, 255))
        
        # Rotación suave
        rotated_surf = pygame.transform.rotate(text_surf, self.rotation)
        
        # Aplicar alpha
        rotated_surf.set_alpha(self.alpha)
        
        # Dibujar con efecto de glow
        if self.alpha > 100:
            glow_surf = font.render(self.emoticon, True, (255, 255, 200))
            glow_surf.set_alpha(self.alpha // 3)
            glow_rect = glow_surf.get_rect(center=(self.x, self.y))
            surface.blit(glow_surf, glow_rect)
        
        text_rect = rotated_surf.get_rect(center=(self.x, self.y))
        surface.blit(rotated_surf, text_rect)

class SyntaxCard:
    def __init__(self, x, y, width, height, question_data):
        self.rect = pygame.Rect(x, y, width, height)
        self.question_data = question_data
        self.revealed = False
        self.answered = False
        self.correct_answer = None
        self.wobble = random.uniform(0, math.pi * 2)
        self.glow_color = (100, 100, 200)
        self.particles = []
        
    def update(self, mouse_pos, mouse_click):
        self.wobble += 0.05
        
        # Efecto de hover
        if self.rect.collidepoint(mouse_pos) and not self.answered:
            self.glow_color = tuple(min(c + 5, 200) for c in self.glow_color)
            
            # Crear partículas de hover
            if random.random() < 0.2:
                self.create_hover_particles()
        else:
            self.glow_color = tuple(max(c - 2, 100) for c in self.glow_color)
        
        # Actualizar partículas
        self.particles = [p for p in self.particles if p.update()]
        
        # Verificar clic
        if self.rect.collidepoint(mouse_pos) and mouse_click and not self.answered:
            return True
        return False
    
    def create_hover_particles(self):
        x = random.randint(self.rect.left + 10, self.rect.right - 10)
        y = self.rect.bottom - 5
        self.particles.append(EmoticonParticle(x, y, 'code'))
    
    def draw(self, surface):
        # Efecto de wobble
        wobble_offset = math.sin(self.wobble) * 3
        
        # Fondo glassmorphism con efecto de glow
        glass_surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        
        # Gradiente de fondo
        for i in range(self.rect.height):
            alpha = 150 - int(i / self.rect.height * 100)
            color = (*self.glow_color, alpha)
            pygame.draw.line(glass_surf, color, (0, i), (self.rect.width, i))
        
        # Borde glass
        pygame.draw.rect(glass_surf, (255, 255, 255, 80), 
                        glass_surf.get_rect(), 3, border_radius=15)
        
        surface.blit(glass_surf, (self.rect.x, self.rect.y + wobble_offset))
        
        # Contenido de la tarjeta
        content_rect = self.rect.move(0, int(wobble_offset))
        
        # Código Python
        code_lines = self.question_data['python_code'].split('\n')
        for i, line in enumerate(code_lines):
            code_surf = code_font.render(line, True, (50, 255, 150))
            surface.blit(code_surf, (content_rect.x + 20, content_rect.y + 20 + i * 30))
        
        # Estado de respuesta
        if self.answered:
            status_emoji = "✅" if self.correct_answer else "❌"
            status_color = COLORS['success'] if self.correct_answer else COLORS['error']
            
            status_surf = emoji_font.render(status_emoji, True, status_color)
            surface.blit(status_surf, (content_rect.right - 50, content_rect.y + 20))
        
        # Dibujar partículas
        for particle in self.particles:
            particle.draw(surface)

class AnimatedBackground:
    def __init__(self):
        self.time = 0
        self.stars = []
        self.gradient_points = []
        self.generate_stars(100)
        self.generate_gradient_points()
        
    def generate_stars(self, count):
        for _ in range(count):
            self.stars.append({
                'x': random.uniform(0, WIDTH),
                'y': random.uniform(0, HEIGHT),
                'size': random.uniform(0.5, 2),
                'speed': random.uniform(0.1, 0.5),
                'brightness': random.uniform(0.3, 1.0)
            })
    
    def generate_gradient_points(self):
        for _ in range(10):
            self.gradient_points.append({
                'x': random.uniform(0, WIDTH),
                'y': random.uniform(0, HEIGHT),
                'radius': random.uniform(100, 300),
                'color': random.choice(COLORS['rainbow']),
                'speed': random.uniform(0.5, 2)
            })
    
    def update(self):
        self.time += 0.01
        
        # Mover estrellas
        for star in self.stars:
            star['y'] += star['speed']
            if star['y'] > HEIGHT:
                star['y'] = 0
                star['x'] = random.uniform(0, WIDTH)
        
        # Mover puntos de gradiente
        for point in self.gradient_points:
            point['x'] += math.sin(self.time * point['speed']) * 0.5
            point['y'] += math.cos(self.time * point['speed']) * 0.5
    
    def draw(self, surface):
        # Fondo base con gradiente animado
        for y in range(0, HEIGHT, 2):
            progress = y / HEIGHT
            r = int(COLORS['background'][0][0] + 
                   (COLORS['background'][1][0] - COLORS['background'][0][0]) * progress)
            g = int(COLORS['background'][0][1] + 
                   (COLORS['background'][1][1] - COLORS['background'][0][1]) * progress)
            b = int(COLORS['background'][0][2] + 
                   (COLORS['background'][1][2] - COLORS['background'][0][2]) * progress)
            
            # Efecto de onda
            wave = math.sin(self.time + y * 0.01) * 10
            pygame.draw.line(surface, (r, g, b), (0, y + wave), (WIDTH, y + wave))
        
        # Puntos de gradiente radial
        for point in self.gradient_points:
            for r in range(int(point['radius']), 0, -10):
                alpha = int(50 * (1 - r / point['radius']))
                color = (*point['color'], alpha)
                pygame.gfxdraw.filled_circle(surface, int(point['x']), int(point['y']), r, color)
        
        # Estrellas titilantes
        for star in self.stars:
            brightness = star['brightness'] * (0.7 + 0.3 * math.sin(self.time * star['speed'] * 10))
            color = (int(255 * brightness), int(255 * brightness), int(200 * brightness))
            pygame.draw.circle(surface, color, (int(star['x']), int(star['y'])), star['size'])

class SyntaxMasterGame:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = AnimatedBackground()
        self.particles = []
        self.cards = []
        self.buttons = []
        self.score = 0
        self.level = 1
        self.current_question = 0
        self.correct_streak = 0
        
        self.setup_game()
    
    def setup_game(self):
        # Crear botones principales
        button_width, button_height = 300, 70
        spacing = 20
        
        self.buttons.append(RainbowButton(
            WIDTH//2 - button_width//2, 650, button_width, button_height,
            "Correcto", "✅", self.answer_correct
        ))
        
        self.buttons.append(RainbowButton(
            WIDTH//2 - button_width//2, 650 + button_height + spacing, 
            button_width, button_height, "Incorrecto", "❌", self.answer_incorrect
        ))
        
        self.buttons.append(RainbowButton(
            WIDTH//2 - button_width//2, 650 + (button_height + spacing) * 2,
            button_width, button_height, "Siguiente Nivel", "🚀", self.next_level
        ))
        
        # Crear cartas de preguntas
        self.load_questions()
    
    def load_questions(self):
        self.cards = []
        card_width, card_height = 600, 200
        spacing = 30
        
        # Seleccionar preguntas para el nivel actual
        level_questions = [q for q in SYNTAX_DATABASE if self.get_difficulty_level(q['difficulty']) <= self.level]
        random.shuffle(level_questions)
        
        for i, question in enumerate(level_questions[:3]):  # Máximo 3 preguntas por pantalla
            x = WIDTH//2 - card_width//2
            y = 150 + i * (card_height + spacing)
            self.cards.append(SyntaxCard(x, y, card_width, card_height, question))
    
    def get_difficulty_level(self, difficulty):
        levels = {'beginner': 1, 'intermediate': 2, 'advanced': 3}
        return levels.get(difficulty, 1)
    
    def answer_correct(self):
        if self.current_question < len(self.cards):
            card = self.cards[self.current_question]
            is_correct = card.question_data['correct']
            card.answered = True
            card.correct_answer = is_correct
            
            if is_correct:
                self.score += 10 * self.level
                self.correct_streak += 1
                self.create_particles(WIDTH//2, 300, 20, 'success')
            else:
                self.correct_streak = 0
                self.create_particles(WIDTH//2, 300, 15, 'error')
            
            self.current_question += 1
    
    def answer_incorrect(self):
        if self.current_question < len(self.cards):
            card = self.cards[self.current_question]
            is_correct = card.question_data['correct']
            card.answered = True
            card.correct_answer = not is_correct  # Porque eligió "Incorrecto"
            
            if not is_correct:  # Si realmente es incorrecto
                self.score += 10 * self.level
                self.correct_streak += 1
                self.create_particles(WIDTH//2, 300, 20, 'success')
            else:
                self.correct_streak = 0
                self.create_particles(WIDTH//2, 300, 15, 'error')
            
            self.current_question += 1
    
    def next_level(self):
        if self.current_question >= len(self.cards):
            self.level += 1
            self.current_question = 0
            self.load_questions()
            self.create_particles(WIDTH//2, HEIGHT//2, 30, 'success')
    
    def create_particles(self, x, y, count, type):
        for _ in range(count):
            self.particles.append(EmoticonParticle(x, y, type))
    
    def draw_interface(self):
        # Panel superior glassmorphism
        glass_surf = pygame.Surface((WIDTH, 120), pygame.SRCALPHA)
        pygame.draw.rect(glass_surf, (255, 255, 255, 50), glass_surf.get_rect())
        pygame.draw.line(glass_surf, (255, 255, 255, 100), (0, 0), (WIDTH, 0), 3)
        screen.blit(glass_surf, (0, 0))
        
        # Título
        title_text = title_font.render("🐍 Syntax Master 🎓", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))
        
        # Información del juego
        info_text = main_font.render(
            f"Level: {self.level} 🌟 | Score: {self.score} ⭐ | Streak: {self.correct_streak} 🔥", 
            True, (255, 255, 200)
        )
        screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, 80))
        
        # Instrucciones bilingües
        if self.current_question < len(self.cards):
            instruction_en = main_font.render(
                "Is this Python syntax correct? 🇺🇸", True, (200, 200, 255)
            )
            instruction_es = main_font.render(
                "¿Es correcta esta sintaxis de Python? 🇪🇸", True, (200, 255, 200)
            )
            
            screen.blit(instruction_en, (WIDTH//2 - instruction_en.get_width()//2, 110))
            screen.blit(instruction_es, (WIDTH//2 - instruction_es.get_width()//2, 140))
    
    def run(self):
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_c:
                        self.answer_correct()
                    elif event.key == pygame.K_i:
                        self.answer_incorrect()
                    elif event.key == pygame.K_n:
                        self.next_level()
            
            # Actualizar
            self.background.update()
            
            # Actualizar partículas
            self.particles = [p for p in self.particles if p.update()]
            
            # Actualizar y verificar cartas
            for card in self.cards:
                if card.update(mouse_pos, mouse_click) and not card.answered:
                    # Mostrar explicación al hacer clic
                    self.show_explanation(card.question_data)
            
            # Actualizar botones
            for button in self.buttons:
                if button.update(mouse_pos, mouse_click) and button.action:
                    button.action()
            
            # Dibujar
            self.background.draw(screen)
            
            # Dibujar partículas
            for particle in self.particles:
                particle.draw(screen)
            
            # Dibujar interfaz
            self.draw_interface()
            
            # Dibujar cartas
            for card in self.cards:
                card.draw(screen)
            
            # Dibujar botones (solo los relevantes)
            if self.current_question < len(self.cards):
                self.buttons[0].draw(screen)  # Correcto
                self.buttons[1].draw(screen)  # Incorrecto
            else:
                self.buttons[2].draw(screen)  # Siguiente nivel
            
            # Efectos de partículas aleatorias
            if random.random() < 0.01:
                x = random.randint(0, WIDTH)
                self.create_particles(x, HEIGHT + 50, 3, random.choice(['code', 'language']))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def show_explanation(self, question_data):
        # Crear superficie de explicación (simplificado)
        print(f"\n💡 Explanation / Explicación:")
        print(f"Python: {question_data['python_code']}")
        print(f"English: {question_data['english_explanation']}")
        print(f"Spanish: {question_data['spanish_explanation']}")
        print(f"Correct: {'Yes ✅' if question_data['correct'] else 'No ❌'}")

# Ejecutar el juego
if __name__ == "__main__":
    game = SyntaxMasterGame()
    game.run()
