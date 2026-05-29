# juego_oraciones_pygame.py
# Juego educativo para aprender oraciones simples y compuestas
# Requiere: pygame
# Run: python juego_oraciones_pygame.py

import pygame
import random
import math
import time
from collections import deque

pygame.init()
pygame.font.init()

# ---------------- CONFIG ----------------
W, H = 1100, 700
FPS = 60
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sintaxis y Oraciones — Juego Educativo 🎓✨")

# Fuentes
F_TITLE = pygame.font.SysFont("Segoe UI", 36, bold=True)
F_BIG = pygame.font.SysFont("Segoe UI", 28)
F_MED = pygame.font.SysFont("Segoe UI", 20)
F_SMALL = pygame.font.SysFont("Segoe UI", 16)

CLOCK = pygame.time.Clock()

# Emoji syntactic map (bilingual hint icons)
SYN_EMOJI = {
    "S": "👤",    # Sujeto / Subject
    "V": "🔤",    # Verbo / Verb
    "O": "🎯",    # Objeto / Object
    "C": "🔗",    # Complemento / Complement
    "SUB": "🔁",  # Subordinada
    "ADV": "⚡",   # Adverbio/Adv
    "DET": "📌",  # Determinante
}

# Colors (RGBA)
def rgba(r, g, b, a=255): return (r, g, b, a)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GLASS = (255, 255, 255, 60)

# ---------------- UTIL: Gradiente animado ----------------
def draw_animated_gradient(surface, t):
    """Dibuja un fondo con gradiente animado en función del tiempo t (segundos)."""
    # colores base que cambian con seno
    r1 = int(90 + 60 * math.sin(t * 0.6))
    g1 = int(130 + 80 * math.sin(t * 0.8 + 1))
    b1 = int(200 + 40 * math.sin(t * 0.5 + 2))
    r2 = int(200 + 30 * math.cos(t * 0.7))
    g2 = int(120 + 50 * math.cos(t * 0.9 + 1))
    b2 = int(160 + 70 * math.cos(t * 0.4 + 2))
    for i in range(H):
        # interpolación vertical
        k = i / H
        r = int(r1 * (1 - k) + r2 * k)
        g = int(g1 * (1 - k) + g2 * k)
        b = int(b1 * (1 - k) + b2 * k)
        pygame.draw.line(surface, (r, g, b), (0, i), (W, i))

# ---------------- UTIL: Glass panel ----------------
def draw_glass_panel(surface, rect, border_radius=12, blur_strength=0):
    """Dibuja un rectángulo translúcido (glassmorphism)."""
    s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    s.fill((255, 255, 255, 32))
    # ligero borde
    pygame.draw.rect(s, (255, 255, 255, 18), (0, 0, rect.width, rect.height), border_radius=border_radius)
    surface.blit(s, (rect.x, rect.y))

# ---------------- RAINBOW BUTTON ----------------
class RainbowButton:
    def __init__(self, rect, text, action=None, icon=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
        self.icon = icon  # emoji string
        self.hovered = False
        self.pulse = 0.0
        self.cooldown = 0.0

    def update(self, dt, mouse_pos, mouse_down):
        self.hovered = self.rect.collidepoint(mouse_pos)
        if self.hovered:
            self.pulse = min(1.2, self.pulse + dt * 4)
        else:
            self.pulse = max(1.0, self.pulse - dt * 3)
        if self.hovered and mouse_down and self.cooldown <= 0:
            if self.action:
                self.action()
            self.cooldown = 0.25
        self.cooldown = max(0.0, self.cooldown - dt)

    def draw(self, surface):
        # efecto rainbow: gradiente horizontal variable
        g = pygame.Surface((self.rect.width, self.rect.height))
        for x in range(self.rect.width):
            t = (x / self.rect.width + time.time() * 0.08) % 1.0
            # hue -> rgb simple (approx)
            r = int(180 + 60 * math.sin(2 * math.pi * t))
            g_ = int(100 + 80 * math.sin(2 * math.pi * (t + 0.33)))
            b = int(200 + 40 * math.sin(2 * math.pi * (t + 0.66)))
            pygame.draw.line(g, (r, g_, b), (x, 0), (x, self.rect.height))
        # rounded border using mask surface
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        s.blit(g, (0, 0))
        # overlay for hover/pulse
        overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        alpha = int(60 * (self.pulse - 1.0))
        overlay.fill((255, 255, 255, alpha))
        s.blit(overlay, (0, 0))
        # border
        pygame.draw.rect(s, (255, 255, 255, 30), s.get_rect(), width=2, border_radius=14)
        surface.blit(s, self.rect.topleft)
        # text + icon
        txt = F_MED.render(self.text, True, BLACK)
        tx = self.rect.x + 20
        ty = self.rect.y + (self.rect.height - txt.get_height()) // 2
        surface.blit(txt, (tx, ty))
        if self.icon:
            ico = F_MED.render(self.icon, True, BLACK)
            surface.blit(ico, (self.rect.right - 40, ty))

# ---------------- PARTICLE SYSTEM (emoticones) ----------------
class EmojiParticle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.vx = random.uniform(-40, 40)
        self.vy = random.uniform(-10, 40)
        self.emoji = emoji
        self.life = random.uniform(1.0, 2.2)
        self.rot = random.uniform(-180, 180)
        self.rotspeed = random.uniform(-120, 120)
        self.size = random.randint(22, 40)
        self.ttl = self.life

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 40 * dt  # gravity
        self.rot += self.rotspeed * dt
        self.ttl -= dt

    def draw(self, surface):
        if self.ttl <= 0: return
        alpha = int(255 * (self.ttl / self.life))
        font = pygame.font.SysFont("Segoe UI Emoji", self.size)
        surf = font.render(self.emoji, True, (255, 255, 255))
        # apply alpha by converting to surface with alpha
        s = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
        s.blit(surf, (0, 0))
        s.set_alpha(alpha)
        # rotate
        s2 = pygame.transform.rotate(s, self.rot)
        surface.blit(s2, (self.x, self.y))

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit(self, x, y, emojis, count=10):
        for _ in range(count):
            e = EmojiParticle(x + random.uniform(-30, 30), y + random.uniform(-10, 10), random.choice(emojis))
            self.particles.append(e)

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        self.particles = [p for p in self.particles if p.ttl > 0 and -200 < p.x < W+200 and p.y < H+200]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)

# ---------------- TEORÍA + EJEMPLOS ----------------
THEORY_PAGES = [
    {
        "title": "Oración Simple",
        "text": [
            "Una oración simple tiene un solo predicado (un verbo principal).",
            "Ejemplo: 'María come manzanas.'",
            "Mapa sintáctico: 👤(Sujeto) 🔤(Verbo) 🎯(Objeto).",
        ]
    },
    {
        "title": "Oración Compuesta Coordinada",
        "text": [
            "Oraciones compuestas por coordinación: dos oraciones independientes unidas.",
            "Ejemplo: 'Salí temprano y llegué a tiempo.'",
            "Conectores: y, pero, o, ni, etc.",
        ]
    },
    {
        "title": "Oración Compuesta Subordinada",
        "text": [
            "Oraciones con cláusulas subordinadas que dependen de otra principal.",
            "Ejemplo: 'Salí porque llovía.'",
            "Mapa: Principal + 🔁(Subordinada).",
        ]
    },
    {
        "title": "Elementos sintácticos (bilingüe)",
        "text": [
            "Sujeto (S) — Subject (👤)",
            "Verbo (V) — Verb (🔤)",
            "Objeto (O) — Object (🎯)",
            "Subordinada — Subordinate clause (🔁)",
            "Complementos — Complement (🔗)",
        ]
    }
]

# ---------------- EJEMPLOS DE ORACIONES (práctica) ----------------
EXAMPLES = [
    # simples
    {"span": "María lee un libro.", "eng": "María reads a book.", "type": "simple"},
    {"span": "Los estudiantes estudian para el examen.", "eng": "The students study for the exam.", "type": "simple"},
    {"span": "El perro corre en el parque.", "eng": "The dog runs in the park.", "type": "simple"},
    {"span": "Ayer llovió mucho.", "eng": "It rained a lot yesterday.", "type": "simple"},
    {"span": "Juan compró pan.", "eng": "Juan bought bread.", "type": "simple"},
    # compuestas coordinadas
    {"span": "Salí temprano y llegué a tiempo.", "eng": "I left early and arrived on time.", "type": "coord."},
    {"span": "Quería ir, pero estaba enfermo.", "eng": "I wanted to go, but I was sick.", "type": "coord."},
    {"span": "Puedes venir o quedarte aquí.", "eng": "You can come or stay here.", "type": "coord."},
    {"span": "Estudia, así que aprobarás.", "eng": "Study, so you will pass.", "type": "coord."},
    {"span": "Ella canta y él toca la guitarra.", "eng": "She sings and he plays the guitar.", "type": "coord."},
    # compuestas subordinadas
    {"span": "Salí porque llovía.", "eng": "I left because it was raining.", "type": "sub."},
    {"span": "Cuando llegues, avísame.", "eng": "When you arrive, let me know.", "type": "sub."},
    {"span": "Si estudias, aprobarás.", "eng": "If you study, you will pass.", "type": "sub."},
    {"span": "Aunque estaba cansado, siguió trabajando.", "eng": "Although he was tired, he continued working.", "type": "sub."},
    {"span": "La casa que compraron es grande.", "eng": "The house that they bought is big.", "type": "sub."},
    # mezcla para variedad (20+ ejercicios)
    {"span": "Pedro abrió la ventana.", "eng": "Pedro opened the window.", "type": "simple"},
    {"span": "El avión llegó y los pasajeros bajaron.", "eng": "The plane arrived and the passengers got off.", "type": "coord."},
    {"span": "No vino porque estaba ocupado.", "eng": "He didn't come because he was busy.", "type": "sub."},
    {"span": "Cerró la puerta y apagó la luz.", "eng": "He closed the door and turned off the light.", "type": "coord."},
    {"span": "Me llamaste cuando saliste.", "eng": "You called me when you left.", "type": "sub."},
    {"span": "Los niños juegan en el patio.", "eng": "The children play in the yard.", "type": "simple"},
    {"span": "La profesora explicó la lección.", "eng": "The teacher explained the lesson.", "type": "simple"},
    {"span": "Llegó tarde, así que perdió la entrada.", "eng": "He arrived late, so he missed the ticket.", "type": "coord."},
    {"span": "Si llueve, cancelaremos el picnic.", "eng": "If it rains, we'll cancel the picnic.", "type": "sub."},
    {"span": "Quiero café, pero no hay leche.", "eng": "I want coffee, but there is no milk.", "type": "coord."},
]

# ---------------- APP STATE / UI ----------------
particle_sys = ParticleSystem()
score = 0
best_score = 0
current_index = 0
used_indices = set()
mode = "menu"  # menu, theory, practice, credits
theory_page = 0
input_active = False
user_text = ""
feedback_msg = ""
feedback_timer = 0.0
fade_alpha = 0
transitioning = False
transition_target = None
transition_start = 0.0

# Buttons
buttons = []

def start_transition(target):
    global transitioning, transition_target, transition_start
    transitioning = True
    transition_target = target
    transition_start = time.time()

# acciones botones
def go_menu(): start_transition("menu")
def go_theory(): start_transition("theory")
def go_practice(): start_transition("practice")
def go_credits(): start_transition("credits")
def quit_game(): pygame.quit(); exit()

# crear botones para menú
def build_menu_buttons():
    btns = []
    btns.append(RainbowButton((60, 200, 380, 64), "📚 Teoría", action=go_theory, icon="📘"))
    btns.append(RainbowButton((60, 280, 380, 64), "📝 Practicar", action=go_practice, icon="🎮"))
    btns.append(RainbowButton((60, 360, 380, 64), "🎯 Quiz libre", action=go_practice, icon="🏆"))
    btns.append(RainbowButton((60, 440, 380, 64), "ℹ️ Créditos", action=go_credits, icon="✨"))
    btns.append(RainbowButton((60, 520, 200, 60), "❌ Salir", action=quit_game, icon="🚪"))
    return btns

menu_buttons = build_menu_buttons()

# práctica: seleccionar nueva pregunta aleatoria
def new_practice_question():
    global current_index, used_indices, user_text, feedback_msg, feedback_timer
    if len(used_indices) >= len(EXAMPLES):
        used_indices = set()
    idx = random.choice([i for i in range(len(EXAMPLES)) if i not in used_indices])
    used_indices.add(idx)
    current_index = idx
    user_text = ""
    feedback_msg = ""
    feedback_timer = 0.0
    # emitir partículas suaves
    particle_sys.emit(W//2, 120, list(SYN_EMOJI.values()), count=6)

# verificar respuesta
def check_answer():
    global feedback_msg, feedback_timer, score, best_score
    correct = EXAMPLES[current_index]['eng'].strip().lower()
    given = user_text.strip().lower()
    # comparación flexible (simple)
    if given == correct:
        score += 1
        best_score = max(best_score, score)
        feedback_msg = "✅ Correcto! " + random.choice(["¡Bien!", "¡Excelente!", "👍"])
        particle_sys.emit(W//2, 180, ["🎉","✨","💡","👍","✅"], count=20)
    else:
        feedback_msg = "❌ Incorrecto. ▶ " + EXAMPLES[current_index]['eng']
        particle_sys.emit(W//2, 180, ["💫","❌","😅"], count=12)
        score = max(0, score - 1)
    feedback_timer = 2.2

# ---------------- UI DRAW ----------------
def draw_menu(dt):
    # título
    title = F_TITLE.render("Sintaxis y Oraciones — Aprende jugando", True, BLACK)
    SCREEN.blit(title, (60, 30))
    subtitle = F_MED.render("Juego interactivo con teoría, práctica y feedback visual", True, BLACK)
    SCREEN.blit(subtitle, (60, 80))
    # panel glass con resumen
    panel = pygame.Rect(480, 150, 560, 440)
    draw_glass_panel(SCREEN, panel)
    # draw some sample text in panel
    txt = [
        "Objetivos:",
        "- Comprender oraciones simples y compuestas",
        "- Identificar sujeto, verbo, objeto y subordinadas",
        "- Practicar traducción ES ↔ EN con feedback inmediato",
    ]
    for i, line in enumerate(txt):
        SCREEN.blit(F_MED.render(line, True, BLACK), (panel.x + 20, panel.y + 20 + i * 30))
    # buttons
    for b in menu_buttons:
        b.draw(SCREEN)

def draw_theory(dt):
    # header
    title = F_TITLE.render("Teoría — Identidad y ejemplos", True, BLACK)
    SCREEN.blit(title, (60, 28))
    # page content panel
    panel = pygame.Rect(60, 90, W - 120, H - 180)
    draw_glass_panel(SCREEN, panel)
    # page
    page = THEORY_PAGES[theory_page]
    SCREEN.blit(F_BIG.render(page['title'], True, BLACK), (panel.x + 20, panel.y + 18))
    for i, p in enumerate(page['text']):
        SCREEN.blit(F_MED.render(p, True, BLACK), (panel.x + 20, panel.y + 70 + i * 28))
    # navigation arrows
    left = RainbowButton((80, H - 70, 140, 48), "⬅ Anterior", action=prev_theory, icon="◀")
    right = RainbowButton((240, H - 70, 140, 48), "Siguiente ➡", action=next_theory, icon="▶")
    menu = RainbowButton((W - 260, H - 70, 180, 48), "⬅ Volver al Menú", action=go_menu, icon="🏠")
    for b in (left, right, menu):
        b.draw(SCREEN)
    # draw small examples panel on right
    ex_panel = pygame.Rect(panel.right - 320, panel.y + 120, 280, 220)
    pygame.draw.rect(SCREEN, (255,255,255,12), ex_panel, border_radius=10)
    SCREEN.blit(F_MED.render("Ejemplos rápidos", True, BLACK), (ex_panel.x + 12, ex_panel.y + 8))
    for i in range(4):
        if i < len(EXAMPLES):
            e = EXAMPLES[(theory_page*4 + i) % len(EXAMPLES)]
            SCREEN.blit(F_SMALL.render("- " + e['span'], True, BLACK), (ex_panel.x + 12, ex_panel.y + 42 + i*40))

def draw_practice(dt):
    global input_active
    title = F_TITLE.render("Práctica — Traduce al inglés", True, BLACK)
    SCREEN.blit(title, (60, 20))
    # score
    score_surf = F_MED.render(f"Puntaje: {score}   Mejor: {best_score}", True, BLACK)
    SCREEN.blit(score_surf, (W - 260, 30))
    # panel for question
    panel = pygame.Rect(60, 90, W - 120, 220)
    draw_glass_panel(SCREEN, panel)
    # show spanish sentence with emoji syntax hints
    ex = EXAMPLES[current_index]
    semap = synthesize_syntax_icons(ex['span'])
    SCREEN.blit(F_BIG.render(ex['span'], True, BLACK), (panel.x + 20, panel.y + 20))
    SCREEN.blit(F_MED.render("Mapa sintáctico: " + semap, True, BLACK), (panel.x + 20, panel.y + 80))
    # input box
    inp_rect = pygame.Rect(panel.x + 20, panel.y + 120, panel.width - 40, 44)
    pygame.draw.rect(SCREEN, (255,255,255,20), inp_rect, border_radius=8)
    pygame.draw.rect(SCREEN, (0,0,0,30), inp_rect, width=1, border_radius=8)
    # user text
    txts = F_MED.render(user_text or "Escribe la traducción en inglés y presiona ENTER...", True, BLACK if user_text else (80,80,80))
    SCREEN.blit(txts, (inp_rect.x + 12, inp_rect.y + 10))
    # buttons
    btn_check = RainbowButton((60, panel.bottom + 24, 160, 56), "✔ Revisar", action=check_answer, icon="✅")
    btn_next = RainbowButton((240, panel.bottom + 24, 160, 56), "🔁 Nueva", action=new_practice_question, icon="🔄")
    btn_menu = RainbowButton((W - 220, panel.bottom + 24, 160, 56), "🏠 Menú", action=go_menu, icon="🏠")
    for b in (btn_check, btn_next, btn_menu):
        b.draw(SCREEN)
    # feedback
    if feedback_msg:
        fb = F_BIG.render(feedback_msg, True, BLACK)
        SCREEN.blit(fb, (60, panel.bottom + 100))

def draw_credits(dt):
    title = F_TITLE.render("Créditos", True, BLACK)
    SCREEN.blit(title, (60, 30))
    panel = pygame.Rect(60, 90, W - 120, H - 180)
    draw_glass_panel(SCREEN, panel)
    lines = [
        "Juego educativo creado con Pygame.",
        "Objetivo: aprender oraciones simples y compuestas.",
        "Características: botones animados, partículas emoji, teoría bilingüe.",
        "",
        "Iconos sintácticos: " + " ".join(f"{v}={k}" for k,v in SYN_EMOJI.items()),
        "",
        "¡Gracias por jugar! 💫",
    ]
    for i, l in enumerate(lines):
        SCREEN.blit(F_MED.render(l, True, BLACK), (panel.x + 20, panel.y + 18 + i * 28))
    back = RainbowButton((W - 220, H - 80, 160, 56), "⬅ Volver", action=go_menu, icon="🏠")
    back.draw(SCREEN)

# ---------------- small helpers ----------------
def synthesize_syntax_icons(spanish_sentence):
    """Versión simple que añade emoticones heurísticos para enseñar sintaxis.
       (Función heurística: detecta palabras funcionales para mostrar iconos)"""
    s = spanish_sentence
    # heuristics: if contains 'porque', 'cuando', 'si', 'aunque', 'que' => subordinada
    icons = []
    low = s.lower()
    if any(k in low for k in ["porque", "cuando", "si ", "aunque", "que "]):
        icons.append(SYN_EMOJI["SUB"])
    # subject heuristic: first word (capitalized proper name) -> S
    icons.append(SYN_EMOJI["S"])
    # verb heuristic: find common verbs forms or space near
    icons.append(SYN_EMOJI["V"])
    # object possibility
    if any(k in low for k in ["un ", "una ", "el ", "la ", "los ", "las ", "mi ", "su "]):
        icons.append(SYN_EMOJI["O"])
    return " ".join(icons)

def prev_theory():
    global theory_page
    theory_page = (theory_page - 1) % len(THEORY_PAGES)

def next_theory():
    global theory_page
    theory_page = (theory_page + 1) % len(THEORY_PAGES)

# ---------------- MAIN LOOP ----------------
def main():
    global mode, user_text, input_active, feedback_timer, fade_alpha, transitioning
    # init first question
    new_practice_question()
    last_time = time.time()
    mouse_down = False

    # main buttons need update per frame
    while True:
        dt = CLOCK.tick(FPS) / 1000.0
        t = time.time()
        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        mouse_clicked = False
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                mouse_clicked = True
            elif e.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            elif e.type == pygame.KEYDOWN:
                if mode == "practice":
                    if e.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif e.key == pygame.K_RETURN:
                        check_answer()
                    elif e.key == pygame.K_ESCAPE:
                        go_menu()
                    else:
                        # get printable
                        if len(e.unicode) > 0:
                            user_text += e.unicode
                else:
                    if e.key == pygame.K_ESCAPE:
                        go_menu()

        # update background & particles
        draw_animated_gradient(SCREEN, t * 0.6)
        particle_sys.update(dt)

        # update UI event handlers (buttons)
        if mode == "menu":
            for b in menu_buttons:
                b.update(dt, mouse_pos, mouse_clicked)
        else:
            # update temporary buttons drawn each frame: we need to update them too
            # build similar to draw functions before
            pass

        # drawing UI
        if mode == "menu":
            draw_menu(dt)
        elif mode == "theory":
            draw_theory(dt)
        elif mode == "practice":
            draw_practice(dt)
        elif mode == "credits":
            draw_credits(dt)

        # particles and overlays on top
        particle_sys.draw(SCREEN)

        # transitions: simple fade
        if transitioning:
            elapsed = time.time() - transition_start
            if elapsed < 0.35:
                alpha = int(255 * (elapsed / 0.35))
                overlay = pygame.Surface((W, H))
                overlay.fill((255,255,255))
                overlay.set_alpha(alpha)
                SCREEN.blit(overlay, (0,0))
            else:
                # switch
                global transition_target, transition_start
                mode = transition_target
                transitioning = False

        # feedback timer
        if feedback_timer > 0:
            feedback_timer -= dt
            if feedback_timer <= 0:
                # hide feedback
                pass

        # draw cursor hint
        # small footer
        footer = F_SMALL.render("Teclas: ENTER revisar | ESC volver | Backspace borrar", True, BLACK)
        SCREEN.blit(footer, (20, H-24))

        pygame.display.flip()

# run
if __name__ == "__main__":
    main()
