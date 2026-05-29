import pygame, sys, sqlite3, random

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Módulo 6 - Oraciones Compuestas con SQLite")
clock = pygame.time.Clock()

# --- Colores rubíes ---
RUBY = (155, 17, 30)
RUBY_DARK = (90, 10, 20)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

font = pygame.font.SysFont("arial", 26)
big_font = pygame.font.SysFont("arial", 34, bold=True)

# --- Fondo con gradiente rubí ---
def draw_ruby_gradient(surf):
    for y in range(HEIGHT):
        r = int(RUBY[0] + (RUBY_DARK[0]-RUBY[0])*y/HEIGHT)
        g = int(RUBY[1] + (RUBY_DARK[1]-RUBY[1])*y/HEIGHT)
        b = int(RUBY[2] + (RUBY_DARK[2]-RUBY[2])*y/HEIGHT)
        pygame.draw.line(surf, (r,g,b), (0,y), (WIDTH,y))

# --- Botón con estilo rubí ---
class RubyButton:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.hover = False
    def draw(self, surf):
        color = RUBY if not self.hover else (200,40,60)
        pygame.draw.rect(surf, color, self.rect, border_radius=12)
        pygame.draw.rect(surf, WHITE, self.rect, 2, border_radius=12)
        label = font.render(self.text, True, WHITE)
        surf.blit(label, label.get_rect(center=self.rect.center))
    def handle_event(self, e):
        if e.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(e.pos)
        if e.type == pygame.MOUSEBUTTONDOWN and self.hover:
            self.callback()

# --- Conexión SQLite ---
def init_db():
    conn = sqlite3.connect("preguntas.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS preguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nivel TEXT,
            pregunta TEXT,
            respuesta TEXT
        )
    """)
    conn.commit()
    return conn

def cargar_preguntas(conn, nivel):
    cur = conn.cursor()
    cur.execute("SELECT pregunta,respuesta FROM preguntas WHERE nivel=?", (nivel,))
    return cur.fetchall()

def insertar_demo(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM preguntas")
    if cur.fetchone()[0] == 0:
        preguntas_demo = [
            ("facil","Fui al cine y compré palomitas","Coordinada copulativa"),
            ("facil","No estudió, pero aprobó","Coordinada adversativa"),
            ("intermedio","Me quedaré en casa si llueve","Subordinada condicional"),
            ("intermedio","Salió tan rápido que se cayó","Subordinada consecutiva"),
            ("avanzado","Transforma: 'Estaba cansado. Me acosté temprano'","Como estaba cansado, me acosté temprano"),
            ("avanzado","Transforma: 'Es muy tarde. No puedo salir'","Como es muy tarde, no puedo salir")
        ]
        cur.executemany("INSERT INTO preguntas (nivel,pregunta,respuesta) VALUES (?,?,?)", preguntas_demo)
        conn.commit()

# --- Lógica del juego ---
nivel = "facil"
p_index = 0
puntos = 0
conn = init_db()
insertar_demo(conn)
preguntas = cargar_preguntas(conn, nivel)

def mostrar_pregunta():
    global p_index, preguntas
    if p_index >= len(preguntas):
        return None
    return preguntas[p_index]

def responder(resp):
    global puntos, p_index, nivel, preguntas
    pregunta = mostrar_pregunta()
    if not pregunta: return
    correcta = pregunta[1]
    if resp.lower() == correcta.lower():
        puntos += 1
    p_index += 1
    if p_index >= len(preguntas):
        cambiar_nivel()

def cambiar_nivel():
    global nivel, p_index, preguntas
    if nivel == "facil": nivel = "intermedio"
    elif nivel == "intermedio": nivel = "avanzado"
    else: nivel = "fin"
    p_index = 0
    preguntas = cargar_preguntas(conn, nivel)

# --- Crear botones dinámicamente ---
buttons = []
def crear_botones():
    global buttons
    buttons = []
    if nivel == "facil":
        opciones = ["Coordinada copulativa","Coordinada adversativa","Coordinada disyuntiva"]
    elif nivel == "intermedio":
        opciones = ["Subordinada causal","Subordinada condicional","Subordinada consecutiva"]
    else:
        opciones = []
    for i, opt in enumerate(opciones):
        btn = RubyButton((100, 380+i*70, 350, 50), opt, lambda t=opt: responder(t))
        buttons.append(btn)

crear_botones()

# --- Loop principal ---
running = True
while running:
    dt = clock.tick(60)/1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running=False
        for b in buttons: b.handle_event(e)
        if nivel == "avanzado" and e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            pregunta = mostrar_pregunta()
            if pregunta: responder(pregunta[1])

    draw_ruby_gradient(screen)

    pregunta = mostrar_pregunta()
    if nivel != "fin" and pregunta:
        text = pregunta[0]
        screen.blit(big_font.render(text, True, WHITE), (60, 100))

    if nivel in ["facil","intermedio"]:
        for b in buttons: b.draw(screen)
    elif nivel == "avanzado" and pregunta:
        screen.blit(font.render("👉 Escribe la oración transformada (ENTER simulado)", True, WHITE), (60, 350))

    score_text = font.render(f"Puntos: {puntos}", True, WHITE)
    screen.blit(score_text, (WIDTH-200, 20))

    pygame.display.flip()
    if nivel in ["facil","intermedio"] and p_index >= len(preguntas):
        crear_botones()

pygame.quit()
sys.exit()
