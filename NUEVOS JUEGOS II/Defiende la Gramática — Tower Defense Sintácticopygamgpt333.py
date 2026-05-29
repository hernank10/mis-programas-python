# defiende_gramatica_spline.py
# Tower Defense Sintáctico — mapa spline + tienda con selección de posición
# Requisitos: pygame
# Ejecutar: python defiende_gramatica_spline.py

import pygame, math, random, sys, time
pygame.init(); pygame.font.init()

# ---------------- Config ----------------
W, H = 1280, 760
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Defiende la Gramática — Spline & Tienda Mejorada")
FPS = 60
CLOCK = pygame.time.Clock()

# Fuentes
F_TITLE = pygame.font.SysFont("Segoe UI", 28, bold=True)
F_MED = pygame.font.SysFont("Segoe UI", 18)
F_SMALL = pygame.font.SysFont("Segoe UI", 14)
try:
    F_EMO = pygame.font.SysFont("Segoe UI Emoji", 26)
except:
    F_EMO = F_MED

# Colores
WHITE = (250,250,250)
BLACK = (18,18,18)
GLASS_A = 110

# Emojis sintácticos
SYN = {"sujeto":"👤","verbo":"🔤","conector":"🔗"}

# ---------------- Util: gradiente animado ----------------
def draw_animated_gradient(surf, t):
    r1 = int(40 + 60*math.sin(t*0.6))
    g1 = int(80 + 60*math.sin(t*0.8+1))
    b1 = int(140 + 40*math.cos(t*0.5+2))
    r2 = int(160 + 30*math.cos(t*0.7))
    g2 = int(90 + 40*math.cos(t*0.9+1))
    b2 = int(120 + 60*math.sin(t*0.4+2))
    for y in range(H):
        k = y / H
        r = int(r1*(1-k) + r2*k); g = int(g1*(1-k)+g2*k); b = int(b1*(1-k)+b2*k)
        pygame.draw.line(surf, (r,g,b), (0,y), (W,y))

def draw_glass(rect, rad=12, alpha=GLASS_A):
    s = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    s.fill((255,255,255,alpha))
    SCREEN.blit(s, (rect.x, rect.y))
    pygame.draw.rect(SCREEN, (255,255,255,18), rect, border_radius=rad, width=1)

# ---------------- RainbowButton ----------------
class RainbowButton:
    def __init__(self, rect, text, action=None, icon=""):
        self.rect = pygame.Rect(rect)
        self.text = text; self.action = action; self.icon = icon
        self.hover = False; self.pulse = 1.0; self.cool = 0.0

    def update(self, dt, mouse_pos, mouse_down):
        self.hover = self.rect.collidepoint(mouse_pos)
        self.pulse = min(1.18, self.pulse + dt*3.5) if self.hover else max(1.0, self.pulse - dt*2.8)
        if self.hover and mouse_down and self.cool <= 0:
            if self.action: self.action()
            self.cool = 0.25
        self.cool = max(0.0, self.cool - dt)

    def draw(self, surf):
        g = pygame.Surface((self.rect.w, self.rect.h))
        for x in range(self.rect.w):
            t = (x/self.rect.w + time.time()*0.08) % 1.0
            r = int(150 + 80*math.sin(2*math.pi*t))
            g_ = int(80 + 70*math.sin(2*math.pi*(t+0.33)))
            b = int(170 + 60*math.sin(2*math.pi*(t+0.66)))
            pygame.draw.line(g, (r,g_,b), (x,0),(x,self.rect.h))
        overlay = pygame.Surface((self.rect.w,self.rect.h), pygame.SRCALPHA)
        overlay.fill((255,255,255, int(60*(self.pulse-1.0))))
        g.blit(overlay,(0,0))
        pygame.draw.rect(g, (255,255,255,20), g.get_rect(), width=2, border_radius=10)
        surf.blit(g, self.rect.topleft)
        txt = F_MED.render(self.text, True, BLACK)
        surf.blit(txt, (self.rect.x+12, self.rect.y + (self.rect.h - txt.get_height())//2))
        if self.icon:
            surf.blit(F_EMO.render(self.icon, True, BLACK), (self.rect.right-36, self.rect.y + (self.rect.h-24)//2))

# ---------------- Particle emoji simple ----------------
class EmojiParticle:
    def __init__(self,x,y,emoji):
        self.x=x+random.uniform(-20,20); self.y=y+random.uniform(-10,10)
        self.vx=random.uniform(-80,80); self.vy=random.uniform(-220,-80)
        self.emoji=emoji; self.life=random.uniform(0.9,1.8); self.ttl=self.life
        self.rot=random.uniform(-180,180); self.rots=random.uniform(-120,120)
        self.size=random.randint(18,34)
    def update(self,dt):
        self.vy += 400*dt; self.x += self.vx*dt; self.y += self.vy*dt; self.rot+=self.rots*dt; self.ttl-=dt
    def draw(self,surf):
        if self.ttl<=0: return
        a=int(255*(self.ttl/self.life))
        f=pygame.font.SysFont("Segoe UI Emoji", self.size)
        s=f.render(self.emoji, True, (255,255,255))
        surf2 = pygame.Surface(s.get_size(), pygame.SRCALPHA); surf2.blit(s,(0,0)); surf2.set_alpha(a)
        surf2 = pygame.transform.rotate(surf2, self.rot)
        surf.blit(surf2,(self.x,self.y))

class ParticleSystem:
    def __init__(self): self.parts=[]
    def emit(self,x,y,emojis,count=12):
        for _ in range(count): self.parts.append(EmojiParticle(x,y,random.choice(emojis)))
    def update(self,dt):
        for p in self.parts: p.update(dt)
        self.parts = [p for p in self.parts if p.ttl>0 and -200<p.x<W+200 and p.y<H+200]
    def draw(self,surf):
        for p in self.parts: p.draw(surf)

particles = ParticleSystem()

# ---------------- Catmull-Rom Spline helpers ----------------
def catmull_rom_point(p0,p1,p2,p3,t):
    # t in [0,1]
    t2 = t*t; t3 = t2*t
    x = 0.5*((2*p1[0]) + (-p0[0]+p2[0])*t + (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2 + (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
    y = 0.5*((2*p1[1]) + (-p0[1]+p2[1])*t + (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2 + (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
    return (x,y)

def build_spline(waypoints, samples=20):
    # extend endpoints
    pts = []
    if len(waypoints) < 2: return waypoints
    p = waypoints
    # replicate ends
    ext = [p[0]] + p + [p[-1]]
    for i in range(len(ext)-3):
        for s in range(samples):
            t = s / samples
            pts.append(catmull_rom_point(ext[i], ext[i+1], ext[i+2], ext[i+3], t))
    pts.append(p[-1])
    return pts

# ---------------- Path waypoints (designer) ----------------
WAYPOINTS = [
    (-80, 160), (120,160), (320, 200), (520,150), (720,200), (900,260),
    (880,360), (680,420), (480,380), (320,480), (180,420), (-80, 420),
    (W+80, 480)
]
PATH = build_spline(WAYPOINTS, samples=28)

def draw_path(surf):
    if len(PATH)<2: return
    for i in range(len(PATH)-1):
        pygame.draw.line(surf, (255,255,255,40), PATH[i], PATH[i+1], 14)
        pygame.draw.line(surf, (0,0,0,30), PATH[i], PATH[i+1], 2)

# ---------------- Enemies (20 datos) ----------------
ENEMIES_DATA = [
    {"txt":"Comiendo en el parque.","type":"sujeto","fixed":"Él estaba comiendo en el parque."},
    {"txt":"Los niño juega en la calle.","type":"verbo","fixed":"Los niños juegan en la calle."},
    {"txt":"Salió tarde, sin embargo estaba cansado.","type":"conector","fixed":"Salió tarde porque estaba cansado."},
    {"txt":"Cuando llegó.","type":"sujeto","fixed":"Cuando llegó, todos lo recibieron."},
    {"txt":"Estudia mucho, y pasa examen.","type":"conector","fixed":"Estudia mucho y pasa el examen."},
    {"txt":"Los perro ladra fuerte.","type":"verbo","fixed":"Los perros ladran fuerte."},
    {"txt":"Jugando con amigos.","type":"sujeto","fixed":"Ella estaba jugando con amigos."},
    {"txt":"Compró manzanas, pero también plátano.","type":"conector","fixed":"Compró manzanas y también plátanos."},
    {"txt":"Los estudiantes estudia la lección.","type":"verbo","fixed":"Los estudiantes estudian la lección."},
    {"txt":"Aunque tenía hambre.","type":"sujeto","fixed":"Aunque tenía hambre, no comió nada."},
    {"txt":"Ellos fue al mercado.","type":"verbo","fixed":"Ellos fueron al mercado."},
    {"txt":"Llegó tarde, sin embargo estaba lloviendo.","type":"conector","fixed":"Llegó tarde porque estaba lloviendo."},
    {"txt":"Los niños juega fútbol.","type":"verbo","fixed":"Los niños juegan fútbol."},
    {"txt":"Cantando en la ducha.","type":"sujeto","fixed":"Él estaba cantando en la ducha."},
    {"txt":"Fuimos a cine, y comimos palomitas.","type":"conector","fixed":"Fuimos al cine y comimos palomitas."},
    {"txt":"La mujer comprar flores.","type":"verbo","fixed":"La mujer compra flores."},
    {"txt":"Si estudia mucho.","type":"sujeto","fixed":"Si estudia mucho, aprobará el examen."},
    {"txt":"Mis hermano viven en Bogotá.","type":"verbo","fixed":"Mis hermanos viven en Bogotá."},
    {"txt":"Llorando en la calle.","type":"sujeto","fixed":"Ella estaba llorando en la calle."},
    {"txt":"Llegó rápido, pero estaba cansado.","type":"conector","fixed":"Llegó rápido porque estaba cansado."},
]

# ---------------- Enemy (follows path by parameter t) ----------------
class Enemy:
    def __init__(self, data, delay=0.0):
        self.txt = data["txt"]; self.type = data["type"]; self.fixed = data["fixed"]
        self.progress = 0.0  # index along PATH as float
        self.speed = random.uniform(30,70)
        self.alive = True; self.hp = 100
        self.spawn_delay = delay
        self.killed_time = None

    def update(self, dt):
        if self.spawn_delay > 0:
            self.spawn_delay -= dt; return
        if not self.alive:
            return
        # progress increments proportionally to speed across PATH length
        # map speed to steps per second: approximate using path points
        dist_step = (self.speed * dt) /  (1.0)  # normalized; we'll translate to index
        self.progress += (self.speed * dt) / 40.0  # calibration
        if self.progress >= len(PATH)-1:
            # reached end -> kill and penalize (handled outside)
            self.alive = False
            self.killed_time = pygame.time.get_ticks()
    
    def pos(self):
        idx = min(int(self.progress), len(PATH)-1)
        return PATH[idx]
    
    def draw(self, surf):
        if self.spawn_delay>0: return
        x,y = self.pos()
        if self.alive:
            rect = pygame.Rect(x-80,y-20,160,40)
            pygame.draw.rect(surf, (190,40,40), rect, border_radius=8)
            surf.blit(F_MED.render(self.txt, True, (255,255,255)), (rect.x+8, rect.y+8))
            surf.blit(F_EMO.render(SYN[self.type], True, (255,255,255)), (rect.x-28, rect.y+6))
        else:
            # show fixed sentence briefly
            rect = pygame.Rect(x-140,y-20,280,40)
            pygame.draw.rect(surf, (40,150,40), rect, border_radius=8)
            surf.blit(F_MED.render(self.fixed, True, (255,255,255)), (rect.x+8, rect.y+10))

# ---------------- Tower class ----------------
class Tower:
    COST = {"sujeto":50,"verbo":60,"conector":70}
    ICON = {"sujeto":SYN["sujeto"], "verbo":SYN["verbo"], "conector":SYN["conector"]}
    def __init__(self,x,y,tipo):
        self.x=x; self.y=y; self.tipo=tipo
        self.range = 160; self.damage = 60
        self.fire_rate = 0.9; self.timer=0.0
    def update(self,dt,enemies):
        self.timer -= dt
        if self.timer<=0:
            # find enemy of matching type in range
            target=None; best=9999
            for e in enemies:
                if e.spawn_delay>0 or not e.alive: continue
                ex,ey = e.pos(); d=math.hypot(ex-self.x, ey-self.y)
                if e.type==self.tipo and d<self.range and d<best:
                    best=d; target=e
            if target:
                target.hp -= self.damage; self.timer = self.fire_rate
                particles.emit(target.pos()[0], target.pos()[1], ["✅","✨","🎯"], count=10)
                if target.hp<=0:
                    target.alive = False
                    target.killed_time = pygame.time.get_ticks()
    def draw(self,surf):
        col = (120,220,140) if self.tipo=="sujeto" else (120,170,240) if self.tipo=="verbo" else (240,210,100)
        pygame.draw.circle(surf, col, (int(self.x),int(self.y)), 22)
        surf.blit(F_EMO.render(self.ICON[self.tipo], True, BLACK), (self.x-12, self.y-16))
    def draw_range(self,surf):
        s = pygame.Surface((self.range*2,self.range*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (255,255,255,10), (self.range,self.range), self.range)
        surf.blit(s,(self.x-self.range, self.y-self.range))

# ---------------- Game state ----------------
enemies=[]; towers=[]; money=250; score=0; lives=6; game_over=False; wave=0
spawn_cool=0.0; placing_type=None; placement_preview=None

# Pre-schedule function
def spawn_wave():
    global wave
    wave += 1
    base_delay=0.5
    for i,d in enumerate(ENEMIES_DATA):
        enemies.append(Enemy(d, delay = i*base_delay + (wave-1)*3.0))

# UI Buttons (shop)
buttons=[]
def make_buy_action(tipo):
    def buy():
        global placing_type
        if money >= Tower.COST[tipo]:
            placing_type = tipo  # now user must click map to confirm placement
    return buy

buttons.append(RainbowButton((W-240, 110, 220, 48), "Comprar Torre Sujeto", action=make_buy_action("sujeto"), icon=SYN["sujeto"]))
buttons.append(RainbowButton((W-240, 170, 220, 48), "Comprar Torre Verbo", action=make_buy_action("verbo"), icon=SYN["verbo"]))
buttons.append(RainbowButton((W-240, 230, 220, 48), "Comprar Torre Conector", action=make_buy_action("conector"), icon=SYN["conector"]))
buttons.append(RainbowButton((W-240, 290, 220, 48), "Iniciar Oleada", action=spawn_wave, icon="⚡"))

# ---------------- Helpers UI ----------------
def draw_ui(dt, mouse_pos):
    # right panel
    panel = pygame.Rect(W-260, 60, 240, H-120)
    draw_glass(panel)
    SCREEN.blit(F_TITLE.render("Tienda & Control", True, BLACK), (panel.x+12, panel.y+8))
    SCREEN.blit(F_MED.render(f"Dinero: ${money}", True, BLACK), (panel.x+12, panel.y+48))
    SCREEN.blit(F_MED.render(f"Puntaje: {score}", True, BLACK), (panel.x+12, panel.y+72))
    SCREEN.blit(F_MED.render(f"Vidas: {lives}", True, BLACK), (panel.x+12, panel.y+96))
    # buttons
    md = pygame.mouse.get_pressed()[0]
    for b in buttons:
        b.update(dt, mouse_pos, md)
        b.draw(SCREEN)
    # placement instructions
    if placing_type:
        hint = F_MED.render(f"Coloca torre {placing_type}. Click en el mapa para colocar o ESC para cancelar.", True, BLACK)
        SCREEN.blit(hint, (panel.x+12, panel.y+200))
    # tower list
    SCREEN.blit(F_SMALL.render("Torres:", True, BLACK), (panel.x+12, panel.y+260))
    for i,t in enumerate(towers[-8:]):
        SCREEN.blit(F_SMALL.render(f"{i+1}. {t.tipo} (dmg {t.damage})", True, BLACK), (panel.x+18, panel.y+290 + i*22))

def draw_hud(dt):
    SCREEN.blit(F_TITLE.render("Defiende la Gramática — Mapa spline", True, BLACK), (18,8))
    SCREEN.blit(F_SMALL.render("Click tienda -> comprar -> clic mapa para colocar. Oleadas: corrige oraciones incorrectas.", True, BLACK), (18,46))

# ---------------- Update loop ----------------
def update_game(dt):
    global money, score, lives, game_over
    # update enemies
    for e in enemies:
        e.update(dt)
    # update towers
    for t in towers:
        t.update(dt, enemies)
    # collect killed or reached
    removed=[]
    for e in enemies:
        if e.spawn_delay>0: continue
        if not e.alive:
            # if killed by tower (hp<=0)
            if e.hp<=0:
                money += 18; score += 12
                removed.append(e)
            else:
                # reached end (progress beyond path)
                lives -= 1; removed.append(e)
    for r in removed: enemies.remove(r)
    if lives<=0: game_over=True

# ---------------- Draw everything ----------------
def draw_all(dt):
    t=time.time()
    draw_animated_gradient(SCREEN, t)
    draw_path(SCREEN)
    # show path points lightly
    # draw towers (ranges faint)
    for tw in towers: tw.draw_range(SCREEN)
    for tw in towers: tw.draw(SCREEN)
    for e in enemies: e.draw(SCREEN)
    draw_ui(dt, pygame.mouse.get_pos())
    draw_hud(dt)
    particles.draw(SCREEN)
    # placement preview
    if placing_type and placement_preview:
        x,y = placement_preview
        pygame.draw.circle(SCREEN, (255,255,255,40), (x,y), 24, 2)
        SCREEN.blit(F_EMO.render(Tower.ICON[placing_type], True, BLACK), (x-12,y-16))

# ---------------- Main ----------------
def main():
    global money, placing_type, placement_preview, game_over
    spawn_wave()  # start first wave
    running=True
    while running:
        dt = CLOCK.tick(FPS)/1000.0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mx,my = pygame.mouse.get_pos()
                # click in playable area (left of sidebar)
                if mx < W-260:
                    if placing_type:
                        cost = Tower.COST[placing_type]
                        if money >= cost:
                            money -= cost
                            towers.append(Tower(mx, my, placing_type))
                            particles.emit(mx, my, [Tower.ICON[placing_type]], count=12)
                            placing_type = None
                            placement_preview = None
                    else:
                        # allow removing tower if click on it? optional
                        pass
            elif event.type==pygame.MOUSEMOTION:
                mx,my = event.pos
                if placing_type:
                    placement_preview = (mx,my)
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE and placing_type:
                    placing_type=None; placement_preview=None

        # update
        particles.update(dt)
        update_game(dt)
        draw_all(dt)

        if game_over:
            overlay=pygame.Surface((W,H)); overlay.fill((0,0,0)); overlay.set_alpha(180); SCREEN.blit(overlay,(0,0))
            msg = F_TITLE.render("GAME OVER — Te quedaste sin vidas", True, (255, 200, 200))
            SCREEN.blit(msg, (W//2-msg.get_width()//2, H//2-40))
            sub = F_MED.render(f"Puntaje final: {score}  |  Presiona ESC para salir", True, WHITE)
            SCREEN.blit(sub, (W//2-sub.get_width()//2, H//2+10))
            pygame.display.flip()
            # wait for exit or ESC
            for ev in pygame.event.get():
                if ev.type==pygame.QUIT: running=False
                if ev.type==pygame.KEYDOWN and ev.key==pygame.K_ESCAPE: running=False
            continue

        pygame.display.flip()
    pygame.quit(); sys.exit()

if __name__=="__main__":
    main()
