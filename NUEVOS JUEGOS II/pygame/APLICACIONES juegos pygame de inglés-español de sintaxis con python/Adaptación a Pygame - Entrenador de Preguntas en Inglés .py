import pygame
import sys
import random
import math
from datetime import datetime
from pygame import mixer

# Inicializar Pygame
pygame.init()
mixer.init()

# Constantes de pantalla
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colores (paleta de naturaleza mejorada)
COLORS = {
    'forest_dark': (45, 90, 39),
    'forest_medium': (74, 124, 89),
    'forest_light': (143, 185, 150),
    'sky_dark': (30, 58, 95),
    'sky_medium': (58, 110, 165),
    'sky_light': (135, 206, 235),
    'sunset_dark': (226, 114, 91),
    'sunset_medium': (244, 162, 97),
    'sunset_light': (249, 199, 79),
    'water_dark': (26, 83, 92),
    'water_medium': (78, 205, 196),
    'water_light': (168, 218, 220),
    'leaf_dark': (56, 102, 65),
    'leaf_medium': (106, 153, 78),
    'leaf_light': (167, 201, 87),
    'background': (248, 249, 250),
    'text_dark': (43, 45, 66),
    'text_light': (248, 249, 250),
    'success': (39, 174, 96),
    'warning': (243, 156, 18),
    'error': (231, 76, 60),
    'panel': (233, 236, 239)
}

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🌍 English Trainer Game - Para Hispanohablantes")
clock = pygame.time.Clock()

# Cargar recursos
def load_fonts():
    """Cargar fuentes de diferentes tamaños"""
    return {
        'title': pygame.font.Font(None, 48),
        'header': pygame.font.Font(None, 36),
        'normal': pygame.font.Font(None, 28),
        'small': pygame.font.Font(None, 22),
        'button': pygame.font.Font(None, 24)
    }

fonts = load_fonts()

# Clase para botones interactivos
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, COLORS['text_dark'], self.rect, 2, border_radius=12)
        
        text_surf = fonts['button'].render(self.text, True, COLORS['text_light'])
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered and self.action:
                return self.action()
        return None

# Clase para cajas de texto
class TextInput:
    def __init__(self, x, y, width, height, placeholder=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0
        
    def draw(self, surface):
        # Fondo de la caja de texto
        color = COLORS['sky_light'] if self.active else COLORS['panel']
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, COLORS['sky_medium'], self.rect, 2, border_radius=8)
        
        # Texto o placeholder
        if self.text:
            text_surf = fonts['normal'].render(self.text, True, COLORS['text_dark'])
        else:
            text_surf = fonts['normal'].render(self.placeholder, True, COLORS['text_medium'])
        
        text_rect = text_surf.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
        surface.blit(text_surf, text_rect)
        
        # Cursor
        if self.active and self.cursor_visible:
            cursor_x = text_rect.right + 2
            pygame.draw.line(surface, COLORS['text_dark'], 
                           (cursor_x, self.rect.y + 10), 
                           (cursor_x, self.rect.y + self.rect.height - 10), 2)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                
        return None
    
    def update(self):
        # Animación del cursor
        self.cursor_timer += 1
        if self.cursor_timer >= 30:  # Cambiar cada medio segundo
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

# Clase para partículas de efectos visuales
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(3, 8)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-3, -1)
        self.lifetime = random.randint(30, 60)
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        self.size = max(0, self.size - 0.1)
        return self.lifetime > 0
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

# Sistema de partículas
class ParticleSystem:
    def __init__(self):
        self.particles = []
        
    def add_particles(self, x, y, color, count=10):
        for _ in range(count):
            self.particles.append(Particle(x, y, color))
            
    def update(self):
        self.particles = [p for p in self.particles if p.update()]
        
    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

# Datos de ejercicios (adaptados para Pygame)
EXERCISES = [
    {
        "type": "Preguntas con 'to be'",
        "instruction": "Convierte la afirmación en pregunta:",
        "spanish": "Él es profesor",
        "correct_answer": "Is he a teacher?",
        "hint": "Invertir orden: Verbo + Sujeto",
        "difficulty": "básico",
        "explanation": "En inglés, invertimos 'to be' para hacer preguntas"
    },
    {
        "type": "Preguntas con Do/Does", 
        "instruction": "Convierte en pregunta usando Do/Does:",
        "spanish": "Ella trabaja aquí",
        "correct_answer": "Does she work here?",
        "hint": "She/he/it → DOES + verbo base",
        "difficulty": "básico",
        "explanation": "Añadimos 'do/does' cuando no hay otro auxiliar"
    },
    {
        "type": "Preguntas WH-",
        "instruction": "Formula una pregunta con WHAT:",
        "spanish": "RESPUESTA: I want a coffee",
        "correct_answer": "What do you want?",
        "hint": "What + do/does + sujeto + verbo",
        "difficulty": "intermedio",
        "explanation": "Las preguntas WH- siguen un orden específico"
    },
    # ... más ejercicios ...
]

class EnglishTrainerGame:
    def __init__(self):
        self.current_exercise = 0
        self.score = 0
        self.total_exercises = 50  # Reducido para demo
        self.start_time = datetime.now()
        self.hints_used = 0
        self.streak = 0
        self.max_streak = 0
        self.particles = ParticleSystem()
        self.feedback_text = ""
        self.feedback_timer = 0
        self.feedback_color = COLORS['text_dark']
        self.exercises = self.generate_exercises()
        
        # Elementos de UI
        self.answer_input = TextInput(300, 400, 600, 60, "Escribe tu respuesta en inglés...")
        self.submit_button = Button(500, 500, 200, 50, "✅ Verificar", 
                                  COLORS['leaf_medium'], COLORS['leaf_light'], self.check_answer)
        self.hint_button = Button(300, 580, 180, 45, "💡 Pista", 
                                COLORS['sunset_medium'], COLORS['sunset_light'], self.show_hint)
        self.skip_button = Button(720, 580, 180, 45, "⏭️ Saltar", 
                                COLORS['sky_medium'], COLORS['sky_light'], self.next_exercise)
        
    def generate_exercises(self):
        """Generar ejercicios variados"""
        exercises = []
        for i in range(self.total_exercises):
            base_exercise = random.choice(EXERCISES).copy()
            # Variar las oraciones
            variations = [
                {"profesor": "médico", "trabaja": "estudia"},
                {"es": "era", "trabaja": "enseña"},
                {"aquí": "allí", "café": "té"}
            ]
            variation = variations[i % len(variations)]
            
            for orig, new in variation.items():
                base_exercise["spanish"] = base_exercise["spanish"].replace(orig, new)
                base_exercise["correct_answer"] = base_exercise["correct_answer"].replace(orig, new)
            
            exercises.append(base_exercise)
        return exercises
    
    def draw_background(self):
        """Dibujar fondo con gradiente y elementos naturales"""
        # Gradiente de cielo
        for y in range(SCREEN_HEIGHT):
            # Interpolación de color cielo
            ratio = y / SCREEN_HEIGHT
            r = int(COLORS['sky_light'][0] * (1 - ratio) + COLORS['sky_medium'][0] * ratio)
            g = int(COLORS['sky_light'][1] * (1 - ratio) + COLORS['sky_medium'][1] * ratio)
            b = int(COLORS['sky_light'][2] * (1 - ratio) + COLORS['sky_medium'][2] * ratio)
            pygame.draw.line(screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Nubes decorativas
        for i, cloud in enumerate([(200, 100), (800, 150), (1000, 80)]):
            self.draw_cloud(cloud[0], cloud[1], 80 + i * 20)
        
        # Sol
        pygame.draw.circle(screen, COLORS['sunset_light'], (1100, 100), 40)
        
    def draw_cloud(self, x, y, size):
        """Dibujar una nube"""
        cloud_color = (255, 255, 255)
        pygame.draw.circle(screen, cloud_color, (x, y), size // 3)
        pygame.draw.circle(screen, cloud_color, (x + size // 3, y - size // 6), size // 2)
        pygame.draw.circle(screen, cloud_color, (x + size // 2, y), size // 3)
        pygame.draw.circle(screen, cloud_color, (x + size // 3, y + size // 6), size // 4)
    
    def draw_progress_bar(self):
        """Dibujar barra de progreso visual"""
        progress = self.current_exercise / self.total_exercises
        bar_width = 800
        bar_height = 20
        bar_x = (SCREEN_WIDTH - bar_width) // 2
        bar_y = 50
        
        # Fondo de la barra
        pygame.draw.rect(screen, COLORS['panel'], (bar_x, bar_y, bar_width, bar_height), border_radius=10)
        
        # Progreso
        progress_width = int(bar_width * progress)
        if progress_width > 0:
            pygame.draw.rect(screen, COLORS['leaf_medium'], 
                           (bar_x, bar_y, progress_width, bar_height), border_radius=10)
        
        # Borde
        pygame.draw.rect(screen, COLORS['text_dark'], (bar_x, bar_y, bar_width, bar_height), 2, border_radius=10)
        
        # Texto de progreso
        progress_text = f"Progreso: {self.current_exercise}/{self.total_exercises}"
        text_surf = fonts['small'].render(progress_text, True, COLORS['text_dark'])
        screen.blit(text_surf, (bar_x, bar_y + 25))
    
    def draw_stats(self):
        """Dibujar estadísticas en tiempo real"""
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        
        stats = [
            f"⭐ Puntuación: {self.score}",
            f"⏱️ Tiempo: {minutes:02d}:{seconds:02d}",
            f"🔥 Racha: {self.streak}",
            f"💡 Pistas: {self.hints_used}"
        ]
        
        for i, stat in enumerate(stats):
            text_surf = fonts['small'].render(stat, True, COLORS['text_dark'])
            screen.blit(text_surf, (50, 150 + i * 30))
    
    def draw_exercise(self):
        """Dibujar el ejercicio actual"""
        if self.current_exercise >= len(self.exercises):
            return
            
        exercise = self.exercises[self.current_exercise]
        
        # Panel de ejercicio
        panel_rect = pygame.Rect(200, 200, 800, 150)
        pygame.draw.rect(screen, COLORS['panel'], panel_rect, border_radius=15)
        pygame.draw.rect(screen, COLORS['forest_medium'], panel_rect, 3, border_radius=15)
        
        # Tipo y dificultad
        type_text = f"{exercise['type']} - [{exercise['difficulty'].upper()}]"
        type_surf = fonts['header'].render(type_text, True, COLORS['forest_dark'])
        screen.blit(type_surf, (panel_rect.x + 20, panel_rect.y + 15))
        
        # Instrucción
        instr_surf = fonts['normal'].render(exercise['instruction'], True, COLORS['text_dark'])
        screen.blit(instr_surf, (panel_rect.x + 20, panel_rect.y + 60))
        
        # Oración en español
        spanish_surf = fonts['normal'].render(f'"{exercise["spanish"]}"', True, COLORS['water_dark'])
        screen.blit(spanish_surf, (panel_rect.x + 20, panel_rect.y + 100))
    
    def draw_feedback(self):
        """Dibujar feedback de la respuesta"""
        if self.feedback_text and self.feedback_timer > 0:
            # Panel de feedback
            feedback_rect = pygame.Rect(300, 300, 600, 80)
            pygame.draw.rect(screen, self.feedback_color, feedback_rect, border_radius=10)
            pygame.draw.rect(screen, COLORS['text_dark'], feedback_rect, 2, border_radius=10)
            
            # Texto de feedback
            feedback_surf = fonts['normal'].render(self.feedback_text, True, COLORS['text_light'])
            screen.blit(feedback_surf, feedback_surf.get_rect(center=feedback_rect.center))
            
            self.feedback_timer -= 1
    
    def show_feedback(self, text, color, duration=180):  # 3 segundos a 60 FPS
        """Mostrar mensaje de feedback"""
        self.feedback_text = text
        self.feedback_color = color
        self.feedback_timer = duration
    
    def check_answer(self):
        """Verificar la respuesta del usuario"""
        user_answer = self.answer_input.text.strip()
        if not user_answer:
            self.show_feedback("⚠️ Por favor, escribe una respuesta", COLORS['warning'])
            return
            
        exercise = self.exercises[self.current_exercise]
        
        # Verificación flexible
        def normalize(text):
            return text.lower().replace("?", "").replace("!", "").strip()
        
        user_norm = normalize(user_answer)
        correct_norm = normalize(exercise['correct_answer'])
        
        is_correct = user_norm == correct_norm or self.calculate_similarity(user_norm, correct_norm) > 0.8
        
        if is_correct:
            self.score += 10 + (self.streak * 2)  # Bonus por racha
            self.streak += 1
            self.max_streak = max(self.max_streak, self.streak)
            self.show_feedback("✅ ¡Correcto! +" + str(10 + (self.streak * 2)), COLORS['success'])
            
            # Partículas de celebración
            self.particles.add_particles(SCREEN_WIDTH // 2, 400, COLORS['success'], 20)
            
            # Siguiente ejercicio después de delay
            pygame.time.set_timer(pygame.USEREVENT, 2000)  # 2 segundos
        else:
            self.streak = 0
            self.show_feedback(f"❌ Incorrecto. Correcto: {exercise['correct_answer']}", COLORS['error'])
            self.answer_input.text = ""  # Limpiar para reintentar
    
    def calculate_similarity(self, text1, text2):
        """Calcular similitud entre textos (simple)"""
        words1 = set(text1.split())
        words2 = set(text2.split())
        if not words2:
            return 0
        return len(words1.intersection(words2)) / len(words2)
    
    def show_hint(self):
        """Mostrar pista del ejercicio actual"""
        exercise = self.exercises[self.current_exercise]
        self.hints_used += 1
        self.show_feedback(f"💡 Pista: {exercise['hint']}", COLORS['warning'], 240)  # 4 segundos
    
    def next_exercise(self):
        """Pasar al siguiente ejercicio"""
        self.current_exercise += 1
        self.answer_input.text = ""
        
        if self.current_exercise >= len(self.exercises):
            self.show_final_results()
        else:
            self.show_feedback("➡️ Siguiente ejercicio", COLORS['sky_medium'], 60)  # 1 segundo
    
    def show_final_results(self):
        """Mostrar resultados finales en pantalla completa"""
        results_screen = True
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        accuracy = (self.score / (len(self.exercises) * 10)) * 100 if self.exercises else 0
        
        # Botones para resultados
        restart_button = Button(450, 600, 150, 50, "🔄 Reiniciar", 
                              COLORS['leaf_medium'], COLORS['leaf_light'])
        exit_button = Button(650, 600, 150, 50, "🚪 Salir", 
                           COLORS['sunset_medium'], COLORS['sunset_light'])
        
        while results_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEMOTION:
                    restart_button.check_hover(event.pos)
                    exit_button.check_hover(event.pos)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.is_hovered:
                        self.__init__()  # Reiniciar juego
                        return
                    elif exit_button.is_hovered:
                        pygame.quit()
                        sys.exit()
            
            # Dibujar resultados
            self.draw_background()
            
            # Panel de resultados
            result_rect = pygame.Rect(200, 150, 800, 400)
            pygame.draw.rect(screen, COLORS['panel'], result_rect, border_radius=20)
            pygame.draw.rect(screen, COLORS['forest_medium'], result_rect, 4, border_radius=20)
            
            # Título
            title_surf = fonts['title'].render("🎓 Resultados Finales", True, COLORS['forest_dark'])
            screen.blit(title_surf, (result_rect.centerx - title_surf.get_width() // 2, result_rect.y + 30))
            
            # Estadísticas
            stats = [
                f"🌿 Ejercicios completados: {self.current_exercise}/{self.total_exercises}",
                f"⭐ Puntuación final: {self.score}",
                f"📈 Precisión: {accuracy:.1f}%",
                f"⏱️ Tiempo total: {minutes:02d}:{seconds:02d}",
                f"🔥 Racha máxima: {self.max_streak}",
                f"💡 Pistas usadas: {self.hints_used}"
            ]
            
            for i, stat in enumerate(stats):
                stat_surf = fonts['header'].render(stat, True, COLORS['text_dark'])
                screen.blit(stat_surf, (result_rect.centerx - stat_surf.get_width() // 2, result_rect.y + 100 + i * 50))
            
            # Evaluación
            if accuracy >= 90:
                eval_text = "🏔️ ¡EXCELENTE! Dominas el inglés"
            elif accuracy >= 70:
                eval_text = "🌅 ¡MUY BIEN! Buen trabajo"
            elif accuracy >= 50:
                eval_text = "🌱 ¡BIEN! Sigue practicando"
            else:
                eval_text = "🌵 ¡Ánimo! La práctica hace al maestro"
            
            eval_surf = fonts['header'].render(eval_text, True, COLORS['water_dark'])
            screen.blit(eval_surf, (result_rect.centerx - eval_surf.get_width() // 2, result_rect.y + 350))
            
            # Botones
            restart_button.draw(screen)
            exit_button.draw(screen)
            
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
                    pygame.time.set_timer(pygame.USEREVENT, 0)  # Cancelar timer
                    self.next_exercise()
                
                # Pasar eventos a los elementos UI
                self.answer_input.handle_event(event)
                self.submit_button.handle_event(event)
                self.hint_button.handle_event(event)
                self.skip_button.handle_event(event)
                
                # Tecla Enter para enviar
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.check_answer()
            
            # Actualizar
            mouse_pos = pygame.mouse.get_pos()
            self.submit_button.check_hover(mouse_pos)
            self.hint_button.check_hover(mouse_pos)
            self.skip_button.check_hover(mouse_pos)
            self.answer_input.update()
            self.particles.update()
            
            # Dibujar
            self.draw_background()
            self.draw_progress_bar()
            self.draw_stats()
            
            if self.current_exercise < len(self.exercises):
                self.draw_exercise()
                self.answer_input.draw(screen)
                self.submit_button.draw(screen)
                self.hint_button.draw(screen)
                self.skip_button.draw(screen)
            
            self.draw_feedback()
            self.particles.draw(screen)
            
            # Actualizar pantalla
            pygame.display.flip()
            clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Ejecutar el juego
if __name__ == "__main__":
    game = EnglishTrainerGame()
    game.run()
