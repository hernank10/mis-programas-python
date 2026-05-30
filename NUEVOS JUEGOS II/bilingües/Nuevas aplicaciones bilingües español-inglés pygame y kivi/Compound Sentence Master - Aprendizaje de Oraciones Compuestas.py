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
pygame.display.set_caption("📚 Compound Sentence Master - Aprendizaje de Oraciones Compuestas")

# Colores vibrantes
COLORS = {
    'background': [(25, 10, 40), (45, 15, 70)],
    'rainbow': [
        (255, 50, 50), (255, 150, 50), (255, 255, 50),
        (50, 255, 50), (50, 200, 255), (180, 50, 255), (255, 50, 200)
    ],
    'glass': (255, 255, 255, 100),
    'success': (46, 204, 113),
    'error': (231, 76, 60),
    'warning': (241, 196, 15),
    'text_light': (240, 240, 255),
    'text_dark': (30, 30, 40)
}

# Fuentes
title_font = pygame.font.Font(None, 72)
main_font = pygame.font.Font(None, 32)
sentence_font = pygame.font.Font(None, 28)
button_font = pygame.font.Font(None, 30)
emoji_font = pygame.font.SysFont('segoeuiemoji', 48)
large_emoji_font = pygame.font.SysFont('segoeuiemoji', 64)

# Base de datos de oraciones compuestas para preuniversitarios
SENTENCE_DATABASE = [
    {
        'id': 1,
        'spanish_simple': 'Estudié mucho. Aprobé el examen.',
        'spanish_compound': 'Estudié mucho, por lo tanto aprobé el examen.',
        'english_simple': 'I studied hard. I passed the exam.',
        'english_compound': 'I studied hard, therefore I passed the exam.',
        'connector_type': 'consecutiva',
        'connector_spanish': 'por lo tanto',
        'connector_english': 'therefore',
        'difficulty': 'easy',
        'explanation_es': 'Conector consecutivo que muestra resultado',
        'explanation_en': 'Consecutive connector showing result'
    },
    {
        'id': 2,
        'spanish_simple': 'Hace frío. Voy a abrigarme.',
        'spanish_compound': 'Como hace frío, voy a abrigarme.',
        'english_simple': "It's cold. I'm going to bundle up.",
        'english_compound': "Since it's cold, I'm going to bundle up.",
        'connector_type': 'causal',
        'connector_spanish': 'como',
        'connector_english': 'since',
        'difficulty': 'easy',
        'explanation_es': 'Conector causal que indica razón',
        'explanation_en': 'Causal connector indicating reason'
    },
    {
        'id': 3,
        'spanish_simple': 'Llovía mucho. Cancelaron el partido.',
        'spanish_compound': 'Dado que llovía mucho, cancelaron el partido.',
        'english_simple': 'It was raining heavily. They canceled the match.',
        'english_compound': 'Given that it was raining heavily, they canceled the match.',
        'connector_type': 'causal',
        'connector_spanish': 'dado que',
        'connector_english': 'given that',
        'difficulty': 'medium',
        'explanation_es': 'Conector causal formal',
        'explanation_en': 'Formal causal connector'
    },
    {
        'id': 4,
        'spanish_simple': 'Termina tu trabajo. Puedes salir a jugar.',
        'spanish_compound': 'En cuanto termines tu trabajo, podrás salir a jugar.',
        'english_simple': 'Finish your work. You can go out to play.',
        'english_compound': 'As soon as you finish your work, you can go out to play.',
        'connector_type': 'temporal',
        'connector_spanish': 'en cuanto',
        'connector_english': 'as soon as',
        'difficulty': 'medium',
        'explanation_es': 'Conector temporal de inmediata sucesión',
        'explanation_en': 'Temporal connector for immediate succession'
    },
    {
        'id': 5,
        'spanish_simple': 'No tengo dinero. No puedo comprar el libro.',
        'spanish_compound': 'No puedo comprar el libro porque no tengo dinero.',
        'english_simple': "I don't have money. I can't buy the book.",
        'english_compound': "I can't buy the book because I don't have money.",
        'connector_type': 'causal',
        'connector_spanish': 'porque',
        'connector_english': 'because',
        'difficulty': 'easy',
        'explanation_es': 'Conector causal más común',
        'explanation_en': 'Most common causal connector'
    },
    {
        'id': 6,
        'spanish_simple': 'Es tarde. Debo irme a casa.',
        'spanish_compound': 'Es tarde, así que debo irme a casa.',
        'english_simple': "It's late. I should go home.",
        'english_compound': "It's late, so I should go home.",
        'connector_type': 'consecutiva',
        'connector_spanish': 'así que',
        'connector_english': 'so',
        'difficulty': 'easy',
        'explanation_es': 'Conector consecutivo informal',
        'explanation_en': 'Informal consecutive connector'
    },
    {
        'id': 7,
        'spanish_simple': 'Estudiaré medicina. Me gusta ayudar a la gente.',
        'spanish_compound': 'Estudiaré medicina puesto que me gusta ayudar a la gente.',
        'english_simple': 'I will study medicine. I like helping people.',
        'english_compound': 'I will study medicine since I like helping people.',
        'connector_type': 'causal',
        'connector_spanish': 'puesto que',
        'connector_english': 'since',
        'difficulty': 'advanced',
        'explanation_es': 'Conector causal formal y explicativo',
        'explanation_en': 'Formal explanatory causal connector'
    },
    {
        'id': 8,
        'spanish_simple': 'Llegó el profesor. Empezó la clase.',
        'spanish_compound': 'Tan pronto como llegó el profesor, empezó la clase.',
        'english_simple': 'The teacher arrived. The class started.',
        'english_compound': 'As soon as the teacher arrived, the class started.',
        'connector_type': 'temporal',
        'connector_spanish': 'tan pronto como',
        'connector_english': 'as soon as',
        'difficulty': 'medium',
        'explanation_es': 'Conector temporal de simultaneidad',
        'explanation_en': 'Temporal connector for simultaneity'
    }
]

# Conectores por tipo para los ejercicios
CONNECTORS_BY_TYPE = {
    'causal': [
        {'es': 'porque', 'en': 'because', 'emoji': '🔍'},
        {'es': 'ya que', 'en': 'since', 'emoji': '📝'},
        {'es': 'puesto que', 'en': 'given that', 'emoji': '🎓'},
        {'es': 'debido a que', 'en': 'due to the fact that', 'emoji': '⚖️'}
    ],
    'consecutiva': [
        {'es': 'por lo tanto', 'en': 'therefore', 'emoji': '🔗'},
        {'es': 'así que', 'en': 'so', 'emoji': '➡️'},
        {'es': 'de modo que', 'en': 'so that', 'emoji': '🔄'},
        {'es': 'en consecuencia', 'en': 'consequently', 'emoji': '🎯'}
    ],
    'temporal': [
        {'es': 'cuando', 'en': 'when', 'emoji': '⏰'},
        {'es': 'mientras', 'en': 'while', 'emoji': '🔄'},
        {'es': 'antes de que', 'en': 'before', 'emoji': '⏪'},
        {'es': 'después de que', 'en': 'after', 'emoji': '⏩'}
    ]
}

class RainbowButton:
    def __init__(self, x, y, width, height, text, emoticon="✨", action=None, connector_data=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoticon = emoticon
        self.action = action
        self.connector_data = connector_data
        self.hovered = False
        self.clicked = False
        self.rainbow_offset = random.randint(0, 360)
        self.pulse = 0
        self.pulse_direction = 1
        self.glow_intensity = 0
        self.particles = []
        self.wobble = random.uniform(0, math.pi * 2)
        
    def update(self, mouse_pos, mouse_click):
        self.hovered = self.rect.collidepoint(mouse_pos)
        was_clicked = self.hovered and mouse_click and not self.clicked
        self.clicked = self.hovered and mouse_click
        
        # Efectos de hover
        if self.hovered:
            self.glow_intensity = min(self.glow_intensity + 15, 100)
            self.pulse += 0.3 * self.pulse_direction
            if self.pulse > 10 or self.pulse < 0:
                self.pulse_direction *= -1
        else:
            self.glow_intensity = max(self.glow_intensity - 8, 0)
            
        # Animaciones
        self.rainbow_offset = (self.rainbow_offset + 3) % 360
        self.wobble += 0.08
        
        # Crear partículas al hacer hover
        if self.hovered and random.random() < 0.15:
            self.create_hover_particles()
            
        # Actualizar partículas
        self.particles = [p for p in self.particles if p.update()]
        
        return was_clicked
    
    def create_hover_particles(self):
        x = random.randint(self.rect.left + 10, self.rect.right - 10)
        y = self.rect.top - 5
        emoticon_type = 'connector' if self.connector_data else 'button'
        self.particles.append(EmoticonParticle(x, y, emoticon_type, self.connector_data))
    
    def draw(self, surface):
        # Efecto de wobble para el rectángulo
        wobble_offset = math.sin(self.wobble) * 2
        
        # Dibujar efecto de glow
        if self.glow_intensity > 0:
            for i in range(5, 0, -1):
                glow_size = i * 4 + self.glow_intensity // 3
                glow_rect = self.rect.inflate(glow_size, glow_size)
                alpha = 60 - i * 10
                glow_surf = pygame.Surface(glow_rect.size, pygame.SRCALPHA)
                
                color_index = int((self.rainbow_offset / 60) % len(COLORS['rainbow']))
                glow_color = COLORS['rainbow'][color_index]
                
                pygame.draw.rect(glow_surf, (*glow_color, alpha), 
                               glow_surf.get_rect(), border_radius=20)
                surface.blit(glow_surf, glow_rect.move(wobble_offset, wobble_offset))
        
        # Color del botón con efecto rainbow y pulsación
        color_index = int((self.rainbow_offset / 60) % len(COLORS['rainbow']))
        base_color = COLORS['rainbow'][color_index]
        
        pulse_offset = int(self.pulse)
        button_color = tuple(min(c + pulse_offset * 8, 255) for c in base_color)
        
        # Dibujar botón principal con wobble
        button_rect = self.rect.move(wobble_offset, wobble_offset)
        pygame.draw.rect(surface, button_color, button_rect, border_radius=15)
        pygame.draw.rect(surface, (255, 255, 255), button_rect, 3, border_radius=15)
        
        # Dibujar partículas
        for particle in self.particles:
            particle.draw(surface)
        
        # Texto y emoticono
        if self.connector_data:
            # Botón de conector - mostrar en ambos idiomas
            connector_text = f"{self.connector_data['emoji']} {self.text}"
            en_text = f"{self.connector_data['en']}"
            
            main_text = button_font.render(connector_text, True, COLORS['text_light'])
            sub_text = main_font.render(en_text, True, (200, 200, 255))
            
            main_rect = main_text.get_rect(center=button_rect.center)
            sub_rect = sub_text.get_rect(center=(button_rect.centerx, button_rect.centery + 20))
            
            # Sombra de texto
            shadow_main = button_font.render(connector_text, True, (0, 0, 0))
            shadow_sub = main_font.render(en_text, True, (0, 0, 0))
            
            surface.blit(shadow_main, (main_rect.x + 2, main_rect.y + 2))
            surface.blit(shadow_sub, (sub_rect.x + 2, sub_rect.y + 2))
            surface.blit(main_text, main_rect)
            surface.blit(sub_text, sub_rect)
        else:
            # Botón normal
            button_text = f"{self.emoticon} {self.text} {self.emoticon}"
            text_surf = button_font.render(button_text, True, COLORS['text_light'])
            text_rect = text_surf.get_rect(center=button_rect.center)
            
            # Sombra de texto
            shadow_surf = button_font.render(button_text, True, (0, 0, 0))
            surface.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
            surface.blit(text_surf, text_rect)

class EmoticonParticle:
    def __init__(self, x, y, type='success', connector_data=None):
        self.x = x
        self.y = y
        self.type = type
        self.connector_data = connector_data
        self.emoticon = self.get_emoticon(type, connector_data)
        self.size = random.randint(24, 48)
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-8, -4)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-6, 6)
        self.life = 100
        self.alpha = 255
        self.gravity = 0.3
        self.wobble = random.uniform(0, math.pi * 2)
        self.wobble_speed = random.uniform(0.08, 0.15)
        self.pulse = 0
        self.pulse_speed = random.uniform(0.1, 0.3)
        
    def get_emoticon(self, type, connector_data):
        emoticon_sets = {
            'success': ['✅', '🎉', '🌟', '💫', '🔥', '✨', '💎', '🏆'],
            'error': ['❌', '💥', '⚠️', '🔴', '🚫', '💔', '😵'],
            'button': ['⚡', '💠', '🔷', '🔶', '💫', '✨', '⭐'],
            'connector': [connector_data['emoji']] if connector_data else ['🔗'],
            'language': ['🇺🇸', '🇪🇸', '🌍', '🔤', '📚', '✏️'],
            'sentence': ['📝', '🔤', '💬', '🗣️', '📄', '📖']
        }
        return random.choice(emoticon_sets.get(type, ['⭐']))
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rotation += self.rotation_speed
        self.life -= 2
        self.alpha = int(255 * (self.life / 100))
        self.wobble += self.wobble_speed
        self.pulse += self.pulse_speed
        
        # Efecto de wobble lateral
        self.x += math.sin(self.wobble) * 0.8
        
        return self.life > 0 and self.alpha > 0
    
    def draw(self, surface):
        # Tamaño con efecto de pulso
        pulse_size = self.size + math.sin(self.pulse) * 3
        font = pygame.font.SysFont('segoeuiemoji', int(pulse_size))
        text_surf = font.render(self.emoticon, True, (255, 255, 255))
        
        # Rotación
        rotated_surf = pygame.transform.rotate(text_surf, self.rotation)
        
        # Aplicar alpha
        rotated_surf.set_alpha(self.alpha)
        
        # Efecto de glow para partículas brillantes
        if self.alpha > 120:
            glow_size = int(pulse_size * 1.3)
            glow_font = pygame.font.SysFont('segoeuiemoji', glow_size)
            glow_surf = glow_font.render(self.emoticon, True, (255, 255, 200))
            glow_surf.set_alpha(self.alpha // 4)
            glow_rect = glow_surf.get_rect(center=(self.x, self.y))
            surface.blit(glow_surf, glow_rect)
        
        text_rect = rotated_surf.get_rect(center=(self.x, self.y))
        surface.blit(rotated_surf, text_rect)

class SentenceCard:
    def __init__(self, x, y, width, height, sentence_data, show_compound=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.sentence_data = sentence_data
        self.show_compound = show_compound
        self.revealed = False
        self.wobble = random.uniform(0, math.pi * 2)
        self.glow_color = (100, 150, 200)
        self.particles = []
        self.pulse = 0
        
    def update(self, mouse_pos, mouse_click):
        self.wobble += 0.04
        self.pulse += 0.05
        
        # Efecto de hover
        if self.rect.collidepoint(mouse_pos):
            self.glow_color = tuple(min(c + 3, 200) for c in self.glow_color)
            
            # Crear partículas de hover
            if random.random() < 0.1:
                self.create_hover_particles()
        else:
            self.glow_color = tuple(max(c - 2, 80) for c in self.glow_color)
        
        # Actualizar partículas
        self.particles = [p for p in self.particles if p.update()]
        
        return False  # Las tarjetas de oración no son clickeables en este diseño
    
    def create_hover_particles(self):
        x = random.randint(self.rect.left + 20, self.rect.right - 20)
        y = self.rect.bottom - 10
        self.particles.append(EmoticonParticle(x, y, 'sentence'))
    
    def draw(self, surface):
        # Efecto de wobble
        wobble_offset = math.sin(self.wobble) * 2
        pulse_alpha = int(50 + math.sin(self.pulse) * 20)
        
        # Fondo glassmorphism
        glass_surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        
        # Gradiente de fondo
        for i in range(self.rect.height):
            alpha = 120 - int(i / self.rect.height * 70)
            color = (*self.glow_color, alpha)
            pygame.draw.line(glass_surf, color, (0, i), (self.rect.width, i))
        
        # Borde glass con efecto de pulso
        border_color = (255, 255, 255, pulse_alpha)
        pygame.draw.rect(glass_surf, border_color, glass_surf.get_rect(), 3, border_radius=12)
        
        surface.blit(glass_surf, (self.rect.x, self.rect.y + wobble_offset))
        
        # Contenido de la tarjeta
        content_rect = self.rect.move(0, int(wobble_offset))
        
        # Título según el tipo de oración
        title_text = "Oración Compuesta 🏗️" if self.show_compound else "Oraciones Simples 📝"
        title_surf = main_font.render(title_text, True, COLORS['text_light'])
        surface.blit(title_surf, (content_rect.x + 20, content_rect.y + 15))
        
        # Oraciones
        y_offset = content_rect.y + 50
        
        if self.show_compound:
            # Mostrar oración compuesta
            spanish_text = f"🇪🇸 {self.sentence_data['spanish_compound']}"
            english_text = f"🇺🇸 {self.sentence_data['english_compound']}"
            
            # Destacar el conector
            connector_es = self.sentence_data['connector_spanish']
            connector_en = self.sentence_data['connector_english']
            
            # Dividir y resaltar
            parts_es = spanish_text.split(connector_es)
            if len(parts_es) == 2:
                part1 = main_font.render(parts_es[0], True, COLORS['text_light'])
                connector = main_font.render(connector_es, True, (255, 255, 100))
                part2 = main_font.render(parts_es[1], True, COLORS['text_light'])
                
                surface.blit(part1, (content_rect.x + 20, y_offset))
                connector_rect = connector.get_rect(midleft=(content_rect.x + 20 + part1.get_width(), y_offset))
                surface.blit(connector, connector_rect)
                surface.blit(part2, (content_rect.x + 20 + part1.get_width() + connector.get_width(), y_offset))
            else:
                text_surf = main_font.render(spanish_text, True, COLORS['text_light'])
                surface.blit(text_surf, (content_rect.x + 20, y_offset))
            
            y_offset += 35
            
            # Inglés
            parts_en = english_text.split(connector_en)
            if len(parts_en) == 2:
                part1 = main_font.render(parts_en[0], True, (200, 200, 255))
                connector = main_font.render(connector_en, True, (255, 255, 150))
                part2 = main_font.render(parts_en[1], True, (200, 200, 255))
                
                surface.blit(part1, (content_rect.x + 20, y_offset))
                connector_rect = connector.get_rect(midleft=(content_rect.x + 20 + part1.get_width(), y_offset))
                surface.blit(connector, connector_rect)
                surface.blit(part2, (content_rect.x + 20 + part1.get_width() + connector.get_width(), y_offset))
            else:
                text_surf = main_font.render(english_text, True, (200, 200, 255))
                surface.blit(text_surf, (content_rect.x + 20, y_offset))
        else:
            # Mostrar oraciones simples
            spanish_text = f"🇪🇸 {self.sentence_data['spanish_simple']}"
            english_text = f"🇺🇸 {self.sentence_data['english_simple']}"
            
            text_surf = main_font.render(spanish_text, True, COLORS['text_light'])
            surface.blit(text_surf, (content_rect.x + 20, y_offset))
            
            y_offset += 30
            
            text_surf = main_font.render(english_text, True, (200, 200, 255))
            surface.blit(text_surf, (content_rect.x + 20, y_offset))
        
        # Dibujar partículas
        for particle in self.particles:
            particle.draw(surface)

class AnimatedBackground:
    def __init__(self):
        self.time = 0
        self.stars = []
        self.gradient_points = []
        self.floating_emoticons = []
        self.generate_stars(150)
        self.generate_gradient_points(15)
        self.generate_floating_emoticons(20)
        
    def generate_stars(self, count):
        for _ in range(count):
            self.stars.append({
                'x': random.uniform(0, WIDTH),
                'y': random.uniform(0, HEIGHT),
                'size': random.uniform(0.5, 3),
                'speed': random.uniform(0.1, 0.8),
                'brightness': random.uniform(0.2, 1.0),
                'twinkle_speed': random.uniform(0.02, 0.1)
            })
    
    def generate_gradient_points(self, count):
        for _ in range(count):
            self.gradient_points.append({
                'x': random.uniform(0, WIDTH),
                'y': random.uniform(0, HEIGHT),
                'radius': random.uniform(50, 400),
                'color': random.choice(COLORS['rainbow']),
                'speed_x': random.uniform(-0.3, 0.3),
                'speed_y': random.uniform(-0.3, 0.3)
            })
    
    def generate_floating_emoticons(self, count):
        emoticons = ['📝', '🔤', '💬', '🗣️', '📚', '✏️', '🔗', '🏗️', '🇪🇸', '🇺🇸']
        for _ in range(count):
            self.floating_emoticons.append({
                'x': random.uniform(0, WIDTH),
                'y': random.uniform(0, HEIGHT),
                'emoticon': random.choice(emoticons),
                'size': random.uniform(20, 60),
                'speed_x': random.uniform(-0.5, 0.5),
                'speed_y': random.uniform(-0.2, 0.2),
                'rotation': random.uniform(0, 360),
                'rotation_speed': random.uniform(-1, 1)
            })
    
    def update(self):
        self.time += 0.02
        
        # Mover estrellas
        for star in self.stars:
            star['y'] += star['speed']
            if star['y'] > HEIGHT:
                star['y'] = 0
                star['x'] = random.uniform(0, WIDTH)
        
        # Mover puntos de gradiente
        for point in self.gradient_points:
            point['x'] += point['speed_x']
            point['y'] += point['speed_y']
            
            # Rebotar en bordes
            if point['x'] < 0 or point['x'] > WIDTH:
                point['speed_x'] *= -1
            if point['y'] < 0 or point['y'] > HEIGHT:
                point['speed_y'] *= -1
        
        # Mover emoticonos flotantes
        for emoji in self.floating_emoticons:
            emoji['x'] += emoji['speed_x']
            emoji['y'] += emoji['speed_y']
            emoji['rotation'] += emoji['rotation_speed']
            
            # Rebotar suavemente
            if emoji['x'] < -50 or emoji['x'] > WIDTH + 50:
                emoji['speed_x'] *= -1
            if emoji['y'] < -50 or emoji['y'] > HEIGHT + 50:
                emoji['speed_y'] *= -1
    
    def draw(self, surface):
        # Fondo base con gradiente animado
        for y in range(0, HEIGHT, 3):
            progress = (y + self.time * 20) % HEIGHT / HEIGHT
            r = int(COLORS['background'][0][0] + 
                   (COLORS['background'][1][0] - COLORS['background'][0][0]) * progress)
            g = int(COLORS['background'][0][1] + 
                   (COLORS['background'][1][1] - COLORS['background'][0][1]) * progress)
            b = int(COLORS['background'][0][2] + 
                   (COLORS['background'][1][2] - COLORS['background'][0][2]) * progress)
            
            # Efecto de onda más pronunciado
            wave = math.sin(self.time * 2 + y * 0.02) * 15
            pygame.draw.line(surface, (r, g, b), (0, y + wave), (WIDTH, y + wave), 3)
        
        # Puntos de gradiente radial con movimiento
        for point in self.gradient_points:
            for r in range(int(point['radius']), 0, -15):
                alpha = int(40 * (1 - r / point['radius']))
                color = (*point['color'], alpha)
                pygame.gfxdraw.filled_circle(surface, int(point['x']), int(point['y']), r, color)
        
        # Estrellas titilantes
        for star in self.stars:
            twinkle = 0.7 + 0.3 * math.sin(self.time * 10 * star['twinkle_speed'])
            brightness = star['brightness'] * twinkle
            color = (int(255 * brightness), int(255 * brightness), int(220 * brightness))
            pygame.draw.circle(surface, color, (int(star['x'])), int(star['y'])),int(star['size'])
        
        # Emoticonos flotantes
        for emoji in self.floating_emoticons:
            font = pygame.font.SysFont('segoeuiemoji', int(emoji['size']))
            text_surf = font.render(emoji['emoticon'], True, (255, 255, 255, 100))
            rotated_surf = pygame.transform.rotate(text_surf, emoji['rotation'])
            text_rect = rotated_surf.get_rect(center=(emoji['x'], emoji['y']))
            surface.blit(rotated_surf, text_rect)

class CompoundSentenceGame:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = AnimatedBackground()
        self.particles = []
        self.current_sentence = None
        self.buttons = []
        self.sentence_card = None
        self.result_card = None
        self.score = 0
        self.streak = 0
        self.level = 1
        self.game_state = "showing_simple"  # showing_simple, choosing_connector, showing_result
        
        self.setup_game()
        self.load_new_sentence()
    
    def setup_game(self):
        # Botones de control principal
        button_width, button_height = 300, 70
        spacing = 15
        
        self.buttons.append(RainbowButton(
            WIDTH//2 - button_width//2, 750, button_width, button_height,
            "Mostrar Oración Compuesta", "🏗️", self.show_compound_sentence
        ))
        
        self.buttons.append(RainbowButton(
            WIDTH//2 - button_width//2, 750 + button_height + spacing, 
            button_width, button_height, "Siguiente Oración", "➡️", self.next_sentence
        ))
    
    def load_new_sentence(self):
        # Seleccionar oración aleatoria según el nivel
        if self.level == 1:
            available_sentences = [s for s in SENTENCE_DATABASE if s['difficulty'] == 'easy']
        elif self.level == 2:
            available_sentences = [s for s in SENTENCE_DATABASE if s['difficulty'] in ['easy', 'medium']]
        else:
            available_sentences = SENTENCE_DATABASE
        
        self.current_sentence = random.choice(available_sentences)
        self.game_state = "showing_simple"
        
        # Crear tarjeta de oraciones simples
        self.sentence_card = SentenceCard(100, 150, WIDTH - 200, 180, self.current_sentence, False)
        
        # Crear botones de conectores
        self.create_connector_buttons()
    
    def create_connector_buttons(self):
        # Limpiar botones de conectores anteriores
        self.buttons = [btn for btn in self.buttons if btn.connector_data is None]
        
        # Obtener conectores del tipo correcto y algunos incorrectos
        correct_type = self.current_sentence['connector_type']
        correct_connectors = CONNECTORS_BY_TYPE[correct_type]
        
        # Mezclar algunos conectores incorrectos
        incorrect_connectors = []
        for conn_type, connectors in CONNECTORS_BY_TYPE.items():
            if conn_type != correct_type:
                incorrect_connectors.extend(connectors)
        
        # Seleccionar 3 incorrectos aleatorios
        selected_incorrect = random.sample(incorrect_connectors, min(3, len(incorrect_connectors)))
        
        # Combinar y mezclar
        all_connectors = correct_connectors + selected_incorrect
        random.shuffle(all_connectors)
        
        # Crear botones de conectores
        button_width, button_height = 280, 80
        start_x = WIDTH // 2 - (len(all_connectors) * button_width + (len(all_connectors) - 1) * 20) // 2
        
        for i, connector in enumerate(all_connectors):
            x = start_x + i * (button_width + 20)
            y = 400
            
            # Verificar si es el conector correcto
            is_correct = (connector['es'] == self.current_sentence['connector_spanish'])
            
            self.buttons.append(RainbowButton(
                x, y, button_width, button_height,
                connector['es'], connector['emoji'],
                lambda c=connector, correct=is_correct: self.connector_selected(c, correct),
                connector
            ))
    
    def show_compound_sentence(self):
        self.game_state = "choosing_connector"
    
    def connector_selected(self, connector, is_correct):
        if is_correct:
            self.score += 10 * self.level
            self.streak += 1
            if self.streak % 5 == 0:
                self.level = min(self.level + 1, 3)
            self.create_particles(WIDTH//2, 300, 25, 'success')
        else:
            self.streak = 0
            self.create_particles(WIDTH//2, 300, 20, 'error')
        
        self.game_state = "showing_result"
        
        # Crear tarjeta de resultado
        self.result_card = SentenceCard(100, 500, WIDTH - 200, 200, self.current_sentence, True)
    
    def next_sentence(self):
        self.load_new_sentence()
        self.create_particles(WIDTH//2, HEIGHT//2, 15, 'sentence')
    
    def create_particles(self, x, y, count, type):
        for _ in range(count):
            self.particles.append(EmoticonParticle(x, y, type))
    
    def draw_interface(self):
        # Panel superior glassmorphism
        glass_surf = pygame.Surface((WIDTH, 120), pygame.SRCALPHA)
        pygame.draw.rect(glass_surf, (255, 255, 255, 60), glass_surf.get_rect())
        pygame.draw.line(glass_surf, (255, 255, 255, 120), (0, 0), (WIDTH, 0), 4)
        screen.blit(glass_surf, (0, 0))
        
        # Título
        title_text = title_font.render("🏗️ Compound Sentence Master 📚", True, COLORS['text_light'])
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))
        
        # Información del juego
        info_text = main_font.render(
            f"Nivel: {self.level} 🌟 | Puntuación: {self.score} ⭐ | Racha: {self.streak} 🔥", 
            True, (255, 255, 200)
        )
        screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, 85))
        
        # Instrucciones según el estado del juego
        if self.game_state == "showing_simple":
            instruction_es = main_font.render(
                "Observa las oraciones simples. Luego elige el conector correcto.", 
                True, (200, 255, 200)
            )
            instruction_en = main_font.render(
                "Observe the simple sentences. Then choose the correct connector.", 
                True, (200, 200, 255)
            )
        elif self.game_state == "choosing_connector":
            instruction_es = main_font.render(
                "¡Elige el conector correcto para unir las oraciones! 💡", 
                True, (255, 255, 150)
            )
            instruction_en = main_font.render(
                "Choose the correct connector to join the sentences! 💡", 
                True, (255, 255, 150)
            )
        else:  # showing_result
            instruction_es = main_font.render(
                f"Conector: {self.current_sentence['connector_spanish']} - {self.current_sentence['explanation_es']}", 
                True, (200, 255, 200)
            )
            instruction_en = main_font.render(
                f"Connector: {self.current_sentence['connector_english']} - {self.current_sentence['explanation_en']}", 
                True, (200, 200, 255)
            )
        
        screen.blit(instruction_es, (WIDTH//2 - instruction_es.get_width()//2, 110))
        screen.blit(instruction_en, (WIDTH//2 - instruction_en.get_width()//2, 140))
    
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
                    elif event.key == pygame.K_n:
                        self.next_sentence()
                    elif event.key == pygame.K_SPACE:
                        if self.game_state == "showing_simple":
                            self.show_compound_sentence()
            
            # Actualizar
            self.background.update()
            self.particles = [p for p in self.particles if p.update()]
            
            # Actualizar elementos según el estado del juego
            if self.sentence_card:
                self.sentence_card.update(mouse_pos, mouse_click)
            
            if self.result_card and self.game_state == "showing_result":
                self.result_card.update(mouse_pos, mouse_click)
            
            # Actualizar y verificar botones
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
            
            # Dibujar tarjetas de oración
            if self.sentence_card:
                self.sentence_card.draw(screen)
            
            # Dibujar tarjeta de resultado si es necesario
            if self.result_card and self.game_state == "showing_result":
                self.result_card.draw(screen)
            
            # Dibujar botones según el estado del juego
            for button in self.buttons:
                # Mostrar solo los botones relevantes para el estado actual
                if self.game_state == "showing_simple":
                    if button.text == "Mostrar Oración Compuesta":
                        button.draw(screen)
                elif self.game_state == "choosing_connector":
                    if button.connector_data is not None:  # Botones de conectores
                        button.draw(screen)
                else:  # showing_result
                    if button.text == "Siguiente Oración":
                        button.draw(screen)
            
            # Efectos de partículas aleatorias de fondo
            if random.random() < 0.02:
                x = random.randint(0, WIDTH)
                self.create_particles(x, HEIGHT + 50, 2, random.choice(['language', 'sentence']))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    game = CompoundSentenceGame()
    game.run()
