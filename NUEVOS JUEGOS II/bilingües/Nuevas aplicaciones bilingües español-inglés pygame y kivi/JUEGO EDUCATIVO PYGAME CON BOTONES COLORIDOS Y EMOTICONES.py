import pygame
import sys
import random
import math
from datetime import datetime
from pygame import mixer

# Inicializar Pygame
pygame.init()
mixer.init()

# Configuración de pantalla
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Paleta de colores VIBRANTE con emoticones
COLORS = {
    # Colores principales - Tema ARCOÍRIS
    'rainbow_red': (255, 89, 94),
    'rainbow_orange': (255, 157, 89),
    'rainbow_yellow': (255, 212, 89),
    'rainbow_green': (138, 201, 38),
    'rainbow_blue': (25, 130, 196),
    'rainbow_purple': (106, 76, 147),
    'rainbow_pink': (255, 101, 132),
    
    # Colores de fondo y UI
    'background_gradient_1': (255, 245, 245),
    'background_gradient_2': (230, 240, 255),
    'panel_light': (255, 255, 255, 180),
    'panel_dark': (40, 44, 52, 220),
    
    # Colores de texto
    'text_white': (255, 255, 255),
    'text_black': (40, 44, 52),
    'text_gray': (120, 124, 132),
    
    # Colores de botones por función
    'btn_success': (46, 204, 113),
    'btn_warning': (241, 196, 15),
    'btn_danger': (231, 76, 60),
    'btn_info': (52, 152, 219),
    'btn_primary': (155, 89, 182),
    
    # Estados de botones
    'btn_hover_light': (255, 255, 255, 50),
    'btn_hover_dark': (0, 0, 0, 30),
}

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🌈 English Fun Trainer - ¡Aprende Inglés Divirtiéndote! 🎮")
clock = pygame.time.Clock()

# Emoticones para diferentes estados y acciones
EMOTICONS = {
    'happy': ['😊', '😄', '😁', '🤩', '🥳', '🎉', '✨', '🌟'],
    'sad': ['😢', '😞', '😔', '🙁', '💔'],
    'thinking': ['🤔', '💭', '🧠', '📚'],
    'celebrate': ['🎊', '🏆', '⭐', '💫', '🔥'],
    'learning': ['📖', '✏️', '🎓', '💡', '🔍'],
    'nature': ['🌿', '🌸', '🌼', '🐦', '🦋'],
    'buttons': ['✅', '💡', '⏭️', '📊', '🔄', '🏠', '⚙️', '🎮']
}

# Cargar fuentes
def load_fonts():
    fonts = {}
    try:
        # Intentar cargar fuentes personalizadas, fallback a fuentes del sistema
        fonts['title'] = pygame.font.Font(None, 48)
        fonts['header'] = pygame.font.Font(None, 36)
        fonts['normal'] = pygame.font.Font(None, 28)
        fonts['small'] = pygame.font.Font(None, 22)
        fonts['button'] = pygame.font.Font(None, 24)
        fonts['emoticon_large'] = pygame.font.Font(None, 64)
    except:
        # Fallback a fuentes por defecto
        fonts = {key: pygame.font.Font(None, size) for key, size in [
            ('title', 48), ('header', 36), ('normal', 28), 
            ('small', 22), ('button', 24), ('emoticon_large', 64)
        ]}
    return fonts

fonts = load_fonts()

# Clase para botones SUPER COLORIDOS con emoticones
class RainbowButton:
    def __init__(self, x, y, width, height, text, emoticon, base_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoticon = emoticon
        self.base_color = base_color
        self.action = action
        self.is_hovered = False
        self.is_clicked = False
        self.animation_progress = 0
        self.pulse_direction = 1
        
    def draw(self, surface):
        # Efecto de pulsación
        pulse = math.sin(self.animation_progress) * 5
        animated_rect = self.rect.inflate(pulse, pulse)
        
        # Color base con efecto hover
        if self.is_clicked:
            color = self.darken_color(self.base_color, 30)
        elif self.is_hovered:
            color = self.lighten_color(self.base_color, 20)
        else:
            color = self.base_color
        
        # Dibujar botón con bordes redondeados
        self.draw_rounded_rect(surface, animated_rect, color, 15)
        
        # Efecto de brillo en hover
        if self.is_hovered:
            glow_color = self.lighten_color(color, 40)
            self.draw_rounded_rect(surface, animated_rect.inflate(8, 8), glow_color, 18, alpha=80)
        
        # Texto y emoticón
        text_color = COLORS['text_white'] if self.is_dark_color(color) else COLORS['text_black']
        
        # Emoticono
        emoticon_surf = fonts['emoticon_large'].render(self.emoticon, True, text_color)
        emoticon_rect = emoticon_surf.get_rect(center=(animated_rect.centerx, animated_rect.centery - 15))
        surface.blit(emoticon_surf, emoticon_rect)
        
        # Texto
        text_surf = fonts['button'].render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=(animated_rect.centerx, animated_rect.centery + 20))
        surface.blit(text_surf, text_rect)
        
    def draw_rounded_rect(self, surface, rect, color, radius, alpha=255):
        """Dibujar rectángulo con bordes redondeados"""
        if alpha < 255:
            # Crear superficie temporal para alpha
            temp_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
            pygame.draw.rect(temp_surface, (*color, alpha), (0, 0, *rect.size), border_radius=radius)
            surface.blit(temp_surface, rect)
        else:
            pygame.draw.rect(surface, color, rect, border_radius=radius)
        
        # Borde
        pygame.draw.rect(surface, self.darken_color(color, 20), rect, 2, border_radius=radius)
    
    def update(self):
        # Animación de pulsación
        self.animation_progress += 0.1
        if self.animation_progress > 2 * math.pi:
            self.animation_progress = 0
    
    def check_hover(self, pos):
        was_hovered = self.is_hovered
        self.is_hovered = self.rect.collidepoint(pos)
        
        # Efecto de sonido al entrar/salir del hover
        if was_hovered != self.is_hovered and self.is_hovered:
            self.play_hover_sound()
        return self.is_hovered
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                self.is_clicked = True
                self.play_click_sound()
                if self.action:
                    return self.action()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_clicked = False
        return None
    
    def lighten_color(self, color, amount):
        return tuple(min(255, c + amount) for c in color)
    
    def darken_color(self, color, amount):
        return tuple(max(0, c - amount) for c in color)
    
    def is_dark_color(self, color):
        # Calcular luminosidad (fórmula estándar)
        luminance = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
        return luminance < 128
    
    def play_hover_sound(self):
        # Efecto de sonido simple (podría cargarse un archivo)
        try:
            pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytes([128] * 100)))
        except:
            pass
    
    def play_click_sound(self):
        try:
            pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytes([200] * 50)))
        except:
            pass

# Clase mejorada para cajas de texto con emoticones
class FunTextInput:
    def __init__(self, x, y, width, height, placeholder="", emoticon="✏️"):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
        self.emoticon = emoticon
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0
        self.shake_offset = 0
        self.shake_timer = 0
        
    def draw(self, surface):
        # Efecto de shake cuando está activo
        draw_rect = self.rect.move(self.shake_offset, 0)
        
        # Fondo con gradiente
        self.draw_gradient_background(surface, draw_rect)
        
        # Borde colorido
        border_color = random.choice(list(COLORS.values())[:6]) if self.active else COLORS['text_gray']
        pygame.draw.rect(surface, border_color, draw_rect, 3, border_radius=10)
        
        # Emoticono
        emoticon_surf = fonts['normal'].render(self.emoticon, True, COLORS['text_black'])
        surface.blit(emoticon_surf, (draw_rect.x + 15, draw_rect.centery - 10))
        
        # Texto
        text_color = COLORS['text_black']
        display_text = self.text if self.text else self.placeholder
        text_alpha = 255 if self.text else 128
        
        text_surf = fonts['normal'].render(display_text, True, text_color)
        text_surf.set_alpha(text_alpha)
        text_rect = text_surf.get_rect(midleft=(draw_rect.x + 50, draw_rect.centery))
        surface.blit(text_surf, text_rect)
        
        # Cursor animado
        if self.active and self.cursor_visible:
            cursor_x = text_rect.right + 5
            pygame.draw.line(surface, COLORS['rainbow_pink'], 
                           (cursor_x, draw_rect.y + 15), 
                           (cursor_x, draw_rect.y + draw_rect.height - 15), 3)
    
    def draw_gradient_background(self, surface, rect):
        for i in range(rect.height):
            # Gradiente suave
            ratio = i / rect.height
            r = int(255 * (1 - ratio) + 240 * ratio)
            g = int(255 * (1 - ratio) + 248 * ratio)
            b = int(255 * (1 - ratio) + 255 * ratio)
            pygame.draw.line(surface, (r, g, b), (rect.x, rect.y + i), (rect.x + rect.width, rect.y + i))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            if self.active:
                self.trigger_shake()
            
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.trigger_shake()
            else:
                self.text += event.unicode
                self.trigger_shake()
                
        return None
    
    def update(self):
        # Animación del cursor
        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0
        
        # Animación de shake
        if self.shake_timer > 0:
            self.shake_timer -= 1
            self.shake_offset = math.sin(self.shake_timer) * 3
        else:
            self.shake_offset = 0
    
    def trigger_shake(self):
        self.shake_timer = 10

# Sistema de partículas MEJORADO con emoticones
class EmoticonParticle:
    def __init__(self, x, y, particle_type="star"):
        self.x = x
        self.y = y
        self.type = particle_type
        self.size = random.randint(20, 40)
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-4, -1)
        self.lifetime = random.randint(40, 80)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        self.emoticon = self.get_emoticon()
        
    def get_emoticon(self):
        if self.type == "star":
            return random.choice(['⭐', '🌟', '✨', '💫'])
        elif self.type == "celebration":
            return random.choice(['🎉', '🎊', '🥳', '😄'])
        elif self.type == "heart":
            return random.choice(['💖', '💕', '💓', '💗'])
        else:
            return random.choice(['✨', '🌟', '💫', '⭐'])
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        self.angle += self.rotation_speed
        self.size = max(5, self.size - 0.2)
        return self.lifetime > 0
        
    def draw(self, surface):
        emoticon_surf = fonts['emoticon_large'].render(self.emoticon, True, COLORS['rainbow_yellow'])
        
        # Rotar el emoticón
        rotated_surf = pygame.transform.rotate(emoticon_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(int(self.x), int(self.y)))
        
        surface.blit(rotated_surf, rotated_rect)

class EnhancedParticleSystem:
    def __init__(self):
        self.particles = []
        
    def add_emoticon_particles(self, x, y, particle_type="star", count=15):
        for _ in range(count):
            self.particles.append(EmoticonParticle(x, y, particle_type))
            
    def update(self):
        self.particles = [p for p in self.particles if p.update()]
        
    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

# Clase principal del juego MEJORADA
class EnglishFunTrainer:
    def __init__(self):
        self.current_exercise = 0
        self.score = 0
        self.total_exercises = 30
        self.start_time = datetime.now()
        self.hints_used = 0
        self.streak = 0
        self.max_streak = 0
        self.particles = EnhancedParticleSystem()
        self.feedback_text = ""
        self.feedback_emoticon = ""
        self.feedback_timer = 0
        self.feedback_color = COLORS['rainbow_blue']
        self.current_emoticon = random.choice(EMOTICONS['happy'])
        self.exercises = self.generate_fun_exercises()
        self.background_offset = 0
        
        # Botones COLORIDOS con emoticones
        self.answer_input = FunTextInput(250, 400, 700, 70, "Escribe tu respuesta aquí...", "✏️")
        
        self.submit_button = RainbowButton(400, 500, 200, 80, "Verificar", "✅", COLORS['btn_success'], self.check_answer)
        self.hint_button = RainbowButton(650, 500, 200, 80, "Pista", "💡", COLORS['btn_warning'], self.show_hint)
        self.skip_button = RainbowButton(400, 600, 200, 80, "Saltar", "⏭️", COLORS['btn_danger'], self.next_exercise)
        self.stats_button = RainbowButton(650, 600, 200, 80, "Estadísticas", "📊", COLORS['btn_info'], self.show_stats)
        
        # Efectos de sonido simples
        self.setup_audio()
        
    def setup_audio(self):
        """Configurar efectos de audio simples"""
        try:
            # Crear sonidos básicos programáticamente
            self.correct_sound = pygame.mixer.Sound(buffer=bytes([100] * 200))
            self.incorrect_sound = pygame.mixer.Sound(buffer=bytes([50] * 100))
        except:
            self.correct_sound = self.incorrect_sound = None
    
    def generate_fun_exercises(self):
        """Generar ejercicios divertidos con emoticones"""
        base_exercises = [
            {
                "type": "🔤 Preguntas con 'to be'",
                "instruction": "Convierte esta afirmación en pregunta: 🎯",
                "spanish": "Él es un profesor muy bueno 👨‍🏫",
                "correct_answer": "Is he a very good teacher?",
                "hint": "💡 Recuerda: Verbo + Sujeto + Complemento",
                "difficulty": "🟢 Básico",
                "explanation": "En inglés invertimos el orden para preguntas ✨"
            },
            {
                "type": "🔄 Preguntas con Do/Does", 
                "instruction": "Convierte usando Do/Does: 🎯",
                "spanish": "Ella trabaja en una oficina grande 🏢",
                "correct_answer": "Does she work in a big office?",
                "hint": "💡 Para he/she/it usa DOES + verbo base",
                "difficulty": "🟡 Intermedio",
                "explanation": "¡No olvides el auxiliar! Es clave 🔑"
            },
            {
                "type": "❓ Preguntas WH-",
                "instruction": "Formula una pregunta con WHAT: 🎯",
                "spanish": "RESPUESTA: I want pizza for dinner 🍕",
                "correct_answer": "What do you want for dinner?",
                "hint": "💡 Estructura: What + do/does + sujeto + verbo",
                "difficulty": "🔴 Avanzado",
                "explanation": "Las preguntas WH- siguen un patrón específico 📐"
            }
        ]
        
        exercises = []
        for i in range(self.total_exercises):
            exercise = random.choice(base_exercises).copy()
            
            # Variar el contenido
            variations = [
                {"profesor": "médico", "oficina": "hospital", "pizza": "sushi", "🍕": "🍣"},
                {"trabaja": "estudia", "bueno": "excelente", "grande": "moderna"},
                {"es": "era", "trabaja": "enseña", "want": "would like"}
            ]
            
            variation = variations[i % len(variations)]
            for orig, new in variation.items():
                exercise["spanish"] = exercise["spanish"].replace(orig, new)
                exercise["correct_answer"] = exercise["correct_answer"].replace(orig, new)
            
            exercises.append(exercise)
        
        return exercises
    
    def draw_animated_background(self):
        """Dibujar fondo animado con gradientes y formas"""
        self.background_offset += 0.5
        
        # Gradiente animado
        for y in range(SCREEN_HEIGHT):
            ratio = (y + self.background_offset) % SCREEN_HEIGHT / SCREEN_HEIGHT
            r = int(255 * (1 - ratio) + 135 * ratio)
            g = int(206 * (1 - ratio) + 206 * ratio)
            b = int(235 * (1 - ratio) + 235 * ratio)
            pygame.draw.line(screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Formas decorativas animadas
        time = pygame.time.get_ticks() / 1000
        for i in range(20):
            x = (i * 100 + time * 50) % (SCREEN_WIDTH + 200) - 100
            y = 100 + math.sin(time + i) * 50
            size = 30 + math.sin(time * 2 + i) * 10
            
            color_index = (i + int(time * 10)) % 6
            color = list(COLORS.values())[color_index]
            
            # Dibujar círculos decorativos
            pygame.draw.circle(screen, (*color, 100), (int(x), int(y)), int(size))
    
    def draw_progress_rainbow(self):
        """Dibujar barra de progreso tipo arcoíris"""
        progress = min(1.0, self.current_exercise / self.total_exercises)
        bar_width = 800
        bar_height = 30
        bar_x = (SCREEN_WIDTH - bar_width) // 2
        bar_y = 80
        
        # Fondo de la barra
        pygame.draw.rect(screen, COLORS['panel_dark'], (bar_x, bar_y, bar_width, bar_height), border_radius=15)
        
        # Barra de progreso con gradiente arcoíris
        if progress > 0:
            progress_width = int(bar_width * progress)
            for i in range(progress_width):
                color_ratio = i / bar_width
                color_index = int(color_ratio * 6) % 6
                color = list(COLORS.values())[color_index]
                pygame.draw.rect(screen, color, (bar_x + i, bar_y, 1, bar_height))
        
        # Emoticono de progreso
        progress_emoticon = "🚀" if progress > 0.7 else "🎯" if progress > 0.3 else "🐢"
        emoticon_surf = fonts['normal'].render(progress_emoticon, True, COLORS['text_white'])
        screen.blit(emoticon_surf, (bar_x + int(bar_width * progress) - 10, bar_y - 5))
        
        # Texto de progreso
        progress_text = f"🌈 Progreso: {self.current_exercise}/{self.total_exercises}"
        text_surf = fonts['small'].render(progress_text, True, COLORS['text_white'])
        screen.blit(text_surf, (bar_x, bar_y + 35))
    
    def draw_animated_stats(self):
        """Dibujar estadísticas con animaciones"""
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        
        stats_data = [
            (f"⭐ {self.score} Puntos", "💎"),
            (f"🔥 {self.streak} Racha", "🚀"),
            (f"⏱️ {minutes:02d}:{seconds:02d}", "⏰"),
            (f"💡 {self.hints_used} Pistas", "🔍")
        ]
        
        for i, (stat, emoticon) in enumerate(stats_data):
            # Fondo para cada estadística
            stat_rect = pygame.Rect(50, 150 + i * 70, 200, 50)
            pygame.draw.rect(screen, (*COLORS['rainbow_purple'], 150), stat_rect, border_radius=10)
            
            # Emoticono
            emoticon_surf = fonts['normal'].render(emoticon, True, COLORS['text_white'])
            screen.blit(emoticon_surf, (stat_rect.x + 15, stat_rect.centery - 10))
            
            # Texto
            text_surf = fonts['small'].render(stat, True, COLORS['text_white'])
            screen.blit(text_surf, (stat_rect.x + 50, stat_rect.centery - 10))
    
    def draw_exercise_card(self):
        """Dibujar tarjeta de ejercicio con diseño atractivo"""
        if self.current_exercise >= len(self.exercises):
            return
            
        exercise = self.exercises[self.current_exercise]
        
        # Tarjeta principal con efecto glassmorphism
        card_rect = pygame.Rect(200, 180, 800, 200)
        self.draw_glass_card(screen, card_rect)
        
        # Encabezado de la tarjeta
        header_rect = pygame.Rect(card_rect.x, card_rect.y, card_rect.width, 50)
        pygame.draw.rect(screen, (*COLORS['rainbow_blue'], 200), header_rect, border_radius=10)
        
        # Tipo y dificultad
        type_surf = fonts['header'].render(exercise['type'], True, COLORS['text_white'])
        screen.blit(type_surf, (header_rect.x + 20, header_rect.centery - 15))
        
        # Dificultad con color
        diff_color = COLORS['rainbow_green'] if 'Básico' in exercise['difficulty'] else \
                    COLORS['rainbow_yellow'] if 'Intermedio' in exercise['difficulty'] else \
                    COLORS['rainbow_red']
        
        diff_surf = fonts['small'].render(exercise['difficulty'], True, diff_color)
        screen.blit(diff_surf, (header_rect.right - diff_surf.get_width() - 20, header_rect.centery - 15))
        
        # Contenido del ejercicio
        instruction_surf = fonts['normal'].render(exercise['instruction'], True, COLORS['text_black'])
        screen.blit(instruction_surf, (card_rect.x + 20, card_rect.y + 70))
        
        # Oración en español con emoticón
        spanish_text = f"🇪🇸 {exercise['spanish']}"
        spanish_surf = fonts['normal'].render(spanish_text, True, COLORS['rainbow_purple'])
        screen.blit(spanish_surf, (card_rect.x + 20, card_rect.y + 110))
    
    def draw_glass_card(self, surface, rect):
        """Dibujar efecto glassmorphism"""
        # Sombra
        shadow_rect = rect.inflate(10, 10)
        pygame.draw.rect(surface, (0, 0, 0, 30), shadow_rect, border_radius=15)
        
        # Fondo glass
        glass_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(glass_surface, (255, 255, 255, 180), (0, 0, *rect.size), border_radius=10)
        
        # Efecto de brillo
        for i in range(3):
            glow_rect = pygame.Rect(i*5, i*5, rect.width-i*10, rect.height-i*10)
            pygame.draw.rect(glass_surface, (255, 255, 255, 50-i*15), glow_rect, border_radius=10)
        
        surface.blit(glass_surface, rect)
    
    def draw_fun_feedback(self):
        """Dibujar feedback animado con emoticones"""
        if self.feedback_text and self.feedback_timer > 0:
            # Calcular opacidad basada en el timer
            alpha = min(255, self.feedback_timer * 2)
            
            # Panel de feedback
            feedback_rect = pygame.Rect(300, 300, 600, 100)
            pygame.draw.rect(screen, (*self.feedback_color, alpha), feedback_rect, border_radius=20)
            pygame.draw.rect(screen, (*COLORS['text_black'], alpha), feedback_rect, 3, border_radius=20)
            
            # Emoticono
            if self.feedback_emoticon:
                emoticon_surf = fonts['emoticon_large'].render(self.feedback_emoticon, True, COLORS['text_white'])
                emoticon_rect = emoticon_surf.get_rect(center=(feedback_rect.centerx, feedback_rect.centery - 10))
                screen.blit(emoticon_surf, emoticon_rect)
            
            # Texto
            text_surf = fonts['normal'].render(self.feedback_text, True, COLORS['text_white'])
            text_rect = text_surf.get_rect(center=(feedback_rect.centerx, feedback_rect.centery + 30))
            screen.blit(text_surf, text_rect)
            
            self.feedback_timer -= 1
    
    def show_fun_feedback(self, text, emoticon, color, duration=180):
        """Mostrar feedback con emoticones"""
        self.feedback_text = text
        self.feedback_emoticon = emoticon
        self.feedback_color = color
        self.feedback_timer = duration
        
        # Efecto de sonido
        if color == COLORS['btn_success'] and self.correct_sound:
            self.correct_sound.play()
        elif color == COLORS['btn_danger'] and self.incorrect_sound:
            self.incorrect_sound.play()
    
    def check_answer(self):
        """Verificar respuesta con efectos especiales"""
        user_answer = self.answer_input.text.strip()
        if not user_answer:
            self.show_fun_feedback("¡Escribe una respuesta! 📝", "✏️", COLORS['btn_warning'])
            return
            
        exercise = self.exercises[self.current_exercise]
        
        # Verificación flexible
        def normalize(text):
            return text.lower().replace("?", "").replace("!", "").replace(".", "").strip()
        
        user_norm = normalize(user_answer)
        correct_norm = normalize(exercise['correct_answer'])
        
        is_correct = user_norm == correct_norm
        
        if is_correct:
            self.score += 20 + (self.streak * 5)
            self.streak += 1
            self.max_streak = max(self.max_streak, self.streak)
            
            # Emoticono aleatorio de celebración
            celebration_emoticon = random.choice(EMOTICONS['celebrate'])
            self.show_fun_feedback(f"¡CORRECTO! +{20 + (self.streak * 5)} puntos", 
                                 celebration_emoticon, COLORS['btn_success'])
            
            # Lluvia de partículas
            self.particles.add_emoticon_particles(SCREEN_WIDTH // 2, 200, "celebration", 25)
            
            # Siguiente ejercicio después de delay
            pygame.time.set_timer(pygame.USEREVENT, 2000)
        else:
            self.streak = 0
            self.show_fun_feedback(f"Intenta otra vez 💪", "😅", COLORS['btn_danger'])
            self.answer_input.text = ""
    
    def show_hint(self):
        """Mostrar pista divertida"""
        exercise = self.exercises[self.current_exercise]
        self.hints_used += 1
        hint_emoticon = random.choice(EMOTICONS['thinking'])
        self.show_fun_feedback(f"Pista: {exercise['hint']}", hint_emoticon, COLORS['btn_warning'], 240)
    
    def show_stats(self):
        """Mostrar estadísticas en pantalla completa temporal"""
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        accuracy = (self.score / ((self.current_exercise + 1) * 20)) * 100
        
        stats_text = [
            f"📊 ESTADÍSTICAS ACTUALES",
            f"🎯 Ejercicios: {self.current_exercise}/{self.total_exercises}",
            f"⭐ Puntuación: {self.score}",
            f"📈 Precisión: {accuracy:.1f}%",
            f"⏱️ Tiempo: {minutes:02d}:{seconds:02d}",
            f"🔥 Racha máxima: {self.max_streak}",
            f"💡 Pistas usadas: {self.hints_used}"
        ]
        
        self.show_fun_feedback("\n".join(stats_text), "📈", COLORS['btn_info'], 300)
    
    def next_exercise(self):
        """Pasar al siguiente ejercicio"""
        self.current_exercise += 1
        self.answer_input.text = ""
        
        if self.current_exercise >= len(self.exercises):
            self.show_final_celebration()
        else:
            self.show_fun_feedback("¡Siguiente ejercicio! 🚀", "➡️", COLORS['btn_primary'], 90)
    
    def show_final_celebration(self):
        """Pantalla final de celebración"""
        celebration_duration = 300  # 5 segundos a 60 FPS
        start_time = pygame.time.get_ticks()
        
        while pygame.time.get_ticks() - start_time < celebration_duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Fondo de celebración
            self.draw_animated_background()
            
            # Añadir partículas continuamente
            if random.random() < 0.3:
                self.particles.add_emoticon_particles(
                    random.randint(100, SCREEN_WIDTH-100),
                    random.randint(100, SCREEN_HEIGHT-100),
                    "celebration", 5
                )
            
            self.particles.update()
            self.particles.draw(screen)
            
            # Mensaje de celebración
            celebration_text = "🎉 ¡FELICIDADES! 🎉"
            text_surf = fonts['title'].render(celebration_text, True, COLORS['rainbow_yellow'])
            screen.blit(text_surf, (SCREEN_WIDTH//2 - text_surf.get_width()//2, SCREEN_HEIGHT//2 - 50))
            
            pygame.display.flip()
            clock.tick(FPS)
        
        # Mostrar resultados finales
        self.show_final_results()
    
    def show_final_results(self):
        """Mostrar pantalla final de resultados"""
        results_screen = True
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        accuracy = (self.score / (len(self.exercises) * 20)) * 100
        
        # Botones de resultados
        restart_btn = RainbowButton(450, 600, 150, 80, "Reiniciar", "🔄", COLORS['btn_success'])
        exit_btn = RainbowButton(650, 600, 150, 80, "Salir", "🚪", COLORS['btn_danger'])
        
        while results_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    restart_btn.check_hover(mouse_pos)
                    exit_btn.check_hover(mouse_pos)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_btn.is_hovered:
                        self.__init__()
                        return
                    elif exit_btn.is_hovered:
                        pygame.quit()
                        sys.exit()
            
            # Dibujar
            self.draw_animated_background()
            
            # Panel de resultados
            result_rect = pygame.Rect(200, 150, 800, 400)
            self.draw_glass_card(screen, result_rect)
            
            # Título
            title_text = "🏆 RESULTADOS FINALES 🏆"
            title_surf = fonts['title'].render(title_text, True, COLORS['rainbow_purple'])
            screen.blit(title_surf, (result_rect.centerx - title_surf.get_width()//2, result_rect.y + 30))
            
            # Estadísticas finales
            stats = [
                f"🎯 Ejercicios completados: {self.current_exercise}/{self.total_exercises}",
                f"⭐ Puntuación total: {self.score}",
                f"📈 Precisión: {accuracy:.1f}%",
                f"⏱️ Tiempo total: {minutes:02d}:{seconds:02d}",
                f"🔥 Racha máxima: {self.max_streak}",
                f"💡 Pistas usadas: {self.hints_used}"
            ]
            
            for i, stat in enumerate(stats):
                stat_surf = fonts['header'].render(stat, True, COLORS['text_black'])
                screen.blit(stat_surf, (result_rect.centerx - stat_surf.get_width()//2, result_rect.y + 100 + i * 50))
            
            # Evaluación final
            if accuracy >= 90:
                eval_text = "🌈 ¡EXCELENTE! Eres un genio del inglés 🌟"
            elif accuracy >= 70:
                eval_text = "🎯 ¡MUY BIEN! Dominas el inglés 🚀"
            elif accuracy >= 50:
                eval_text = "👍 ¡BIEN! Sigue practicando 💪"
            else:
                eval_text = "🌱 ¡Ánimo! La práctica hace al maestro 📚"
            
            eval_surf = fonts['normal'].render(eval_text, True, COLORS['rainbow_blue'])
            screen.blit(eval_surf, (result_rect.centerx - eval_surf.get_width()//2, result_rect.y + 350))
            
            # Botones
            restart_btn.draw(screen)
            exit_btn.draw(screen)
            
            pygame.display.flip()
            clock.tick(FPS)
    
    def run(self):
        """Bucle principal del juego"""
        running = True
        
        while running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    self.next_exercise()
                
                # Pasar eventos a los elementos UI
                self.answer_input.handle_event(event)
                self.submit_button.handle_event(event)
                self.hint_button.handle_event(event)
                self.skip_button.handle_event(event)
                self.stats_button.handle_event(event)
                
                # Tecla Enter para enviar
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.check_answer()
            
            # Actualizar
            mouse_pos = pygame.mouse.get_pos()
            self.submit_button.check_hover(mouse_pos)
            self.hint_button.check_hover(mouse_pos)
            self.skip_button.check_hover(mouse_pos)
            self.stats_button.check_hover(mouse_pos)
            
            self.answer_input.update()
            self.submit_button.update()
            self.hint_button.update()
            self.skip_button.update()
            self.stats_button.update()
            self.particles.update()
            
            # Dibujar
            self.draw_animated_background()
            self.draw_progress_rainbow()
            self.draw_animated_stats()
            
            if self.current_exercise < len(self.exercises):
                self.draw_exercise_card()
                self.answer_input.draw(screen)
                self.submit_button.draw(screen)
                self.hint_button.draw(screen)
                self.skip_button.draw(screen)
                self.stats_button.draw(screen)
            
            self.draw_fun_feedback()
            self.particles.draw(screen)
            
            # Actualizar pantalla
            pygame.display.flip()
            clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    print("🎮 Iniciando English Fun Trainer...")
    print("🌈 ¡Prepárate para aprender inglés divirtiéndote!")
    game = EnglishFunTrainer()
    game.run()
