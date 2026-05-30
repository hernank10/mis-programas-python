# modulo10_boss_final.py
"""
Módulo 10 - Boss Final de la Aventura Gramatical
Guardar como: modulo10_boss_final.py
Requisitos: pip install pygame
Ejecutar: python modulo10_boss_final.py
"""

import pygame, sys, random, math, time
pygame.init()

# ----- Configuración -----
WIDTH, HEIGHT = 960, 680
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Módulo 10 - Boss Final Gramatical")
CLOCK = pygame.time.Clock()
FPS = 60

# ----- Colores -----
WHITE = (255,255,255)
BLACK = (20,20,20)
RUBY = (180,30,80)

# ----- Fuentes -----
FONT_LG = pygame.font.Font(None, 42)
FONT_MD = pygame.font.Font(None, 28)
FONT_SM = pygame.font.Font(None, 20)

# ----- Fondo animado -----
def draw_bg(t):
    for i in range(0, HEIGHT, 4):
        r = int(80 + 80 * math.sin((i/60.0) + t))
        g = int(30 + 60 * math.sin((i/90.0) + t + 2))
        b = int(100 + 100 * math.sin((i/70.0) + t + 4))
        pygame.draw.rect(SCREEN, (r,g,b), (0,i,WIDTH,4))

# ----- Partículas -----
class Particle:
    def __init__(self,x,y,emoji):
        self.x,self.y = x,y
        self.vx = random.uniform(-120,120)
        self.vy = random.uniform(-220,-60)
        self.life = random.uniform(1.2,2.2)
        self.age = 0
        self.emoji = emoji
        self.font = pygame.font.Font(None, 40)
    def update(self,dt):
        self.age += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self,surf):
        if self.age < self.life:
            img = self.font.render(self.emoji,True,WHITE)
            surf.blit(img,(self.x,self.y))
    def alive(self): return self.age < self.life

particles = []
def spawn_particles(x,y,count=20,good=True):
    pool = ['🎉','✨','🌟','🔥','📘'] if good else ['💥','⚠️','❗']
    for _ in range(count):
        particles.append(Particle(x,y,random.choice(pool)))

# ----- Botón Rainbow -----
class RainbowButton:
    def __init__(self,rect,text,onclick):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.onclick = onclick
        self.hover = False
        self.hue = random.random()*360
    def update(self,dt):
        self.hue = (self.hue+dt*80)%360
    def draw(self,surf):
        h = self.hue/360
        r = int(150+100*math.sin(h*6.28))
        g = int(100+120*math.sin((h+0.33)*6.28))
        b = int(180+80*math.sin((h+0.66)*6.28))
        col = (max(0,min(255,r)),max(0,min(255,g)),max(0,min(255,b)))
        pygame.draw.rect(surf,col,self.rect,border_radius=12)
        txt = FONT_MD.render(self.text,True,BLACK)
        surf.blit(txt,(self.rect.x+(self.rect.w-txt.get_width())//2,
                       self.rect.y+(self.rect.h-txt.get_height())//2))
    def handle(self,event):
        if event.type==pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos): self.onclick()

# ----- Preguntas finales -----
QUESTIONS = [
    {"q":"Oración afirmativa correcta","opts":["He studies","He doesn’t study"],"ans":0},
    {"q":"Transforma en pregunta: 'You like pizza'","opts":["Do you like pizza?","You do like pizza?"],"ans":0},
    {"q":"Elige compuesta:","opts":["I was late. I missed the bus.","I was late because I missed the bus."],"ans":1}
]

# ----- Modal de preguntas -----
class Quiz:
    def __init__(self):
        self.active=False
        self.index=0
        self.feedback=""
        self.buttons=[]
    def start(self): 
        self.active=True; self.index=0; self.feedback=""; self.load()
    def load(self):
        self.buttons=[]
        q=QUESTIONS[self.index]
        for i,opt in enumerate(q["opts"]):
            rect=(WIDTH//2-200, HEIGHT//2+40+i*70,400,50)
            self.buttons.append(RainbowButton(rect,opt,onclick=lambda i=i:self.check(i)))
    def check(self,idx):
        q=QUESTIONS[self.index]
        if idx==q["ans"]:
            self.feedback="✅ Correcto!"
            spawn_particles(WIDTH//2,HEIGHT//2,25,good=True)
            self.index+=1
            if self.index>=len(QUESTIONS):
                self.active=False
                global WIN
                WIN=True
            else:
                self.load()
        else:
            self.feedback="❌ Incorrecto"
            spawn_particles(WIDTH//2,HEIGHT//2,15,good=False)
    def draw(self,surf):
        q=QUESTIONS[self.index]
        txt=FONT_LG.render(q["q"],True,WHITE)
        surf.blit(txt,(WIDTH//2-txt.get_width()//2,HEIGHT//2-60))
        for b in self.buttons: b.draw(surf)
        if self.feedback:
            fb=FONT_MD.render(self.feedback,True,WHITE)
            surf.blit(fb,(WIDTH//2-fb.get_width()//2,HEIGHT//2+180))
    def handle(self,event):
        for b in self.buttons: b.handle(event)

QUIZ=Quiz()
WIN=False

# ----- Libro “Boss” -----
book_rect=pygame.Rect(WIDTH//2-80,HEIGHT//2-160,160,120)

# ----- Loop principal -----
t=0; running=True
while running:
    dt=CLOCK.tick(FPS)/1000; t+=dt
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        if QUIZ.active: QUIZ.handle(e)
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            if book_rect.collidepoint(WIDTH//2,HEIGHT//2): QUIZ.start()
    # update
    for b in QUIZ.buttons: b.update(dt)
    for p in particles[:]:
        p.update(dt)
        if not p.alive(): particles.remove(p)
    # draw
    draw_bg(t)
    pygame.draw.rect(SCREEN,RUBY,book_rect,border_radius=16)
    SCREEN.blit(FONT_LG.render("📖",True,WHITE),(book_rect.centerx-20,book_rect.centery-30))
    SCREEN.blit(FONT_MD.render("Presiona ESPACIO para abrir el Libro Final",True,WHITE),(200,100))
    if QUIZ.active: QUIZ.draw(SCREEN)
    for p in particles: p.draw(SCREEN)
    if WIN:
        msg=FONT_LG.render("🎓 ¡Graduación! Has vencido el Boss Final 🎉",True,WHITE)
        SCREEN.blit(msg,(WIDTH//2-msg.get_width()//2,HEIGHT-120))
    pygame.display.flip()

pygame.quit(); sys.exit()
