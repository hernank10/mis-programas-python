# subordinate_game.py
import pygame, random, math, sys, time
from pygame import gfxdraw

pygame.init()
pygame.font.init()

# -------------------------
# Config
# -------------------------
WIDTH, HEIGHT = 1200, 720
FPS = 60
BG_SPEED = 0.5

# Colores RGBA (0-255)
def rgba(r,g,b,a=255): return (r,g,b,a)

# Paleta vibrante (nature + rainbow accents)
PALETTE = {
    "deep": rgba(12, 37, 24),
    "sand": rgba(246, 236, 218),
    "sky1": rgba(61, 147, 193),
    "sky2": rgba(142, 197, 230),
    "leaf": rgba(34,139,34),
    "sun": rgba(252, 186, 3),
    "glass_tint": rgba(255,255,255,60)
}

# Fuentes
try:
    FONT = pygame.font.Font(None, 26)
    FONT_LG = pygame.font.Font(None, 36)
    FONT_XL = pygame.font.Font(None, 46)
except:
    FONT = pygame.font.SysFont("arial", 20)
    FONT_LG = pygame.font.SysFont("arial", 28)
    FONT_XL = pygame.font.SysFont("arial", 40)

# Intentar fuente emoji (puede fallar según SO)
try:
    EMOJI_FONT = pygame.font.Font(None, 36)
except:
    EMOJI_FONT = FONT

# -------------------------
# Utilities: easing, rounded rect, gradients
# -------------------------
def lerp(a,b,t): return a + (b-a)*t
def ease_out_cubic(t): return 1 - pow(1-t, 3)

def rounded_rect(surface, rect, color, radius=12):
    x,y,w,h = rect
    # filled rounded rectangle using gfxdraw
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

def vertical_gradient(surface, top_color, bottom_color):
    # draw vertical gradient
    height = surface.get_height()
    for y in range(height):
        t = y / max(1, height-1)
        r = int(lerp(top_color[0], bottom_color[0], t))
        g = int(lerp(top_color[1], bottom_color[1], t))
        b = int(lerp(top_color[2], bottom_color[2], t))
        pygame.draw.line(surface, (r,g,b), (0,y), (surface.get_width(), y))

# -------------------------
# RainbowButton: hover/pulse/animated color
# -------------------------
class RainbowButton:
    def __init__(self, rect, text, emoji="🙂", on_click=None, base_hue_offset=0):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.emoji = emoji
        self.on_click = on_click
        self.hover = False
        self.pressed = False
        self.scale = 1.0
        self.anim_t = 0.0
        self.hue_offset = base_hue_offset
        self.enabled = True

    def update(self, dt):
        # animate hue offset slowly
        self.hue_offset += dt*10
        self.anim_t = (self.anim_t + dt) % 1.0
        target_scale = 1.05 if self.hover else 1.0
        if self.pressed:
            target_scale = 0.92
        self.scale += (target_scale - self.scale) * min(1, dt*8)

    def draw(self, surf):
        # color cycle (simple HSV->RGB approximation)
        t = (math.sin(pygame.time.get_ticks()/400.0 + self.hue_offset) + 1)/2
        # choose vibrant gradient between two colors
        c1 = (int(lerp(255, 128, t)), int(lerp(100, 200, t)), int(lerp(100, 255, t)))
        c2 = (int(lerp(100, 50, t)), int(lerp(200, 255, t)), int(lerp(255, 180, t)))
        # draw rounded gradient background by drawing vertical gradient onto temp
        w,h = self.rect.size
        temp = pygame.Surface((w,h), pygame.SRCALPHA)
        for y in range(h):
            ty = y / (h-1)
            rr = int(lerp(c1[0], c2[0], ty))
            gg = int(lerp(c1[1], c2[1], ty))
            bb = int(lerp(c1[2], c2[2], ty))
            pygame.draw.line(temp, (rr,gg,bb,230), (0,y), (w,y))
        # glass highlight
        highlight = pygame.Surface((w,h//2), pygame.SRCALPHA)
        pygame.draw.rect(highlight, (255,255,255,40), highlight.get_rect(), border_radius=10)
        temp.blit(highlight, (0,0), special_flags=pygame.BLEND_PREMULTIPLIED)
        # scale for hover/pulse effect
        scaled = pygame.transform.smoothscale(temp, (int(w*self.scale), int(h*self.scale)))
        draw_x = self.rect.x + (w - scaled.get_width())//2
        draw_y = self.rect.y + (h - scaled.get_height())//2
        surf.blit(scaled, (draw_x, draw_y))
        # border
        pygame.draw.rect(surf, (255,255,255,60), (draw_x, draw_y, scaled.get_width(), scaled.get_height()), 2, border_radius=12)
        # text and emoji centered
        text_surf = FONT.render(self.text, True, (20,20,20))
        emoji_surf = EMOJI_FONT.render(self.emoji, True, (20,20,20))
        tx = draw_x + 20
        ty = draw_y + (scaled.get_height() - text_surf.get_height())//2
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

# -------------------------
# Particle system (emoticon particles)
# -------------------------
class EmojiParticle:
    def __init__(self, x, y, emoji, color=(255,255,255)):
        self.x = x
        self.y = y
        self.vx = random.uniform(-40, 40)
        self.vy = random.uniform(-80, -200)
        self.emoji = emoji
        self.life = random.uniform(1.2, 2.4)
        self.age = 0.0
        self.spin = random.uniform(-180, 180)
        self.angle = random.uniform(0,360)
        self.color = color
        self.size = random.randint(22, 42)

    def update(self, dt):
        self.age += dt
        self.vy += 300 * dt  # gravity
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.spin * dt

    def draw(self, surf):
        alpha = max(0, 1 - self.age / self.life)
        s = pygame.Surface((self.size*2,self.size*2), pygame.SRCALPHA)
        text_s = EMOJI_FONT.render(self.emoji, True, self.color)
        # center
        rect = text_s.get_rect(center=(self.size,self.size))
        s.blit(text_s, rect)
        s = pygame.transform.rotozoom(s, self.angle, alpha*1.0)
        s.set_alpha(int(alpha*255))
        surf.blit(s, (self.x - s.get_width()/2, self.y - s.get_height()/2))

# -------------------------
# Exercises: subordinate clauses (small set, can expand)
# Each item: prompt (spanish or english), options list, answer index, type label, emoji
# -------------------------
EXERCISES = [
    # Cause: because, since, as
    {"prompt":"No vino a la fiesta porque estaba enfermo. / Translate to English:",
     "options":["He didn't come to the party because he was sick.",
                "He didn't come to the party if he was sick.",
                "He didn't come to the party when he was sick."],
     "answer":0, "type":"Causa / Cause", "emoji":"🤒"},
    # Time
    {"prompt":"Llámame cuando llegues. / Translate to English:",
     "options":["Call me when you arrive.","Call me before you arrive.","Call me because you arrive."],
     "answer":0, "type":"Tiempo / Time", "emoji":"⏰"},
    # Condition (1st)
    {"prompt":"Si estudias, aprobarás. / Translate to English:",
     "options":["If you study, you will pass.","If you studied, you will pass.","If you study, you pass."],
     "answer":0, "type":"Condicional / Condition", "emoji":"📘"},
    # Purpose
    {"prompt":"Estudia para que apruebes. / Translate to English:",
     "options":["Study so that you pass.","Study because you pass.","Study when you pass."],
     "answer":0, "type":"Finalidad / Purpose", "emoji":"🎯"},
    # Concession
    {"prompt":"Aunque estaba cansado, siguió trabajando. / Translate to English:",
     "options":["Although he was tired, he kept working.","If he was tired, he kept working.","Because he was tired, he kept working."],
     "answer":0, "type":"Concesiva / Concession", "emoji":"😴"},
    # Conditional (2nd)
    {"prompt":"Si yo fuera rico, viajaría más. / Translate to English:",
     "options":["If I were rich, I would travel more.","If I am rich, I will travel more.","If I was rich, I travel more."],
     "answer":0, "type":"Condicional 2 / 2nd Conditional", "emoji":"💭"},
    # Time - as soon as
    {"prompt":"Tan pronto como termine, te llamo. / Translate to English:",
     "options":["As soon as I finish, I'll call you.","Because I finish, I'll call you.","If I finish, I'll call you."],
     "answer":0, "type":"Tiempo / Time", "emoji":"📞"},
    # Cause - since
    {"prompt":"Ya que no viniste, salimos sin ti. / Translate to English:",
     "options":["Since you didn't come, we left without you.","If you didn't come, we left without you.","When you didn't come, we left without you."],
     "answer":0, "type":"Causa / Cause", "emoji":"🚶‍♂️"},
    # Purpose - in order to
    {"prompt":"Trabaja duro para lograr sus metas. / Translate to English:",
     "options":["He works hard in order to achieve his goals.","He works hard although he achieves his goals.","He works hard when he achieves his goals."],
     "answer":0, "type":"Finalidad / Purpose", "emoji":"🏆"},
    # Conditional (0)
    {"prompt":"Si calientas hielo, se derrite. / Translate to English:",
     "options":["If you heat ice, it melts.","If you heat ice, it would melt.","If you heat ice, it melted."],
     "answer":0, "type":"Condicional 0 / 0 Conditional", "emoji":"❄️"},
]

# Shuffle questions for gameplay
random.shuffle(EXERCISES)

# -------------------------
# Game state
# -------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
particles = []

score = 0
current_idx = 0
last_spawn = 0.0
feedback_text = ""
feedback_time = 0.0

# Buttons for current options (created dynamically)
buttons = []

def spawn_particles_at(x,y, emoji, count=12):
    for _ in range(count):
        p = EmojiParticle(x + random.uniform(-20,20), y + random.uniform(-10,10), emoji)
        particles.append(p)

def make_option_buttons_for_exercise(ex):
    btns = []
    # arrange options vertically on right half
    base_x = WIDTH//2 + 30
    base_y = 200
    w = 520
    h = 64
    spacing = 18
    for i,opt in enumerate(ex["options"]):
        rect = (base_x, base_y + i*(h+spacing), w, h)
        # emoji for option: include type emoji on left
        btn = RainbowButton(rect, opt, emoji=ex["emoji"], on_click=lambda b, idx=i: on_option_selected(idx))
        btns.append(btn)
    return btns

def on_option_selected(idx):
    global current_idx, score, feedback_text, feedback_time, particles
    ex = EXERCISES[current_idx]
    correct = ex["answer"]
    # find the button clicked by matching index
    if idx == correct:
        score += 1
        feedback_text = "✔ Correcto / Correct! " + ex["type"] + " " + ex["emoji"]
        # spawn nice particle explosion
        spawn_particles_at(WIDTH//2, HEIGHT//2 - 40, ex["emoji"], count=24)
    else:
        feedback_text = "✖ Incorrecto / Incorrect! Ans: " + ex["options"][correct]
        # spawn sad particles
        spawn_particles_at(WIDTH//2, HEIGHT//2 - 40, "💥", count=12)
    feedback_time = time.time()
    # next question after short delay
    pygame.time.set_timer(pygame.USEREVENT+1, 900, loops=1)

# Initialize buttons for first exercise
buttons = make_option_buttons_for_exercise(EXERCISES[current_idx])

# -------------------------
# Animated gradient background (two-layer moving)
# -------------------------
bg_surf = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
def draw_background(t):
    # create dynamic vertical gradient shifting with time
    top = PALETTE["sky1"]
    bottom = PALETTE["sky2"]
    # we will blend two gradients using sin offset for motion
    temp = pygame.Surface((WIDTH, HEIGHT))
    # modify colors slightly with time
    shift = (math.sin(t*0.2) + 1)/2
    top_mod = (int(lerp(top[0], PALETTE["leaf"][0], shift)), int(lerp(top[1], PALETTE["leaf"][1], shift)), int(lerp(top[2], PALETTE["leaf"][2], shift)))
    bottom_mod = (int(lerp(bottom[0], PALETTE["sand"][0], shift)), int(lerp(bottom[1], PALETTE["sand"][1], shift)), int(lerp(bottom[2], PALETTE["sand"][2], shift)))
    vertical_gradient(temp, top_mod, bottom_mod)
    # subtle overlay waves (transparent)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(6):
        a = int(20 + 20*math.sin(t*0.5 + i))
        pygame.draw.ellipse(overlay, (255,255,255,a), (-200 + i*220, int(80*math.sin(t*0.3 + i)), 800, 300), 0)
    temp.blit(overlay, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return temp

# -------------------------
# Main loop
# -------------------------
running = True
start_time = time.time()

while running:
    dt = clock.tick(FPS) / 1000.0
    now = time.time()
    t = now - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # timer to advance question
        if event.type == pygame.USEREVENT+1:
            # advance question
            current_idx = (current_idx + 1) % len(EXERCISES)
            buttons = make_option_buttons_for_exercise(EXERCISES[current_idx])
            feedback_text = ""
        # pass events to buttons
        for b in buttons:
            b.handle_event(event)

        if event.type == pygame.MOUSEMOTION:
            for b in buttons:
                b.handle_event(event)  # updates hover
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.handle_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            for b in buttons:
                b.handle_event(event)

    # update buttons
    for i,b in enumerate(buttons):
        b.update(dt)

    # update particles
    for p in particles[:]:
        p.update(dt)
        if p.age >= p.life:
            particles.remove(p)

    # draw background
    bg = draw_background(t)
    screen.blit(bg, (0,0))

    # glass panel (left side) for the prompt
    panel_w = WIDTH//2 - 80
    panel_h = HEIGHT - 140
    panel_x = 40
    panel_y = 60
    glass = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    # glassmorphism: translucent + blur-like highlight
    glass.fill((255,255,255,32))
    rounded_rect(glass, (0,0,panel_w,panel_h), (255,255,255,32), radius=18)
    # inner semi-transparent darker strip
    pygame.draw.rect(glass, (255,255,255,12), (10,10,panel_w-20, panel_h-20), border_radius=14)
    # label text on glass
    prompt_lines = []
    # wrap prompt text
    raw_prompt = EXERCISES[current_idx]["prompt"]
    # simple text wrap
    words = raw_prompt.split(" ")
    line = ""
    for w in words:
        if FONT_XL.size(line + " " + w)[0] > panel_w - 60:
            prompt_lines.append(line)
            line = w
        else:
            if line == "":
                line = w
            else:
                line += " " + w
    if line:
        prompt_lines.append(line)
    # draw into glass
    ytext = 40
    for ln in prompt_lines:
        txt = FONT_XL.render(ln, True, (30,30,30))
        glass.blit(txt, (30, ytext))
        ytext += txt.get_height() + 8

    # draw type label & emoji
    type_label = EXERCISES[current_idx]["type"]
    emoji_label = EXERCISES[current_idx]["emoji"]
    glass.blit(FONT_LG.render(type_label, True, (20,20,20)), (30, panel_h - 90))
    glass.blit(EMOJI_FONT.render(emoji_label, True, (20,20,20)), (panel_w - 80, panel_h - 110))

    screen.blit(glass, (panel_x, panel_y))

    # draw buttons (options)
    for b in buttons:
        b.draw(screen)

    # show score and header
    header = FONT_XL.render("Subordinate Syntax Game (ES/EN)", True, (20,20,20))
    screen.blit(header, (WIDTH//2 - header.get_width()//2, 10))
    score_label = FONT.render(f"Score: {score}", True, (10,10,10))
    screen.blit(score_label, (WIDTH - 140, 20))

    # show feedback (small floating text)
    if feedback_text:
        elapsed = now - feedback_time
        alpha = max(0, 1 - elapsed*1.4)
        ft = FONT_LG.render(feedback_text, True, (10,10,10))
        # fade
        s = pygame.Surface(ft.get_size(), pygame.SRCALPHA)
        s.blit(ft, (0,0))
        s.set_alpha(int(alpha*255))
        screen.blit(s, (WIDTH//2 - ft.get_width()//2, HEIGHT//2 + 120))

    # draw particles
    for p in particles:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
