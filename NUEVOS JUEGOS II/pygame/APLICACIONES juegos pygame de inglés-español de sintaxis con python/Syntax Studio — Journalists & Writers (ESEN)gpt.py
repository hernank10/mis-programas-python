# syntax_game_journalism_lit.py
#
# Juego educativo Pygame: Sintaxis para periodistas digitales y escritores de literatura (bilingüe)
# Características:
# - RainbowButton con hover y pulsación
# - Emoticones integrados y partículas-emoticon
# - Fondos animados con gradiente
# - Glassmorphism panel para preguntas
# - Opciones múltiples, feedback visual y sonido opcional (sin archivos externos)
#
# Nota: la visualización de emojis depende de la fuente del sistema. Si ves cuadrados, instala una fuente con emojis.
# ================================================================================

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()
# ---------------- Config ----------------
WIDTH, HEIGHT = 1200, 720
FPS = 60

# Colores (0-255)
def rgba(r,g,b,a=255): return (r,g,b,a)
PALETTE = {
    "bg_top": (30, 58, 92),
    "bg_bottom": (150, 199, 230),
    "panel_tint": (255,255,255,40),
    "text_dark": (24, 30, 36),
    "accent": (255, 110, 96),
    "accent2": (123, 201, 111)
}

# Fuentes (usar None para fuente por defecto)
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 28)
    FONT_XL = pygame.font.Font(None, 36)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 26)
    FONT_XL = pygame.font.SysFont("arial", 34)

# Intento de fuente emoji (puede que no muestre color)
try:
    EMOJI_FONT = pygame.font.Font(None, 34)
except:
    EMOJI_FONT = FONT

# Easing / util
def lerp(a,b,t): return a + (b-a)*t
def rounded_rect(surface, rect, color, radius=12):
    x,y,w,h = rect
    # anti-aliased rounded rect
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
    def __init__(self, rect, text, emoji="✍️", on_click=None, hue_base=0):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.emoji = emoji
        self.on_click = on_click
        self.hue_base = hue_base
        self.hover = False
        self.pressed = False
        self.anim_scale = 1.0
        self.anim = 0.0
        self.enabled = True

    def update(self, dt):
        # animate hue/time
        self.anim += dt
        target_scale = 1.08 if self.hover else 1.0
        if self.pressed:
            target_scale = 0.94
        # smooth scale
        self.anim_scale += (target_scale - self.anim_scale) * min(1, dt * 8)

    def draw(self, surf):
        # color cycle for vibrant look
        t = (math.sin(self.anim*2.0 + self.hue_base) + 1) / 2
        c1 = (int(lerp(255, 120, t)), int(lerp(90, 200, t)), int(lerp(140, 255, t)))
        c2 = (int(lerp(120, 60, t)), int(lerp(200, 230, t)), int(lerp(255, 190, t)))
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
        pygame.draw.rect(overlay, (255,255,255,40), overlay.get_rect(), border_radius=10)
        temp.blit(overlay, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale
        sw = int(w * self.anim_scale)
        sh = int(h * self.anim_scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        draw_x = self.rect.x + (w - sw)//2
        draw_y = self.rect.y + (h - sh)//2
        surf.blit(scaled, (draw_x, draw_y))
        # border
        pygame.draw.rect(surf, (255,255,255,80), (draw_x,draw_y,sw,sh), 2, border_radius=12)
        # draw emoji + text
        try:
            emoji_surf = EMOJI_FONT.render(self.emoji, True, (10,10,10))
        except:
            emoji_surf = FONT.render(self.emoji, True, (10,10,10))
        text_surf = FONT.render(self.text, True, (10,10,10))
        tx = draw_x + 14
        ty = draw_y + (sh - text_surf.get_height())//2
        surf.blit(emoji_surf, (tx, ty))
        surf.blit(text_surf, (tx + 42, ty))

    def handle_event(self, event):
        if not self.enabled:
            return
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

# ---------------- Partículas (emojis) ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji, color=(255,255,255)):
        self.x = x
        self.y = y
        self.vx = random.uniform(-90,90)
        self.vy = random.uniform(-250,-80)
        self.emoji = emoji
        self.age = 0.0
        self.life = random.uniform(1.0,2.2)
        self.spin = random.uniform(-360,360)
        self.angle = random.uniform(0,360)
        self.size = random.randint(22,48)
        self.color = color

    def update(self, dt):
        self.age += dt
        self.vy += 300 * dt  # gravity
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

# ---------------- Exercises (journalism & literature syntax) ----------------
# Each item: prompt (ES + hint), options (EN / ES choices), answer index, type, emoji
EXERCISES = [
    # Journalism: active voice preferred for clarity
    {"prompt":"(ES) En periodismo, ¿qué opción es más directa para una noticia? \n'La policía detuvo al sospechoso' -> Choose English:",
     "options":["The police arrested the suspect.","The suspect was arrested by the police.","There was an arrest of the suspect."],
     "answer":0, "type":"Journalism: Active", "emoji":"📰"},
    {"prompt":"(ES) Titular breve: elige la forma más 'headline-style' en inglés:",
     "options":["Mayor Opens New Park","Mayor Opens New Park Today","The Mayor has opened a new park today"],
     "answer":0, "type":"Journalism: Headline", "emoji":"🗞️"},
    # Journalism: inverted order for lead
    {"prompt":"(ES) Para un lead informativo, ¿qué orden es estándar en inglés? \n'Tras el terremoto, autoridades rescataron...':",
     "options":["After the earthquake, authorities rescued...","Authorities rescued... after the earthquake.","Rescued were... after the earthquake."],
     "answer":0, "type":"Journalism: Lead", "emoji":"📢"},
    # Literature: periodic sentence (delayed main clause)
    {"prompt":"(ES) Estilo literario: oraciones periódicas producen tensión. Which reads as periodic style?",
     "options":["After many days of waiting, finally the letter arrived.","Finally the letter arrived after many days of waiting.","The letter arrived, and it had been many days."],
     "answer":0, "type":"Literature: Periodic", "emoji":"✒️"},
    # Literature: anaphora (repetition)
    {"prompt":"(ES) Anáfora (repetición al inicio): choose the example of anaphora in English:",
     "options":["We shall fight on the beaches. We shall fight on the landing grounds.","He walked, then he slept.","They went; they saw; they conquered."],
     "answer":0, "type":"Literature: Anaphora", "emoji":"🔁"},
    # Journalism: concise dateline style, omit 'the'
    {"prompt":"(ES) Estilo conciso: which is concise and journalistic?",
     "options":["President visits city.","The president visits the city.","Today the president did a visit to the city."],
     "answer":0, "type":"Journalism: Concision", "emoji":"✂️"},
    # Literature: metaphor vs literal
    {"prompt":"(ES) ¿Cuál es metáfora literaria (figurative language)?",
     "options":["Her voice was a warm blanket.","She wore a warm blanket.","She was warm."],
     "answer":0, "type":"Literature: Metaphor", "emoji":"🌊"},
    # Journalism: passive allowed for object focus but less direct
    {"prompt":"(ES) When the actor is unknown, reporters sometimes use passive. Which is a passive-news example?",
     "options":["A suspect was arrested last night.","Police arrested a suspect last night.","Last night the police made an arrest."],
     "answer":0, "type":"Journalism: Passive", "emoji":"🔎"},
    # Literature: long vs short sentences (rhythm)
    {"prompt":"(ES) For rhythmic short sentence after a long one, pick the pair that shows contrast:",
     "options":["He ran through the night, past ruined walls and empty fields. He stopped.","He ran through the night. Past ruined walls and empty fields he stopped.","He ran through the night past ruined walls and empty fields enduring."],
     "answer":0, "type":"Literature: Rhythm", "emoji":"🎵"},
    # Journalism: lead with most important info (inverted pyramid)
    {"prompt":"(ES) Inverted pyramid: which lead places the key fact first?",
     "options":["Mayor resigns amid scandal.","Because of scandal, mayor resigns.","Amid scandal, the mayor offers resignation."],
     "answer":0, "type":"Journalism: Inverted pyramid", "emoji":"🏛️"},
]

# Can expand EXERCISES to 50-100 as needed
random.shuffle(EXERCISES)

# ---------------- Init Pygame ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Studio: Journalism & Literature (ES/EN)")
clock = pygame.time.Clock()

# particles list
particles = []

# Buttons for options (made per-question)
option_buttons = []
current_idx = 0
score = 0
feedback = ""
feedback_timer = 0.0

# Helpers
def spawn_emojis(x,y,emoji,count=18):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-30,30), y + random.uniform(-20,20), emoji))

def make_option_buttons(ex):
    btns = []
    base_x = WIDTH//2 + 40
    base_y = 200
    w = 520
    h = 64
    gap = 18
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+gap), w, h)
        btn = RainbowButton(rect, opt, emoji=ex["emoji"], on_click=lambda b, idx=i: on_select(idx))
        btns.append(btn)
    return btns

def on_select(idx):
    global current_idx, score, feedback, feedback_timer, option_buttons
    ex = EXERCISES[current_idx]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ Correcto / Correct! {ex['type']} {ex['emoji']}"
        spawn_emojis(WIDTH//2, HEIGHT//2 - 40, ex['emoji'], count=22)
    else:
        correct_text = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrecto / Incorrect! Ans: {correct_text}"
        spawn_emojis(WIDTH//2, HEIGHT//2 - 40, "💥", count=10)
    feedback_timer = time.time()
    # schedule next question after short delay
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# initialize option buttons for first question
option_buttons = make_option_buttons(EXERCISES[current_idx])

# Background gradient generator
def draw_background(t):
    surf = pygame.Surface((WIDTH, HEIGHT))
    top = PALETTE["bg_top"]
    bottom = PALETTE["bg_bottom"]
    # animate color shift slightly
    shift = (math.sin(t*0.2)+1)/2
    top_mod = (int(lerp(top[0], 40, shift)), int(lerp(top[1], 80, shift)), int(lerp(top[2], 100, shift)))
    bottom_mod = (int(lerp(bottom[0], 120, shift)), int(lerp(bottom[1], 200, shift)), int(lerp(bottom[2], 230, shift)))
    # vertical gradient
    for y in range(HEIGHT):
        ty = y/(HEIGHT-1)
        r = int(lerp(top_mod[0], bottom_mod[0], ty))
        g = int(lerp(top_mod[1], bottom_mod[1], ty))
        b = int(lerp(top_mod[2], bottom_mod[2], ty))
        pygame.draw.line(surf, (r,g,b), (0,y),(WIDTH,y))
    # overlay subtle moving shapes
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(5):
        rx = int((math.sin(t*0.3 + i) + 1)/2 * WIDTH) - 400
        ry = int(50 * math.sin(t*0.4 + i))
        pygame.draw.ellipse(overlay, (255,255,255,30), (rx, 100+ry, 700, 260))
    surf.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return surf

# ---------------- Main loop ----------------
running = True
start_time = time.time()

while running:
    dt = clock.tick(FPS)/1000.0
    now = time.time()
    t = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # advance question
            current_idx = (current_idx + 1) % len(EXERCISES)
            option_buttons = make_option_buttons(EXERCISES[current_idx])
            feedback = ""
        # pass events to buttons
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

    # update buttons
    for b in option_buttons:
        b.update(dt)
    # update particles
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # draw background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # glass panel (left) for prompt
    panel_w = WIDTH//2 - 80
    panel_h = HEIGHT - 140
    panel_x = 40
    panel_y = 60
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill((255,255,255,24))
    rounded_rect(glass, (0,0,panel_w,panel_h), (255,255,255,24), radius=18)
    # inner subtle rectangle
    pygame.draw.rect(glass, (255,255,255,10), (10,10,panel_w-20, panel_h-20), border_radius=14)
    # render prompt text (wrap)
    prompt = EXERCISES[current_idx]["prompt"]
    # wrap into lines
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
    if line:
        lines.append(line)
    y_text = 36
    for ln in lines:
        surf_t = FONT_XL.render(ln, True, PALETTE["text_dark"])
        glass.blit(surf_t, (30, y_text))
        y_text += surf_t.get_height() + 8
    # type label and emoji
    typ = EXERCISES[current_idx]["type"]
    emo = EXERCISES[current_idx]["emoji"]
    glass.blit(FONT_LG.render(typ, True, PALETTE["text_dark"]), (30, panel_h-88))
    try:
        glass.blit(EMOJI_FONT.render(emo, True, (20,20,20)), (panel_w-80, panel_h-110))
    except:
        glass.blit(FONT.render(emo, True, (20,20,20)), (panel_w-80, panel_h-110))

    screen.blit(glass, (panel_x, panel_y))

    # draw option buttons
    for b in option_buttons:
        b.draw(screen)

    # header & score
    header = FONT_XL.render("Syntax Studio — Journalists & Writers (ES/EN)", True, PALETTE["text_dark"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 12))
    score_label = FONT.render(f"Score: {score}", True, PALETTE["text_dark"])
    screen.blit(score_label, (WIDTH - 140, 20))

    # feedback text
    if feedback:
        elapsed = now - feedback_timer
        # render with fade
        ft = FONT_LG.render(feedback, True, PALETTE["text_dark"])
        s = pygame.Surface(ft.get_size(), pygame.SRCALPHA)
        s.blit(ft, (0,0))
        screen.blit(s, (WIDTH//2 - ft.get_width()//2, HEIGHT//2 + 120))

    # draw particles
    for p in particles:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
