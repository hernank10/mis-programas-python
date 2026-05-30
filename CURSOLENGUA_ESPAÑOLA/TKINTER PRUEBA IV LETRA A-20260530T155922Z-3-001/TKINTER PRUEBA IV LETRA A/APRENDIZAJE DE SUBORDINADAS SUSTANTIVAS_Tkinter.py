import sys
import random
import json
import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------- Módulo compartido -------------------------
EJEMPLOS_BASE = {
    "Sujeto": [
        "Que llueva es una bendición para los cultivos.",
        "Que estudies medicina sorprende a todos."
    ],
    "Complemento Directo": [
        "Quiero que me escuches.",
        "Ella cree que el examen será fácil."
    ],
    "Complemento Indirecto": [
        "Le dije que no llegaría tarde (a Juan).",
        "Le pregunté si necesitaba ayuda (a mi hermana)."
    ],
    "Complemento Circunstancial": [
        "Llegamos antes de que empezara la lluvia.",
        "Saldré después de que termines de comer."
    ],
    "Complemento Preposicional": [
        "La idea de que viajemos juntos me emociona.",
        "Estoy seguro de que aprobarás."
    ]
}

def cargar_ejemplos_usuario():
    try:
        with open("user_ejemplos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {k: [] for k in EJEMPLOS_BASE.keys()}

def guardar_ejemplos_usuario(user_ejemplos):
    with open("user_ejemplos.json", "w") as f:
        json.dump(user_ejemplos, f, indent=2)

# ------------------------- Versión CLI -------------------------
def cli_menu():
    user_ejemplos = cargar_ejemplos_usuario()
    
    while True:
        print("\n" + "="*50)
        print("MODO CONSOLA - Subordinadas Sustantivas")
        print("="*50)
        print("1. Practicar")
        print("2. Crear ejemplo")
        print("3. Ver ejemplos")
        print("4. Cambiar a GUI")
        print("5. Salir")
        
        opcion = input("Selección: ")
        
        if opcion == "1":
            cli_practicar(user_ejemplos)
        elif opcion == "2":
            cli_crear_ejemplo(user_ejemplos)
        elif opcion == "3":
            cli_ver_ejemplos(user_ejemplos)
        elif opcion == "4":
            gui_iniciar()
        elif opcion == "5":
            sys.exit()
        else:
            print("Opción inválida")

def cli_practicar(user_ejemplos):
    categorias = list(EJEMPLOS_BASE.keys())
    ejemplos_combinados = {**EJEMPLOS_BASE, **user_ejemplos}
    
    while True:
        categoria = random.choice(categorias)
        if not ejemplos_combinados[categoria]:
            continue
            
        ejemplo = random.choice(ejemplos_combinados[categoria])
        
        print("\n" + "-"*50)
        print(f"ORACIÓN: {ejemplo}")
        print("1. Sujeto | 2. Directo | 3. Indirecto | 4. Circunstancial | 5. Preposicional")
        print("n. Crear similar | x. Volver")
        
        respuesta = input("Tu respuesta: ").lower()
        
        if respuesta == "x":
            break
        elif respuesta == "n":
            cli_crear_similar(categoria, user_ejemplos)
        elif respuesta in {"1","2","3","4","5"}:
            cli_verificar_respuesta(int(respuesta), categoria)
        else:
            print("Opción inválida")

# ... (Funciones CLI restantes similares a versiones anteriores)

# ------------------------- Versión GUI -------------------------
class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Subordinadas Sustantivas - GUI")
        self.geometry("800x600")
        self.user_ejemplos = cargar_ejemplos_usuario()
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # ... (Implementación GUI similar a versión anterior)
        
    def gui_volver_menu(self):
        self.destroy()
        cli_menu()

# ------------------------- Menú inicial -------------------------
def menu_inicial():
    print("\n" + "="*50)
    print("")
    print("="*50)
    print("1. Modo Consola (CLI)")
    print("2. Modo Gráfico (GUI)")
    print("3. Salir")
    
    while True:
        opcion = input("Seleccione modo (1-3): ")
        if opcion == "1":
            cli_menu()
        elif opcion == "2":
            gui_iniciar()
        elif opcion == "3":
            sys.exit()
        else:
            print("Opción inválida")

def gui_iniciar():
    app = GUIApp()
    app.mainloop()

if __name__ == "__main__":
    menu_inicial()
