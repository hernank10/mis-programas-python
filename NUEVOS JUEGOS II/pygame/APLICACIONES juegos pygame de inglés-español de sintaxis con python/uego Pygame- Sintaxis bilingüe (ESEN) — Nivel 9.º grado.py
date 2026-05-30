# syntax_game_grade9.py
# Juego Pygame: Sintaxis bilingüe (ES/EN) — Nivel 9.º grado
# Características: RainbowButton, hover/press, emoticon particles, animated gradients,
# glassmorphism panels, transitions, bilingual prompts focused on advanced syntax.
#
# Guardar y ejecutar: python syntax_game_grade9.py
# Requiere pygame: pip install pygame

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# ---------------- Configuración ----------------
WIDTH, HEIGHT = 1280, 720
FPS = 60

# Paleta
PALETTE = {
    "top": (36, 59, 95),
    "bottom": (175, 211, 236),
    "panel_tint": (255, 255, 255, 36),
    "text": (18, 20, 23)
}

# Fuentes
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 26)
    FONT_XL = pygame.font.Font(None, 34)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 24)
    FONT_XL = pygame.font.SysFont("arial", 32)

# Intento de fuente emoji (puede fallar en algunos SO)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# ---------------- Utilidades ----------------
def lerp(a,b,t): return a + (b-a)*t
def rounded_rect(surface, rect, color, radius=14):
    x,y,w,h = rect
    # draw rounded rect via circles+rects
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

# ---------------- RainbowButton (hover + press + animated gradient) ----------------
class RainbowButton:
    def __init__(self, rect, text, emoji="✨", on_click=None, hue_offset=0):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.emoji = emoji
        self.on_click = on_click
        self.hue_offset = hue_offset
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.anim = 0.0
        self.enabled = True

    def update(self, dt):
        self.anim += dt
        target = 1.06 if self.hover else 1.0
        if self.pressed:
            target = 0.92
        self.scale += (target - self.scale) * min(1, dt*8)

    def draw(self, surf):
        # animated gradient between two computed colors
        t = (math.sin(self.anim*2.0 + self.hue_offset) + 1)/2
        c1 = (int(lerp(255, 160, t)), int(lerp(120, 210, t)), int(lerp(140, 255, t)))
        c2 = (int(lerp(120, 80, t)), int(lerp(200, 240, t)), int(lerp(255, 180, t)))
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        # vertical gradient
        for y in range(h):
            ty = y/(h-1) if h>1 else 0
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,220), (0,y),(w,y))
        # glass highlight
        highlight = pygame.Surface((w, h//2), pygame.SRCALPHA)
        pygame.draw.rect(highlight, (255,255,255,40), highlight.get_rect(), border_radius=10)
        temp.blit(highlight, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale for hover/pulse
        sw = int(w * self.scale)
        sh = int(h * self.scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        dx = self.rect.x + (w - sw)//2
        dy = self.rect.y + (h - sh)//2
        surf.blit(scaled, (dx, dy))
        # subtle border
        pygame.draw.rect(surf, (255,255,255,80), (dx, dy, sw, sh), 2, border_radius=12)
        # emoji + text
        try:
            e_s = EMOJI_FONT.render(self.emoji, True, (10,10,10))
        except:
            e_s = FONT.render(self.emoji, True, (10,10,10))
        t_s = FONT.render(self.text, True, (10,10,10))
        tx = dx + 12
        ty = dy + (sh - t_s.get_height())//2
        surf.blit(e_s, (tx, ty))
        surf.blit(t_s, (tx + 44, ty))

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

# ---------------- Emoji particle ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji, color=(255,255,255)):
        self.x = x
        self.y = y
        self.vx = random.uniform(-120,120)
        self.vy = random.uniform(-260,-80)
        self.emoji = emoji
        self.life = random.uniform(1.0,2.6)
        self.age = 0.0
        self.spin = random.uniform(-360,360)
        self.angle = random.uniform(0,360)
        self.size = random.randint(22,48)
        self.color = color

    def update(self, dt):
        self.age += dt
        self.vy += 340 * dt  # gravity
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        a = max(0, 1 - self.age / self.life)
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        try:
            text_s = EMOJI_FONT.render(self.emoji, True, self.color)
        except:
            text_s = FONT.render(self.emoji, True, self.color)
        rect = text_s.get_rect(center=(self.size,self.size))
        s.blit(text_s, rect)
        s = pygame.transform.rotozoom(s, self.angle, a*1.0)
        s.set_alpha(int(a*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# ---------------- Exercises (9th grade, bilingual) ----------------
BASE_EXERCISES = [
    {"prompt":"(ES) Voz pasiva avanzada: 'La ciudad construyó el puente en 1990.' → Choose passive:",
     "options":["The bridge was built by the city in 1990.","The bridge built the city in 1990.","The city was built the bridge in 1990."],
     "answer":0, "type":"Passive / Voz pasiva", "emoji":"🏗️"},
    {"prompt":"(ES) Reported speech con cambio de tiempo: She said: \"I have finished.\" → Choose:",
     "options":["She said she had finished.","She said she has finished.","She said she will finish."],
     "answer":0, "type":"Reported Speech / Estilo indirecto", "emoji":"🗣️"},
    {"prompt":"(ES) Mixed conditional: Si hubiera estudiado, ahora tendría un mejor trabajo. → Choose English:",
     "options":["If I had studied, I would have a better job now.","If I had studied, I would have had a better job.","If I study, I will have a better job now."],
     "answer":0, "type":"Mixed Conditional", "emoji":"🔁"},
    {"prompt":"(ES) Third conditional (lament): 'Si hubieras venido, lo habrías visto.' → Choose:",
     "options":["If you had come, you would have seen it.","If you had come, you will see it.","If you came, you would see it."],
     "answer":0, "type":"Third Conditional", "emoji":"⏳"},
    {"prompt":"(ES) Inversion for emphasis: 'Nunca había visto algo así.' → Choose inversion:",
     "options":["Never had I seen anything like that.","I had never seen anything like that.","Never I had seen anything like that."],
     "answer":0, "type":"Inversion / Énfasis", "emoji":"✨"},
    {"prompt":"(ES) Cleft sentence to emphasize agent: 'Fue María quien rompió la ventana.' → Choose:",
     "options":["It was Maria who broke the window.","Maria was who broke the window.","It Maria broke the window."],
     "answer":0, "type":"Cleft / Énfasis", "emoji":"🎯"},
    {"prompt":"(ES) Reduced relative clause: 'The book written in 1920 is rare.' → ¿Cuál es la forma completa?",
     "options":["The book that was written in 1920 is rare.","The book which wrote in 1920 is rare.","The book who was written in 1920 is rare."],
     "answer":0, "type":"Reduced Relatives", "emoji":"📚"},
    {"prompt":"(ES) Nominalisation: 'They investigated the problem' → More formal (noun):",
     "options":["An investigation of the problem was conducted.","They conducted an investigate.","The problem investigate was made."],
     "answer":0, "type":"Nominalisation / Registro", "emoji":"📝"},
    {"prompt":"(ES) Subjunctive-like structure (wish): 'Ojalá que gane.' → Choose English:",
     "options":["I hope he wins.","I wish he would win.","I wish he won."],
     "answer":2, "type":"Subjunctive / Wishes", "emoji":"🍀"},
    {"prompt":"(ES) Reported question: 'Where did she go?' → Choose reported question:",
     "options":["He asked where she had gone.","He asked where did she go.","He asked where she has gone."],
     "answer":0, "type":"Reported Questions", "emoji":"❓"},
    {"prompt":"(ES) Modal verb nuance: 'You should have told me' → Meaning?",
     "options":["It was advisable in the past and didn't happen.","It is a requirement now.","It is impossible."],
     "answer":0, "type":"Modals / Matiz", "emoji":"⚖️"},
    {"prompt":"(ES) Punctuation for lists: Choose the correct sentence:",
     "options":["She bought apples, oranges, and bananas.","She bought apples oranges and bananas.","She bought apples; oranges and bananas."],
     "answer":0, "type":"Punctuation / Puntuación", "emoji":"🔤"},
    {"prompt":"(ES) Relative pronoun choice: 'The people ___ we met were friendly.' → Choose:",
     "options":["whom","who","that"], "answer":0, "type":"Relative Pronouns", "emoji":"👥"},
    {"prompt":"(ES) Formal register: choose formal alternative for 'ask about' →",
     "options":["inquire into","ask about","talk about"], "answer":0, "type":"Register / Registro", "emoji":"🎩"},
    {"prompt":"(ES) Contrast connector: 'Although it was late, he continued.' → Choose correct connector:",
     "options":["Although","Because","So"], "answer":0, "type":"Connectors / Conectores", "emoji":"🔗"},
    {"prompt":"(ES) Passive with reporting verbs: 'They reported that the building was damaged.' → Active equivalent:",
     "options":["Reporters said the building had been damaged.","They damaged the building.","The building damaged them."],
     "answer":0, "type":"Reporting / Periodismo", "emoji":"🏛️"},
    {"prompt":"(ES) Parallelism in lists: Choose the correct parallel structure:",
     "options":["She likes reading, writing and to swim.","She likes reading, writing and swimming.","She likes to read, writing and swim."],
     "answer":1, "type":"Parallelism", "emoji":"⚖️"},
    {"prompt":"(ES) Tag question with modal: 'You will join us, ___?' → Choose tag:",
     "options":["won't you","will you","don't you"], "answer":0, "type":"Tag Questions", "emoji":"❗"},
    {"prompt":"(ES) Mixed conditional nuance: 'If I had taken the job, I would be living in Tokyo now.' → Type:",
     "options":["Past result / Present consequence","Past consequence / Past result","Future possibility"], "answer":0, "type":"Mixed Conditional", "emoji":"🔄"},
    {"prompt":"(ES) Ellipsis in conversation: 'Want to come?' → Full form:",
     "options":["Do you want to come?","You want to come?","Want you to come?"], "answer":0, "type":"Ellipsis / Conversación", "emoji":"💬"},
]

# Expand to ~100 by repeating variations (for practice)
EXERCISES = []
while len(EXERCISES) < 100:
    for e in BASE_EXERCISES:
        copy = dict(e)
        EXERCISES.append(copy)
        if len(EXERCISES) >= 100:
            break

random.shuffle(EXERCISES)

# ---------------- Pygame init ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Studio — Grade 9 (ES/EN)")
clock = pygame.time.Clock()

particles = []
score = 0
current = 0
feedback = ""
feedback_time = 0.0

# helper: spawn emoji particles
def spawn_particles(x,y,emoji,count=18):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-30,30), y + random.uniform(-20,20), emoji))

# make option buttons for current exercise
def make_buttons_for(ex):
    btns = []
    base_x = WIDTH//2 + 20
    base_y = 180
    w = 540
    h = 64
    gap = 16
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+gap), w, h)
        btn = RainbowButton(rect, opt, emoji=ex.get("emoji","✨"), on_click=lambda b, idx=i: on_select(idx))
        btns.append(btn)
    return btns

option_buttons = make_buttons_for(EXERCISES[current])

# handle selection
def on_select(idx):
    global score, current, feedback, feedback_time, option_buttons
    ex = EXERCISES[current]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ Correct / ¡Correcto! — {ex['type']} {ex['emoji']}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, ex['emoji'], count=26)
    else:
        correct_text = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrect / ¡Incorrecto! Ans: {correct_text}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, "💥", count=12)
    feedback_time = time.time()
    # schedule next question after delay (use timer event)
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# animated gradient background generator
def draw_background(t):
    surf = pygame.Surface((WIDTH, HEIGHT))
    top = PALETTE["top"]
    bottom = PALETTE["bottom"]
    shift = (math.sin(t*0.14) + 1)/2
    top_mod = (int(lerp(top[0], 60, shift)), int(lerp(top[1], 110, shift)), int(lerp(top[2], 150, shift)))
    bottom_mod = (int(lerp(bottom[0], 200, shift)), int(lerp(bottom[1], 220, shift)), int(lerp(bottom[2], 210, shift)))
    for y in range(HEIGHT):
        ty = y/(HEIGHT-1)
        r = int(lerp(top_mod[0], bottom_mod[0], ty))
        g = int(lerp(top_mod[1], bottom_mod[1], ty))
        b = int(lerp(top_mod[2], bottom_mod[2], ty))
        pygame.draw.line(surf, (r,g,b), (0,y),(WIDTH,y))
    # floating translucent wave shapes
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(6):
        rx = int((math.sin(t*0.25 + i) + 1)/2 * WIDTH) - 450
        ry = int(60 * math.sin(t*0.33 + i))
        pygame.draw.ellipse(overlay, (255,255,255,24), (rx, 80+ry, 900, 320))
    surf.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return surf

# main loop
start_time = time.time()
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    now = time.time()
    t = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # advance question
            current = (current + 1) % len(EXERCISES)
            option_buttons = make_buttons_for(EXERCISES[current])
            feedback = ""
        # forward events to buttons
        for b in option_buttons:
            b.handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            for b in option_buttons:
                b.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in option_buttons:
                b.handle_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            for b in option_buttons:
                b.handle_event(event)

    # update buttons and particles
    for b in option_buttons:
        b.update(dt)
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # render background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # left glass panel for prompt
    panel_w = WIDTH//2 - 80
    panel_h = HEIGHT - 140
    panel_x = 40
    panel_y = 60
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill(PALETTE["panel_tint"])
    rounded_rect(glass, (0,0,panel_w,panel_h), PALETTE["panel_tint"], radius=18)
    pygame.draw.rect(glass, (255,255,255,12), (10,10,panel_w-20, panel_h-20), border_radius=14)

    # prepare prompt (wrap)
    prompt = EXERCISES[current]["prompt"]
    words = prompt.split(" ")
    lines = []
    line = ""
    maxw = panel_w - 80
    for w in words:
        test = (line + " " + w).strip()
        if FONT_XL.size(test)[0] > maxw and line != "":
            lines.append(line)
            line = w
        else:
            line = test
    if line: lines.append(line)
    y_text = 36
    for ln in lines:
        surf_t = FONT_XL.render(ln, True, PALETTE["text"])
        glass.blit(surf_t, (30, y_text))
        y_text += surf_t.get_height() + 8

    # type label & emoji
    typ = EXERCISES[current]["type"]
    emo = EXERCISES[current].get("emoji","✨")
    glass.blit(FONT_LG.render(typ, True, PALETTE["text"]), (30, panel_h-88))
    try:
        glass.blit(EMOJI_FONT.render(emo, True, PALETTE["text"]), (panel_w-80, panel_h-110))
    except:
        glass.blit(FONT.render(emo, True, PALETTE["text"]), (panel_w-80, panel_h-110))

    screen.blit(glass, (panel_x, panel_y))

    # draw option buttons
    for b in option_buttons:
        b.draw(screen)

    # header & score
    header = FONT_XL.render("Syntax Studio — Grade 9 (ES/EN)", True, PALETTE["text"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 12))
    score_lbl = FONT.render(f"Score: {score}", True, PALETTE["text"])
    screen.blit(score_lbl, (WIDTH - 160, 22))

    # feedback text
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
