# modulo9_aventura_expandida.py
"""
Módulo 9 - Aventura Gramatical Expandida (Pygame)
Guardar como: modulo9_aventura_expandida.py
Requisitos: pip install pygame
Ejecutar: python modulo9_aventura_expandida.py
"""

import pygame, sys, random, math, time
from pygame import Rect

pygame.init()
# ----- Config -----
WIDTH, HEIGHT = 960, 680
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Ranch — Aventura Gramatical (Módulo 9 Expandido)")
CLOCK = pygame.time.Clock()
FPS = 60

# ----- Colores -----
WHITE = (255,255,255)
BLACK = (18,18,20)
RUBY = (180,20,60)
TRANSLUCENT = (0,0,0,120)

# ----- Fuentes -----
FONT_LG = pygame.font.Font(None, 36)
FONT_MD = pygame.font.Font(None, 24)
FONT_SM = pygame.font.Font(None, 18)
EMOJI_FONT = pygame.font.Font(None, 36)  # emoji rendering is best-effort

# ----- Utilidades -----
def lerp(a,b,t): return a + (b-a)*t

# ----- Fondo animado (gradiente) -----
class AnimatedBG:
    def __init__(self,w,h):
        self.w, self.h = w,h
        self.t = 0.0
    def update(self, dt): self.t += dt * 0.4
    def render(self, surf):
        t = self.t
        for i in range(0, self.h, 4):
            r = int(30 + 60*(1 + math.sin((i/60.0)+t)))
            g = int(20 + 70*(1 + math.sin((i/70.0)+t+2.0)))
            b = int(90 + 60*(1 + math.sin((i/80.0)+t+4.0)))
            pygame.draw.rect(surf, (r,g,b), (0,i,self.w,4))

BG = AnimatedBG(WIDTH, HEIGHT)

# ----- Partículas (emoji) -----
class EmojiParticle:
    def __init__(self, x, y, emoji='✨'):
        self.x = x; self.y = y
        self.vx = random.uniform(-120,120)
        self.vy = random.uniform(-200,-80)
        self.size = random.randint(18,36)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(1.0, 2.6)
        self.angle = random.uniform(0,360)
        self.spin = random.uniform(-220,220)
        # render once
        try:
            self.surf = EMOJI_FONT.render(self.emoji, True, WHITE)
            if self.surf.get_width() == 0: raise Exception()
        except Exception:
            # fallback circle
            self.surf = pygame.Surface((self.size,self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.surf, (255,255,0), (self.size//2,self.size//2), self.size//2)
    def update(self, dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt
    def draw(self, surf):
        alpha = max(0, int(255 * (1 - self.age/self.life)))
        img = pygame.transform.rotozoom(self.surf, self.angle, 1.0)
        img.set_alpha(alpha)
        w,h = img.get_size()
        surf.blit(img, (self.x - w//2, self.y - h//2))
    def dead(self):
        return self.age >= self.life or self.y < -100 or self.y > HEIGHT + 200

PARTICLES = []
def spawn_particles(x,y,count=18,good=True):
    pool_good = ['🎉','✨','🌟','👏','📘']
    pool_bad  = ['❗','💥','😅','⚠️']
    pool = pool_good if good else pool_bad
    for _ in range(count):
        emo = random.choice(pool)
        p = EmojiParticle(x + random.uniform(-40,40), y + random.uniform(-20,20), emo)
        # upward or outward
        if good:
            p.vy = random.uniform(-220,-80)
            p.vx = random.uniform(-160,160)
        else:
            p.vy = random.uniform(-90,30)
            p.vx = random.uniform(-80,80)
        PARTICLES.append(p)

# ----- RainbowButton (hover + press + color cycle) -----
class RainbowButton:
    def __init__(self, rect, text, onclick=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.onclick = onclick
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.hue = random.random() * 360.0
    def update(self, dt):
        self.hue = (self.hue + dt * 80) % 360
        target = 0.96 if self.pressed else (1.05 if self.hover else 1.0)
        self.scale = lerp(self.scale, target, min(1.0, dt * 12))
    def draw(self, surf):
        h = self.hue / 360.0
        r = int(140 + 100 * math.sin(h*2*math.pi))
        g = int(60 + 100 * math.sin((h+0.33)*2*math.pi))
        b = int(160 + 80 * math.sin((h+0.66)*2*math.pi))
        color = (max(0,min(255,r)), max(0,min(255,g)), max(0,min(255,b)))
        rw = int(self.rect.w * self.scale)
        rh = int(self.rect.h * self.scale)
        rx = int(self.rect.centerx - rw//2)
        ry = int(self.rect.centery - rh//2)
        base = pygame.Surface((rw,rh), pygame.SRCALPHA)
        base.fill((*color, 230))
        pygame.draw.rect(base, color, base.get_rect(), border_radius=12)
        # glossy
        pygame.draw.rect(base, (255,255,255,30), (6,6,rw-12, rh//2), border_radius=10)
        surf.blit(base, (rx, ry))
        # text
        txt = FONT_MD.render(self.text, True, BLACK)
        surf.blit(txt, (rx + (rw - txt.get_width())//2, ry + (rh - txt.get_height())//2))
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

# ----- Player -----
class Player:
    def __init__(self, x,y):
        self.rect = Rect(x,y,44,44)
        self.speed = 160
        self.color = (120,220,180)
    def handle_movement(self, keys, dt):
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy += 1
        if dx!=0 or dy!=0:
            norm = math.hypot(dx,dy) or 1
            self.rect.x += int(self.speed * (dx/norm) * dt)
            self.rect.y += int(self.speed * (dy/norm) * dt)
            # keep in bounds
            self.rect.x = max(10, min(WIDTH - self.rect.w - 10, self.rect.x))
            self.rect.y = max(10, min(HEIGHT - self.rect.h - 10, self.rect.y))
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)
        # face
        surf.blit(FONT_SM.render("🙂", True, BLACK), (self.rect.x+6, self.rect.y+4))

# ----- Interactive objects -----
class Interactive:
    def __init__(self, x,y,w,h,kind,emoji,label):
        self.rect = Rect(x,y,w,h)
        self.kind = kind   # 'book','teacher','door','board'
        self.emoji = emoji
        self.label = label
        self.completed = False
        self.locked = True if kind=='door' else False
    def draw(self, surf):
        # base
        color = (200,200,200) if not self.completed else (120,220,180)
        pygame.draw.rect(surf, color, self.rect, border_radius=8)
        # emoji
        surf.blit(EMOJI_FONT.render(self.emoji, True, BLACK), (self.rect.x+8, self.rect.y+6))
        txt = FONT_SM.render(self.label, True, BLACK)
        surf.blit(txt, (self.rect.x+48, self.rect.y + (self.rect.h - txt.get_height())//2))
        # if locked show lock icon
        if self.locked and not self.completed:
            surf.blit(FONT_SM.render("🔒", True, (200,40,40)), (self.rect.right-30, self.rect.y+8))

# ----- Question bank: each object maps to a question type -----
QUESTION_BANK = {
    'book': [
        {"es":"Traduce: 'I eat apples'","options":["Yo como manzanas","Yo comí manzanas","Yo comeré manzanas"], "answer":0},
        {"es":"Traduce: 'She reads a book'","options":["Ella lee un libro","Ella leyó un libro","Ella leerá un libro"], "answer":0}
    ],
    'teacher': [
        {"es":"¿Cuál es afirmativa?: 'He studies' vs 'He doesn't study'","options":["He studies","He doesn't study"], "answer":0},
        {"es":"Cuál opción es afirmativa: 'They are' / 'They aren't'","options":["They are","They aren't"], "answer":0}
    ],
    'door': [
        {"es":"Transforma a pregunta: 'You like pizza.'","options":["Do you like pizza?","You do like pizza?"], "answer":0},
        {"es":"Pregunta de ejemplo: 'She can sing.' → ?","options":["Can she sing?","She can sing?"], "answer":0}
    ],
    'board': [
        {"es":"Elige la compuesta: 'I was late. I missed the bus.'","options":["Because I missed the bus, I was late.","I was late because I missed the bus."], "answer":1},
        {"es":"Une con nexo adecuado: 'It rained. We stayed home.'","options":["We stayed home because it rained.","We stayed home but it rained."], "answer":0}
    ]
}

# ----- Setup world objects -----
player = Player(80, HEIGHT//2)
objects = [
    Interactive(320, 120, 220, 56, 'book', '📘', 'Libro (vocabulario)'),
    Interactive(620, 120, 220, 56, 'teacher', '🎓', 'Profesor (afirmativa)'),
    Interactive(320, 420, 220, 56, 'board', '📝', 'Tablero (compuestas)'),
    Interactive(620, 420, 220, 56, 'door', '🚪', 'Puerta (preguntas)')
]
# door unlocked once door's question answered; we'll set door.locked True initially
for obj in objects:
    if obj.kind=='door':
        obj.locked = True

# ----- Modal UI for questions -----
class QuestionModal:
    def __init__(self):
        self.active = False
        self.question = None
        self.options = []
        self.correct_idx = None
        self.selected = None
        self.buttons = []
        self.origin_obj = None
        self.feedback = ""
    def open(self, obj):
        self.origin_obj = obj
        bank = QUESTION_BANK.get(obj.kind, [])
        if not bank:
            return
        q = random.choice(bank)
        self.question = q['es']
        self.options = q['options']
        self.correct_idx = q['answer']
        self.selected = None
        self.feedback = ""
        self.buttons = []
        # create buttons positions
        w = 420; h = 56
        startx = (WIDTH - w) // 2
        starty = HEIGHT//2 - 20
        spacing = 72
        for i,opt in enumerate(self.options):
            rect = (startx, starty + i*spacing, w, h)
            btn = RainbowButton(rect, opt, onclick=lambda i=i: self.select(i))
            self.buttons.append(btn)
        self.active = True
    def select(self, idx):
        self.selected = idx
        correct = (idx == self.correct_idx)
        # mark completion and actions
        if correct:
            self.feedback = "✅ Correcto!"
            spawn_particles(WIDTH//2, HEIGHT//2, 26, good=True) if 'spawn_particles' in globals() else None
            # mark object completed
            if self.origin_obj:
                self.origin_obj.completed = True
                # special: if it's 'door', we unlock after correct answer OR if it's the door's question, door unlocks itself
                if self.origin_obj.kind == 'door':
                    self.origin_obj.locked = False
        else:
            self.feedback = "❌ Incorrecto — intenta otra vez"
            spawn_particles(WIDTH//2, HEIGHT//2, 12, good=False) if 'spawn_particles' in globals() else None
        # auto-close later
        pygame.time.set_timer(pygame.USEREVENT+2, 900)
    def draw(self, surf):
        # dark overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,160))
        surf.blit(overlay, (0,0))
        # panel
        panel_w, panel_h = 760, 360
        panel = Rect((WIDTH-panel_w)//2, (HEIGHT-panel_h)//2, panel_w, panel_h)
        panel_surf = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        # glass effect
        panel_surf.fill((255,255,255,18))
        pygame.draw.rect(panel_surf, (255,255,255,20), panel_surf.get_rect(), border_radius=16)
        surf.blit(panel_surf, (panel.x, panel.y))
        # question text
        qrect = Rect(panel.x+24, panel.y+18, panel.w-48, 80)
        draw_centered_text(surf, self.question, FONT_LG, WHITE, qrect)
        # draw buttons
        for b in self.buttons:
            b.draw(surf)
        # feedback
        if self.feedback:
            fb = FONT_MD.render(self.feedback, True, WHITE)
            surf.blit(fb, (panel.x + (panel.w - fb.get_width())//2, panel.y + panel.h - 48))
    def handle_event(self, event):
        for b in self.buttons:
            b.handle_event(event)

def draw_centered_text(surface, text, font, color, rect):
    lines = text.splitlines()
    total_h = sum(font.size(l)[1] for l in lines)
    y = rect.y + (rect.h - total_h)//2
    for line in lines:
        surf_line = font.render(line, True, color)
        x = rect.x + (rect.w - surf_line.get_width())//2
        surface.blit(surf_line, (x,y))
        y += surf_line.get_height()

MODAL = QuestionModal()

# ----- Helper: spawn_particles wrapper uses global spawn_particles -----
def spawn_particles(x,y,count,good=True):
    spawn_particles.__wrapped__(x,y,count,good) if False else None  # avoid linter; actual function defined above
# we already defined spawn_particles earlier; rebind to local name
spawn_particles = globals()['spawn_particles']

# ----- Game loop variables -----
running = True
modal_open = False
win_message = ""
start_time = time.time()

# ----- Main loop -----
def all_tasks_completed():
    # consider all objects except door need to be completed, and door must be unlocked (not locked)
    for obj in objects:
        if obj.kind == 'door':
            if obj.locked: return False
        else:
            if not obj.completed: return False
    return True

while running:
    dt = CLOCK.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # modal auto-close timer
        if event.type == pygame.USEREVENT+2:
            MODAL.active = False
            pygame.time.set_timer(pygame.USEREVENT+2, 0)
        # route events to buttons if modal active
        if MODAL.active:
            MODAL.handle_event(event)
        else:
            # handle button hover/press events for potential UI later
            pass
        # allow RainbowButtons in modal to get mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not MODAL.active:
                # if click when not modal, maybe interact with objects via mouse (optional)
                pass

    # update
    BG.update(dt)
    # update buttons inside modal
    if MODAL.active:
        for b in MODAL.buttons:
            b.update(dt)
    # update player movement if no modal
    keys = pygame.key.get_pressed()
    if not MODAL.active:
        player.handle_movement(keys, dt)

    # update particles
    for p in PARTICLES[:]:
        p.update(dt)
        if p.dead():
            try: PARTICLES.remove(p)
            except: pass

    # check collisions: if player overlaps interactive object and not modal open:
    if not MODAL.active:
        for obj in objects:
            if player.rect.colliderect(obj.rect):
                # door special rules: if locked, open modal about the door; if unlocked and completed, pass through (simulate)
                if obj.kind == 'door':
                    if obj.locked:
                        MODAL.open(obj)
                    else:
                        # door completed/unlocked: teleport player to "goal area" and mark as completed
                        obj.completed = True
                        spawn_particles(obj.rect.centerx, obj.rect.centery, 28, good=True)
                        # optionally move player to start to continue exploring
                        player.rect.x, player.rect.y = 40,40
                else:
                    if not obj.completed:
                        MODAL.open(obj)
                    # if already completed, small reward
                    else:
                        # gentle particles if touching completed object
                        if random.random() < 0.02:
                            spawn_particles(obj.rect.centerx, obj.rect.centery, 6, good=True)

    # Drawing
    BG.render(SCREEN)
    # draw ground panel (glass look)
    panel = Rect(24,24, WIDTH-48, HEIGHT-48)
    panel_surf = pygame.Surface((panel.w, panel.h), pygame.SRCALPHA)
    panel_surf.fill((255,255,255,12))
    pygame.draw.rect(panel_surf, (255,255,255,20), panel_surf.get_rect(), border_radius=18)
    SCREEN.blit(panel_surf, (panel.x, panel.y))

    # draw world title and progress
    title = FONT_LG.render("Aventura Gramatical — Explora y responde", True, WHITE)
    SCREEN.blit(title, (40,36))
    progress = FONT_SM.render(f"Progreso: {sum(1 for o in objects if o.completed)} / {len(objects)}", True, WHITE)
    SCREEN.blit(progress, (40, 80))
    # draw objects (background layer)
    for obj in objects:
        obj.draw(SCREEN)
    # draw player on top
    player.draw(SCREEN)
    # draw particles above
    for p in PARTICLES:
        p.draw(SCREEN)

    # if modal active draw it
    if MODAL.active:
        MODAL.draw(SCREEN)

    # check win
    if all_tasks_completed():
        win_message = "🎉 ¡Has completado la aventura! Todos los retos resueltos."
        # show victory modal small
        overlay = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,160))
        SCREEN.blit(overlay,(0,0))
        draw_centered_text(SCREEN, win_message, FONT_LG, WHITE, Rect(0, HEIGHT//2-40, WIDTH, 80))
        draw_centered_text(SCREEN, "Reinicia el juego para jugar otra vez (cierra y abre).", FONT_SM, WHITE, Rect(0, HEIGHT//2 + 20, WIDTH, 40))
        pygame.display.flip()
        # freeze for a few seconds then exit loop
        pygame.time.delay(3000)
        running = False
        continue

    pygame.display.flip()

pygame.quit()
sys.exit()
