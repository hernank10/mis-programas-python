"""
Rainbow Learn — Pygame (Módulo 3: Introducción a Tkinter / Widgets básicos)

Características:
- RainbowButton: hover + press scaling + color cycle
- Emoticones y partículas que caen y rotan
- Fondo animado tipo gradiente
- Panel glassmorphism semitransparente
- Transiciones suaves y mensajes explicativos
- Mini-lecciones y preguntas sobre Label, Button, Frame, Entry, MessageBox
- Feedback visual enriquecido con emoticones y partículas

Guardar como: rainbow_modulo3_pygame.py
Ejecutar: pip install pygame
         python rainbow_modulo3_pygame.py
"""

import pygame, sys, random, math, time
from pygame import Rect

# ---------- Config ----------
WIDTH, HEIGHT = 1000, 640
FPS = 60

# Colors
WHITE = (255,255,255)
BLACK = (22,22,28)
PANEL_ALPHA = 180

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Learn — Módulo 3: Tkinter Widgets")
clock = pygame.time.Clock()

# Fonts (best-effort; pygame may not render colored emoji)
FONT_XL = pygame.font.Font(None, 44)
FONT_LG = pygame.font.Font(None, 28)
FONT_MD = pygame.font.Font(None, 22)
FONT_SM = pygame.font.Font(None, 18)

# ---------- Utilities ----------
def lerp(a,b,t): return a + (b-a)*t

def draw_text_center(surf, text, font, color, rect):
    lines = text.splitlines()
    total_h = sum(font.size(line)[1] for line in lines)
    y = rect.y + (rect.h - total_h)/2
    for line in lines:
        txt = font.render(line, True, color)
        x = rect.x + (rect.w - txt.get_width())/2
        surf.blit(txt, (x,y))
        y += txt.get_height()

# ---------- Background animated gradient ----------
class AnimatedBG:
    def __init__(self,w,h):
        self.w = w; self.h = h; self.t = 0.0
    def update(self,dt): self.t += dt * 0.6
    def render(self,surf):
        t = self.t
        for i in range(0,self.h,4):
            r = int(40 + 60*(1+math.sin((i/40.0)+t)))
            g = int(20 + 50*(1+math.sin((i/60.0)+t+1.5)))
            b = int(70 + 60*(1+math.sin((i/50.0)+t+3.0)))
            pygame.draw.rect(surf, (r,g,b), (0,i,self.w,4))

bg = AnimatedBG(WIDTH, HEIGHT)

# ---------- Glass panel ----------
def draw_glass(surface, rect):
    panel = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    # subtle blur-like overlay (simulated)
    panel.fill((255,255,255, 30))
    pygame.draw.rect(panel, (255,255,255,18), (0,0,rect.w,rect.h), border_radius=18)
    surface.blit(panel, (rect.x, rect.y))
    # inner border
    pygame.draw.rect(surface, (255,255,255,20), rect, 2, border_radius=18)

# ---------- Particles (emoji) ----------
class EmojiParticle:
    def __init__(self, x, y, emoji='✨'):
        self.x = x; self.y = y
        self.vx = random.uniform(-60,60)
        self.vy = random.uniform(40,220)
        self.size = random.randint(18,44)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(2.0,4.0)
        self.angle = random.uniform(0,360); self.spin = random.uniform(-180,180)
        self.font = pygame.font.Font(None, self.size)
        self.surf = self.font.render(self.emoji, True, (255,255,255))
        if self.surf.get_width()==0:
            # fallback circle
            self.surf = pygame.Surface((self.size,self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.surf, (255,255,0), (self.size//2,self.size//2), self.size//2)
    def update(self,dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt
    def draw(self,surf):
        alpha = max(0, int(255*(1 - self.age/self.life)))
        im = pygame.transform.rotozoom(self.surf, self.angle, 1.0)
        im.set_alpha(alpha)
        w,h = im.get_size()
        surf.blit(im, (self.x - w//2, self.y - h//2))
    def dead(self): return self.age >= self.life or self.y > HEIGHT + 120

particles = []
def spawn_particles(x, count=12, correct=True):
    emojis_ok = ['🎉','✨','👍','🌟','👏','💫']
    emojis_bad = ['💡','❗','😅','😕','⚠️']
    for _ in range(count):
        e = random.choice(emojis_ok if correct else emojis_bad)
        p = EmojiParticle(x + random.uniform(-80,80), -10 + random.uniform(-30,30), emoji=e)
        if correct:
            p.vy = random.uniform(40,160); p.vx = random.uniform(-140,140)
        else:
            p.vy = random.uniform(80,240); p.vx = random.uniform(-60,60)
        particles.append(p)

# ---------- RainbowButton ----------
class RainbowButton:
    def __init__(self, rect, text, onclick=None):
        self.rect = Rect(rect)
        self.text = text
        self.onclick = onclick
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.hue = random.random()*360
    def update(self,dt):
        self.hue = (self.hue + dt*60) % 360
        target = 0.96 if self.pressed else (1.06 if self.hover else 1.0)
        self.scale = lerp(self.scale, target, min(1.0, dt*10))
    def draw(self, surface):
        # color from hue
        h = self.hue/360.0
        r = int(160 + 80*math.sin(h*2*math.pi))
        g = int(60 + 120*math.sin((h+0.33)*2*math.pi))
        b = int(160 + 80*math.sin((h+0.66)*2*math.pi))
        col = (max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b)))
        rw = int(self.rect.w * self.scale); rh = int(self.rect.h * self.scale)
        rx = int(self.rect.centerx - rw/2); ry = int(self.rect.centery - rh/2)
        surf_btn = pygame.Surface((rw,rh), pygame.SRCALPHA)
        surf_btn.fill((*col,230))
        pygame.draw.rect(surf_btn, (*col,255), surf_btn.get_rect(), border_radius=14)
        # glossy highlight
        pygame.draw.rect(surf_btn, (255,255,255,40), (6,6,rw-12, rh//2), border_radius=12)
        surface.blit(surf_btn, (rx,ry))
        # text
        txt = FONT_MD.render(self.text, True, BLACK)
        surface.blit(txt, (rx + (rw - txt.get_width())/2, ry + (rh - txt.get_height())/2))
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos): self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                if self.onclick: self.onclick()
            self.pressed = False

# ---------- Module 3 content (mini lessons & quiz) ----------
LESSONS = [
    {
        "widget": "Label",
        "explain": "Label: muestra texto estático en la ventana. Ej: títulos, instrucciones.",
        "question": "¿Dónde usarías un Label?",
        "options": ["Para mostrar texto estático", "Para que el usuario escriba texto"],
        "answer": 0
    },
    {
        "widget": "Button",
        "explain": "Button: recibe pulsaciones del usuario y ejecuta acciones (callbacks).",
        "question": "¿Qué hace un Button?",
        "options": ["Envia formularios automáticamente", "Llama una función al pulsarlo"],
        "answer": 1
    },
    {
        "widget": "Frame",
        "explain": "Frame: contenedor que organiza widgets en grupos/áreas.",
        "question": "¿Para qué sirve un Frame?",
        "options": ["Organizar visualmente widgets", "Reemplazar un Label"],
        "answer": 0
    },
    {
        "widget": "Entry",
        "explain": "Entry (Tkinter): campo de texto donde el usuario escribe una sola línea.",
        "question": "¿Cuál es la función principal de Entry?",
        "options": ["Mostrar imágenes", "Capturar texto del usuario"],
        "answer": 1
    },
    {
        "widget": "MessageBox",
        "explain": "MessageBox: ventanas emergentes para alertas o información importante.",
        "question": "¿Cuándo usarías un MessageBox?",
        "options": ["Para mostrar un diálogo con información", "Para dibujar gráficos"],
        "answer": 0
    }
]

# ---------- Game State ----------
class Game:
    def __init__(self):
        self.index = 0
        self.score = 0
        self.attempts = 0
        self.mode = 'learn'  # learn -> explains rule, quiz -> choose option, result
        self.message = "Pulsa 'Iniciar Lección' para comenzar"
        self.message_timer = 0.0
        self.create_ui()
    def create_ui(self):
        self.btn_start = RainbowButton((60, HEIGHT-90, 220, 60), "Iniciar Lección", onclick=self.start)
        self.btn_option_a = RainbowButton((WIDTH//2 - 320, HEIGHT-170, 300, 70), "Opción A", onclick=lambda:self.choose(0))
        self.btn_option_b = RainbowButton((WIDTH//2 + 20, HEIGHT-170, 300, 70), "Opción B", onclick=lambda:self.choose(1))
        self.btn_next = RainbowButton((WIDTH-240, HEIGHT-90, 200, 60), "Siguiente »", onclick=self.next_item)
        self.btn_restart = RainbowButton((20,20,160,50), "Reiniciar", onclick=self.restart)
        self.buttons = [self.btn_start, self.btn_option_a, self.btn_option_b, self.btn_next, self.btn_restart]
    def start(self):
        self.index = 0; self.score = 0; self.attempts = 0; self.mode = 'learn'; self.prepare()
    def prepare(self):
        if self.index >= len(LESSONS):
            self.mode = 'result'
            self.message = f"Juego terminado — Puntaje: {self.score}/{len(LESSONS)}"
            return
        item = LESSONS[self.index]
        # set option texts
        self.btn_option_a.text = item['options'][0]
        self.btn_option_b.text = item['options'][1]
        self.message = item['explain']
        spawn_particles(WIDTH//2, count=6, correct=True)
    def choose(self, opt):
        if self.mode == 'result': return
        item = LESSONS[self.index]
        self.attempts += 1
        correct = (opt == item['answer'])
        if correct:
            self.score += 1
            self.message = f"✅ Correcto — {item['widget']} explicado ✅"
            spawn_particles(WIDTH//2, count=16, correct=True)
        else:
            self.message = f"❌ Incorrecto — respuesta: {item['options'][item['answer']]}"
            spawn_particles(WIDTH//2, count=10, correct=False)
        # after feedback auto-advance
        pygame.time.set_timer(pygame.USEREVENT+1, 1200)
    def next_item(self):
        if self.mode == 'result': return
        self.index += 1
        if self.index < len(LESSONS):
            self.mode = 'learn'
            self.prepare()
        else:
            self.mode = 'result'
            self.message = f"Juego terminado — Puntaje: {self.score}/{len(LESSONS)}"
    def restart(self):
        random.shuffle(LESSONS)
        self.start()
    def update(self,dt):
        for b in self.buttons: b.update(dt)
        for p in particles[:]:
            p.update(dt)
            if p.dead(): particles.remove(p)
    def draw(self,surf):
        # panel
        panel = Rect(60,48, WIDTH-120, HEIGHT-120)
        draw_glass(surf, panel)
        # title
        title = "Rainbow Learn — Módulo 3: Widgets básicos (Tkinter)"
        surf.blit(FONT_XL.render(title, True, WHITE), (panel.x+20, panel.y+10))
        # score
        surf.blit(FONT_SM.render(f"Puntos: {self.score}  |  Intentos: {self.attempts}", True, WHITE), (panel.x+panel.w-260, panel.y+18))
        # content area
        inner = Rect(panel.x+28, panel.y+68, panel.w-56, panel.h-140)
        # show explanation / question
        if self.mode != 'result' and self.index < len(LESSONS):
            item = LESSONS[self.index]
            # explanation box
            expl = Rect(inner.x, inner.y, inner.w, 120)
            pygame.draw.rect(surf, (0,0,0,60), expl, border_radius=12)
            draw_text_center(surf, item['explain'], FONT_MD, WHITE, expl)
            # question
            qrect = Rect(inner.x, inner.y+140, inner.w, 80)
            pygame.draw.rect(surf, (0,0,0,40), qrect, border_radius=12)
            draw_text_center(surf, "❓  " + item['question'], FONT_LG, WHITE, qrect)
            # options drawn by buttons
        else:
            # result screen
            res = f"🎯 Fin — Puntaje final: {self.score}/{len(LESSONS)}"
            draw_text_center(surf, res, FONT_LG, WHITE, inner)
        # message area at bottom of panel
        msg_rect = Rect(panel.x+28, panel.y+panel.h-52, panel.w-56, 40)
        pygame.draw.rect(surf, (0,0,0,90), msg_rect, border_radius=10)
        surf.blit(FONT_MD.render(self.message, True, WHITE), (msg_rect.x+12, msg_rect.y+8))
        # draw buttons
        for b in self.buttons: b.draw(surf)
        # draw particles
        for p in particles: p.draw(surf)

game = Game()
game.prepare()

# ---------- Event handling ----------
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.USEREVENT+1:
            pygame.time.set_timer(pygame.USEREVENT+1, 0)
            # auto-advance after feedback
            game.index += 1
            if game.index < len(LESSONS): game.prepare()
            else:
                game.mode = 'result'; game.message = f"Juego terminado — Puntaje: {game.score}/{len(LESSONS)}"
        for b in game.buttons:
            b.handle_event(event)

# ---------- Main loop ----------
while True:
    dt = clock.tick(FPS)/1000.0
    handle_events()
    bg.update(dt)
    game.update(dt)
    # clear screen with animated background
    bg_surf = pygame.Surface((WIDTH, HEIGHT))
    bg.render(bg_surf)
    screen.blit(bg_surf, (0,0))
    # draw game UI
    game.draw(screen)
    pygame.display.flip()
