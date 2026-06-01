import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import json
import sys
import os

# --- 1. CONFIGURACIÓN Y LÓGICA DEL JUEGO (GameState) ---

MILES_TOTALES = 2000
CONSUMO_POR_DIA = 1.5  # Comida por persona por día

class GameState:
    """Clase para gestionar el estado de la caravana y la lógica."""
    def __init__(self, party_name="Pioneros"):
        self.party_name = party_name
        self.distance = 0
        self.days = 0
        self.money = 500  
        self.food = 500   
        self.oxen = 2     
        self.members = 5  
        self.health = 100 
        self.wheels = 4   # Ruedas de repuesto
        self.kits = 2     # Kits médicos
        self.status = "Viajando"
        self.log = []

    def is_game_over(self):
        """Verifica las condiciones de fin de juego."""
        if self.distance >= MILES_TOTALES:
            self.status = "¡Victoria! Llegaste a Oregon."
            return True
        if self.members <= 0 or self.health <= 0 or self.oxen <= 0 or self.wheels <= 0:
            self.status = "Derrota: La caravana no puede continuar."
            return True
        return False
        
    def add_log(self, entry):
        """Añade una entrada al registro de eventos."""
        self.log.append(f"Día {self.days}: {entry}")

    # Método para serializar el estado para guardado en JSON
    def to_dict(self):
        return self.__dict__

    # Método para cargar el estado desde un diccionario
    def from_dict(self, data):
        self.__dict__.update(data)

# --- Lógica de Eventos y Juego (Simplificada para la GUI) ---

def handle_random_event(state):
    """Genera y maneja un evento aleatorio con impacto en el estado."""
    
    # 20% de probabilidad de un evento adverso
    if random.random() < 0.2:
        
        event_roll = random.randint(1, 100)
        
        if event_roll <= 30: # 30% de probabilidad de enfermedad
            state.health = max(0, state.health - random.randint(10, 20))
            state.add_log("Enfermedad grave: La salud del grupo ha bajado.")
            return "El grupo se enfermó."
            
        elif event_roll <= 60: # 30% de probabilidad de rotura
            state.wheels -= 1
            state.add_log("¡Rueda rota! Tienes que reparar (Repair).")
            return "Una rueda se rompió."

        elif event_roll <= 80: # 20% de probabilidad de pérdida de Buey
            state.oxen -= 1
            state.add_log("¡Pérdida de buey! El carro va más lento.")
            return "Pérdida de un buey."
            
        else: # 20% Bandidos
            robbed = random.randint(10, 50)
            state.money = max(0, state.money - robbed)
            state.add_log(f"¡Bandidos! Perdiste ${robbed}.")
            return "Ataque de bandidos."
            
    return None # No hubo evento

# --- 2. LA INTERFAZ GRÁFICA (Tkinter) ---

class OregonTrailApp:
    def __init__(self, master):
        self.master = master
        master.title("Python Trail: Tkinter Edition")

        self.state = GameState("Pioneros")
        
        # Widgets para etiquetas dinámicas
        self.status_labels = {}
        
        self.create_widgets()
        self.update_status_display()
        self.log_message("Comienza tu viaje a Oregon. Compra provisiones y ¡Viaja!")
        
    # --- Estructura y Creación de Widgets ---
    
    def create_widgets(self):
        # Frame principal dividido en LADO (Estado) y DERECHA (Controles/Log)
        
        # 1. Panel de Estado (Izquierda)
        status_frame = tk.LabelFrame(self.master, text="ESTADO DE LA CARAVANA", padx=10, pady=10)
        status_frame.pack(side=tk.LEFT, fill="y", padx=10, pady=10)
        
        # Inicializar Etiquetas de Estado
        items = ["Nombre", "Día", "Millas", "Salud", "Dinero ($)", "Comida (lbs)", 
                 "Bueyes", "Ruedas Repuesto", "Kits Médicos", "Estado"]
                 
        for i, item in enumerate(items):
            tk.Label(status_frame, text=f"{item}:").grid(row=i, column=0, sticky="w", pady=2)
            label = tk.Label(status_frame, text="N/A", width=15, anchor="w")
            label.grid(row=i, column=1, sticky="w", pady=2)
            self.status_labels[item] = label
            
        # 2. Barra de Progreso
        tk.Label(status_frame, text="\nProgreso hacia Oregon:").grid(row=len(items), column=0, columnspan=2, pady=(10, 0))
        self.progress_bar = tk.Label(status_frame, text="", bg="green", fg="white", anchor="w")
        self.progress_bar.grid(row=len(items)+1, column=0, columnspan=2, sticky="ew")

        # 3. Panel de Control y Log (Derecha)
        control_frame = tk.Frame(self.master, padx=10, pady=10)
        control_frame.pack(side=tk.RIGHT, fill="both", expand=True)

        # Botones de Acción
        tk.Label(control_frame, text="ACCIONES").pack(pady=5)
        button_frame = tk.Frame(control_frame)
        button_frame.pack(pady=10)
        
        actions = [
            ("Viajar (1 Día)", self.travel), 
            ("Descansar (1 Día)", self.rest), 
            ("Cazar", self.hunt), 
            ("Comerciar", self.trade),
            ("Reparar", self.repair), 
            ("Guardar", self.save_game), 
            ("Cargar", self.load_game), 
            ("Salir", master.quit)
        ]
        
        for text, command in actions:
            tk.Button(button_frame, text=text, command=command, width=15).pack(side=tk.LEFT, padx=5, pady=5)
            
        # 4. Registro de Eventos (Log)
        tk.Label(control_frame, text="REGISTRO DE EVENTOS").pack(pady=5)
        self.log_area = scrolledtext.ScrolledText(control_frame, height=15, width=60)
        self.log_area.pack(fill="both", expand=True)
        self.log_area.config(state=tk.DISABLED) # Solo lectura
        
    # --- Lógica de Actualización y Mensajes ---
    
    def update_status_display(self):
        """Actualiza todas las etiquetas de estado con los valores de self.state."""
        
        # Mapeo de valores
        data = {
            "Nombre": self.state.party_name,
            "Día": self.state.days,
            "Millas": f"{self.state.distance} / {MILES_TOTALES}",
            "Salud": f"{self.state.health}%",
            "Dinero ($)": f"${self.state.money}",
            "Comida (lbs)": f"{self.state.food:.1f}",
            "Bueyes": self.state.oxen,
            "Ruedas Repuesto": self.state.wheels,
            "Kits Médicos": self.state.kits,
            "Estado": self.state.status
        }
        
        for key, label in self.status_labels.items():
            label.config(text=str(data.get(key, 'N/A')))
            
        # Actualizar Barra de Progreso
        progress_ratio = self.state.distance / MILES_TOTALES
        progress_width = int(500 * progress_ratio) # 500 es un valor arbitrario de ancho
        self.progress_bar.config(width=progress_width, text=f"{progress_ratio*100:.1f}% Completado")
        
        self.check_game_over()
        
    def log_message(self, message):
        """Añade un mensaje al registro de eventos."""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, f"Día {self.state.days}: {message}\n")
        self.log_area.see(tk.END) # Scroll hasta el final
        self.log_area.config(state=tk.DISABLED)
        
    def check_game_over(self):
        """Revisa si el juego ha terminado y muestra el resultado."""
        if self.state.is_game_over():
            messagebox.showinfo("Fin del Juego", self.state.status)
            for widget in self.master.winfo_children():
                widget.destroy() # Destruye todos los widgets para finalizar

    # --- 3. Lógica de Botones y Acciones ---
    
    def travel(self):
        """Simula un día de viaje."""
        if self.state.is_game_over(): return

        self.state.days += 1
        self.state.status = "Viajando"
        
        # 1. Consumo y Salud
        food_needed = self.state.members * CONSUMO_POR_DIA
        if self.state.food >= food_needed:
            self.state.food -= food_needed
            self.log_message("Viaje de un día. Consumo normal de comida.")
        else:
            self.state.food = 0
            self.state.health = max(0, self.state.health - random.randint(5, 10))
            self.log_message("¡HAMBRE! No hay comida suficiente. La salud bajó.")
        
        # 2. Movimiento
        travel_speed = 15 * self.state.oxen / 2 * (self.state.health / 100)
        miles_traveled = random.randint(int(travel_speed * 0.8), int(travel_speed * 1.2))
        self.state.distance += miles_traveled
        self.log_message(f"Avanzaste {miles_traveled} millas.")
        
        # 3. Evento Aleatorio
        event_message = handle_random_event(self.state)
        if event_message:
            messagebox.showwarning("¡Evento!", event_message)
            self.log_message(f"EVENTO ADVERSO: {event_message}")

        self.update_status_display()

    def rest(self):
        """Simula un día de descanso."""
        self.state.days += 1
        self.state.status = "Descansando"
        self.state.health = min(100, self.state.health + 10) # Recupera salud
        self.state.food = max(0, self.state.food - self.state.members * CONSUMO_POR_DIA) # Consume comida
        self.log_message("Día de descanso. Salud recuperada (10 puntos).")
        self.update_status_display()
        
    def hunt(self):
        """Simula una sesión de caza."""
        self.state.days += 1
        self.state.status = "Cazando"
        self.state.food = max(0, self.state.food - self.state.members * CONSUMO_POR_DIA) # Consume comida del día
        
        if random.random() < 0.6:
            food_gained = random.randint(30, 70)
            self.state.food += food_gained
            self.log_message(f"Caza exitosa! Ganaste {food_gained:.1f} lbs de comida.")
        else:
            self.log_message("Caza fallida. Perdiste tiempo y un poco de comida.")
        self.update_status_display()
        
    def repair(self):
        """Intenta reparar el carro."""
        if self.state.wheels < 4:
            if self.state.wheels < 4 and self.state.money >= 50:
                self.state.wheels += 1
                self.state.money -= 50
                self.log_message("Rueda reparada (compraste una pieza de repuesto por $50).")
            elif self.state.wheels < 4 and self.state.money < 50:
                self.log_message("No tienes dinero para comprar una rueda de repuesto ($50).")
        elif self.state.kits > 0:
            self.state.kits -= 1
            self.state.health = min(100, self.state.health + 20)
            self.log_message("Usaste un kit médico. La salud del grupo mejoró.")
        else:
            self.log_message("El carro está bien o no tienes repuestos/kits para usar.")
        self.update_status_display()
        
    def trade(self):
        """Abre un diálogo simple de comercio."""
        trade_amount = simpledialog.askinteger("Comercio", "¿Cuánto dinero quieres gastar en comida (1 lb = $1)?", 
                                                parent=self.master, minvalue=0, maxvalue=self.state.money)
        if trade_amount is not None and trade_amount > 0:
            self.state.money -= trade_amount
            self.state.food += trade_amount
            self.log_message(f"Comercio exitoso: Gastaste ${trade_amount} y ganaste {trade_amount} lbs de comida.")
        else:
            self.log_message("Comercio cancelado.")
        self.update_status_display()
        
    # --- 4. Persistencia (Guardar/Cargar) ---
    
    def save_game(self):
        """Guarda el estado del juego en un archivo JSON."""
        try:
            with open("oregon_trail.save", "w") as f:
                json.dump(self.state.to_dict(), f, indent=4)
            self.log_message("¡Juego guardado exitosamente!")
        except Exception as e:
            messagebox.showerror("Error de Guardado", f"No se pudo guardar el juego: {e}")

    def load_game(self):
        """Carga el estado del juego desde un archivo JSON."""
        if not os.path.exists("oregon_trail.save"):
            messagebox.showinfo("Cargar Juego", "No se encontró ningún archivo de guardado.")
            return

        try:
            with open("oregon_trail.save", "r") as f:
                data = json.load(f)
            
            # Crear una nueva instancia y actualizar desde los datos
            new_state = GameState()
            new_state.from_dict(data)
            self.state = new_state
            
            self.update_status_display()
            self.log_area.config(state=tk.NORMAL)
            self.log_area.delete(1.0, tk.END) # Limpiar log
            self.log_message("¡Juego cargado exitosamente!")
            
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudo cargar el juego: {e}")
            
# --- 5. Ejecución Principal ---

if __name__ == "__main__":
    root = tk.Tk()
    app = OregonTrailApp(root)
    root.mainloop()
