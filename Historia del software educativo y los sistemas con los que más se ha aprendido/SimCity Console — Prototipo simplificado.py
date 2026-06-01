#!/usr/bin/env python3
"""
SimCity Console — Prototipo simplificado

Guarda como: simcity_console.py
Ejecuta: python3 simcity_console.py

Controles básicos (en el prompt):
- map                     : muestra el mapa
- build <type> x y        : construye en coordenada (type: R,C,I,P,road)
- demolish x y            : demuele la parcela
- step [n]                : avanza n turns (por defecto 1)
- tax <rate>              : fija tasa impositiva (0..100 %)
- status                  : muestra indicadores (población, dinero, polución...)
- save <file>             : guarda estado en JSON
- load <file>             : carga estado desde JSON
- help                    : ayuda
- quit                    : salir

Diseñado para ser simple y pedagógico: modifica parámetros y observa efectos.
"""
import random
import json
import math
import os
from datetime import datetime

# -------------------------
# Configuración del mundo
# -------------------------
MAP_W = 12
MAP_H = 12

# Tile types
EMPTY = '.'
ROAD = '='
RES = 'R'
COM = 'C'
IND = 'I'
PARK = 'P'

# Costs
COST_BUILD = {
    ROAD: 10,
    RES: 100,
    COM: 300,
    IND: 350,
    PARK: 50
}
MAINTENANCE = {
    ROAD: 1,
    RES: 1,
    COM: 3,
    IND: 4,
    PARK: 0
}

# Economic parameters
BASE_WAGE = 10              # wage per worker / turn
COMMERCE_REVENUE = 5       # revenue per commercial tile / turn
IND_POLLUTION = 3          # pollution per industrial tile / turn
GROWTH_BASE = 0.02         # base population growth per turn (2%)
MAX_POP_PER_RES = 5        # capacity per R zone (when fully attractive)
JOBS_PER_COM = 4
JOBS_PER_IND = 6

# Events probabilities
EVENT_PROBS = {
    'fire': 0.03,
    'boom': 0.02,
    'recession': 0.02,
    'migration': 0.015
}

SAVE_DIR = "saves"
os.makedirs(SAVE_DIR, exist_ok=True)

# -------------------------
# Helper utilities
# -------------------------
def in_bounds(x, y):
    return 0 <= x < MAP_W and 0 <= y < MAP_H

def neighbors(x, y):
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if in_bounds(nx, ny):
            yield nx, ny

# -------------------------
# City class (state)
# -------------------------
class City:
    def __init__(self, w=MAP_W, h=MAP_H):
        self.w = w
        self.h = h
        self.map = [[EMPTY for _ in range(w)] for _ in range(h)]
        # initialize with a small road cross in center
        cx, cy = w//2, h//2
        self.map[cy][cx] = ROAD
        self.map[cy][cx-1] = ROAD
        self.map[cy][cx+1] = ROAD
        self.map[cy-1][cx] = ROAD
        self.map[cy+1][cx] = ROAD

        # state variables
        self.turn = 0
        self.money = 5000.0
        self.tax_rate = 10.0  # percent
        self.population = 10.0
        self.unemployed = 2.0
        self.pollution = 0.0
        self.happiness = 0.8  # 0..1
        self.history = []

    # -------------------------
    # Map operations
    # -------------------------
    def get_tile(self, x, y):
        if in_bounds(x, y):
            return self.map[y][x]
        return None

    def set_tile(self, x, y, t):
        if in_bounds(x, y):
            self.map[y][x] = t
            return True
        return False

    def build(self, kind, x, y):
        if not in_bounds(x, y):
            return False, "Fuera de límites."
        if self.map[y][x] != EMPTY:
            return False, "Parcela ocupada."
        if kind == 'road':
            tile = ROAD
        else:
            tile = kind.upper()
        cost = COST_BUILD.get(tile, None)
        if cost is None:
            return False, "Tipo inválido."
        if self.money < cost:
            return False, "Fondos insuficientes."
        self.money -= cost
        self.map[y][x] = tile
        self.log(f"Construido {tile} en ({x},{y}) por ${cost}.")
        return True, f"Construido {tile}."

    def demolish(self, x, y):
        if not in_bounds(x, y):
            return False, "Fuera de límites."
        t = self.map[y][x]
        if t == EMPTY:
            return False, "No hay nada para demoler."
        # refund fraction
        refund = COST_BUILD.get(t, 0) * 0.3
        self.money += refund
        self.map[y][x] = EMPTY
        self.log(f"Demolido {t} en ({x},{y}). Recuperado ${refund:.1f}.")
        return True, f"Demolido {t}. Recuperado ${refund:.1f}."

    # -------------------------
    # Simulation step
    # -------------------------
    def step(self, n=1):
        for i in range(n):
            self.turn += 1
            # maintenance costs
            maint = self.compute_maintenance()
            self.money -= maint
            # compute jobs and capacity
            jobs = self.compute_jobs()
            capacity = self.compute_res_capacity()
            # employment
            employed = min(self.population, jobs)
            unemployed = max(0.0, self.population - employed)
            # incomes
            wages = employed * BASE_WAGE
            commerce = self.count_tiles(COM) * COMMERCE_REVENUE
            tax = (wages + commerce) * (self.tax_rate / 100.0)
            self.money += tax
            # changes to population: growth influenced by happiness, pollution, jobs vs capacity
            growth_factor = GROWTH_BASE * (self.happiness) * max(0.2, (1 - (self.pollution/100)))
            # if jobs very low relative to pop, negative growth
            job_ratio = jobs / max(1.0, self.population)
            if job_ratio < 0.5:
                growth_factor *= job_ratio
                growth_factor -= 0.01  # slight decline
            # cap by housing capacity
            if self.population >= capacity:
                growth_factor -= 0.02  # limit
            delta_pop = self.population * growth_factor
            # randomness small
            delta_pop += random.uniform(-0.5, 0.5)
            self.population = max(0.0, self.population + delta_pop)
            # update unemployment
            self.unemployed = max(0.0, self.population - employed)
            # pollution increments by industry tiles
            self.pollution += self.count_tiles(IND) * IND_POLLUTION * 0.1
            # natural decay of pollution slightly
            self.pollution = max(0.0, self.pollution - 0.5)
            # happiness depends on money per capita, pollution, parks per capita
            money_pc = max(0.0, self.money / max(1.0, self.population))
            parks = self.count_tiles(PARK)
            park_factor = min(1.0, (parks * 3) / max(1.0, self.population))
            self.happiness = self.sigmoid(0.001*money_pc + 0.5*park_factor - 0.03*(self.pollution/10))
            # log economy
            self.log_turn_summary(employed, jobs, tax, maint)
            # events
            self.possible_event()
        return True

    def compute_jobs(self):
        return self.count_tiles(COM) * JOBS_PER_COM + self.count_tiles(IND) * JOBS_PER_IND

    def compute_res_capacity(self):
        # each residential tile provides housing, scaled by access to road
        capacity = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.map[y][x] == RES:
                    # capacity increases if adjacent to road
                    adj_road = any(self.get_tile(nx,ny) == ROAD for nx,ny in neighbors(x,y))
                    capacity += MAX_POP_PER_RES * (1.5 if adj_road else 1.0)
        return capacity

    def compute_maintenance(self):
        total = 0.0
        for y in range(self.h):
            for x in range(self.w):
                t = self.map[y][x]
                total += MAINTENANCE.get(t, 0)
        return total

    def count_tiles(self, tiletype):
        c = 0
        for row in self.map:
            for t in row:
                if t == tiletype:
                    c += 1
        return c

    def possible_event(self):
        r = random.random()
        # fire: destroys a random non-road tile
        if r < EVENT_PROBS['fire']:
            # choose a target tile among buildings
            targets = [(x,y) for y in range(self.h) for x in range(self.w) if self.map[y][x] in (RES,COM,IND)]
            if targets:
                tx, ty = random.choice(targets)
                lost = self.map[ty][tx]
                self.map[ty][tx] = EMPTY
                cost = COST_BUILD.get(lost, 0) * 0.5
                self.money -= cost
                self.log(f"Evento: incendio destruyó {lost} en ({tx},{ty}). Coste de emergencia ${cost:.1f}.")
        # economic boom
        elif r < EVENT_PROBS['fire'] + EVENT_PROBS['boom']:
            bonus = random.uniform(200, 800)
            self.money += bonus
            self.log(f"Evento: auge económico local. Ganaste ${bonus:.1f} en ingresos.")
        # recession
        elif r < EVENT_PROBS['fire'] + EVENT_PROBS['boom'] + EVENT_PROBS['recession']:
            loss = random.uniform(200, 700)
            self.money -= loss
            self.happiness -= 0.05
            self.log(f"Evento: recesión. Perdida ${loss:.1f}.")
        # migration influx/outflow
        elif r < sum(EVENT_PROBS.values()):
            change = random.randint(-10, 30)
            self.population = max(0.0, self.population + change)
            self.log(f"Evento: migración neta: {'llegaron' if change>0 else 'se fueron'} {abs(change)} personas.")

    # -------------------------
    # Utilities & IO
    # -------------------------
    def sigmoid(self, x):
        # bound to 0..1
        return 1.0 / (1.0 + math.exp(-x))

    def log(self, text):
        ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
        self.history.append(f"[{ts}] {text}")

    def log_turn_summary(self, employed, jobs, tax, maintenance):
        self.log(f"Turn {self.turn}: Población={self.population:.1f} Empleados={employed:.1f}/{jobs} Impuestos+={tax:.1f} Mantenimiento-={maintenance:.1f} Dinero=${self.money:.1f}")

    def status(self):
        s = {
            "turn": self.turn,
            "money": round(self.money,1),
            "population": round(self.population,1),
            "unemployed": round(self.unemployed,1),
            "pollution": round(self.pollution,1),
            "happiness": round(self.happiness,2),
            "tax_rate": round(self.tax_rate,1),
            "residential": self.count_tiles(RES),
            "commercial": self.count_tiles(COM),
            "industrial": self.count_tiles(IND),
            "roads": self.count_tiles(ROAD),
            "parks": self.count_tiles(PARK),
        }
        return s

    def print_map(self):
        header = "   " + " ".join(f"{i:2d}" for i in range(self.w))
        print(header)
        for y in range(self.h):
            row = f"{y:2d} " + " ".join(f" {self.map[y][x]}" for x in range(self.w))
            print(row)

    def save(self, filename):
        data = {
            "w": self.w, "h": self.h, "map": self.map,
            "turn": self.turn, "money": self.money, "tax_rate": self.tax_rate,
            "population": self.population, "pollution": self.pollution,
            "happiness": self.happiness, "history": self.history
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.w = data.get("w", self.w)
        self.h = data.get("h", self.h)
        self.map = data.get("map", self.map)
        self.turn = data.get("turn", self.turn)
        self.money = data.get("money", self.money)
        self.tax_rate = data.get("tax_rate", self.tax_rate)
        self.population = data.get("population", self.population)
        self.pollution = data.get("pollution", self.pollution)
        self.happiness = data.get("happiness", self.happiness)
        self.history = data.get("history", self.history)
        return True

# -------------------------
# CLI
# -------------------------
def help_text():
    print("""
Comandos:
 map                     : muestra el mapa (coordenadas x y)
 build <type> x y        : construye en (x,y). type: R (res), C (com), I (ind), P (park), road
 demolish x y            : demuele parcela
 step [n]                : avanza n turns (default 1)
 tax <rate>              : fija la tasa fiscal (0..100 %)
 status                  : indicadores económicos y sociales
 save <name>             : guarda partida (en carpeta 'saves')
 load <name>             : carga partida
 help                    : este texto
 quit                    : salir
""")

def main():
    city = City()
    print("SimCity Console - prototipo simplificado")
    help_text()

    while True:
        cmd = input("\n> ").strip().split()
        if not cmd:
            continue
        c = cmd[0].lower()

        try:
            if c == "help":
                help_text()
            elif c == "map":
                city.print_map()
            elif c == "build":
                if len(cmd) < 4:
                    print("Uso: build <type> x y")
                    continue
                typ = cmd[1].lower()
                x = int(cmd[2]); y = int(cmd[3])
                kind = typ
                if typ in ('r','res','residential'): kind = RES
                elif typ in ('c','com','commercial'): kind = COM
                elif typ in ('i','ind','industrial'): kind = IND
                elif typ in ('p','park'): kind = PARK
                elif typ == 'road': kind = 'road'
                else:
                    print("Tipo inválido.")
                    continue
                ok, msg = city.build(kind, x, y)
                print(msg)
            elif c == "demolish":
                if len(cmd) < 3:
                    print("Uso: demolish x y")
                    continue
                x = int(cmd[1]); y = int(cmd[2])
                ok, msg = city.demolish(x, y)
                print(msg)
            elif c == "step":
                n = 1
                if len(cmd) >= 2:
                    n = int(cmd[1])
                city.step(n)
                print(f"Avanzados {n} turns. Turn actual: {city.turn}")
            elif c == "tax":
                if len(cmd) < 2:
                    print("Uso: tax <rate>")
                    continue
                rate = float(cmd[1])
                if rate < 0 or rate > 100:
                    print("Rate 0..100")
                    continue
                city.tax_rate = rate
                print(f"Tasa fijada: {rate}%")
            elif c == "status":
                s = city.status()
                print("---- Estado ----")
                for k, v in s.items():
                    print(f"{k}: {v}")
                print("Ultimos eventos:")
                for e in city.history[-6:]:
                    print(" ", e)
            elif c == "save":
                name = "simcity"
                if len(cmd) >= 2:
                    name = cmd[1]
                fname = os.path.join(SAVE_DIR, f"{name}.json")
                city.save(fname)
                print(f"Guardado en {fname}")
            elif c == "load":
                name = "simcity"
                if len(cmd) >= 2:
                    name = cmd[1]
                fname = os.path.join(SAVE_DIR, f"{name}.json")
                if not os.path.exists(fname):
                    print("Archivo no encontrado:", fname)
                    continue
                city.load(fname)
                print(f"Cargado desde {fname}")
            elif c == "quit" or c == "exit":
                print("Saliendo.")
                break
            else:
                print("Comando desconocido. Escribe 'help'.")
        except Exception as e:
            print("Error procesando comando:", e)

if __name__ == "__main__":
    main()
