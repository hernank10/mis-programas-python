# syntax_game_grade12.py
# Juego Pygame: Syntax Studio — Grade 12 / Pre-university
# - RainbowButton: hover + press + animated gradient
# - Emoji particles: falling/rotating/fading
# - Animated gradient backgrounds + subtle motion
# - Glassmorphism panels for prompts
# - Bilingual prompts (ES/EN) for advanced syntax, style and academic writing
# - Replicates exercises to ~100 for extended practice
#
# Ejecutar: python syntax_game_grade12.py
# Requiere pygame: pip install pygame

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# ---------------- Configuración ----------------
WIDTH, HEIGHT = 1280, 760
FPS = 60

# Paleta (vibrante + profesional)
PALETTE = {
    "top": (22, 50, 93),
    "mid": (86, 148, 199),
    "bottom": (234, 240, 248),
    "panel_tint": (255, 255, 255, 36),
    "text": (18, 20, 24)
}

# Fuentes
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 26)
    FONT_XL = pygame.font.Font(None, 32)
    FONT_XXL = pygame.font.Font(None, 44)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 24)
    FONT_XL = pygame.font.SysFont("arial", 30)
    FONT_XXL = pygame.font.SysFont("arial", 40)

# Intento de fuente emoji (puede no mostrar color en algunos SO)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# Utilidad: linear interpolation
def lerp(a,b,t): return a + (b-a)*t

# rounded rect drawing helper (antialiased-ish)
def rounded_rect(surface, rect, color, radius=14):
    x,y,w,h = rect
    # corners
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
    def __init__(self, rect, text, emoji="✨", on_click=None, hue_offset=0):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.emoji = emoji
        self.on_click = on_click
        self.hue = hue_offset
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.anim = 0.0
        self.enabled = True

    def update(self, dt):
        self.anim += dt
        # hover scaling; pressed shrinks
        target = 1.06 if self.hover else 1.0
        if self.pressed: target = 0.92
        self.scale += (target - self.scale) * min(1, dt*8)

    def draw(self, surf):
        # animated gradient background for button
        t = (math.sin(self.anim*2.0 + self.hue) + 1) / 2
        c1 = (int(lerp(255,120,t)), int(lerp(180,220,t)), int(lerp(120,255,t)))
        c2 = (int(lerp(120,60,t)), int(lerp(200,240,t)), int(lerp(255,180,t)))
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        for y in range(h):
            ty = y / max(1,h-1)
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,230), (0,y), (w,y))
        # glass highlight
        overlay = pygame.Surface((w, h//2), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (255,255,255,40), overlay.get_rect(), border_radius=10)
        temp.blit(overlay, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale and blit
        sw = int(w * self.scale)
        sh = int(h * self.scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        dx = self.rect.x + (w - sw)//2
        dy = self.rect.y + (h - sh)//2
        surf.blit(scaled, (dx, dy))
        # border
        pygame.draw.rect(surf, (255,255,255,80), (dx,dy,sw,sh), 2, border_radius=12)
        # emoji and text
        try:
            e_s = EMOJI_FONT.render(self.emoji, True, (16,16,16))
        except:
            e_s = FONT.render(self.emoji, True, (16,16,16))
        t_s = FONT.render(self.text, True, (16,16,16))
        surf.blit(e_s, (dx + 12, dy + (sh - e_s.get_height())//2))
        surf.blit(t_s, (dx + 56, dy + (sh - t_s.get_height())//2))

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

# ---------------- Emoji Particle ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji, color=(255,255,255)):
        self.x = x
        self.y = y
        self.emoji = emoji
        self.vx = random.uniform(-140,140)
        self.vy = random.uniform(-320,-100)
        self.life = random.uniform(1.0,2.8)
        self.age = 0.0
        self.spin = random.uniform(-360,360)
        self.angle = random.uniform(0,360)
        self.size = random.randint(22,52)
        self.color = color

    def update(self, dt):
        self.age += dt
        self.vy += 380 * dt  # gravity
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        try:
            text_s = EMOJI_FONT.render(self.emoji, True, self.color)
        except:
            text_s = FONT.render(self.emoji, True, self.color)
        rect = text_s.get_rect(center=(self.size,self.size))
        s.blit(text_s, rect)
        s = pygame.transform.rotozoom(s, self.angle, alpha*1.0)
        s.set_alpha(int(alpha*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# ---------------- Banco de ejercicios (avanzado, ES/EN) ----------------
BASE_EXERCISES = [
    {"prompt":"(ES) Voz pasiva en contexto académico: 'Los investigadores publicaron los resultados.' → Traduce a voz pasiva:",
     "options":["The results were published by the researchers.","The researchers were published the results.","The results published by the researchers."],
     "answer":0, "type":"Passive Voice / Voz pasiva", "emoji":"🔬"},
    {"prompt":"(ES) Reported speech con cambio de tiempo: She said: \"I will finish it tomorrow.\" → Elige:",
     "options":["She said she would finish it the next day.","She said she will finish it the next day.","She said she finishes it tomorrow."],
     "answer":0, "type":"Reported Speech", "emoji":"🗣️"},
    {"prompt":"(ES) Third conditional: 'Si hubieras tomado el tren, habrías llegado a tiempo.' → Choose:",
     "options":["If you had taken the train, you would have arrived on time.","If you took the train, you would have arrived on time.","If you had taken the train, you would arrive on time."],
     "answer":0, "type":"Third Conditional", "emoji":"⏳"},
    {"prompt":"(ES) Mixed conditional: 'Si hubiera aceptado, ahora estaría viviendo en Londres.' → Choose:",
     "options":["If I had accepted it, I would be living in London now.","If I accepted it, I would be living in London now.","If I accept it, I would live in London."],
     "answer":0, "type":"Mixed Conditional", "emoji":"🔁"},
    {"prompt":"(ES) Nominalisation para ensayo académico: 'They investigated the causes' → Reescribe formalmente:",
     "options":["An investigation into the causes was conducted.","They conducted an investigate of the causes.","The causes were investigating."],
     "answer":0, "type":"Nominalisation / Academic", "emoji":"📝"},
    {"prompt":"(ES) Cleft sentence (énfasis): 'Fue el profesor quien explicó el teorema.' → Traduce:",
     "options":["It was the teacher who explained the theorem.","The teacher was who explained the theorem.","It teacher explained the theorem."],
     "answer":0, "type":"Cleft / Énfasis", "emoji":"🎯"},
    {"prompt":"(ES) Inversion for emphasis: 'Rara vez habíamos visto tal evidencia.' → Elige inversión:",
     "options":["Rarely had we seen such evidence.","We had rarely seen such evidence.","Rarely we had seen such evidence."],
     "answer":0, "type":"Inversion / Emphasis", "emoji":"✨"},
    {"prompt":"(ES) Nominal relative reduction: 'Los estudiantes seleccionados para la beca...' → Full form:",
     "options":["The students who were selected for the scholarship...","The students selected for the scholarship...","The students that selected for the scholarship..."],
     "answer":0, "type":"Reduced Relatives", "emoji":"🎓"},
    {"prompt":"(ES) Subjunctive-like expression: 'Ojalá que hubieras venido.' → Choose best English:",
     "options":["I wish you had come.","I hope you had come.","I wish you would come."],
     "answer":0, "type":"Wishes / Subjunctive", "emoji":"🍀"},
    {"prompt":"(ES) Modal perfect nuance: 'You should have argued differently.' → Significado:",
     "options":["It would have been better to argue differently (criticism).","It's optional now.","It's impossible."],
     "answer":0, "type":"Modals / Nuance", "emoji":"⚖️"},
    {"prompt":"(ES) Relative pronoun accuracy: 'The committee, ____ met last week, decided...' → Choose:",
     "options":["which","that","who"], "answer":0, "type":"Relative Pronouns", "emoji":"👥"},
    {"prompt":"(ES) Reported question (tense & word order): 'Where have they gone?' → Choose:",
     "options":["He asked where they had gone.","He asked: Where have they gone?","He asked where have they gone."],
     "answer":0, "type":"Reported Questions", "emoji":"❓"},
    {"prompt":"(ES) Parallelism in complex lists: which is correct?",
     "options":["She values honesty, working hard, and to be creative.","She values honesty, working hard, and creativity.","She values honesty, to work hard, and creativity."],
     "answer":1, "type":"Parallelism", "emoji":"⚖️"},
    {"prompt":"(ES) Cohesive device: pick a connector that signals concession:",
     "options":["Although","Therefore","Because"], "answer":0, "type":"Cohesion / Connectors", "emoji":"🔗"},
    {"prompt":"(ES) Passive causative: 'Hicimos reparar el equipo.' → Choose English:",
     "options":["We had the equipment repaired.","The equipment repaired us.","We repaired the equipment."],
     "answer":0, "type":"Causative", "emoji":"🔧"},
    {"prompt":"(ES) Ellipsis and register: 'Going to the lecture?' → Full form (formal):",
     "options":["Are you going to the lecture?","You going to the lecture?","Shall go to the lecture?"], "answer":0, "type":"Ellipsis / Register", "emoji":"🎓"},
    {"prompt":"(ES) Appositive phrase: Which sentence uses apposition correctly?",
     "options":["My friend, a talented musician, won the prize.","My friend a talented musician won the prize.","My friend, who a talented musician won the prize."],
     "answer":0, "type":"Apposition", "emoji":"🎼"},
    {"prompt":"(ES) Academic linking: choose best transition to show cause-effect:",
     "options":["Therefore","Meanwhile","However"], "answer":0, "type":"Academic Linking", "emoji":"➡️"},
    {"prompt":"(ES) Punctuation: correctly punctuate complex sentence with subordinate clause:",
     "options":["Although it rained, the match continued.","Although, it rained the match continued.","Although it rained the match continued."],
     "answer":0, "type":"Punctuation", "emoji":","},
]

# Replicar hasta ~100 ejercicios (variaciones simples)
EXERCISES = []
while len(EXERCISES) < 100:
    for e in BASE_EXERCISES:
        EXERCISES.append(dict(e))  # shallow copy
        if len(EXERCISES) >= 100:
            break
random.shuffle(EXERCISES)

# ---------------- Inicialización Pygame ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Syntax Studio — Grade 12 (ES/EN)")
clock = pygame.time.Clock()

particles = []
score = 0
current_idx = 0
feedback = ""
feedback_time = 0.0

# Crear botones de opciones para ejercicio actual
def make_option_buttons(ex):
    btns = []
    base_x = WIDTH//2 + 20
    base_y = 200
    w = 540
    h = 68
    gap = 16
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+gap), w, h)
        emoji = ex.get("emoji", "✨")
        btn = RainbowButton(rect, opt, emoji=emoji, on_click=lambda b, idx=i: on_select(idx), hue_offset=i*0.7)
        btns.append(btn)
    return btns

option_buttons = make_option_buttons(EXERCISES[current_idx])

# Partículas helper
def spawn_particles_at(x,y,emoji,count=20):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-30,30), y + random.uniform(-20,20), emoji))

# Respuesta seleccionada
def on_select(idx):
    global score, current_idx, feedback, feedback_time, option_buttons
    ex = EXERCISES[current_idx]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ Correct / ¡Correcto! — {ex['type']} {ex.get('emoji','✨')}"
        spawn_particles_at(WIDTH//2, HEIGHT//2 - 40, ex.get('emoji','✨'), count=26)
    else:
        corr = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrect / ¡Incorrecto! Respuesta: {corr}"
        spawn_particles_at(WIDTH//2, HEIGHT//2 - 40, "💥", count=12)
    feedback_time = time.time()
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# Fondo con gradiente animado y overlay
def draw_background(t):
    surf = pygame.Surface((WIDTH, HEIGHT))
    top = PALETTE["top"]
    mid = PALETTE["mid"]
    bottom = PALETTE["bottom"]
    shift = (math.sin(t*0.12) + 1)/2
    top_mod = (int(lerp(top[0], mid[0], shift)), int(lerp(top[1], mid[1], shift)), int(lerp(top[2], mid[2], shift)))
    bottom_mod = (int(lerp(bottom[0], mid[0], shift)), int(lerp(bottom[1], mid[1], shift)), int(lerp(bottom[2], mid[2], shift)))
    for y in range(HEIGHT):
        ty = y/(HEIGHT-1)
        r = int(lerp(top_mod[0], bottom_mod[0], ty))
        g = int(lerp(top_mod[1], bottom_mod[1], ty))
        b = int(lerp(top_mod[2], bottom_mod[2], ty))
        pygame.draw.line(surf, (r,g,b), (0,y),(WIDTH,y))
    # overlay soft shapes moving
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(5):
        rx = int((math.sin(t*0.2 + i) + 1)/2 * WIDTH) - 400
        ry = int(60 * math.sin(t*0.33 + i))
        pygame.draw.ellipse(overlay, (255,255,255,22), (rx, 80+ry, 900, 320))
    surf.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return surf

# ---------------- Bucle principal ----------------
start_time = time.time()
running = True

while running:
    dt = clock.tick(FPS)/1000.0
    now = time.time()
    t = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT+1:
            # siguiente pregunta
            current_idx = (current_idx + 1) % len(EXERCISES)
            option_buttons = make_option_buttons(EXERCISES[current_idx])
            feedback = ""
        # forwarding events to buttons
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
    panel_h = HEIGHT - 160
    panel_x = 40
    panel_y = 80
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill(PALETTE["panel_tint"])
    rounded_rect(glass, (0,0,panel_w,panel_h), PALETTE["panel_tint"], radius=20)
    pygame.draw.rect(glass, (255,255,255,12), (12,12,panel_w-24, panel_h-24), border_radius=16)

    # prompt wrapping
    prompt = EXERCISES[current_idx]["prompt"]
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
    typ = EXERCISES[current_idx].get("type","")
    emo = EXERCISES[current_idx].get("emoji","✨")
    glass.blit(FONT_LG.render(typ, True, PALETTE["text"]), (30, panel_h - 88))
    try:
        glass.blit(EMOJI_FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 112))
    except:
        glass.blit(FONT.render(emo, True, PALETTE["text"]), (panel_w - 90, panel_h - 112))

    screen.blit(glass, (panel_x, panel_y))

    # draw buttons
    for b in option_buttons:
        b.draw(screen)

    # header & score
    header = FONT_XXL.render("Syntax Studio — Grade 12 (Pre-University) (ES/EN)", True, PALETTE["text"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 18))
    score_lbl = FONT.render(f"Score: {score}", True, PALETTE["text"])
    screen.blit(score_lbl, (WIDTH - 160, 28))

    # feedback (fades)
    if feedback:
        elapsed = now - feedback_time
        alpha = max(0, 1 - elapsed*1.4)
        ft = FONT_LG.render(feedback, True, PALETTE["text"])
        s = pygame.Surface(ft.get_size(), pygame.SRCALPHA)
        s.blit(ft, (0,0))
        s.set_alpha(int(alpha*255))
        screen.blit(s, (WIDTH//2 - ft.get_width()//2, HEIGHT//2 + 140))

    # draw particles
    for p in particles:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
