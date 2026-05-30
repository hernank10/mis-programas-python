# syntax_game_grade7.py
# Juego educativo Pygame: Sintaxis bilingüe (ES/EN) para estudiantes de 7º grado
# - RainbowButton: hover/pulse, animated vibrant colors
# - Emoticons integrated (may require emoji-supporting font)
# - Emoji particle system with rotation & fade
# - Animated gradient backgrounds, glassmorphism panel
# - Bilingual prompts (Spanish instruction + English choices/hints)
# - Content: subordinate clauses more advanced, passive voice, reported speech, modals, conditionals, relative clauses, punctuation
#
# Guardar como syntax_game_grade7.py; ejecutar `python syntax_game_grade7.py`
# Requiere pygame: pip install pygame

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# ---------------- Config ----------------
WIDTH, HEIGHT = 1200, 720
FPS = 60

# Paleta vibrante / natural
PALETTE = {
    "bg_top": (45, 98, 160),    # deep sky tone
    "bg_bottom": (240, 230, 200),# warm sand
    "glass": (255,255,255,40),
    "text": (18,18,20),
    "accent": (255,110,96),
    "accent2": (70,180,140)
}

# Fuentes (None -> default)
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 26)
    FONT_XL = pygame.font.Font(None, 34)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 24)
    FONT_XL = pygame.font.SysFont("arial", 30)

# Intento de fuente emoji (depende del SO)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# Utilidades
def lerp(a,b,t): return a + (b-a)*t
def rounded_rect(surface, rect, color, radius=12):
    x,y,w,h = rect
    # anti-aliased rounded rect + filled
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
        target = 1.07 if self.hover else 1.0
        if self.pressed: target = 0.94
        self.scale += (target - self.scale) * min(1, dt*8)

    def draw(self, surf):
        # animated gradient
        t = (math.sin(self.anim*2.0 + self.hue_offset) + 1)/2
        c1 = (int(lerp(255, 150, t)), int(lerp(120, 200, t)), int(lerp(140, 255, t)))
        c2 = (int(lerp(90, 40, t)), int(lerp(200, 240, t)), int(lerp(255, 190, t)))
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        for y in range(h):
            ty = y / max(1,h-1)
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,230), (0,y),(w,y))
        # glass highlight
        overlay = pygame.Surface((w,h//2), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (255,255,255,40), overlay.get_rect(), border_radius=10)
        temp.blit(overlay, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale and blit
        sw = int(w * self.scale)
        sh = int(h * self.scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        draw_x = self.rect.x + (w - sw)//2
        draw_y = self.rect.y + (h - sh)//2
        surf.blit(scaled, (draw_x, draw_y))
        # border
        pygame.draw.rect(surf, (255,255,255,80), (draw_x,draw_y,sw,sh), 2, border_radius=12)
        # emoji and text
        try:
            emoji_surf = EMOJI_FONT.render(self.emoji, True, (10,10,10))
        except:
            emoji_surf = FONT.render(self.emoji, True, (10,10,10))
        text_surf = FONT.render(self.text, True, (10,10,10))
        tx = draw_x + 12
        ty = draw_y + (sh - text_surf.get_height())//2
        surf.blit(emoji_surf, (tx, ty))
        surf.blit(text_surf, (tx + 44, ty))

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

# ---------------- Emoji Particles ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji, color=(255,255,255)):
        self.x = x
        self.y = y
        self.vx = random.uniform(-100,100)
        self.vy = random.uniform(-240,-80)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(1.0,2.6)
        self.spin = random.uniform(-360,360)
        self.angle = random.uniform(0,360)
        self.size = random.randint(20,46)
        self.color = color

    def update(self, dt):
        self.age += dt
        self.vy += 320 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        s = pygame.Surface((self.size*2,self.size*2), pygame.SRCALPHA)
        try:
            text_s = EMOJI_FONT.render(self.emoji, True, self.color)
        except:
            text_s = FONT.render(self.emoji, True, self.color)
        rect = text_s.get_rect(center=(self.size,self.size))
        s.blit(text_s, rect)
        s = pygame.transform.rotozoom(s, self.angle, alpha*1.0)
        s.set_alpha(int(alpha*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# ---------------- Exercises for Grade 7 (sample base set) ----------------
# Each exercise: prompt (ES instruction + context), options (EN choices), answer index, type label, emoji
BASE_EXERCISES = [
    {"prompt":"(ES) Voz pasiva: 'Los científicos descubrieron una nueva especie.' → Elige la voz pasiva en inglés:",
     "options":["A new species was discovered by scientists.","Scientists were discovered a new species.","A new species discovered scientists."],
     "answer":0, "type":"Passive Voice / Voz pasiva", "emoji":"🔬"},
    {"prompt":"(ES) Reported speech: Él dijo: 'I will come tomorrow.' → ¿Cuál es reported speech?",
     "options":["He said he would come the next day.","He said: he will come tomorrow.","He told: he will come the next day."],
     "answer":0, "type":"Reported Speech / Estilo indirecto", "emoji":"🗣️"},
    {"prompt":"(ES) 1st conditional: 'Si estudias, aprobarás.' → Elige la traducción correcta:",
     "options":["If you study, you will pass.","If you studied, you would pass.","If you study, you pass."],
     "answer":0, "type":"Conditional 1 / Condicional 1", "emoji":"📘"},
    {"prompt":"(ES) 2nd conditional: 'Si yo fuera rico, viajaría.' → ¿Cuál es la forma correcta?",
     "options":["If I were rich, I would travel.","If I am rich, I will travel.","If I was rich, I travel."],
     "answer":0, "type":"Conditional 2 / Condicional 2", "emoji":"💭"},
    {"prompt":"(ES) Relative clause: 'La chica que canta es mi prima.' → Traduce:",
     "options":["The girl who sings is my cousin.","The girl sings is my cousin.","The girl which sings is my cousin."],
     "answer":0, "type":"Relative Clauses / Oraciones de relativo", "emoji":"👧"},
    {"prompt":"(ES) Adverbial clause of time: 'Antes de que llegues, prepararé la cena.' → Choose:",
     "options":["Before you arrive, I will prepare dinner.","I will prepare dinner before you arrived.","Before you will arrive, I prepare dinner."],
     "answer":0, "type":"Time Clauses / Tiempo", "emoji":"⏰"},
    {"prompt":"(ES) Modal verb for obligation: 'Debes hacer la tarea.' → Choose English:",
     "options":["You must do your homework.","You may do your homework.","You might do your homework."],
     "answer":0, "type":"Modals / Modales", "emoji":"📝"},
    {"prompt":"(ES) Punctuation: choose correct placement of comma in complex sentence: 'Cuando llueve nos quedamos en casa.' →",
     "options":["When it rains, we stay at home.","When it rains we stay, at home.","When, it rains we stay at home."],
     "answer":0, "type":"Punctuation / Puntuación", "emoji":", "},
    {"prompt":"(ES) Reduced relative clause: 'El hombre contratado ayer es amable.' → Elige la forma reducida en inglés:",
     "options":["The man hired yesterday is friendly.","The man who was hired yesterday is friendly.","The man that hired yesterday is friendly."],
     "answer":0, "type":"Reduced Clauses / Oraciones reducidas", "emoji":"👔"},
    {"prompt":"(ES) Linking words: choose the correct connector: 'No fui, ___ estaba enfermo.' →",
     "options":["because","but","so"], "answer":0, "type":"Connectors / Conectores", "emoji":"🤒"},
    {"prompt":"(ES) Reported question: '¿Dónde vives?' → Elige estilo indirecto:",
     "options":["He asked where I lived.","He asked where do I live.","He asked: Where do you live?"], "answer":0, "type":"Reported Questions / Preguntas indirectas", "emoji":"❓"},
    {"prompt":"(ES) Passive vs active: Why use passive in news headlines? Choose the best reason:",
     "options":["To focus on the action/result.","To hide the agent always.","Because passive is shorter."], "answer":0, "type":"Style / Estilo periodístico", "emoji":"📰"},
    {"prompt":"(ES) Verb pattern: 'He enjoys ___ soccer.' → choose correct form:",
     "options":["playing","to play","play"], "answer":0, "type":"Gerunds / Verb patterns", "emoji":"⚽"},
    {"prompt":"(ES) Condition type 0 (general truths): 'Si calientas agua, ___.' → choose:",
     "options":["it boils","it will boil","it boiled"], "answer":0, "type":"Conditional 0 / Hechos generales", "emoji":"❄️"},
    {"prompt":"(ES) Relative pronoun choice: 'The book ___ I borrowed was great.' → choose:",
     "options":["that","which","who"], "answer":0, "type":"Relatives / Pronombres relativos", "emoji":"📖"},
    {"prompt":"(ES) Modal for permission: '¿Puedo ir al baño?' → Choose:",
     "options":["May I go to the bathroom?","Must I go to the bathroom?","Should I go to the bathroom?"], "answer":0, "type":"Modals / Permiso", "emoji":"🚻"},
    {"prompt":"(ES) Reported speech tense shift: 'He said: \"I am tired\"' → Choose:",
     "options":["He said he was tired.","He said he is tired.","He said he has been tired."], "answer":0, "type":"Reported Speech / Tense shift", "emoji":"😴"},
    {"prompt":"(ES) Formal vs informal: choose the formal register for 'ask for help' →",
     "options":["request assistance","ask help","get help"], "answer":0, "type":"Register / Registro", "emoji":"🎩"},
    {"prompt":"(ES) Inversion for emphasis: which is inversion? 'Rarely ___ so late.' → choose:",
     "options":["had he arrived","he had arrived","did he arrive"], "answer":0, "type":"Inversion / Énfasis", "emoji":"✨"},
    {"prompt":"(ES) Cleft sentence to emphasize: 'It was the teacher who solved the problem.' → What is purpose?",
     "options":["emphasize agent","make it passive","change tense"], "answer":0, "type":"Cleft / Énfasis", "emoji":"🎯"},
]

# Expand to ~100 by repeating variants (you can replace with unique items)
EXERCISES = []
while len(EXERCISES) < 100:
    for e in BASE_EXERCISES:
        copy = dict(e)
        EXERCISES.append(copy)
        if len(EXERCISES) >= 100: break

random.shuffle(EXERCISES)

# ---------------- Init Pygame ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Studio — Grade 7 (ES/EN)")
clock = pygame.time.Clock()

particles = []
score = 0
current = 0
feedback = ""
feedback_time = 0.0

# Buttons generation per question
def make_option_buttons(ex):
    btns = []
    base_x = WIDTH//2 + 30
    base_y = 180
    w = 540
    h = 64
    spacing = 18
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+spacing), w, h)
        emoji = ex.get("emoji", "🙂")
        btn = RainbowButton(rect, opt, emoji=emoji, on_click=lambda b, idx=i: on_select(idx))
        btns.append(btn)
    return btns

option_buttons = make_option_buttons(EXERCISES[current])

# spawn particles helper
def spawn_particles(x,y,emoji,count=18):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-26,26), y + random.uniform(-12,12), emoji))

# handle selection
def on_select(idx):
    global score, current, feedback, feedback_time, option_buttons
    ex = EXERCISES[current]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ Correcto / Correct! {ex['type']} {ex['emoji']}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, ex['emoji'], count=22)
    else:
        correct_text = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrecto / Incorrect! Answer: {correct_text}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, "💥", count=12)
    feedback_time = time.time()
    # schedule next question
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# background gradient with subtle motion
def draw_background(t):
    surf = pygame.Surface((WIDTH, HEIGHT))
    top = PALETTE["bg_top"]
    bottom = PALETTE["bg_bottom"]
    shift = (math.sin(t*0.18) + 1)/2
    top_mod = (int(lerp(top[0], 50, shift)), int(lerp(top[1], 100, shift)), int(lerp(top[2], 140, shift)))
    bottom_mod = (int(lerp(bottom[0], 180, shift)), int(lerp(bottom[1], 220, shift)), int(lerp(bottom[2], 210, shift)))
    for y in range(HEIGHT):
        ty = y/(HEIGHT-1)
        r = int(lerp(top_mod[0], bottom_mod[0], ty))
        g = int(lerp(top_mod[1], bottom_mod[1], ty))
        b = int(lerp(top_mod[2], bottom_mod[2], ty))
        pygame.draw.line(surf, (r,g,b), (0,y),(WIDTH,y))
    # floating translucent shapes
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(5):
        rx = int((math.sin(t*0.25 + i) + 1)/2 * WIDTH) - 380
        ry = int(40 * math.sin(t*0.3 + i))
        pygame.draw.ellipse(overlay, (255,255,255,26), (rx, 80+ry, 800, 260))
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
            # advance to next question
            current = (current + 1) % len(EXERCISES)
            option_buttons = make_option_buttons(EXERCISES[current])
            feedback = ""
        # deliver events to buttons
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

    # update animations
    for b in option_buttons:
        b.update(dt)
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # draw background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # glass panel left for prompt
    panel_w = WIDTH//2 - 80
    panel_h = HEIGHT - 140
    panel_x = 40
    panel_y = 60
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill(PALETTE["glass"])
    rounded_rect(glass, (0,0,panel_w,panel_h), PALETTE["glass"], radius=18)
    pygame.draw.rect(glass, (255,255,255,12), (10,10,panel_w-20, panel_h-20), border_radius=14)

    # render prompt text with wrapping
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

    # type label and emoji
    typ = EXERCISES[current]["type"]
    emo = EXERCISES[current]["emoji"]
    glass.blit(FONT_LG.render(typ, True, PALETTE["text"]), (30, panel_h - 88))
    try:
        glass.blit(EMOJI_FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 110))
    except:
        glass.blit(FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 110))

    screen.blit(glass, (panel_x, panel_y))

    # draw option buttons
    for b in option_buttons:
        b.draw(screen)

    # header and score
    header = FONT_XL.render("Syntax Studio — Grade 7 (ES/EN)", True, PALETTE["text"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 12))
    score_label = FONT.render(f"Score: {score}", True, PALETTE["text"])
    screen.blit(score_label, (WIDTH - 150, 20))

    # feedback message
    if feedback:
        elapsed = now - feedback_time
        ft = FONT_LG.render(feedback, True, PALETTE["text"])
        s = pygame.Surface(ft.get_size(), pygame.SRCALPHA)
        s.blit(ft, (0,0))
        # fade effect (simple)
        screen.blit(s, (WIDTH//2 - ft.get_width()//2, HEIGHT//2 + 120))

    # draw particles
    for p in particles:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
