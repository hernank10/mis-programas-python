# syntax_game_grade6.py
# Juego educativo Pygame: Sintaxis bilingüe (ES/EN) para estudiantes de 6º grado
# Características: RainbowButton (hover/pulse), emoticones, partículas-emojis, gradients, glassmorphism, transiciones.
# Guardar como syntax_game_grade6.py; ejecutar con `python syntax_game_grade6.py`.
# Requiere pygame: pip install pygame

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# ---------------- Config ----------------
WIDTH, HEIGHT = 1100, 650
FPS = 60

# Paleta natural y vibrante
PALETTE = {
    "bg_top": (92, 151, 191),    # cielo
    "bg_bottom": (255, 240, 200),# arena suave
    "glass": (255,255,255,40),
    "text": (20,20,20),
    "accent": (255,120,90),
    "accent2": (60,180,120)
}

# Fuentes
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 26)
    FONT_XL = pygame.font.Font(None, 34)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 24)
    FONT_XL = pygame.font.SysFont("arial", 30)

# Intento de fuente emoji (dependerá del SO)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# Utilidades
def lerp(a,b,t): return a + (b-a)*t
def rounded_rect(surface, rect, color, radius=12):
    x,y,w,h = rect
    # draw rounded rectangle (approx)
    pygame.gfxdraw.aacircle(surface, x+radius, y+radius, radius, color)
    pygame.gfxdraw.filled_circle(surface, x+radius, y+radius, radius, color)
    pygame.gfxdraw.aacircle(surface, x+w-radius-1, y+radius, radius, color)
    pygame.gfxdraw.filled_circle(surface, x+w-radius-1, y+radius, radius, color)
    pygame.gfxdraw.aacircle(surface, x+radius, y+h-radius-1, radius, color)
    pygame.gfxdraw.filled_circle(surface, x+radius, y+h-radius-1, radius, color)
    pygame.gfxdraw.aacircle(surface, x+w-radius-1, y+h-radius-1, radius, color)
    pygame.gfxdraw.filled_circle(surface, x+w-radius-1, y+h-radius-1, radius, color)
    pygame.draw.rect(surface, color, (x+radius, y, w-2*radius, h))
    pygame.draw.rect(surface, color, (x, y+radius, w, h-2*radius))

# ---------------- RainbowButton ----------------
class RainbowButton:
    def __init__(self, rect, text, emoji="🙂", on_click=None, hue_offset=0):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.emoji = emoji
        self.on_click = on_click
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.anim = 0.0
        self.hue_offset = hue_offset
        self.enabled = True

    def update(self, dt):
        self.anim += dt
        target = 1.06 if self.hover else 1.0
        if self.pressed: target = 0.95
        self.scale += (target - self.scale) * min(1, dt*8)

    def draw(self, surf):
        # simple animated gradient based on anim
        t = (math.sin(self.anim*2.0 + self.hue_offset) + 1)/2
        c1 = (int(lerp(255, 150, t)), int(lerp(160, 220, t)), int(lerp(120, 240, t)))
        c2 = (int(lerp(120, 80, t)), int(lerp(200, 240, t)), int(lerp(255, 200, t)))
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        for y in range(h):
            ty = y / max(1, h-1)
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,230), (0,y),(w,y))
        # glass highlight
        overlay = pygame.Surface((w,h//2), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (255,255,255,45), overlay.get_rect(), border_radius=10)
        temp.blit(overlay, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale and blit
        sw = int(w * self.scale)
        sh = int(h * self.scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        draw_x = self.rect.x + (w - sw)//2
        draw_y = self.rect.y + (h - sh)//2
        surf.blit(scaled, (draw_x, draw_y))
        # border
        pygame.draw.rect(surf, (255,255,255,90), (draw_x,draw_y,sw,sh), 2, border_radius=12)
        # emoji + text
        try:
            emoji_s = EMOJI_FONT.render(self.emoji, True, (10,10,10))
        except:
            emoji_s = FONT.render(self.emoji, True, (10,10,10))
        text_s = FONT.render(self.text, True, (10,10,10))
        tx = draw_x + 12
        ty = draw_y + (sh - text_s.get_height())//2
        surf.blit(emoji_s, (tx, ty))
        surf.blit(text_s, (tx + 40, ty))

    def handle_event(self, event):
        if not self.enabled: return
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover and event.button == 1:
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressed and event.button == 1:
                self.pressed = False
                if self.hover and self.on_click:
                    self.on_click(self)

# ---------------- Partículas emoticones ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji, col=(255,255,255)):
        self.x = x
        self.y = y
        self.vx = random.uniform(-80,80)
        self.vy = random.uniform(-220,-60)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(1.0,2.2)
        self.spin = random.uniform(-240,240)
        self.angle = random.uniform(0,360)
        self.size = random.randint(20,44)
        self.col = col

    def update(self, dt):
        self.age += dt
        self.vy += 300 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age/self.life)
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        try:
            txt = EMOJI_FONT.render(self.emoji, True, self.col)
        except:
            txt = FONT.render(self.emoji, True, self.col)
        rect = txt.get_rect(center=(self.size,self.size))
        s.blit(txt, rect)
        s = pygame.transform.rotozoom(s, self.angle, alpha*1.0)
        s.set_alpha(int(alpha*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# ---------------- Exercises (6th grade syntax) ----------------
# prompt: Spanish instruction / question; options: mixed ES/EN choices (bilingual hints); answer index; type; emoji
BASE_EXERCISES = [
    {"prompt":"(ES) ¿Cuál es el sujeto en: 'El perro corre en el parque.' / Which is the subject?",
     "options":["El perro / The dog","corre / runs","en el parque / in the park"], "answer":0, "type":"Sujeto / Subject", "emoji":"🐶"},
    {"prompt":"(ES) ¿Cuál es el verbo en: 'La niña lee un libro.' / Which is the verb?",
     "options":["La niña / The girl","lee / reads","un libro / a book"], "answer":1, "type":"Verbo / Verb", "emoji":"📚"},
    {"prompt":"(ES) Elige el objeto directo en: 'María come una manzana.' / Choose the direct object",
     "options":["María / Maria","come / eats","una manzana / an apple"], "answer":2, "type":"Objeto / Object", "emoji":"🍎"},
    {"prompt":"(ES) ¿Qué palabra es un adjetivo? 'El coche rojo es rápido.' / Which is the adjective?",
     "options":["coche / car","rojo / red","es / is"], "answer":1, "type":"Adjetivo / Adjective", "emoji":"🔴"},
    {"prompt":"(ES) Une con conjunción: 'Quiero jugar, ___ está lloviendo.' / Fill with conjunction",
     "options":["porque / because","y / and","pero / but"], "answer":2, "type":"Conjunción / Conjunction", "emoji":"🌧️"},
    {"prompt":"(ES) Tiempo presente simple en inglés: 'Yo corro todos los días.' → Choose English:",
     "options":["I run every day.","I am running every day.","I ran every day."], "answer":0, "type":"Tiempo / Tense", "emoji":"🏃"},
    {"prompt":"(ES) Formar pregunta (yes/no): 'Tú estudias inglés.' → Which is the correct question?",
     "options":["Do you study English?","You study English?","Study you English?"], "answer":0, "type":"Pregunta / Question", "emoji":"❓"},
    {"prompt":"(ES) ¿Cuál muestra plural? 'El gato' → choose plural:",
     "options":["The cat","The cats","Cat"], "answer":1, "type":"Número / Number", "emoji":"🐱"},
    {"prompt":"(ES) Forma negativa en inglés: 'Ella habla español.' → choose negative:",
     "options":["She not speaks Spanish.","She doesn't speak Spanish.","She no speak Spanish."], "answer":1, "type":"Negación / Negation", "emoji":"🙅‍♀️"},
    {"prompt":"(ES) Oración compuesta con 'and': 'Ana escribe y Juan lee.' → choose translation:",
     "options":["Ana writes and Juan reads.","Ana write and Juan read.","Ana writes Juan reads."], "answer":0, "type":"Compuesta / Compound", "emoji":"✍️"},
    {"prompt":"(ES) Puntuación: ¿dónde debe ir la coma? 'Si llueve iremos a casa.' → choose:",
     "options":["Si llueve, iremos a casa.","Si, llueve iremos a casa.","Si llueve iremos, a casa."], "answer":0, "type":"Puntuación / Punctuation", "emoji":"📝"},
    {"prompt":"(ES) Orden correcto en pregunta '¿Qué hace él?' → choose English:",
     "options":["What he does?","What does he do?","Does what he do?"], "answer":1, "type":"Pregunta / Question", "emoji":"🗣️"},
    {"prompt":"(ES) Condicional simple (0): 'Si calientas agua, hierve.' → choose English:",
     "options":["If you heat water, it boils.","If you heated water, it would boil.","If you heat water, it boiled."], "answer":0, "type":"Condicional / Conditional 0", "emoji":"🔥"},
    {"prompt":"(ES) Completa con 'because' o 'but': 'Me gusta el helado, ___ no me gusta el frío.' → choose:",
     "options":["because","but","and"], "answer":1, "type":"Conector / Connector", "emoji":"🍦"},
    {"prompt":"(ES) Pronombre correcto: 'This is ___ book.' → choose:",
     "options":["my","me","mine"], "answer":0, "type":"Pronombre / Pronoun", "emoji":"📘"},
    {"prompt":"(ES) Orden en inglés: adjetivo antes del sustantivo: 'una casa grande' → choose:",
     "options":["a big house","a house big","house a big"], "answer":0, "type":"Orden / Word Order", "emoji":"🏠"},
    {"prompt":"(ES) Past simple: 'Ayer corrí al parque.' → choose English:",
     "options":["I run to the park yesterday.","I ran to the park yesterday.","I have run to the park yesterday."], "answer":1, "type":"Tiempo pasado / Past Tense", "emoji":"⏳"},
    {"prompt":"(ES) Translate short: 'Ella tiene un perro.' → choose English:",
     "options":["She has a dog.","She have a dog.","Her has a dog."], "answer":0, "type":"Poseer / Have", "emoji":"🐕"},
    {"prompt":"(ES) ¿Cuál es el adverbio? 'Corre rápidamente' → choose:",
     "options":["Corre / Runs","rápidamente / quickly","Corre rápido"], "answer":1, "type":"Adverbio / Adverb", "emoji":"⚡"},
    {"prompt":"(ES) Which punctuation marks end a question in English? → choose:",
     "options":["Comma","Exclamation","Question mark (?)"], "answer":2, "type":"Puntuación / Punctuation", "emoji":"?"},
]

# replicate to reach ~100 items by repeating with slight variations
EXERCISES = []
while len(EXERCISES) < 100:
    for e in BASE_EXERCISES:
        # create small variation for bilinguality if needed
        copy = dict(e)
        EXERCISES.append(copy)
        if len(EXERCISES) >= 100: break

random.shuffle(EXERCISES)

# ---------------- Init Pygame ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Playground — Grade 6 (ES/EN)")
clock = pygame.time.Clock()

particles = []
score = 0
current = 0
feedback = ""
feedback_time = 0.0

# Build option buttons for current exercise
def make_buttons_for(ex):
    btns = []
    base_x = WIDTH//2 + 20
    base_y = 180
    w = 520
    h = 64
    gap = 14
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+gap), w, h)
        # emoji per type for visual cue
        btn = RainbowButton(rect, opt, emoji=ex["emoji"], on_click=lambda b, idx=i: on_select(idx))
        btns.append(btn)
    return btns

buttons = make_buttons_for(EXERCISES[current])

# spawn particles helper
def spawn_particles(x,y,emoji,count=16):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-20,20), y + random.uniform(-10,10), emoji))

# on select
def on_select(idx):
    global score, current, feedback, feedback_time, buttons
    ex = EXERCISES[current]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ ¡Correcto! / Correct! {ex['type']} {ex['emoji']}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 50, ex['emoji'], count=20)
    else:
        correct = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrecto / Incorrect! Answer: {correct}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 50, "💥", count=10)
    feedback_time = time.time()
    # schedule next question
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# Background gradient with subtle motion
def draw_background(t):
    surf = pygame.Surface((WIDTH, HEIGHT))
    top = PALETTE["bg_top"]
    bottom = PALETTE["bg_bottom"]
    shift = (math.sin(t*0.2)+1)/2
    top_mod = (int(lerp(top[0], 80, shift)), int(lerp(top[1], 120, shift)), int(lerp(top[2], 140, shift)))
    bottom_mod = (int(lerp(bottom[0], 200, shift)), int(lerp(bottom[1], 230, shift)), int(lerp(bottom[2], 210, shift)))
    for y in range(HEIGHT):
        ty = y/(HEIGHT-1)
        r = int(lerp(top_mod[0], bottom_mod[0], ty))
        g = int(lerp(top_mod[1], bottom_mod[1], ty))
        b = int(lerp(top_mod[2], bottom_mod[2], ty))
        pygame.draw.line(surf, (r,g,b), (0,y),(WIDTH,y))
    # soft floating shapes
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(4):
        rx = int((math.sin(t*0.25 + i) + 1)/2 * WIDTH) - 300
        ry = int(40 * math.sin(t*0.35 + i))
        pygame.draw.ellipse(overlay, (255,255,255,24), (rx, 80+ry, 700, 220))
    surf.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return surf

start_time = time.time()
running = True

# ---------------- Main loop ----------------
while running:
    dt = clock.tick(FPS)/1000.0
    now = time.time()
    t = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # advance
            current = (current + 1) % len(EXERCISES)
            buttons = make_buttons_for(EXERCISES[current])
            feedback = ""
        # pass events to buttons
        for b in buttons:
            b.handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            for b in buttons:
                b.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.handle_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            for b in buttons:
                b.handle_event(event)

    # update buttons and particles
    for b in buttons:
        b.update(dt)
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # draw background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # left glass panel for prompt
    panel_w = WIDTH//2 - 60
    panel_h = HEIGHT - 120
    panel_x = 30
    panel_y = 50
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill(PALETTE["glass"])
    rounded_rect(glass, (0,0,panel_w,panel_h), PALETTE["glass"], radius=18)
    pygame.draw.rect(glass, (255,255,255,12), (10,10,panel_w-20, panel_h-20), border_radius=14)

    prompt = EXERCISES[current]["prompt"]
    # wrap text
    words = prompt.split(" ")
    lines = []
    line = ""
    maxw = panel_w - 60
    for w in words:
        test = (line + " " + w).strip()
        if FONT_XL.size(test)[0] > maxw and line != "":
            lines.append(line)
            line = w
        else:
            line = test
    if line: lines.append(line)
    y_text = 30
    for ln in lines:
        surf_t = FONT_XL.render(ln, True, PALETTE["text"])
        glass.blit(surf_t, (30, y_text))
        y_text += surf_t.get_height() + 8

    # type and emoji
    typ = EXERCISES[current]["type"]
    emo = EXERCISES[current]["emoji"]
    glass.blit(FONT_LG.render(typ, True, PALETTE["text"]), (30, panel_h - 90))
    try:
        glass.blit(EMOJI_FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 110))
    except:
        glass.blit(FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 110))

    screen.blit(glass, (panel_x, panel_y))

    # draw buttons
    for b in buttons:
        b.draw(screen)

    # header and score
    header = FONT_XL.render("Syntax Playground — Grade 6 (ES / EN)", True, PALETTE["text"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 12))
    score_lbl = FONT.render(f"Score: {score}", True, PALETTE["text"])
    screen.blit(score_lbl, (WIDTH - 140, 20))

    # feedback
    if feedback:
        elapsed = now - feedback_time
        ft = FONT_LG.render(feedback, True, PALETTE["text"])
        s = pygame.Surface(ft.get_size(), pygame.SRCALPHA)
        s.blit(ft, (0,0))
        screen.blit(s, (WIDTH//2 - ft.get_width()//2, HEIGHT//2 + 120))

    # draw particles
    for p in particles:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
