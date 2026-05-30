# syntax_game_grade10.py
# Juego Pygame: Syntax Studio — Grade 10 (ES/EN)
# - RainbowButton (hover + press + animated gradient)
# - Emoji particles (falling, rotating, fade)
# - Animated gradient backgrounds
# - Glassmorphism panels, smooth transitions
# - Bilingual prompts for advanced syntax topics
#
# Guardar y ejecutar: python syntax_game_grade10.py
# Requiere pygame: pip install pygame

import pygame, random, math, time, sys
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# ---------------- Config ----------------
WIDTH, HEIGHT = 1280, 720
FPS = 60

# Palette
PALETTE = {
    "top": (25, 60, 120),
    "bottom": (200, 230, 245),
    "panel_tint": (255, 255, 255, 34),
    "text": (18, 20, 23)
}

# Fonts
try:
    FONT = pygame.font.Font(None, 20)
    FONT_LG = pygame.font.Font(None, 26)
    FONT_XL = pygame.font.Font(None, 32)
except:
    FONT = pygame.font.SysFont("arial", 18)
    FONT_LG = pygame.font.SysFont("arial", 24)
    FONT_XL = pygame.font.SysFont("arial", 30)

# Emoji font attempt (may show squares on some systems)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# Utilities
def lerp(a,b,t): return a + (b-a)*t

def rounded_rect(surface, rect, color, radius=14):
    x,y,w,h = rect
    # anti-aliased rounded rect (approx)
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
        # animated gradient colors
        t = (math.sin(self.anim*2.0 + self.hue_offset) + 1)/2
        c1 = (int(lerp(255, 160, t)), int(lerp(120, 210, t)), int(lerp(140, 255, t)))
        c2 = (int(lerp(120, 70, t)), int(lerp(200, 240, t)), int(lerp(255, 190, t)))
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        for y in range(h):
            ty = y/(h-1) if h>1 else 0
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,220), (0,y),(w,y))
        # glass highlight
        overlay = pygame.Surface((w, h//2), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (255,255,255,40), overlay.get_rect(), border_radius=10)
        temp.blit(overlay, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        sw = int(w * self.scale)
        sh = int(h * self.scale)
        scaled = pygame.transform.smoothscale(temp, (sw, sh))
        dx = self.rect.x + (w - sw)//2
        dy = self.rect.y + (h - sh)//2
        surf.blit(scaled, (dx, dy))
        # border
        pygame.draw.rect(surf, (255,255,255,80), (dx, dy, sw, sh), 2, border_radius=12)
        # emoji + text
        try:
            emoji_s = EMOJI_FONT.render(self.emoji, True, (20,20,20))
        except:
            emoji_s = FONT.render(self.emoji, True, (20,20,20))
        text_s = FONT.render(self.text, True, (20,20,20))
        tx = dx + 12
        ty = dy + (sh - text_s.get_height())//2
        surf.blit(emoji_s, (tx, ty))
        surf.blit(text_s, (tx + 44, ty))

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
        self.vx = random.uniform(-140,140)
        self.vy = random.uniform(-300,-80)
        self.emoji = emoji
        self.life = random.uniform(1.0,2.8)
        self.age = 0.0
        self.spin = random.uniform(-360,360)
        self.angle = random.uniform(0,360)
        self.size = random.randint(22,52)
        self.color = color

    def update(self, dt):
        self.age += dt
        self.vy += 360 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        try:
            txt = EMOJI_FONT.render(self.emoji, True, self.color)
        except:
            txt = FONT.render(self.emoji, True, self.color)
        rect = txt.get_rect(center=(self.size,self.size))
        s.blit(txt, rect)
        s = pygame.transform.rotozoom(s, self.angle, alpha*1.0)
        s.set_alpha(int(alpha*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# ---------------- Exercises (advanced syntax for Grade 10) ----------------
BASE_EXERCISES = [
    {"prompt":"(ES) Voz pasiva (matiz temporal): 'Se inauguró el museo en 2001.' → Choose correct English passive:",
     "options":["The museum was inaugurated in 2001.","They inaugurated the museum in 2001.","The museum inaugurated in 2001."],
     "answer":0, "type":"Passive Voice / Voz pasiva", "emoji":"🏛️"},
    {"prompt":"(ES) Reported speech (tiempo pasado): 'She said: \"I have seen it.\"' → Choose:",
     "options":["She said she had seen it.","She said she has seen it.","She said she will have seen it."],
     "answer":0, "type":"Reported Speech / Estilo indirecto", "emoji":"🗣️"},
    {"prompt":"(ES) Third conditional: 'Si hubieras estudiado, habrías aprobado.' → Choose:",
     "options":["If you had studied, you would have passed.","If you had studied, you will have passed.","If you studied, you would have passed."],
     "answer":0, "type":"Third Conditional", "emoji":"⏳"},
    {"prompt":"(ES) Mixed conditional (past → present result): 'Si hubiera aceptado el trabajo, ahora viviría en Madrid.' → Choose:",
     "options":["If I had accepted the job, I would be living in Madrid now.","If I accepted the job, I would be living in Madrid now.","If I accept the job, I would be living in Madrid now."],
     "answer":0, "type":"Mixed Conditional", "emoji":"🔁"},
    {"prompt":"(ES) Nominalisation (formal writing): 'They investigated' → More formal noun form:",
     "options":["An investigation was conducted.","They conducted an investigation.","The investigating was conduct."],
     "answer":0, "type":"Nominalisation / Registro", "emoji":"📝"},
    {"prompt":"(ES) Cleft sentence for emphasis: 'Fue Juan quien ganó la carrera.' → Choose:",
     "options":["It was Juan who won the race.","Juan was who won the race.","It Juan who won the race."],
     "answer":0, "type":"Cleft / Énfasis", "emoji":"🎯"},
    {"prompt":"(ES) Inversion after negative adverbial: 'Nunca había visto...' → Choose inversion:",
     "options":["Never had I seen such a thing.","I had never seen such a thing.","Never I had seen such a thing."],
     "answer":0, "type":"Inversion / Énfasis", "emoji":"✨"},
    {"prompt":"(ES) Reduced relative clause: 'The students selected for the team are ready.' → Full form is:",
     "options":["The students who were selected for the team are ready.","The students that selected for the team are ready.","The students selected are ready."],
     "answer":0, "type":"Reduced Relatives", "emoji":"👥"},
    {"prompt":"(ES) Subjunctive-like expression (wish): 'Ojalá fuera verano.' → Choose English:",
     "options":["I wish it were summer.","I wish it was summer.","I hope it will be summer."],
     "answer":0, "type":"Subjunctive / Wishes", "emoji":"☀️"},
    {"prompt":"(ES) Modal perfect for criticism: 'You should have told me.' → Meaning:",
     "options":["It was better to tell in the past (criticizing).","It is necessary now.","It was impossible."],
     "answer":0, "type":"Modals / Matiz", "emoji":"⚖️"},
    {"prompt":"(ES) Relative clause choice: 'The book ___ I recommended was a bestseller.' → Choose:",
     "options":["that","which","who"], "answer":0, "type":"Relative Pronouns", "emoji":"📖"},
    {"prompt":"(ES) Reported question: '¿Dónde está la estación?' → Choose reported question:",
     "options":["He asked where the station was.","He asked where is the station.","He asked where was the station."],
     "answer":0, "type":"Reported Questions", "emoji":"❓"},
    {"prompt":"(ES) Parallelism in writing: choose the grammatically parallel option:",
     "options":["She likes to swim, running and biking.","She likes swimming, running, and biking.","She likes to swim, running, and bike."],
     "answer":1, "type":"Parallelism", "emoji":"⚖️"},
    {"prompt":"(ES) Punctuation: choose the correct sentence with commas:",
     "options":["Before we leave, check the doors, and lock up.","Before we leave check the doors and lock up.","Before, we leave check the doors and lock up."],
     "answer":0, "type":"Punctuation / Puntuación", "emoji":","},
    {"prompt":"(ES) Cohesion / Linking: choose the best connector to show consequence:",
     "options":["Therefore","Although","Despite"], "answer":0, "type":"Cohesion / Cohesión", "emoji":"➡️"},
    {"prompt":"(ES) Formal vs informal: choose the formal register alternative for 'get information':",
     "options":["obtain information","get info","find out"], "answer":0, "type":"Register / Registro", "emoji":"🎩"},
    {"prompt":"(ES) Ellipsis in informal speech: 'Want to come?' → Full form:",
     "options":["Do you want to come?","You want to come?","Want you to come?"], "answer":0, "type":"Ellipsis / Conversación", "emoji":"💬"},
    {"prompt":"(ES) Tag question with 'should': 'We should leave now, ___?' → Choose:",
     "options":["shouldn't we","should we","don't we"], "answer":0, "type":"Tag Questions", "emoji":"❗"},
    {"prompt":"(ES) Nominalisation for academic writing: 'They discussed the issue' → noun form:",
     "options":["A discussion of the issue took place.","They had a discuss about the issue.","The issue was discussing."], "answer":0, "type":"Academic Style", "emoji":"🏫"},
    {"prompt":"(ES) Passive causative: 'Se reparó la máquina.' → Choose English:",
     "options":["They had the machine repaired.","The machine repaired itself.","The machine was repairing."], "answer":0, "type":"Causative / Voz causativa", "emoji":"🔧"},
]

# Expand to ~100 by replicating with slight variations (for practice)
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
pygame.display.set_caption("Syntax Studio — Grade 10 (ES/EN)")
clock = pygame.time.Clock()

particles = []
score = 0
current = 0
feedback = ""
feedback_time = 0.0

# Helpers
def spawn_particles(x,y,emoji,count=20):
    for _ in range(count):
        particles.append(EmojiParticle(x + random.uniform(-30,30), y + random.uniform(-20,20), emoji))

def make_option_buttons(ex):
    btns = []
    base_x = WIDTH//2 + 30
    base_y = 180
    w = 520
    h = 64
    gap = 18
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+gap), w, h)
        btn = RainbowButton(rect, opt, emoji=ex.get("emoji","✨"), on_click=lambda b, idx=i: on_select(idx))
        btns.append(btn)
    return btns

option_buttons = make_option_buttons(EXERCISES[current])

# Selection handler
def on_select(idx):
    global score, current, feedback, feedback_time, option_buttons
    ex = EXERCISES[current]
    if idx == ex["answer"]:
        score += 1
        feedback = f"✔ Correct / ¡Correcto! — {ex['type']} {ex.get('emoji','✨')}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, ex.get('emoji','✨'), count=26)
    else:
        correct_text = ex["options"][ex["answer"]]
        feedback = f"✖ Incorrect / ¡Incorrecto! Ans: {correct_text}"
        spawn_particles(WIDTH//2, HEIGHT//2 - 40, "💥", count=12)
    feedback_time = time.time()
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# Animated gradient background
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
    # subtle floating shapes overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(6):
        rx = int((math.sin(t*0.25 + i) + 1)/2 * WIDTH) - 450
        ry = int(60 * math.sin(t*0.33 + i))
        pygame.draw.ellipse(overlay, (255,255,255,22), (rx, 80+ry, 900, 320))
    surf.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return surf

# Main loop
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
            current = (current + 1) % len(EXERCISES)
            option_buttons = make_option_buttons(EXERCISES[current])
            feedback = ""
        # send events to buttons
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

    # update
    for b in option_buttons:
        b.update(dt)
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # draw background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # left glass panel
    panel_w = WIDTH//2 - 80
    panel_h = HEIGHT - 140
    panel_x = 40
    panel_y = 60
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    glass.fill(PALETTE["panel_tint"])
    rounded_rect(glass, (0,0,panel_w,panel_h), PALETTE["panel_tint"], radius=18)
    pygame.draw.rect(glass, (255,255,255,12), (10,10,panel_w-20, panel_h-20), border_radius=14)

    # render prompt (wrap)
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
    typ = EXERCISES[current].get("type","")
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
    header = FONT_XL.render("Syntax Studio — Grade 10 (ES/EN)", True, PALETTE["text"])
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 12))
    score_lbl = FONT.render(f"Score: {score}", True, PALETTE["text"])
    screen.blit(score_lbl, (WIDTH - 160, 22))

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
