import tkinter as tk
from tkinter import ttk, messagebox
import random

class PrefijosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Practicador de Prefijos")
        self.root.geometry("600x400")
        self.setup_ui()
        self.inicializar_juego()
        
    def setup_ui(self):
        # Configuración de estilo
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 10))
        
        # Marco principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Encabezado
        self.header = ttk.Label(main_frame, text="✍️ ESCRIBE LA PALABRA CORRECTA", 
                              font=("Arial", 14, "bold"), foreground="#2c3e50")
        self.header.pack(pady=10)
        
        # Panel de información
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=5)
        
        self.lbl_puntaje = ttk.Label(info_frame, text="Puntaje: 0")
        self.lbl_puntaje.pack(side=tk.LEFT)
        
        self.lbl_nivel = ttk.Label(info_frame, text="Nivel: 1")
        self.lbl_nivel.pack(side=tk.RIGHT)
        
        # Palabra oculta
        self.lbl_palabra = ttk.Label(main_frame, text="", 
                                    font=("Courier New", 24, "bold"),
                                    foreground="#34495e")
        self.lbl_palabra.pack(pady=20)
        
        # Entrada de usuario
        self.entrada = ttk.Entry(main_frame, font=("Arial", 14), width=25)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.verificar_respuesta)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=15)
        
        self.btn_verificar = ttk.Button(btn_frame, text="Verificar", 
                                      command=self.verificar_respuesta)
        self.btn_verificar.pack(side=tk.LEFT, padx=5)
        
        self.btn_pista = ttk.Button(btn_frame, text="Pista", 
                                  command=self.mostrar_pista)
        self.btn_pista.pack(side=tk.LEFT, padx=5)
        
        # Historial
        self.historial = tk.Listbox(main_frame, height=5, font=("Arial", 10))
        self.historial.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Variables de juego
        self.palabras = [
            "polisílabo", "multicolor", "pluricelular", "monocromo", 
            "bicéfalo", "tricolor", "pluriempleado", "multiforme"
        ]
        self.porcentaje_ocultar = 30
        self.puntaje = 0
        self.racha = 0
        self.palabra_actual = ""
        
    def inicializar_juego(self):
        self.generar_nueva_palabra()
        self.actualizar_interfaz()
        
    def generar_nueva_palabra(self):
        self.palabra_actual = random.choice(self.palabras)
        self.palabra_oculta = self.ocultar_letras(self.palabra_actual)
        self.intentos = 0
        self.pista_mostrada = False
        
    def ocultar_letras(self, palabra):
        letras = list(palabra)
        indices = random.sample(
            range(len(letras)), 
            max(1, int(len(letras) * self.porcentaje_ocultar / 100))
        )
        return "".join(["_" if i in indices else c for i, c in enumerate(letras)])
    
    def actualizar_interfaz(self):
        self.lbl_palabra.config(text=self.palabra_oculta)
        self.lbl_puntaje.config(text=f"Puntaje: {self.puntaje}")
        self.lbl_nivel.config(text=f"Nivel: {self.porcentaje_ocultar//10}")
        self.entrada.delete(0, tk.END)
        
    def verificar_respuesta(self, event=None):
        respuesta = self.entrada.get().strip().lower()
        if respuesta == self.palabra_actual.lower():
            self.puntaje += 10
            self.racha += 1
            self.historial.insert(0, f"✅ {self.palabra_actual}")
            self.actualizar_dificultad()
            self.generar_nueva_palabra()
        else:
            self.intentos += 1
            self.racha = 0
            self.historial.insert(0, f"❌ Intento {self.intentos}: {respuesta}")
            if self.intentos >= 2:
                self.historial.insert(0, f"💡 La respuesta era: {self.palabra_actual}")
                self.generar_nueva_palabra()
        
        self.actualizar_interfaz()
        
    def actualizar_dificultad(self):
        if self.racha % 3 == 0 and self.porcentaje_ocultar < 70:
            self.porcentaje_ocultar += 10
            messagebox.showinfo(
                "Nivel superior!", 
                f"¡Nuevo nivel! Letras ocultas: {self.porcentaje_ocultar}%"
            )
        
    def mostrar_pista(self):
        if not self.pista_mostrada:
            pista = f"Prefijo: {self.palabra_actual[:3].upper()}... ({len(self.palabra_actual)} letras)"
            messagebox.showinfo("Pista", pista)
            self.puntaje -= 5
            self.pista_mostrada = True
            self.actualizar_interfaz()

if __name__ == "__main__":
    root = tk.Tk()
    app = PrefijosGUI(root)
    root.mainloop()
