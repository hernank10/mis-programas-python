# estudio_aumentativos.py
import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Datos iniciales para ejemplos.json
DATOS_INICIALES = [
    {"base": "gigante", "modificado": "gigantazo", "tipo": "aumentativo"},
    {"base": "señor", "modificado": "señorón", "tipo": "aumentativo"},
    {"base": "grande", "modificado": "grandote", "tipo": "aumentativo"},
    {"base": "libro", "modificado": "librote", "tipo": "aumentativo"},
    {"base": "pobre", "modificado": "pobretón", "tipo": "aumentativo"},
    {"base": "rico", "modificado": "ricacho", "tipo": "aumentativo"},
    {"base": "vivo", "modificado": "vivaracho", "tipo": "aumentativo"},
    {"base": "nube", "modificado": "nubarrón", "tipo": "aumentativo"},
    {"base": "bobo", "modificado": "bobarrón", "tipo": "aumentativo"},
    {"base": "mozo", "modificado": "mocetón", "tipo": "aumentativo"},
    {"base": "flor", "modificado": "florecilla", "tipo": "diminutivo"},
    {"base": "mano", "modificado": "manecita", "tipo": "diminutivo"},
    {"base": "pez", "modificado": "pececillo", "tipo": "diminutivo"},
    {"base": "ave", "modificado": "avecita", "tipo": "diminutivo"},
    {"base": "autor", "modificado": "autorzuelo", "tipo": "diminutivo"},
    # ... (agregar los 35 ejemplos restantes aquí)
]

class AumentativosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio de Aumentativos y Diminutivos")
        self.root.geometry("800x600")
        self.inicializar_archivos()
        self.cargar_datos()
        self.configurar_interfaz()
        
    def inicializar_archivos(self):
        # Crear ejemplos.json si no existe
        if not os.path.exists("ejemplos.json"):
            with open("ejemplos.json", "w", encoding="utf-8") as f:
                json.dump(DATOS_INICIALES, f, ensure_ascii=False, indent=2)
        
        # Crear custom_ejemplos.json si no existe
        if not os.path.exists("custom_ejemplos.json"):
            with open("custom_ejemplos.json", "w", encoding="utf-8") as f:
                json.dump([], f)
                
    def cargar_datos(self):
        with open("ejemplos.json", "r", encoding="utf-8") as f:
            self.ejemplos = json.load(f)
        
        with open("custom_ejemplos.json", "r", encoding="utf-8") as f:
            self.custom_ejemplos = json.load(f)
    
    def configurar_interfaz(self):
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#F0F0F0")
        self.style.configure("TButton", font=("Arial", 10), padding=5)
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.crear_menu_principal()
    
    def crear_menu_principal(self):
        self.limpiar_frame()
        
        ttk.Label(self.main_frame, 
                 text="Estudio de Aumentativos y Diminutivos",
                 font=("Arial", 16, "bold")).pack(pady=20)
        
        botones = [
            ("Práctica con Ejemplos", self.practica_ejemplos),
            ("Diapositiva Conceptual", self.mostrar_conceptos),
            ("Cuestionario Interactivo", self.cuestionario),
            ("Gestionar Ejemplos", self.gestion_ejemplos),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            ttk.Button(self.main_frame, 
                      text=texto, 
                      command=comando).pack(pady=5, fill=tk.X, padx=50)
    
    # ... (mantener el resto de métodos de la clase anterior)

if __name__ == "__main__":
    root = tk.Tk()
    app = AumentativosApp(root)
    root.mainloop()
