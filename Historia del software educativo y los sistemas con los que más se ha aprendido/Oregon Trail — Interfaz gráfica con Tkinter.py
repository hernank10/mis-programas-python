#!/usr/bin/env python3
"""
Oregon Trail — Interfaz gráfica con Tkinter

Guarda como: oregon_trail_tk.py
Ejecuta: python3 oregon_trail_tk.py

Versión GUI basada en la simulación consola previa.
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import random
import json
import os
import sys

# ---------------------------
# Configuración
# ---------------------------
DESTINATION_DISTANCE = 2000
DAILY_FOOD_CONSUMPTION_PER_PERSON = 2
HUNT_FOOD_AVG = 80
INITIAL_PARTY = ["Leader (you)", "Spouse", "Child1", "Child2"]
DEFAULT_SAVE = "oregon_save_gui.json"

# ---------------------------
# Utilidades
# ---------------------------
def clamp(v, a, b):
    return max(a, min(b, v))

def rand_event(p):
    return random.random() < p

# ---------------------------
# Lógica del juego (GameState)
# ---------------------------
class GameState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.day = 0
        self.miles_traveled = 0
        self.distance_remaining = DESTINATION_DISTANCE
        self.money = 200.0
        self.food = 600
        self.wheels = 2
        self.kits = 1
        self.oxen = 4
        self.party = list(INITIAL_PARTY)
        self.dead = []
        self.pace = "steady"
        self.condition = "good"
        self.location = "Start"
        self.history = []
        self.game_over = False
        self.win = False

    def party_count(self):
        return len(self.party)

    def consume_food(self, days=1):
        required = int(self.party_count() * DAILY_FOOD_CONSUMPTION_PER_PERSON * days)
        consumed = min(self.food, required)
        self.food -= consumed
        return consumed, required

    def update_pace(self, pace):
        if pace in ("slow", "steady", "fast"):
            self.pace = pace

    def save(self, filename=DEFAULT_SAVE):
        payload = self.__dict__.copy()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        return filename

    def load(self, filename=DEFAULT_SAVE):
        if not os.path.exists(filename):
            return False
        with open(filename, "r", encoding="utf-8") as f:
            payload = json.load(f)
        self.__dict__.update(payload)
        return True

# ---------------------------
# Eventos aleatorios (misma lógica base)
# ---------------------------
def random_event(state: GameState):
    events = []
    # Storm
    if rand_event(0.06):
        storm_days = random.randint(1, 3)
        loss = random.randint(10, 60)
        state.food = max(0, state.food - int(loss/2))
        events.append(f"Tormenta: perdiste {loss//2} raciones y el viaje se retrasó {storm_days} días.")
    # Disease
    if rand_event(0.05) and state.party:
        victim = random.choice(state.party)
        if state.kits > 0 and rand_event(0.6):
            state.kits -= 1
            events.append(f"{victim} se enfermó pero se recuperó con un kit médico.")
        else:
            if rand_event(0.4):
                state.party.remove(victim); state.dead.append(victim)
                events.append(f"{victim} murió de enfermedad.")
            else:
                events.append(f"{victim} se enfermó pero se recuperó sin kit.")
    # Wheel break
    if rand_event(0.04):
        if state.wheels > 0:
            state.wheels -= 1
            cost = random.uniform(5, 20)
            state.money = max(0, state.money - cost)
            events.append("Una rueda se rompió; usaste un repuesto y pagaste reparación.")
        else:
            lost = random.randint(10, 40)
            state.food = max(0, state.food - lost)
            events.append(f"Se rompió una rueda sin repuesto. Perdiste {lost} raciones reparando.")
    # Bandits
    if rand_event(0.03):
        stolen = int(min(state.money, random.uniform(5, 50)))
        state.money -= stolen
        if rand_event(0.5):
            lostfood = random.randint(20, 80)
            state.food = max(0, state.food - lostfood)
            events.append(f"Los bandidos robaron ${stolen:.2f} y {lostfood} raciones.")
        else:
            events.append(f"Los bandidos robaron ${stolen:.2f}.")
    # Forage success
    if rand_event(0.02):
        found = random.randint(20, 100)
        state.food += found
        events.append(f"Encontraste {found} raciones recolectando.")
    return events

# ---------------------------
# Acciones
# ---------------------------
def travel_action(state: GameState):
    base = {"slow": 8, "steady": 12, "fast": 18}
    fatigue_penalty = {"good": 1.0, "fair": 0.85, "poor": 0.6}
    ox_factor = clamp(state.oxen / 4.0, 0.5, 1.2)
    miles = int(base[state.pace] * fatigue_penalty[state.condition] * ox_factor)
    consumed, required = state.consume_food(days=1)
    if consumed < required:
        if rand_event(0.3) and state.party:
            victim = random.choice(state.party)
            state.party.remove(victim); state.dead.append(victim)
            return 0, [f"Debido a la inanición, {victim} murió." ]
        state.condition = "poor"
    state.miles_traveled += miles
    state.distance_remaining = max(0, state.distance_remaining - miles)
    state.day += 1
    events = random_event(state)
    if state.pace == "fast" and rand_event(0.08) and state.party:
        victim = random.choice(state.party)
        state.party.remove(victim); state.dead.append(victim)
        events.append(f"Viajar muy rápido fue arriesgado. {victim} murió por el esfuerzo.")
    return miles, events

def rest_action(state: GameState, days=1):
    consumed, required = state.consume_food(days=days)
    for _ in range(days):
        state.day += 1
        if rand_event(0.12):
            found = random.randint(5, 30); state.food += found
    if state.condition == "poor":
        state.condition = "fair"
    elif state.condition == "fair":
        state.condition = "good"
    events = random_event(state)
    return consumed, events

def hunt_action(state: GameState):
    state.day += 1
    consumed, req = state.consume_food(days=1)
    success_chance = 0.6 if state.pace != "fast" else 0.4
    if rand_event(success_chance):
        food_gained = random.randint(int(HUNT_FOOD_AVG*0.4), int(HUNT_FOOD_AVG*1.4))
        state.food += food_gained
        return True, food_gained, random_event(state)
    else:
        if rand_event(0.05) and state.party:
            victim = random.choice(state.party)
            if state.kits > 0 and rand_event(0.6):
                state.kits -= 1
                return False, 0, [f"{victim} resultó herido pero se salvó con kit médico."]
            else:
                state.party.remove(victim); state.dead.append(victim)
                return False, 0, [f"{victim} murió durante la caza."]
        return False, 0, random_event(state)

def repair_action(state: GameState):
    if state.wheels > 0:
        return "Tienes ruedas de repuesto."
    else:
        cost = 20 + random.randint(0, 40)
        if state.money >= cost:
            state.money -= cost; state.wheels += 1
            return f"Pagaste ${cost} y obtuviste 1 rueda de repuesto."
        else:
            return "No tienes dinero suficiente para reparar."

# ---------------------------
# Interfaz gráfica (Tkinter)
# ---------------------------
class OregonGUI:
    def __init__(self, root):
        self.root = root
        root.title("Oregon Trail — GUI (Tkinter)")
        self.state = GameState()
        self.create_widgets()
        self.update_ui("Bienvenido a Oregon Trail (GUI). Escribe 'Ayuda' o usa los botones.")

    def create_widgets(self):
        # Main frames
        main = ttk.Frame(self.root, padding=8)
        main.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right = ttk.Frame(main, width=300)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas area (simple background and caravana icon)
        self.canvas = tk.Canvas(left, bg="#e6f2ff", height=360)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.draw_map()

        # Event log
        log_frame = ttk.LabelFrame(left, text="Registro de eventos")
        log_frame.pack(fill=tk.BOTH, expand=False, pady=6)
        self.log_text = tk.Text(log_frame, height=8, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Controls on right
        status_frame = ttk.LabelFrame(right, text="Estado")
        status_frame.pack(fill=tk.X, padx=4, pady=4)

        # Status labels
        self.labels = {}
        items = ["Day", "Miles", "Remaining", "People", "Food", "Money", "Wheels", "Kits", "Oxen", "Pace", "Condition"]
        for it in items:
            row = ttk.Frame(status_frame)
            row.pack(fill=tk.X, padx=2, pady=1)
            lab = ttk.Label(row, text=it + ": ", width=12)
            lab.pack(side=tk.LEFT)
            val = ttk.Label(row, text="", width=20)
            val.pack(side=tk.LEFT)
            self.labels[it] = val

        # Progress bar
        prog_frame = ttk.Frame(right)
        prog_frame.pack(fill=tk.X, padx=4, pady=(2,8))
        ttk.Label(prog_frame, text="Progreso hacia Oregon").pack(anchor=tk.W)
        self.progress = ttk.Progressbar(prog_frame, maximum=DESTINATION_DISTANCE, length=260)
        self.progress.pack(fill=tk.X)

        # Buttons
        btns = ttk.LabelFrame(right, text="Acciones")
        btns.pack(fill=tk.X, padx=4, pady=4)
        actions = [
            ("Travel", self.on_travel),
            ("Rest", self.on_rest),
            ("Hunt", self.on_hunt),
            ("Trade", self.on_trade),
            ("Repair", self.on_repair),
            ("Status", self.on_status),
            ("Save", self.on_save),
            ("Load", self.on_load),
            ("Quit", self.on_quit)
        ]
        for (text, cmd) in actions:
            b = ttk.Button(btns, text=text, command=cmd)
            b.pack(fill=tk.X, pady=2)

        # Pace control (radio)
        pace_frame = ttk.LabelFrame(right, text="Ritmo (Pace)")
        pace_frame.pack(fill=tk.X, padx=4, pady=4)
        self.pace_var = tk.StringVar(value=self.state.pace)
        for p in ("slow", "steady", "fast"):
            r = ttk.Radiobutton(pace_frame, text=p.title(), variable=self.pace_var, value=p, command=self.change_pace)
            r.pack(anchor=tk.W)

    def draw_map(self):
        # Simple representation: path line and wagon
        self.canvas.delete("all")
        w = self.canvas.winfo_width() or 600
        h = self.canvas.winfo_height() or 360
        margin = 40
        self.canvas.create_line(margin, h//2, w-margin, h//2, width=3, fill="#996633")
        # wagon position based on miles_traveled
        fraction = (self.state.miles_traveled / DESTINATION_DISTANCE) if DESTINATION_DISTANCE>0 else 0
        fraction = clamp(fraction, 0.0, 1.0)
        x = margin + fraction * (w - 2*margin)
        y = h//2
        # wagon (simple rectangle + wheels)
        self.canvas.create_rectangle(x-20, y-20, x+20, y+10, fill="#8B4513", outline="black")
        self.canvas.create_oval(x-16, y+6, x-6, y+16, fill="black")
        self.canvas.create_oval(x+6, y+6, x+16, y+16, fill="black")
        # markers for start and dest
        self.canvas.create_text(margin, h//2-20, text="Start", anchor=tk.SW)
        self.canvas.create_text(w-margin, h//2-20, text="Oregon", anchor=tk.SE)

    def update_ui(self, message=None):
        # update labels
        s = self.state
        self.labels["Day"].config(text=str(s.day))
        self.labels["Miles"].config(text=str(s.miles_traveled))
        self.labels["Remaining"].config(text=str(s.distance_remaining))
        self.labels["People"].config(text=f"{s.party_count()} (Dead: {len(s.dead)})")
        self.labels["Food"].config(text=str(s.food))
        self.labels["Money"].config(text=f"${s.money:.2f}")
        self.labels["Wheels"].config(text=str(s.wheels))
        self.labels["Kits"].config(text=str(s.kits))
        self.labels["Oxen"].config(text=str(s.oxen))
        self.labels["Pace"].config(text=s.pace)
        self.labels["Condition"].config(text=s.condition)
        self.progress['value'] = s.miles_traveled
        self.draw_map()
        if message:
            self.append_log(message)

    def append_log(self, text):
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)

    # ---------------- Action handlers ----------------
    def on_travel(self):
        miles, events = travel_action(self.state)
        if miles == 0 and not events:
            self.append_log("No avanzaste hoy (problema de recursos).")
        else:
            self.append_log(f"Viajaste {miles} millas hoy.")
        for e in events:
            self.append_log("Evento: " + e)
        self.state.history.append(f"travel {miles} (pace {self.state.pace})")
        if self.state.distance_remaining <= 0:
            self.state.win = True; self.state.game_over = True
            messagebox.showinfo("¡Victoria!", "¡Llegaste a Oregon!")
        if self.state.party_count() == 0:
            self.state.game_over = True
            messagebox.showerror("Derrota", "Todos han muerto. Fin del juego.")
        self.update_ui()

    def on_rest(self):
        days = simpledialog.askinteger("Descansar", "¿Cuántos días deseas descansar?", parent=self.root, minvalue=1, maxvalue=10)
        if days is None:
            return
        consumed, events = rest_action(self.state, days=days)
        self.append_log(f"Descansaste {days} días. Consumo: {consumed} raciones.")
        for e in events:
            self.append_log("Evento: " + e)
        self.state.history.append(f"rest {days}")
        self.update_ui()

    def on_hunt(self):
        ok, food_gained, events = hunt_action(self.state)
        if ok:
            self.append_log(f"Cazaste con éxito y obtuviste {food_gained} raciones.")
        else:
            self.append_log("La caza falló.")
        for e in events:
            if isinstance(e, str):
                self.append_log("Evento: " + e)
        self.state.history.append(f"hunt success={ok} food={food_gained}")
        self.update_ui()

    def on_trade(self):
        # simple dialog for trade
        choice = simpledialog.askstring("Comercio", "Opciones: buyfood, buywheel, buykit, sellfood\nEscribe tu opción:", parent=self.root)
        if not choice:
            return
        action = choice.strip().lower()
        if action == "buyfood":
            price_per_ration = 0.5 + random.random()*1.5
            amt = simpledialog.askinteger("Comprar comida", f"Precio {price_per_ration:.2f} $/ración. ¿Cuántas raciones?", parent=self.root, minvalue=1, maxvalue=10000)
            if not amt: return
            cost = price_per_ration * amt
            if cost > self.state.money:
                messagebox.showwarning("Dinero insuficiente", "No tienes suficiente dinero para esa compra.")
            else:
                self.state.money -= cost; self.state.food += amt
                self.append_log(f"Compraste {amt} raciones por ${cost:.2f}.")
        elif action == "buywheel":
            cost = 25 + random.randint(-5, 20)
            if self.state.money < cost:
                messagebox.showwarning("Dinero insuficiente", "No tienes suficiente dinero.")
            else:
                self.state.money -= cost; self.state.wheels += 1
                self.append_log(f"Compraste una rueda por ${cost}.")
        elif action == "buykit":
            cost = 15 + random.randint(-2, 10)
            if self.state.money < cost:
                messagebox.showwarning("Dinero insuficiente", "No tienes suficiente dinero.")
            else:
                self.state.money -= cost; self.state.kits += 1
                self.append_log(f"Compraste un kit médico por ${cost}.")
        elif action == "sellfood":
            amt = simpledialog.askinteger("Vender comida", "¿Cuántas raciones deseas vender?", parent=self.root, minvalue=1, maxvalue=self.state.food if self.state.food>0 else 1)
            if not amt: return
            price = 0.3 + random.random()*0.7
            revenue = price * amt
            self.state.food -= amt; self.state.money += revenue
            self.append_log(f"Vendiste {amt} raciones por ${revenue:.2f}.")
        else:
            messagebox.showinfo("Comercio", "Acción no reconocida.")
        self.state.history.append("trade")
        self.update_ui()

    def on_repair(self):
        msg = repair_action(self.state)
        self.append_log(msg)
        self.state.history.append("repair")
        self.update_ui()

    def on_status(self):
        s = self.state
        info = (
            f"Día: {s.day}\n"
            f"Millas recorridas: {s.miles_traveled}\n"
            f"Millas restantes: {s.distance_remaining}\n"
            f"Personas vivas: {s.party_count()} (Fallecidos: {len(s.dead)})\n"
            f"Comida: {s.food} raciones\n"
            f"Dinero: ${s.money:.2f}\n"
            f"Ruedas: {s.wheels}\n"
            f"Kits médicos: {s.kits}\n"
            f"Bueyes: {s.oxen}\n"
            f"Ritmo: {s.pace}\n"
            f"Condición: {s.condition}\n"
        )
        messagebox.showinfo("Estado actual", info)

    def on_save(self):
        fn = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON","*.json")], initialfile=DEFAULT_SAVE, title="Guardar partida")
        if not fn: return
        try:
            self.state.save(fn)
            self.append_log(f"Partida guardada en {fn}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def on_load(self):
        fn = filedialog.askopenfilename(filetypes=[("JSON","*.json")], initialfile=DEFAULT_SAVE, title="Cargar partida")
        if not fn: return
        ok = self.state.load(fn)
        if not ok:
            messagebox.showerror("Error", "Archivo no encontrado o inválido.")
        else:
            self.append_log(f"Partida cargada desde {fn}")
            self.update_ui()

    def on_quit(self):
        if messagebox.askyesno("Salir", "¿Deseas guardar la partida antes de salir?"):
            fn = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON","*.json")], initialfile=DEFAULT_SAVE)
            if fn:
                self.state.save(fn)
        self.root.quit()
        sys.exit(0)

    def change_pace(self):
        p = self.pace_var.get()
        self.state.update_pace(p)
        self.append_log(f"Ritmo cambiado a {p}.")
        self.update_ui()

# ---------------------------
# Arranque
# ---------------------------
def main():
    root = tk.Tk()
    app = OregonGUI(root)
    root.geometry("900x600")
    root.mainloop()

if __name__ == "__main__":
    main()
