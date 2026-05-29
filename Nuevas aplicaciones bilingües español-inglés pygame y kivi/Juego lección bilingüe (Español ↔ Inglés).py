"""
Rainbow Write - Pygame (Módulo 2: Diseño pedagógico digital)
Juego educativo: reglas de adjetivos y prácticas de traducción/opción múltiple.

Características:
- RainbowButton con hover & press effects
- Fondo animado tipo gradiente
- Panel glassmorphism semitransparente
- Sistema de partículas con emoticones que caen y rotan
- Feedback visual enriquecido
- Banco de reglas + preguntas (módulo 2)
"""

import pygame
import random
import math
import time
import sys

# ---------- Config ----------
WIDTH, HEIGHT = 1000, 640
FPS = 60
BG_ANIM_SPEED = 0.5

# Colors
WHITE = (255, 255, 255)
BLACK = (18, 18, 20)
PANEL_ALPHA = 160  # translucency for glass panel (0-255)

# Init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Write — Módulo 2 (Adjetivos)")
clock = pygame.time.Clock()

# Fonts
def load_font(preferred_size=20):
    # Try to find a font that can show emoji; fallback to default
    # Pygame may not render colored emoji; this is best-effort
    try:
        f = pygame.font.Font(None, preferred_size)
    except:
        f = pygame.font.SysFont("Arial", preferred_size)
    return f

FONT_LG = load_font(32)
FONT_MD = load_font(22)
FONT_SM = load_font(18)
FONT_XL = load_font(44)

# ---------- Data: reglas y preguntas ----------
REGULAS = [
    {
        "explicacion": "🇬🇧 En inglés, los adjetivos suelen ir ANTES del sustantivo.\nEj: a red car 🚗",
        "pregunta": "Traduce correctamente: 'un coche rojo'",
        "opciones": ["a car red", "a red car"],
        "respuesta": "a red car"
    },
    {
        "explicacion": "🇪🇸 En español, los adjetivos suelen ir DESPUÉS del sustantivo.\nEj: una casa grande 🏠",
        "pregunta": "Traduce correctamente: 'a big house'",
        "opciones": ["una grande casa", "una casa grande"],
        "respuesta": "una casa grande"
    },
    {
        "explicacion": "🇬🇧 Algunos adjetivos cambian de significado según su posición.\nEj: 'the only man' vs. 'the man only'.",
        "pregunta": "Elige la traducción correcta: 'el único hombre'",
        "opciones": ["the man only", "the only man"],
        "respuesta": "the only man"
    },
    {
        "explicacion": "🇪🇸 En español, los adjetivos calificativos normalmente van después.\nEj: un libro interesante 📖",
        "pregunta": "Elige la traducción correcta: 'an interesting book'",
        "opciones": ["un libro interesante", "un interesante libro"],
        "respuesta": "un libro interesante"
    }
]

# duplicate & shuffle for play variety
QUESTIONS = REGULAS.copy()
random.shuffle(QUESTIONS)

# ---------- Utilities ----------
def draw_text(surface, text, font, color, rect, align="center"):
    """Draw multi-line text inside rect with alignment"""
    lines = text.splitlines()
    total_h = sum(font.size(line)[1] for line in lines)
    y = rect[1] + (rect[3] - total_h) // 2
    for line in lines:
        text_surf = font.render(line, True, color)
        x = rect[0] + {
            "left": 8,
            "center": (rect[2] - text_surf.get_width()) // 2,
            "right": rect[2] - text_surf.get_width() - 8
        }[align]
        surface.blit(text_surf, (rect[0] + x, y))
        y += text_surf.get_height()

def lerp(a, b, t):
    return a + (b - a) * t

# ---------- Background gradient animated ----------
class AnimatedBackground:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.t = 0.0

    def update(self, dt):
        self.t += dt * BG_ANIM_SPEED

    def render(self, surf):
        # We'll draw vertical gradient with oscillating colors
        t = self.t
        for i in range(0, self.h, 4):
            # compute a rainbow-ish color by sin waves
            r = int(80 + 70 * (1 + math.sin((i/50.0) + t)) )
            g = int(30 + 60 * (1 + math.sin((i/40.0) + t + 2.0)) )
            b = int(120 + 60 * (1 + math.sin((i/60.0) + t + 4.0)) )
            pygame.draw.rect(surf, (r, g, b), (0, i, self.w, 4))

bg = AnimatedBackground(WIDTH, HEIGHT)

# ---------- Glass panel ----------
def draw_glass_panel(surface, rect, alpha=PANEL_ALPHA):
    panel = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    # translucent white overlay
    panel.fill((255, 255, 255, alpha // 3))
    # subtle border
    border = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    border.fill((255, 255, 255, 0))
    pygame.draw.rect(border, (255,255,255,30), (0,0,rect[2],rect[3]), 2, border_radius=18)
    surface.blit(panel, (rect[0], rect[1]))
    surface.blit(border, (rect[0], rect[1]))

# ---------- Particles (emojis) ----------
class EmojiParticle:
    def __init__(self, x, y, emoji='✨'):
        self.x = x
        self.y = y
        self.vy = random.uniform(80, 220)
        self.vx = random.uniform(-40, 40)
        self.size = random.randint(18, 44)
        self.emoji = emoji
        self.life = random.uniform(2.0, 4.0)
        self.age = 0.0
        self.angle = random.uniform(0, 360)
        self.spin = random.uniform(-120, 120)  # degrees per second
        # create surface once
        self.font = pygame.font.Font(None, self.size)
        self.surf = self.font.render(self.emoji, True, (255,255,255))
        # fallback if empty
        if self.surf.get_width() == 0:
            self.surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.surf, (255,255,0), (self.size//2, self.size//2), self.size//2)

    def update(self, dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surface):
        # rotate surf
        rotated = pygame.transform.rotozoom(self.surf, self.angle, 1.0)
        alpha = max(0, int(255 * (1 - (self.age / self.life))))
        rotated.set_alpha(alpha)
        w, h = rotated.get_size()
        surface.blit(rotated, (self.x - w//2, self.y - h//2))

    def is_dead(self):
        return self.age >= self.life or self.y > HEIGHT + 100

particles = []

def spawn_emoji_burst(center_x, count=12, correct=True):
    emojis_ok = ['🎉','✨','👍','🌟','👏']
    emojis_bad = ['💡','❗','😅','😕']
    for _ in range(count):
        emo = random.choice(emojis_ok if correct else emojis_bad)
        p = EmojiParticle(center_x + random.uniform(-80,80), -20 + random.uniform(-30,30), emoji=emo)
        # faster upward when correct
        if correct:
            p.vy = random.uniform(60, 180)
            p.vx = random.uniform(-80, 80)
        else:
            p.vy = random.uniform(80, 220)
            p.vx = random.uniform(-40, 40)
        particles.append(p)

# ---------- RainbowButton ----------
class RainbowButton:
    def __init__(self, rect, text, onclick=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.onclick = onclick
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.hue_offset = random.random() * 360.0

    def update(self, dt):
        # color cycle
        self.hue_offset = (self.hue_offset + dt * 60) % 360
        # scale animation toward target
        target = 0.96 if self.pressed else (1.06 if self.hover else 1.0)
        self.scale = lerp(self.scale, target, min(1.0, dt * 10))

    def draw(self, surface):
        # compute rainbow color
        h = (self.hue_offset) / 360.0
        r = int(200 + 55 * math.sin(h*2*math.pi))
        g = int(80 + 90 * math.sin((h+0.33)*2*math.pi))
        b = int(200 + 55 * math.sin((h+0.66)*2*math.pi))
        color = (max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b)))

        # draw rounded rect with gradient-like border
        rect_w = int(self.rect.w * self.scale)
        rect_h = int(self.rect.h * self.scale)
        rect_x = int(self.rect.centerx - rect_w//2)
        rect_y = int(self.rect.centery - rect_h//2)
        # base
        base = pygame.Surface((rect_w, rect_h), pygame.SRCALPHA)
        base.fill((*color, 230))
        pygame.draw.rect(base, (*color, 255), (0,0,rect_w,rect_h), border_radius=14)
        # glossy highlight
        pygame.draw.rect(base, (255,255,255,40), (6,6,rect_w-12, rect_h//2), border_radius=12)
        surface.blit(base, (rect_x, rect_y))

        # text
        font = FONT_MD
        txt = font.render(self.text, True, BLACK)
        surface.blit(txt, (rect_x + (rect_w - txt.get_width())//2, rect_y + (rect_h - txt.get_height())//2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                if self.onclick:
                    self.onclick()
            self.pressed = False

# ---------- Game state ----------
class GameState:
    def __init__(self):
        self.index = 0
        self.score = 0
        self.attempts = 0
        self.mode = 'learn'  # or 'quiz' or 'result'
        self.current_q = None
        self.message = ""
        self.message_timer = 0.0
        self.transition_alpha = 0
        self.shuffled_qs = QUESTIONS.copy()
        random.shuffle(self.shuffled_qs)
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        # Buttons: Next / Option1 / Option2 / Quit
        w = 260
        h = 64
        spacing = 24
        # option buttons placed centered below panel
        bx = WIDTH//2 - w - spacing//2
        by = HEIGHT - 140
        self.opt1 = RainbowButton((bx, by, w, h), "Opción 1", onclick=lambda: self.choose(0))
        self.opt2 = RainbowButton((bx + w + spacing, by, w, h), "Opción 2", onclick=lambda: self.choose(1))
        self.next_btn = RainbowButton((WIDTH - 220, 20, 200, 56), "Siguiente »", onclick=self.next_question)
        self.restart_btn = RainbowButton((20, 20, 180, 56), "Reiniciar", onclick=self.restart)
        self.buttons = [self.opt1, self.opt2, self.next_btn, self.restart_btn]

    def start(self):
        self.index = 0
        self.score = 0
        self.attempts = 0
        self.mode = 'quiz'
        self.prepare_question()

    def prepare_question(self):
        if self.index >= len(self.shuffled_qs):
            self.mode = 'result'
            return
        self.current_q = self.shuffled_qs[self.index]
        # set option texts
        self.opt1.text = self.current_q['opciones'][0]
        self.opt2.text = self.current_q['opciones'][1]
        self.message = self.current_q['explicacion']
        self.message_timer = 0.0
        # small spawn of ambient particles
        spawn_emoji_burst(WIDTH//2, count=6, correct=True)

    def choose(self, opt_index):
        if self.mode != 'quiz' or not self.current_q:
            return
        selected = self.current_q['opciones'][opt_index]
        correct = selected == self.current_q['respuesta']
        self.attempts += 1
        if correct:
            self.score += 1
            self.message = f"✅ Correcto! {random.choice(['🎉','🌟','👏'])}"
            spawn_emoji_burst(WIDTH//2, count=18, correct=True)
        else:
            self.message = f"❌ Incorrecto. → {self.current_q['respuesta']}"
            spawn_emoji_burst(WIDTH//2, count=10, correct=False)
        # Auto-advance after a short delay
        pygame.time.set_timer(pygame.USEREVENT + 1, 1200)  # custom timer event

    def next_question(self):
        if self.mode == 'result':
            return
        if self.index < len(self.shuffled_qs):
            self.index += 1
            if self.index < len(self.shuffled_qs):
                self.prepare_question()
            else:
                self.mode = 'result'

    def restart(self):
        random.shuffle(self.shuffled_qs)
        self.start()

    def update(self, dt):
        # update buttons
        for b in self.buttons:
            b.update(dt)
        # update particles
        for p in particles[:]:
            p.update(dt)
            if p.is_dead():
                particles.remove(p)

    def draw(self, surface):
        # draw content panel (glass)
        panel_w, panel_h = WIDTH - 160, HEIGHT - 220
        panel_x, panel_y = 80, 80
        draw_glass_panel(surface, (panel_x, panel_y, panel_w, panel_h), alpha=160)

        # Title
        title_txt = "Rainbow Write — Reglas de Adjetivos (Módulo 2)"
        title_surf = FONT_XL.render(title_txt, True, WHITE)
        surface.blit(title_surf, (panel_x + 20, panel_y + 16))

        # Score
        score_surf = FONT_SM.render(f"Puntos: {self.score}  |  Intentos: {self.attempts}", True, WHITE)
        surface.blit(score_surf, (panel_x + panel_w - score_surf.get_width() - 16, panel_y + 26))

        # If in quiz mode show question and options
        inner_rect = (panel_x + 32, panel_y + 96, panel_w - 64, panel_h - 160)
        if self.mode == 'quiz' and self.current_q:
            # explanation box
            expl_rect = pygame.Rect(inner_rect[0], inner_rect[1], inner_rect[2], 96)
            pygame.draw.rect(surface, (0,0,0,40), expl_rect, border_radius=12)
            draw_text(surface, self.current_q['explicacion'], FONT_MD, WHITE, (expl_rect.x, expl_rect.y, expl_rect.w, expl_rect.h), align="center")

            # question
            q_rect = pygame.Rect(inner_rect[0], inner_rect[1] + 110, inner_rect[2], 72)
            draw_text(surface, "❓ " + self.current_q['pregunta'], FONT_LG, WHITE, (q_rect.x, q_rect.y, q_rect.w, q_rect.h), align="center")

            # options are rendered via RainbowButtons (they draw themselves)
        elif self.mode == 'result':
            # show final score
            res_txt = f"🎯 Juego terminado\nPuntaje final: {self.score}/{len(self.shuffled_qs)}"
            draw_text(surface, res_txt, FONT_LG, WHITE, (inner_rect[0], inner_rect[1], inner_rect[2], inner_rect[3]), align="center")

        # draw message area
        msg_rect = pygame.Rect(panel_x + 32, panel_y + panel_h - 48, panel_w - 64, 40)
        # translucent background for message
        msg_bg = pygame.Surface((msg_rect.w, msg_rect.h), pygame.SRCALPHA)
        msg_bg.fill((0,0,0,90))
        surface.blit(msg_bg, (msg_rect.x, msg_rect.y))
        msg_surf = FONT_MD.render(self.message, True, WHITE)
        surface.blit(msg_surf, (msg_rect.x + 12, msg_rect.y + (msg_rect.h - msg_surf.get_height())//2))

        # draw buttons
        for b in self.buttons:
            b.draw(surface)

        # draw particles
        for p in particles:
            p.draw(surface)

# ---------- Main ----------
game = GameState()
game.start()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # custom timer to auto-advance after feedback
        if event.type == pygame.USEREVENT + 1:
            # advance index and prepare next
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # disable timer
            game.next_question()
        for b in game.buttons:
            b.handle_event(event)

# Main loop
while True:
    dt = clock.tick(FPS) / 1000.0
    handle_events()
    bg.update(dt)
    game.update(dt)

    # Draw
    bg_surf = pygame.Surface((WIDTH, HEIGHT))
    bg.render(bg_surf)
    screen.blit(bg_surf, (0, 0))

    game.draw(screen)

    pygame.display.flip()
