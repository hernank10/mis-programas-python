"""
modulo4_oraciones_compuestas.py
Módulo 4 — Oraciones compuestas interactivas (Pygame)

Características:
- Niveles de dificultad (Fácil / Intermedio / Avanzado)
- Banco ampliado de preguntas sobre oraciones compuestas (coordinadas y subordinadas)
- RainbowButton (hover + press + color cycling)
- Fondo animado (gradiente), panel glassmorphism
- Partículas con emoticones, feedback bilingüe
- Siluetas animadas: vaqueros, caballos, perros, vacas (parallax)
- Guarda puntuación en memoria durante la sesión
"""

import pygame, sys, random, math, json, time
from pygame import Rect

# ---------- Config ----------
WIDTH, HEIGHT = 1100, 700
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Módulo 4 — Oraciones Compuestas (Rainbow Ranch)")
clock = pygame.time.Clock()

# ---------- Fonts colors ----------
WHITE = (255,255,255)
BLACK = (18,18,22)
PANEL_ALPHA = 180

# Fonts (fallbacks)
try:
    FONT_XL = pygame.font.Font(None, 44)
    FONT_LG = pygame.font.Font(None, 28)
    FONT_MD = pygame.font.Font(None, 22)
    FONT_SM = pygame.font.Font(None, 18)
except:
    pygame.font.init()
    FONT_XL = pygame.font.SysFont("Arial", 44)
    FONT_LG = pygame.font.SysFont("Arial", 28)
    FONT_MD = pygame.font.SysFont("Arial", 22)
    FONT_SM = pygame.font.SysFont("Arial", 18)

# ---------- Utilities ----------
def lerp(a,b,t): return a + (b-a)*t

def draw_multiline_center(surface, text, font, color, rect):
    lines = text.splitlines()
    total_h = sum(font.size(line)[1] for line in lines)
    y = rect.y + (rect.h - total_h)/2
    for line in lines:
        surf_line = font.render(line, True, color)
        x = rect.x + (rect.w - surf_line.get_width())/2
        surface.blit(surf_line, (x, y))
        y += surf_line.get_height()

# ---------- Animated Background ----------
class AnimatedBG:
    def __init__(self, w, h):
        self.w = w; self.h = h; self.t = 0.0
    def update(self, dt):
        self.t += dt * 0.4
    def render(self, surf):
        t = self.t
        for i in range(0, self.h, 4):
            r = int(40 + 80*(1 + math.sin((i/48.0) + t)))
            g = int(20 + 60*(1 + math.sin((i/60.0) + t + 1.5)))
            b = int(100 + 70*(1 + math.sin((i/72.0) + t + 3.0)))
            pygame.draw.rect(surf, (r,g,b), (0, i, self.w, 4))

bg = AnimatedBG(WIDTH, HEIGHT)

# ---------- Glass Panel ----------
def draw_glass_panel(surface, rect, alpha=160):
    panel = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    panel.fill((255,255,255, alpha//4))
    pygame.draw.rect(panel, (255,255,255, alpha//6), panel.get_rect(), border_radius=20)
    surface.blit(panel, (rect.x, rect.y))
    pygame.draw.rect(surface, (255,255,255,20), rect, 2, border_radius=20)

# ---------- Particles (emojis) ----------
class EmojiParticle:
    def __init__(self, x, y, emoji='✨'):
        self.x = x; self.y = y
        self.vx = random.uniform(-140,140)
        self.vy = random.uniform(40, 220)
        self.size = random.randint(20,44)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(1.6, 3.8)
        self.angle = random.uniform(0, 360)
        self.spin = random.uniform(-200, 200)
        # create surface
        try:
            self.font = pygame.font.Font(None, self.size)
            self.surf = self.font.render(self.emoji, True, WHITE)
            if self.surf.get_width() == 0:
                raise Exception("emoji not rendered")
        except Exception:
            self.surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.surf, (255,255,0), (self.size//2, self.size//2), self.size//2)
    def update(self, dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt
    def draw(self, surface):
        alpha = max(0, int(255*(1 - self.age/self.life)))
        im = pygame.transform.rotozoom(self.surf, self.angle, 1.0)
        im.set_alpha(alpha)
        w, h = im.get_size()
        surface.blit(im, (self.x - w//2, self.y - h//2))
    def dead(self):
        return self.age >= self.life or self.y > HEIGHT + 100

particles = []
def spawn_particles(center_x, count=12, correct=True):
    good = ['🎉','✨','🌟','👏','🤠']
    bad = ['❗','😅','💡','⚠️']
    pool = good if correct else bad
    for _ in range(count):
        emo = random.choice(pool)
        p = EmojiParticle(center_x + random.uniform(-80,80), -20 + random.uniform(-40,40), emoji=emo)
        if correct:
            p.vy = random.uniform(40,160); p.vx = random.uniform(-140,140)
        else:
            p.vy = random.uniform(80,240); p.vx = random.uniform(-60,60)
        particles.append(p)

# ---------- RainbowButton ----------
class RainbowButton:
    def __init__(self, rect, text, onclick=None, font=FONT_MD):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.onclick = onclick
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.hue = random.random() * 360.0
        self.font = font
    def update(self, dt):
        self.hue = (self.hue + dt * 60) % 360
        target = 0.96 if self.pressed else (1.06 if self.hover else 1.0)
        self.scale = lerp(self.scale, target, min(1.0, dt * 12))
    def draw(self, surface):
        h = self.hue / 360.0
        r = int(160 + 80 * math.sin(h*2*math.pi))
        g = int(60 + 120 * math.sin((h+0.33)*2*math.pi))
        b = int(160 + 80 * math.sin((h+0.66)*2*math.pi))
        col = (max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b)))
        rw = int(self.rect.w * self.scale)
        rh = int(self.rect.h * self.scale)
        rx = int(self.rect.centerx - rw/2)
        ry = int(self.rect.centery - rh/2)
        base = pygame.Surface((rw, rh), pygame.SRCALPHA)
        base.fill((*col, 230))
        pygame.draw.rect(base, col, base.get_rect(), border_radius=14)
        pygame.draw.rect(base, (255,255,255,40), (6,6,rw-12, rh//2), border_radius=12)
        surface.blit(base, (rx, ry))
        txt = self.font.render(self.text, True, BLACK)
        surface.blit(txt, (rx + (rw - txt.get_width())/2, ry + (rh - txt.get_height())/2))
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                if self.onclick: self.onclick()
            self.pressed = False

# ---------- Ranch Silhouettes (vaqueros, caballos, vacas, perros) ----------
class Cowboy:
    def __init__(self, x, y):
        self.x = x; self.y = y
        self.arm_angle = 0; self.arm_dir = 1
    def update(self, dt):
        self.arm_angle += dt * 40 * self.arm_dir
        if self.arm_angle > 35 or self.arm_angle < -5:
            self.arm_dir *= -1
    def draw(self, surf):
        # simple silhouette
        # body
        pygame.draw.rect(surf, BLACK, (self.x, self.y-60, 20, 60))
        # head
        pygame.draw.circle(surf, BLACK, (self.x+10, self.y-72), 12)
        # hat
        pygame.draw.rect(surf, BLACK, (self.x-5, self.y-86, 30, 8))
        # arm
        arm_x = self.x + 10 + int(30 * math.cos(math.radians(self.arm_angle)))
        arm_y = self.y - 40 - int(20 * math.sin(math.radians(self.arm_angle)))
        pygame.draw.line(surf, BLACK, (self.x+10, self.y-40), (arm_x, arm_y), 6)

class Horse:
    def __init__(self, x, y):
        self.x = x; self.y = y
        self.dir = random.choice([-1,1])
    def update(self, dt):
        self.x += self.dir * 60 * dt
        if self.x < 40 or self.x > WIDTH - 40:
            self.dir *= -1
    def draw(self, surf):
        pygame.draw.rect(surf, BLACK, (self.x-40, self.y-20, 80, 40))
        pygame.draw.circle(surf, BLACK, (self.x+45, self.y), 15)

class Cow:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def update(self, dt): pass
    def draw(self, surf):
        pygame.draw.rect(surf, BLACK, (self.x-30, self.y-15, 60, 30))

class Dog:
    def __init__(self, x, y):
        self.x = x; self.y = y; self.dir = random.choice([-1,1])
    def update(self, dt):
        self.x += self.dir * 40 * dt
        if self.x < 20 or self.x > WIDTH - 20:
            self.dir *= -1
    def draw(self, surf):
        pygame.draw.rect(surf, BLACK, (self.x-20, self.y-10, 40, 20))

# instantiate ranch actors (parallax layers)
ranch_front = [Cowboy(150, HEIGHT-150), Horse(320, HEIGHT-140)]
ranch_mid   = [Cow(600, HEIGHT-120), Dog(480, HEIGHT-130)]
ranch_back  = [Cow(750, HEIGHT-140), Horse(880, HEIGHT-150)]

# ---------- Bank of questions (ampliado) ----------
# Each question: text (spanish), options [two], correct index, explanation (es), explanation_en, difficulty
QUESTION_BANK = [
    # Easy
    {"text":"¿Qué tipo de oración es?\n\n'Hoy hace sol y vamos al parque.'",
     "options":["Coordinada copulativa", "Subordinada"], "correct":0,
     "explain":"Copulativa (y). / Copulative (and).", "difficulty":"easy"},
    {"text":"¿Qué tipo de oración es?\n\n'No vino porque estaba enfermo.'",
     "options":["Subordinada causal", "Coordinada adversativa"], "correct":0,
     "explain":"Subordinada causal (porque). / Subordinate causal (because).", "difficulty":"easy"},
    {"text":"Transforma en pregunta:\n\n'Tú estudias matemáticas.'",
     "options":["¿Estudias tú matemáticas?", "¿Tú estudias matemáticas?"], "correct":0,
     "explain":"Pregunta con inversión/auxiliary in English equivalent.", "difficulty":"easy"},
    # Intermediate
    {"text":"¿Qué tipo de oración es?\n\n'Se enfadó, sin embargo vino a clase.'",
     "options":["Coordinada adversativa", "Subordinada condicional"], "correct":0,
     "explain":"Adversativa (sin embargo). / Adversative (however).", "difficulty":"medium"},
    {"text":"Une con nexo causal:\n\n'No fuiste. Tenías fiebre.' (escoge la mejor mezcla)",
     "options":["No fuiste porque tenías fiebre.", "No fuiste y tenías fiebre."], "correct":0,
     "explain":"Porque introduce la causa. / 'and' is not causal.", "difficulty":"medium"},
    {"text":"Detecta: 'Aunque llueva, iremos al concierto.'",
     "options":["Subordinada concesiva", "Coordinada disyuntiva"], "correct":0,
     "explain":"Concesiva: 'aunque'. / Concessive.", "difficulty":"medium"},
    # Advanced
    {"text":"Transforma en subordinada:\n\n'Estudié mucho. Aprobaré el examen.' (mejor opción)",
     "options":["Porque estudié mucho, aprobaré el examen.", "Estudié mucho y aprobaré el examen."], "correct":0,
     "explain":"Subordinada causal (porque). / Causal subordinate.", "difficulty":"hard"},
    {"text":"Identifica el tipo:\n\n'Si termino temprano, saldré contigo.'",
     "options":["Subordinada condicional", "Coordinada consecutiva"], "correct":0,
     "explain":"Condicional (si). / Conditional subordinate.", "difficulty":"hard"},
    {"text":"¿Cuál es la oración compuesta por subordinación?\n\n'La mujer que vino ayer es profesora.'",
     "options":["Subordinada de relativo", "Coordinada copulativa"], "correct":0,
     "explain":"Subordinada de relativo (que). / Relative clause.", "difficulty":"hard"},
    # More varied questions (to reach a larger bank)
    {"text":"¿Qué tipo es?\n\n'Corremos o caminamos por el parque.'",
     "options":["Coordinada disyuntiva", "Subordinada"], "correct":0,
     "explain":"Disyuntiva (o). / Disjunctive.", "difficulty":"easy"},
    {"text":"¿Qué tipo?\n\n'Llovió tanto que la calle se inundó.'",
     "options":["Coordinada consecutiva", "Subordinada consecutiva"], "correct":1,
     "explain":"Subordinada consecutiva (que introduces result). / Consecutive subordinate.", "difficulty":"medium"},
    {"text":"Transforma en pregunta:\n\n'Ella ha llegado temprano.'",
     "options":["¿Ha llegado ella temprano?", "¿Ella ha llegado temprano?"], "correct":0,
     "explain":"Question uses auxiliary before subject.", "difficulty":"easy"},
    {"text":"Combina con nexo apropiado:\n\n'No hizo la tarea. Se enfermó.'",
     "options":["No hizo la tarea porque se enfermó.", "No hizo la tarea, sin embargo se enfermó."], "correct":0,
     "explain":"Causal: porque.", "difficulty":"medium"},
    {"text":"Identifica:\n\n'Te lo digo para que lo sepas.'",
     "options":["Subordinada final", "Coordinada"], "correct":0,
     "explain":"Final (para que). / Purpose subordinate.", "difficulty":"hard"},
    {"text":"¿Qué tipo?\n\n'Se esforzó tanto que ganó el premio.'",
     "options":["Subordinada consecutiva", "Coordinada adversativa"], "correct":0,
     "explain":"Consecutive (result).", "difficulty":"medium"},
    {"text":"¿Cuál es coordinada?\n\n'Entró y saludó a todos.'",
     "options":["Coordinada copulativa", "Subordinada"], "correct":0,
     "explain":"Copulativa (y).", "difficulty":"easy"},
    {"text":"Detecta:\n\n'Si llueve, cancelaremos el viaje.'",
     "options":["Condicional", "Causal"], "correct":0,
     "explain":"Condicional (si).", "difficulty":"medium"},
    {"text":"Transforma a compuesta:\n\n'Quiero café. No tengo dinero.'",
     "options":["Quiero café aunque no tengo dinero.", "Quiero café pero no tengo dinero."], "correct":1,
     "explain":"Adversativa 'pero'.", "difficulty":"hard"},
    {"text":"Identifica:\n\n'Porque estudiaste, aprobaste.'",
     "options":["Causal", "Concesiva"], "correct":0,
     "explain":"Causal (porque).", "difficulty":"easy"},
]

# We will split by difficulty when building levels
LEVELS = {
    "Fácil": [q for q in QUESTION_BANK if q['difficulty']=='easy'],
    "Intermedio": [q for q in QUESTION_BANK if q['difficulty']=='medium'],
    "Avanzado": [q for q in QUESTION_BANK if q['difficulty']=='hard']
}

# ---------- Game State ----------
class GameState:
    def __init__(self):
        self.level_name = "Fácil"
        self.levels = list(LEVELS.keys())
        self.level_idx = 0
        self.reset_session()
        self.create_ui()
    def reset_session(self):
        self.score = 0
        self.attempts = 0
        self.question_idx = 0
        self.questions = LEVELS[self.level_name].copy()
        random.shuffle(self.questions)
        self.current = self.questions[self.question_idx] if self.questions else None
        self.message = "Selecciona un nivel y pulsa Iniciar ✅"
    def create_ui(self):
        # Buttons
        self.btn_start = RainbowButton((40, HEIGHT-90, 180, 56), "Iniciar", onclick=self.start)
        self.btn_prev_level = RainbowButton((240, HEIGHT-90, 140, 56), "Nivel -", onclick=self.prev_level)
        self.btn_next_level = RainbowButton((400, HEIGHT-90, 140, 56), "Nivel +", onclick=self.next_level)
        self.btn_opt_a = RainbowButton((WIDTH//2 - 360, HEIGHT-170, 320, 72), "Opción A", onclick=lambda: self.answer(0))
        self.btn_opt_b = RainbowButton((WIDTH//2 + 40, HEIGHT-170, 320, 72), "Opción B", onclick=lambda: self.answer(1))
        self.btn_next = RainbowButton((WIDTH-220, HEIGHT-90, 180, 56), "Siguiente »", onclick=self.next_question)
        self.buttons = [self.btn_start, self.btn_prev_level, self.btn_next_level, self.btn_opt_a, self.btn_opt_b, self.btn_next]
    def start(self):
        if not self.questions:
            self.message = "No hay preguntas para este nivel."
            return
        self.score = 0; self.attempts = 0
        self.question_idx = 0
        random.shuffle(self.questions)
        self.current = self.questions[self.question_idx]
        self.message = f"Nivel: {self.level_name} — buena suerte 🤠"
        spawn_particles(WIDTH//2, count=12, correct=True)
    def prev_level(self):
        self.level_idx = (self.level_idx - 1) % len(self.levels)
        self.level_name = self.levels[self.level_idx]
        self.questions = LEVELS[self.level_name].copy()
        random.shuffle(self.questions)
        self.current = self.questions[0] if self.questions else None
        self.message = f"Nivel cambiado a: {self.level_name}"
    def next_level(self):
        self.level_idx = (self.level_idx + 1) % len(self.levels)
        self.level_name = self.levels[self.level_idx]
        self.questions = LEVELS[self.level_name].copy()
        random.shuffle(self.questions)
        self.current = self.questions[0] if self.questions else None
        self.message = f"Nivel cambiado a: {self.level_name}"
    def answer(self, opt_idx):
        if not self.current:
            self.message = "Pulsa Iniciar para comenzar."
            return
        correct = (opt_idx == self.current['correct'])
        self.attempts += 1
        if correct:
            self.score += 1
            self.message = "✅ Correcto — " + self.current['explain']
            spawn_particles(WIDTH//2, count=18, correct=True)
        else:
            self.message = "❌ Incorrecto — " + self.current['explain']
            spawn_particles(WIDTH//2, count=12, correct=False)
        # auto advance next after short delay (use timer event)
        pygame.time.set_timer(pygame.USEREVENT + 1, 1200)
    def next_question(self):
        # manually advance
        if not self.questions: 
            self.message = "No hay preguntas en este nivel."
            return
        self.question_idx += 1
        if self.question_idx >= len(self.questions):
            # finished
            self.message = f"Nivel completado. Puntos: {self.score}/{self.attempts}"
            spawn_particles(WIDTH//2, count=40, correct=True)
            self.question_idx = 0
            random.shuffle(self.questions)
            # keep progress (we do not persist to disk in this example)
        self.current = self.questions[self.question_idx]
    def update(self, dt):
        for b in self.buttons:
            b.update(dt)
        for r in ranch_back + ranch_mid + ranch_front:
            r.update(dt)
        for p in particles[:]:
            p.update(dt)
            if p.dead():
                particles.remove(p)
    def draw(self, surface):
        # draw glass main panel
        panel = Rect(40, 40, WIDTH - 80, HEIGHT - 160)
        draw_glass_panel(surface, panel, alpha=160)
        # title
        surface.blit(FONT_XL.render("Rainbow Ranch — Oraciones Compuestas (Módulo 4)", True, WHITE), (panel.x + 20, panel.y + 12))
        # level & score
        level_txt = FONT_MD.render(f"Nivel: {self.level_name}    Puntos: {self.score}    Intentos: {self.attempts}", True, WHITE)
        surface.blit(level_txt, (panel.x + 20, panel.y + 64))
        # question area
        inner = Rect(panel.x + 24, panel.y + 100, panel.w - 48, panel.h - 180)
        pygame.draw.rect(surface, (0,0,0,50), inner, border_radius=12)
        if self.current:
            # show Spanish question on top
            qrect = Rect(inner.x + 8, inner.y + 8, inner.w - 16, inner.h//2 - 16)
            pygame.draw.rect(surface, (0,0,0,40), qrect, border_radius=10)
            draw_multiline_center(surface, self.current['text'], FONT_LG, WHITE, qrect)
            # draw bilingual hint smaller
            hint_rect = Rect(inner.x + 8, inner.y + inner.h//2, inner.w - 16, inner.h//2 - 16)
            pygame.draw.rect(surface, (0,0,0,28), hint_rect, border_radius=10)
            # show english explanation (short) in lower part
            draw_multiline_center(surface, "(EN) " + self.current['explain'], FONT_MD, WHITE, hint_rect)
        else:
            draw_multiline_center(surface, "Pulsa Iniciar para cargar preguntas del nivel seleccionado", FONT_LG, WHITE, inner)
        # draw buttons
        for b in self.buttons:
            b.draw(surface)
        # draw ranch silhouettes (parallax)
        for obj in ranch_back:
            obj.draw(surface)
        for obj in ranch_mid:
            obj.draw(surface)
        for obj in ranch_front:
            obj.draw(surface)
        # draw particles
        for p in particles:
            p.draw(surface)
        # message bar
        msg_rect = Rect(panel.x + 24, panel.y + panel.h - 56, panel.w - 48, 40)
        pygame.draw.rect(surface, (0,0,0,100), msg_rect, border_radius=10)
        surface.blit(FONT_MD.render(self.message, True, WHITE), (msg_rect.x + 10, msg_rect.y + 8))

# ---------- Instantiate ranch silhouettes (reuse small set for performance) ----------
ranch_front = [Cowboy(140, HEIGHT-160), Horse(350, HEIGHT-150)]
ranch_mid   = [Cow(520, HEIGHT-140), Dog(420, HEIGHT-150)]
ranch_back  = [Cow(800, HEIGHT-160), Horse(980, HEIGHT-155)]

# ---------- Instantiate game ----------
game = GameState()

# ---------- Event handling ----------
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.USEREVENT + 1:
            # auto-advance after feedback
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)
            game.next_question()
        # route events to buttons
        for b in game.buttons:
            b.handle_event(event)

# ---------- Main loop ----------
def main():
    while True:
        dt = clock.tick(FPS) / 1000.0
        handle_events()
        bg.update(dt)
        game.update(dt)
        # draw background
        bg_surf = pygame.Surface((WIDTH, HEIGHT))
        bg.render(bg_surf)
        screen.blit(bg_surf, (0, 0))
        # draw game
        game.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
