import tkinter as tk
import random, math

# ---------------- CONFIG ----------------
W, H = 960, 600
CELL = 40  # tamaño de paso

# colores
COLORS = {"bg":"#223344","path":"#cccccc","enemy":"#ee4444","tower":"#44cc88"}

# emojis
SYN = {"sujeto":"👤","verbo":"🔤","conector":"🔗"}

# enemigos (20)
ENEMIES_DATA = [
    {"txt":"Los niño juega en la calle.","type":"verbo","fixed":"Los niños juegan en la calle."},
    {"txt":"Comiendo en el parque.","type":"sujeto","fixed":"Él estaba comiendo en el parque."},
    {"txt":"Salió tarde, sin embargo estaba cansado.","type":"conector","fixed":"Salió tarde porque estaba cansado."},
    {"txt":"Cuando llegó.","type":"sujeto","fixed":"Cuando llegó, todos lo recibieron."},
    {"txt":"Los perro ladra fuerte.","type":"verbo","fixed":"Los perros ladran fuerte."},
    {"txt":"Jugando con amigos.","type":"sujeto","fixed":"Ella estaba jugando con amigos."},
    {"txt":"Compró manzanas, pero también plátano.","type":"conector","fixed":"Compró manzanas y plátanos."},
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
    {"txt":"Estudia mucho, y pasa examen.","type":"conector","fixed":"Estudia mucho y pasa el examen."},
]

# ---------------- CLASES ----------------
class Enemy:
    def __init__(self, canvas, data, path):
        self.canvas = canvas
        self.txt, self.type, self.fixed = data["txt"], data["type"], data["fixed"]
        self.path = path
        self.index = 0
        self.speed = 1
        self.hp = 100
        self.shape = self.canvas.create_oval(0,0,0,0,fill=COLORS["enemy"])
        self.label = self.canvas.create_text(0,0,text=self.txt,fill="white",font=("Arial",10))
        self.update()

    def update(self):
        if self.index < len(self.path):
            x,y = self.path[self.index]
            self.canvas.coords(self.shape, x-12,y-12,x+12,y+12)
            self.canvas.coords(self.label, x, y-20)
            self.index += self.speed
        else:
            return False
        return True

    def damage(self, d):
        self.hp -= d
        if self.hp <= 0:
            self.canvas.itemconfig(self.shape, fill="green")
            self.canvas.itemconfig(self.label, text=self.fixed)
            return True
        return False

class Tower:
    COST = {"sujeto":50,"verbo":60,"conector":70}
    def __init__(self, canvas,x,y,tipo):
        self.canvas=canvas; self.x=x; self.y=y; self.tipo=tipo
        self.range=100; self.damage=50
        self.shape=self.canvas.create_rectangle(x-15,y-15,x+15,y+15,fill=COLORS["tower"])
        self.icon=self.canvas.create_text(x,y,text=SYN[tipo],font=("Arial",14))

    def attack(self,enemies):
        for e in enemies:
            if e.type==self.tipo and e.hp>0:
                ex,ey = e.path[e.index] if e.index < len(e.path) else (0,0)
                if math.hypot(ex-self.x,ey-self.y) < self.range:
                    if e.damage(self.damage): return 10,5
        return 0,0

# ---------------- GAME ----------------
class Game:
    def __init__(self, root):
        self.root=root
        self.canvas=tk.Canvas(root,width=W,height=H,bg=COLORS["bg"])
        self.canvas.pack(side="left")

        self.sidebar=tk.Frame(root,width=200,bg="#eeeeee")
        self.sidebar.pack(side="right",fill="y")

        self.money=200; self.score=0; self.lives=5
        self.enemies=[]; self.towers=[]
        self.placing=None
        self.wave=0

        # HUD
        self.lbl_money=tk.Label(self.sidebar,text=f"Dinero: {self.money}")
        self.lbl_money.pack(pady=4)
        self.lbl_score=tk.Label(self.sidebar,text=f"Puntaje: {self.score}")
        self.lbl_score.pack(pady=4)
        self.lbl_lives=tk.Label(self.sidebar,text=f"Vidas: {self.lives}")
        self.lbl_lives.pack(pady=4)

        # tienda
        for tipo in ["sujeto","verbo","conector"]:
            tk.Button(self.sidebar,text=f"Comprar {tipo} ({Tower.COST[tipo]})",
                      command=lambda t=tipo:self.buy_tower(t)).pack(pady=2)
        tk.Button(self.sidebar,text="Iniciar oleada",command=self.spawn_wave).pack(pady=6)

        # path
        self.path=[(40,80),(160,80),(160,200),(320,200),(320,400),(480,400),(480,520),(640,520),(640,320),(800,320),(800,100),(920,100)]
        for i in range(len(self.path)-1):
            self.canvas.create_line(*self.path[i],*self.path[i+1],width=20,fill=COLORS["path"])

        self.canvas.bind("<Button-1>",self.on_click)

        self.update()

    def buy_tower(self,tipo):
        if self.money >= Tower.COST[tipo]:
            self.placing=tipo

    def on_click(self,event):
        if self.placing:
            t=Tower(self.canvas,event.x,event.y,self.placing)
            self.towers.append(t)
            self.money-=Tower.COST[self.placing]
            self.placing=None
            self.update_labels()

    def spawn_wave(self):
        if self.wave*5 < len(ENEMIES_DATA):
            for i in range(5):
                d=ENEMIES_DATA[self.wave*5+i]
                self.enemies.append(Enemy(self.canvas,d,self.path))
            self.wave+=1

    def update(self):
        # enemigos
        alive=[]
        for e in self.enemies:
            if e.hp>0 and e.update():
                alive.append(e)
            elif e.hp<=0:
                self.score+=5; self.money+=10
        self.enemies=alive

        # torres
        for t in self.towers:
            g,s=t.attack(self.enemies)
            self.money+=g; self.score+=s

        self.update_labels()

        if self.lives>0:
            self.root.after(500,self.update)
        else:
            self.lbl_score.config(text=f"Game Over! Puntaje {self.score}")

    def update_labels(self):
        self.lbl_money.config(text=f"Dinero: {self.money}")
        self.lbl_score.config(text=f"Puntaje: {self.score}")
        self.lbl_lives.config(text=f"Vidas: {self.lives}")

# ---------------- MAIN ----------------
if __name__=="__main__":
    root=tk.Tk(); root.title("Tower Defense Sintáctico (Tkinter)")
    game=Game(root)
    root.mainloop()
