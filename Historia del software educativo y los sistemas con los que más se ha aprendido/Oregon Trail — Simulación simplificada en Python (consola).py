#!/usr/bin/env python3
"""
Oregon Trail — Simulación simplificada en Python (consola)

Características:
- Gestión de recursos y decisiones
- Eventos aleatorios que afectan la partida
- Guardar / cargar partida (archivo .save simple)
- Objetivo: llegar a Oregon (distancia definida)

Autor: Generado por ChatGPT
"""
import random
import json
import os
import sys
from datetime import datetime

# ---------------------------
# Configuración inicial
# ---------------------------
DESTINATION_DISTANCE = 2000  # millas hasta Oregon (simplificado)
DAILY_FOOD_CONSUMPTION_PER_PERSON = 2  # raciones por persona y día
HUNT_FOOD_AVG = 80  # comida aproximada obtenida al cazar con éxito
INITIAL_PARTY = ["Leader (you)", "Spouse", "Child1", "Child2"]
SAVE_FILENAME = "oregon_save.json"

# ---------------------------
# Utilidades
# ---------------------------
def clamp(v, a, b):
    return max(a, min(b, v))

def rand_event(prob):
    return random.random() < prob

# ---------------------------
# Clase GameState
# ---------------------------
class GameState:
    def __init__(self):
        # Progresión
        self.day = 0
        self.miles_traveled = 0
        self.distance_remaining = DESTINATION_DISTANCE
        # Recursos
        self.money = 200.0  # dólares
        self.food = 600  # raciones
        self.wheels = 2  # ruedas de repuesto
        self.kits = 1  # kits médicos
        self.oxen = 4  # número de bueyes
        self.party = list(INITIAL_PARTY)
        self.dead = []
        # Ritmo y estado
        self.pace = "steady"  # slow, steady, fast
        self.condition = "good"  # good, fair, poor
        # game flags
        self.game_over = False
        self.win = False
        # Misc
        self.location = "Start"
        self.history = []

    def save(self, filename=SAVE_FILENAME):
        payload = {
            "day": self.day,
            "miles_traveled": self.miles_traveled,
            "distance_remaining": self.distance_remaining,
            "money": self.money,
            "food": self.food,
            "wheels": self.wheels,
            "kits": self.kits,
            "oxen": self.oxen,
            "party": self.party,
            "dead": self.dead,
            "pace": self.pace,
            "condition": self.condition,
            "location": self.location,
            "history": self.history,
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"[Guardado] Partida guardada en {filename}.")

    def load(self, filename=SAVE_FILENAME):
        if not os.path.exists(filename):
            print("[Error] Archivo de guardado no encontrado.")
            return False
        with open(filename, "r", encoding="utf-8") as f:
            payload = json.load(f)
        self.day = payload["day"]
        self.miles_traveled = payload["miles_traveled"]
        self.distance_remaining = payload["distance_remaining"]
        self.money = payload["money"]
        self.food = payload["food"]
        self.wheels = payload["wheels"]
        self.kits = payload["kits"]
        self.oxen = payload["oxen"]
        self.party = payload["party"]
        self.dead = payload["dead"]
        self.pace = payload["pace"]
        self.condition = payload["condition"]
        self.location = payload.get("location", "Unknown")
        self.history = payload.get("history", [])
        print(f"[Cargado] Partida cargada desde {filename}. Día {self.day}, {self.distance_remaining} millas restantes.")
        return True

    def party_count(self):
        return len(self.party)

    def consume_food(self, days=1):
        # Consumo depende de cuántas personas vivas
        required = int(self.party_count() * DAILY_FOOD_CONSUMPTION_PER_PERSON * days)
        consumed = min(self.food, required)
        self.food -= consumed
        return consumed, required

    def update_pace(self, pace):
        if pace in ("slow", "steady", "fast"):
            self.pace = pace
            print(f"Pace set to {pace}.")
        else:
            print("Pace inválido. Usa slow, steady o fast.")

# ---------------------------
# Eventos aleatorios
# ---------------------------
def random_event(state: GameState):
    # Ocurre cada día potencialmente un evento
    # Probabilidades aproximadas y efectos
    events = []
    # Weather event (nieve/tormenta) - retraso o pérdida
    if rand_event(0.06):
        storm_days = random.randint(1, 4)
        loss = random.randint(10, 60)
        state.distance_remaining += 0  # stay in place that day (handled by caller)
        state.food = max(0, state.food - int(loss/2))
        events.append(f"Storm hit: lost {loss//2} food; travel delayed {storm_days} days.")
    # Disease
    if rand_event(0.05):
        victim = random.choice(state.party)
        if state.kits > 0 and rand_event(0.6):
            state.kits -= 1
            events.append(f"{victim} got sick but recovered with a medical kit.")
        else:
            # chance of death
            if rand_event(0.4):
                state.party.remove(victim)
                state.dead.append(victim)
                events.append(f"{victim} died of disease.")
            else:
                events.append(f"{victim} fell ill but recovered.")
    # Wheel break
    if rand_event(0.04):
        if state.wheels > 0:
            state.wheels -= 1
            state.money -= random.uniform(5, 20)  # repair cost/time lost
            events.append("A wagon wheel broke. You used a spare and paid repair costs.")
        else:
            # forced stop, possible loss of supplies
            lost = random.randint(10, 40)
            state.food = max(0, state.food - lost)
            events.append(f"Wagon wheel broke and you had no spares. Lost {lost} food while repairing.")
    # Bandits / theft
    if rand_event(0.03):
        stolen = int(min(state.money, random.uniform(5, 50)))
        state.money -= stolen
        # maybe take food too
        if rand_event(0.5):
            lostfood = random.randint(20, 80)
            state.food = max(0, state.food - lostfood)
            events.append(f"Bandits stole ${stolen:.2f} and {lostfood} food.")
        else:
            events.append(f"Bandits stole ${stolen:.2f}.")
    # Good fortune / find
    if rand_event(0.02):
        found = random.randint(20, 100)
        state.food += found
        events.append(f"You foraged and found {found} food.")
    return events

# ---------------------------
# Actions: travel, rest, hunt, trade, repair
# ---------------------------
def travel(state: GameState):
    # Travel advances miles based on pace and condition
    base = {"slow": 8, "steady": 12, "fast": 18}
    fatigue_penalty = {"good": 1.0, "fair": 0.85, "poor": 0.6}
    ox_factor = clamp(state.oxen / 4.0, 0.5, 1.2)
    miles = int(base[state.pace] * fatigue_penalty[state.condition] * ox_factor)
    # consume food for one day
    consumed, required = state.consume_food(days=1)
    if consumed < required:
        # starvation effect: chance of dying or losing condition
        if rand_event(0.3):
            victim = random.choice(state.party)
            state.party.remove(victim); state.dead.append(victim)
            print(f"Due to starvation, {victim} has died.")
        state.condition = "poor"
    # progress
    state.miles_traveled += miles
    state.distance_remaining = max(0, state.distance_remaining - miles)
    state.day += 1
    # random events
    events = random_event(state)
    # pace consequences: traveling fast increases illness chance
    if state.pace == "fast" and rand_event(0.08):
        victim = random.choice(state.party)
        state.party.remove(victim); state.dead.append(victim)
        events.append(f"Traveling fast was risky. {victim} died from strain.")
    return miles, events

def rest(state: GameState, days=1):
    # Rest to recover condition, consumes food
    consumed, required = state.consume_food(days=days)
    for _ in range(days):
        state.day += 1
        # small chance to heal someone or find food
        if rand_event(0.12):
            found = random.randint(5, 30)
            state.food += found
    # improve condition
    if state.condition == "poor":
        state.condition = "fair"
    elif state.condition == "fair":
        state.condition = "good"
    else:
        state.condition = "good"
    events = random_event(state)
    return consumed, events

def hunt(state: GameState):
    # Hunting consumes a day and yields food depending on success and party size
    state.day += 1
    consumed, req = state.consume_food(days=1)
    success_chance = 0.6 if state.pace != "fast" else 0.4
    if rand_event(success_chance):
        food_gained = random.randint(int(HUNT_FOOD_AVG*0.4), int(HUNT_FOOD_AVG*1.4))
        state.food += food_gained
        events = random_event(state)
        return True, food_gained, events
    else:
        # failure maybe causes injury
        if rand_event(0.05):
            victim = random.choice(state.party)
            if state.kits > 0 and rand_event(0.6):
                state.kits -= 1
                injury = False
            else:
                state.party.remove(victim); state.dead.append(victim)
                injury = True
                return False, 0, [f"{victim} was injured and died while hunting."]
        return False, 0, random_event(state)

def trade(state: GameState):
    # Simple trade: trade money for food or buy parts
    print("Te encuentras en un puesto de comercio. Opciones: buyfood, buywheel, buykit, sellfood")
    action = input("trade> ").strip().lower()
    if action == "buyfood":
        price_per_ration = 0.5 + random.random()*1.5
        amt = int(input("¿Cuántas raciones deseas comprar? "))
        cost = price_per_ration * amt
        if cost > state.money:
            print("No tienes dinero suficiente.")
            return []
        state.money -= cost
        state.food += amt
        print(f"Compraste {amt} raciones por ${cost:.2f}.")
        return []
    elif action == "buywheel":
        cost = 25 + random.randint(-5, 20)
        if state.money < cost:
            print("No tienes suficiente dinero.")
            return []
        state.money -= cost; state.wheels += 1
        print(f"Compraste una rueda de repuesto por ${cost}.")
        return []
    elif action == "buykit":
        cost = 15 + random.randint(-2, 10)
        if state.money < cost:
            print("No tienes suficiente dinero.")
            return []
        state.money -= cost; state.kits += 1
        print(f"Compraste un kit médico por ${cost}.")
        return []
    elif action == "sellfood":
        amt = int(input("¿Cuántas raciones quieres vender? "))
        if amt > state.food:
            print("No tienes tanta comida.")
            return []
        price = 0.3 + random.random()*0.7
        revenue = price * amt
        state.food -= amt; state.money += revenue
        print(f"Vendiste {amt} raciones por ${revenue:.2f}.")
        return []
    else:
        print("Acción de comercio no reconocida.")
        return []

def repair(state: GameState):
    # Use money to buy wheel or repair; small chance to restore condition
    if state.wheels > 0:
        print("Tienes ruedas de repuesto disponibles; no necesitas reparar ahora.")
    else:
        cost = 20 + random.randint(0, 40)
        if state.money >= cost:
            state.money -= cost
            state.wheels += 1
            print(f"Pagaste ${cost} por reparaciones y obtuviste 1 rueda de repuesto.")
        else:
            print("No tienes dinero suficiente para reparar.")

# ---------------------------
# UI: status display
# ---------------------------
def print_status(state: GameState):
    print("\n--- Estado de la caravana ---")
    print(f"Día: {state.day} | Millas recorridas: {state.miles_traveled} | Millas restantes: {state.distance_remaining}")
    print(f"Personas vivas: {state.party_count()} | Fallecidos: {len(state.dead)}")
    print("Miembros:", ", ".join(state.party))
    print(f"Comida: {state.food} raciones | Dinero: ${state.money:.2f} | Ruedas de repuesto: {state.wheels} | Kits médicos: {state.kits}")
    print(f"Bueyes: {state.oxen} | Ritmo: {state.pace} | Condición: {state.condition}")
    print("-----------------------------\n")

# ---------------------------
# Game loop and commands
# ---------------------------
def main_loop():
    state = GameState()
    print("Oregon Trail — Simulación en Python (simplificada). Escribe 'help' para ver comandos.")
    while not state.game_over:
        cmd = input("comando> ").strip().lower()
        if not cmd:
            continue
        if cmd in ("quit", "exit"):
            print("¿Deseas guardar antes de salir? (y/n)")
            if input("> ").strip().lower().startswith('y'):
                state.save()
            print("Saliendo. Gracias por jugar.")
            break

        if cmd == "help":
            print("""Comandos:
  travel        : avanzar (viajar un día según tu ritmo)
  rest [n]      : descansar n días (default 1)
  hunt          : cazar (un día, posibilidad de obtener comida)
  trade         : comerciar en un puesto
  repair        : reparar o comprar rueda si es necesario
  pace [slow|steady|fast] : ajustar ritmo de viaje
  status        : ver estado actual
  save          : guardar partida
  load          : cargar partida
  history       : ver acciones previas
  help          : mostrar esta ayuda
  quit / exit   : salir del juego
""")
            continue

        if cmd == "status":
            print_status(state)
            continue

        if cmd.startswith("save"):
            fname = SAVE_FILENAME
            parts = cmd.split()
            if len(parts) > 1:
                fname = parts[1]
            state.save(fname)
            continue

        if cmd.startswith("load"):
            fname = SAVE_FILENAME
            parts = cmd.split()
            if len(parts) > 1:
                fname = parts[1]
            state.load(fname)
            continue

        if cmd.startswith("pace"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Uso: pace slow|steady|fast")
            else:
                state.update_pace(parts[1])
            continue

        if cmd == "travel":
            miles, events = travel(state)
            print(f"Viajaste {miles} millas hoy.")
            for e in events:
                print("Evento:", e)
            state.history.append(f"travel {miles} miles (pace {state.pace})")
            # check win/lose
            if state.distance_remaining <= 0:
                state.win = True
                state.game_over = True
                print("¡Felicidades! Llegaste a Oregon.")
            if state.party_count() == 0:
                state.game_over = True
                print("Todos han muerto. Fin del juego.")
            continue

        if cmd.startswith("rest"):
            parts = cmd.split()
            days = 1
            if len(parts) > 1:
                try:
                    days = int(parts[1])
                except:
                    days = 1
            consumed, events = rest(state, days=days)
            print(f"Descansaste {days} días. Comida consumida: {consumed} raciones.")
            for e in events:
                print("Evento:", e)
            state.history.append(f"rest {days} days")
            continue

        if cmd == "hunt":
            ok, food_gained, events = hunt(state)
            if ok:
                print(f"Cazaste con éxito y obtuviste {food_gained} raciones de comida.")
            else:
                print("La caza falló.")
            for e in events:
                print("Evento:", e)
            state.history.append(f"hunt success={ok} food={food_gained}")
            continue

        if cmd == "trade":
            trade(state)
            state.history.append("trade")
            continue

        if cmd == "repair":
            repair(state)
            state.history.append("repair")
            continue

        if cmd == "history":
            for i, h in enumerate(state.history, start=1):
                print(f"{i}: {h}")
            continue

        # hidden debug: spawn event to add food
        if cmd.startswith("addfood"):
            parts = cmd.split()
            if len(parts) > 1:
                n = int(parts[1]); state.food += n; print(f"Added {n} food.")
                continue

        print("Comando no reconocido. Escribe 'help' para ver comandos.")

    # End loop summary
    print("\n=== Resumen final ===")
    print_status(state)
    if state.win:
        print("Has ganado: llegaste a Oregon. ¡Bien hecho!")
    elif state.party_count() == 0:
        print("Derrota: todos murieron en el camino.")
    else:
        print("Partida terminada.")

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Guardando partida automática...")
        gs = GameState(); gs.save()
        sys.exit(0)
