# sintaxis_bilingue_game.py
# Juego: Sintaxis Bilingüe (español - inglés) con UI inmersiva en Pygame
# Requisitos: pygame
# Ejecutar: python sintaxis_bilingue_game.py

import pygame, sys, random, math, time

pygame.init()
pygame.font.init()

# ----------------- Config -----------------
W, H = 1200, 720
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sintaxis Bilingüe — Practica Español ↔ English 🎓🌈")
CLOCK = pygame.time.Clock()
FPS = 60

# Fuentes
try:
    FONT_TITLE = pygame.font.SysFont("Segoe UI", 30, bold=True)
    FONT_MED = pygame.font.SysFont("Segoe UI", 20)
    FONT_SMALL = pygame.font.SysFont("Segoe UI", 16)
    FONT_EMO = pygame.font.SysFont("Segoe UI Emoji", 32)
except:
    FONT_TITLE = pygame.font.SysFont(None, 30, bold=True)
    FONT_MED = pygame.font.SysFont(None, 20)
    FONT_SMALL = pygame.font.SysFont(None, 16)
    FONT_EMO = pygame.font.SysFont(None, 24)

# Colores
WHITE = (250, 250, 250)
BLACK = (18, 18, 18)
GLASS_ALPHA = 120

# Emojis hints
SYN_EMO = {"simple":"🟢", "coordinada":"🔵", "subordinada":"🟣", "yuxtapuesta":"🟠"}

# ----------------- Utilidades gráficas -----------------
def draw_animated_gradient(surface, t):
    """Dibuja un gradiente vertical animado"""
    r1 = int(40 + 60*math.sin(t*0.6))
    g1 = int(60 + 70*math.sin(t*0.8+1))
    b1 = int(140 + 40*math.cos(t*0.5+2))
    r2 = int(180 + 40*math.cos(t*0.7))
    g2 = int(70 + 60*math.cos(t*0.9+1))
    b2 = int(120 + 60*math.sin(t*0.4+2))
    for y in range(H):
        k = y / H
        r = int(r1*(1-k) + r2*k)
        g = int(g1*(1-k) + g2*k)
        b = int(b1*(1-k) + b2*k)
        pygame.draw.line(surface, (r,g,b), (0,y), (W,y))

def draw_glass(surface, rect, radius=12, alpha=GLASS_ALPHA):
    s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    s.fill((255,255,255, alpha))
    surface.blit(s, (rect.x, rect.y))
    pygame.draw.rect(surface, (255,255,255, 18), rect, border_radius=radius, width=1)

# ----------------- RainbowButton -----------------
class RainbowButton:
    def __init__(self, rect, text, action=None, icon=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
        self.icon = icon or ""
        self.hover = False
        self.pulse = 1.0
        self.cooldown = 0.0

    def update(self, dt, mouse_pos, mouse_down):
        self.hover = self.rect.collidepoint(mouse_pos)
        if self.hover:
            self.pulse = min(1.12, self.pulse + dt * 3.8)
        else:
            self.pulse = max(1.0, self.pulse - dt * 3.2)
        if self.hover and mouse_down and self.cooldown <= 0:
            if self.action:
                self.action()
            self.cooldown = 0.2
        self.cooldown = max(0.0, self.cooldown - dt)

    def draw(self, surface):
        # gradient base
        gsurf = pygame.Surface((self.rect.w, self.rect.h))
        for x in range(self.rect.w):
            t = (x / self.rect.w + time.time() * 0.12) % 1.0
            r = int(150 + 90 * math.sin(2*math.pi*t))
            g = int(80 + 90 * math.sin(2*math.pi*(t + 0.33)))
            b = int(180 + 70 * math.sin(2*math.pi*(t + 0.66)))
            pygame.draw.line(gsurf, (r,g,b), (x,0), (x,self.rect.h))
        # overlay pulse
        ov = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
        alpha = int(40 * (self.pulse - 1.0))
        ov.fill((255,255,255, alpha))
        gsurf.blit(ov, (0,0))
        pygame.draw.rect(gsurf, (255,255,255, 24), gsurf.get_rect(), width=2, border_radius=10)
        surface.blit(gsurf, (self.rect.x, self.rect.y))
        # text and icon
        txt = FONT_MED.render(self.text, True, BLACK)
        surface.blit(txt, (self.rect.x + 12, self.rect.y + (self.rect.h - txt.get_height())//2))
        if self.icon:
            ico = FONT_EMO.render(self.icon, True, BLACK)
            surface.blit(ico, (self.rect.right - 40, self.rect.y + (self.rect.h - ico.get_height())//2))

# ----------------- Partículas emoji -----------------
class EmojiParticle:
    def __init__(self, x, y, emoji):
        self.x = x + random.uniform(-12,12)
        self.y = y + random.uniform(-8,8)
        self.vx = random.uniform(-120,120)
        self.vy = random.uniform(-260,-80)
        self.emoji = emoji
        self.life = random.uniform(0.9, 1.9)
        self.ttl = self.life
        self.rot = random.uniform(-180,180)
        self.rotspeed = random.uniform(-100,100)
        self.size = random.randint(18,36)

    def update(self, dt):
        self.vy += 420 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rot += self.rotspeed * dt
        self.ttl -= dt

    def draw(self, surface):
        if self.ttl <= 0: 
            return
        alpha = max(0, int(255 * (self.ttl / self.life)))
        f = pygame.font.SysFont("Segoe UI Emoji", self.size)
        s = f.render(self.emoji, True, (255,255,255))
        surf = pygame.Surface(s.get_size(), pygame.SRCALPHA)
        surf.blit(s, (0,0))
        surf.set_alpha(alpha)
        surf = pygame.transform.rotate(surf, self.rot)
        surface.blit(surf, (self.x, self.y))

class ParticleSystem:
    def __init__(self):
        self.parts = []
    def emit(self, x, y, emojis, count=12):
        for _ in range(count):
            self.parts.append(EmojiParticle(x, y, random.choice(emojis)))
    def update(self, dt):
        for p in self.parts: p.update(dt)
        self.parts = [p for p in self.parts if p.ttl > 0 and -200 < p.x < W+200 and p.y < H+200]
    def draw(self, surface):
        for p in self.parts: p.draw(surface)

particles = ParticleSystem()

# ----------------- Datos: 20 oraciones bilingües y tipos -----------------
# Cada item: {es: "spanish sentence", en: "english translation", type: one of "simple","coordinada","subordinada","yuxtapuesta"}
QA = [
    {"es":"El perro duerme en el sofá.", "en":"The dog sleeps on the sofa.", "type":"simple"},
    {"es":"María estudia todas las noches.", "en":"María studies every night.", "type":"simple"},
    {"es":"Fui al cine y luego cené con mis amigos.", "en":"I went to the movies and then had dinner with my friends.", "type":"coordinada"},
    {"es":"El sol brillaba, pero hacía frío.", "en":"The sun was shining, but it was cold.", "type":"coordinada"},
    {"es":"Si estudias, aprobarás el examen.", "en":"If you study, you will pass the exam.", "type":"subordinada"},
    {"es":"Aunque estaba cansado, siguió trabajando.", "en":"Although he was tired, he continued working.", "type":"subordinada"},
    {"es":"Llegué tarde; no encontré a nadie.", "en":"I arrived late; I didn't find anyone.", "type":"yuxtapuesta"},
    {"es":"El libro que compré ayer es interesante.", "en":"The book I bought yesterday is interesting.", "type":"subordinada"},
    {"es":"No vino a clase porque estaba enfermo.", "en":"He didn't come to class because he was ill.", "type":"coordinada"},
    {"es":"Llegaré tarde ya que hay mucho tráfico.", "en":"I'll be late since there's a lot of traffic.", "type":"coordinada"},
    {"es":"No estudió, así que reprobó.", "en":"He didn't study, so he failed.", "type":"coordinada"},
    {"es":"Cuando llegues, avísame.", "en":"When you arrive, let me know.", "type":"subordinada"},
    {"es":"Laura canta y Juan toca la guitarra.", "en":"Laura sings and Juan plays the guitar.", "type":"coordinada"},
    {"es":"Los niños juegan; los padres conversan.", "en":"The children play; the parents talk.", "type":"yuxtapuesta"},
    {"es":"Apenas salió de casa empezó a llover.", "en":"Hardly had he left the house when it began to rain.", "type":"subordinada"},
    {"es":"No solo cantó, sino que también bailó.", "en":"Not only did she sing, but she also danced.", "type":"coordinada"},
    {"es":"Me alegra que hayas venido.", "en":"I am glad that you came.", "type":"subordinada"},
    {"es":"Él estudia y además trabaja medio tiempo.", "en":"He studies and also works part-time.", "type":"coordinada"},
    {"es":"Llegaron, saludaron y se fueron.", "en":"They arrived, greeted, and left.", "type":"yuxtapuesta"},
    {"es":"La ciudad despertó; la gente salió a la calle.", "en":"The city woke up; people went out to the streets.", "type":"yuxtapuesta"},
]

random.shuffle(QA)

# ----------------- Estado del juego -----------------
index = 0
score = 0
lives = 3
show_hint = False
current_choices_en = []  # 3 choices (one correct)
correct_choice_idx = 0
selected_type = None
message = ""
message_color = (0,0,0)
particle_emojis = ["✅","🎉","✨","🎯","📚"]

# ----------------- Helpers para crear opciones -----------------
def make_choices(correct_en):
    # pick two distractors from other QA english sentences
    pool = [q["en"] for q in QA if q["en"] != correct_en]
    choices = random.sample(pool, 2) + [correct_en]
    random.shuffle(choices)
    return choices

# ----------------- UI: botones de respuesta y clasificacion -----------------
answer_buttons = []
class_buttons = []

def on_answer(i):
    global message, message_color, score, lives, selected_type
    chosen = current_choices_en[i]
    correct_en = QA[index]["en"]
    if chosen == correct_en:
        message = "¡Traducción correcta! " + FONT_EMO.render("✅", True, (0,0,0)).to_string()  # placeholder
        message_color = (20,120,20)
        # now check classification too
        if selected_type == QA[index]["type"]:
            # full correct
            score += 2
            particles.emit(W//2, 120, particle_emojis, count=20)
            # small reward
            message = "Perfecto: traducción + clasificación ✅"
            message_color = (20,120,20)
            next_question(delay=0.9)
        else:
            # correct translation but type not chosen
            score += 1
            message = "Traducción correcta — elige la clasificación sintáctica."
            message_color = (20,120,20)
    else:
        lives -= 1
        message = "Traducción incorrecta ❌"
        message_color = (180,30,30)
        particles.emit(W//2, 120, ["😢","❌"], count=12)
        next_question(delay=1.2)

def on_class(tipo):
    global selected_type, message, message_color, score, lives
    selected_type = tipo
    # if translation already correct and type matches -> reward
    correct_en = QA[index]["en"]
    # we don't know if player already clicked translation; so check nothing here.
    message = f"Seleccionaste: {tipo} {SYN_EMO.get(tipo,'')}"
    message_color = (60,60,200)

# ----------------- Next question logic -----------------
next_time = 0
def next_question(delay=0.0):
    global next_time
    next_time = pygame.time.get_ticks() + int(delay*1000)

# ----------------- Build UI objects (buttons) -----------------
def build_ui():
    global answer_buttons, class_buttons
    answer_buttons = []
    class_buttons = []
    # answer buttons area
    ay = 200
    bw = 520; bh = 56; gap = 16
    left = 40
    for i in range(3):
        btn = RainbowButton((left, ay + i*(bh+gap), bw, bh), "Answer", action=lambda i=i: on_answer(i))
        answer_buttons.append(btn)
    # classification buttons on right
    cx = W - 320
    cy = 180
    for i, t in enumerate(["simple","coordinada","subordinada","yuxtapuesta"]):
        btn = RainbowButton((cx, cy + i*(50), 260, 44), t.capitalize(), action=lambda tt=t: on_class(tt), icon=SYN_EMO.get(t))
        class_buttons.append(btn)

# ----------------- Render helpers -----------------
def render_question():
    # Spanish sentence at top (glass panel)
    rect = pygame.Rect(30, 40, W-380, 110)
    draw_glass(SCREEN, rect, radius=14)
    es = QA[index]["es"]
    txt = FONT_MED.render("Español:", True, BLACK)
    SCREEN.blit(txt, (rect.x+12, rect.y+8))
    es_surface = FONT_TITLE.render(es, True, BLACK)
    SCREEN.blit(es_surface, (rect.x+12, rect.y+40))
    # small bilingual hint (icon)
    hint = f"Tip: {SYN_EMO[QA[index]['type']] }  ({QA[index]['type']})"
    SCREEN.blit(FONT_SMALL.render(hint, True, BLACK), (rect.x+12, rect.y + rect.h - 24))

def render_answers():
    for i, btn in enumerate(answer_buttons):
        btn.text = current_choices_en[i]
        btn.draw(SCREEN)

def render_class_buttons():
    for b in class_buttons:
        b.draw(SCREEN)

def render_sidebar():
    panel = pygame.Rect(W-340, 20, 300, H-40)
    draw_glass(SCREEN, panel, radius=14)
    SCREEN.blit(FONT_TITLE.render("Sintaxis Bilingüe", True, BLACK), (panel.x+12, panel.y+12))
    SCREEN.blit(FONT_MED.render(f"Puntaje: {score}", True, BLACK), (panel.x+12, panel.y+58))
    SCREEN.blit(FONT_MED.render(f"Vidas: {lives}", True, BLACK), (panel.x+12, panel.y+82))
    SCREEN.blit(FONT_SMALL.render("Instrucciones:", True, BLACK), (panel.x+12, panel.y+120))
    lines = [
        "1) Elige la traducción correcta (inglés).",
        "2) Selecciona el tipo sintáctico correcto.",
        "3) Si aciertas ambos, obtienes +2 puntos.",
        "4) Acierto parcial (solo traducción) +1 punto.",
        "5) Fallar resta vidas.",
    ]
    for i,l in enumerate(lines):
        SCREEN.blit(FONT_SMALL.render(l, True, BLACK), (panel.x+12, panel.y+150 + i*20))

def render_message():
    if message:
        sur = FONT_MED.render(message, True, message_color)
        SCREEN.blit(sur, (40, 360))

# ----------------- Game loop helpers -----------------
def start_round():
    global current_choices_en, correct_choice_idx, selected_type, message, message_color
    selected_type = None
    message = ""
    message_color = (0,0,0)
    # prepare choices
    correct = QA[index]["en"]
    current_choices_en = make_choices(correct)
    correct_choice_idx = current_choices_en.index(correct)
    # set rainbow buttons actions
    for i, btn in enumerate(answer_buttons):
        # redefine action closure properly
        btn.action = (lambda i=i: on_answer(i))
    for i, b in enumerate(class_buttons):
        b.action = (lambda t=["simple","coordinada","subordinada","yuxtapuesta"][i]: on_class(t))

# ----------------- Main loop -----------------
build_ui()
start_round()
running = True
mouse_down_prev = False
last_tick = pygame.time.get_ticks()
auto_next = False

while running:
    dt = CLOCK.tick(FPS)/1000.0
    t = time.time()
    mouse_pos = pygame.mouse.get_pos()
    mouse_down = pygame.mouse.get_pressed()[0]

    # input events
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False

    # update buttons
    for b in answer_buttons + class_buttons:
        b.update(dt, mouse_pos, mouse_down)

    # auto advance if next_time passed (managed by next_question)
    if next_time and pygame.time.get_ticks() >= next_time:
        # advance index
        next_time = 0
        index += 1
        if index >= len(QA):
            # end game summary
            running = False
            continue
        start_round()

    # render
    draw_animated_gradient(SCREEN, t)
    render_question()
    render_answers()
    render_class_buttons()
    render_sidebar()
    particles.update(dt)
    particles.draw(SCREEN)
    render_message()

    # hover effect: show selected classification
    if selected_type:
        hint = f"Seleccionado: {selected_type} {SYN_EMO.get(selected_type,'')}"
        SCREEN.blit(FONT_SMALL.render(hint, True, (30,30,30)), (40, 400))

    pygame.display.flip()

# End screen
SCREEN.fill((20,20,20))
end_text = FONT_TITLE.render("Gracias por jugar — Resultado final", True, (255,255,255))
SCREEN.blit(end_text, (W//2 - end_text.get_width()//2, H//2 - 60))
score_text = FONT_MED.render(f"Puntaje: {score}", True, (255,255,255))
SCREEN.blit(score_text, (W//2 - score_text.get_width()//2, H//2))
pygame.display.flip()
pygame.time.delay(4000)

pygame.quit()
sys.exit()
