import tkinter as tk
from tkinter import messagebox
import random
import json
import time
import threading
from colorama import init, Fore
init(autoreset=True)

CONSEJOS = {
    "Temporales": ["Cuando llegues, avísame.", "Después que saliste, te llamé."],
    "Locativas": ["Vive donde nacieron sus abuelos.", "Se sentaron en donde había sombra."],
    "Modales": ["Hazlo como te dije.", "Cocinó según la receta."],
    "Combinadas": ["Te llamé cuando llegué donde tú estás.", "Volverá cuando lo decida, como siempre."]
}

EJEMPLOS = {
    "Temporales": ["Cuando amaneció, salimos a correr."],
    "Locativas": ["Estaba donde lo vi ayer."],
    "Modales": ["Actuó como si supiera todo."],
    "Combinadas": ["Cuando llovía, donde vivíamos, se inundaba todo."]
}

PROGRESO_FILE = "progreso_tk.json"

class PracticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Consejos y Ejemplos")
        self.nivel = 1
        self.tiempo_limite = 60
        self.timer_running = False

        self.progreso = self.cargar_progreso()

        self.lbl_categoria = tk.Label(root, text="Selecciona una categoría")
        self.lbl_categoria.pack()

        self.lista = tk.Listbox(root)
        for cat in CONSEJOS:
            self.lista.insert(tk.END, cat)
        self.lista.pack()

        self.btn_iniciar = tk.Button(root, text="Iniciar", command=self.seleccionar_categoria)
        self.btn_iniciar.pack()

        self.lbl_ejemplo = tk.Label(root, text="", fg="blue")
        self.lbl_ejemplo.pack()

        self.entrada = tk.Entry(root, width=60)
        self.entrada.pack()

        self.btn_validar = tk.Button(root, text="Validar", command=self.validar_respuesta)
        self.btn_validar.pack()

        self.lbl_tiempo = tk.Label(root, text="Tiempo: --")
        self.lbl_tiempo.pack()

        self.cronometro_thread = None

    def cargar_progreso(self):
        try:
            with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {cat: [] for cat in CONSEJOS}

    def guardar_progreso(self):
        with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
            json.dump(self.progreso, f, ensure_ascii=False, indent=4)

    def seleccionar_categoria(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("¡Atención!", "Selecciona una categoría.")
            return
        self.categoria = self.lista.get(seleccion)
        self.nivel += 1
        self.tiempo_limite = max(30, 90 - self.nivel * 5)
        self.nuevo_ejercicio()

    def nuevo_ejercicio(self):
        disponibles = [e for e in CONSEJOS[self.categoria] if e not in self.progreso[self.categoria]]
        if not disponibles:
            self.lbl_ejemplo.config(text="Categoría completada.")
            return
        self.ejemplo = random.choice(disponibles)
        self.lbl_ejemplo.config(text=f"Escribe: {self.ejemplo}")
        self.entrada.delete(0, tk.END)
        self.iniciar_cronometro()

    def iniciar_cronometro(self):
        self.timer_running = True
        self.tiempo_restante = self.tiempo_limite
        if self.cronometro_thread is None or not self.cronometro_thread.is_alive():
            self.cronometro_thread = threading.Thread(target=self.actualizar_tiempo)
            self.cronometro_thread.start()

    def actualizar_tiempo(self):
        while self.timer_running and self.tiempo_restante > 0:
            self.lbl_tiempo.config(text=f"Tiempo: {self.tiempo_restante}s")
            time.sleep(1)
            self.tiempo_restante -= 1
        if self.tiempo_restante == 0:
            self.lbl_tiempo.config(text="⏰ ¡Tiempo agotado!")
            messagebox.showinfo("Tiempo", "Se acabó el tiempo.")
            self.timer_running = False

    def validar_respuesta(self):
        respuesta = self.entrada.get().strip()
        if respuesta.lower() == self.ejemplo.lower():
            self.progreso[self.categoria].append(self.ejemplo)
            self.guardar_progreso()
            nuevo = tk.simpledialog.askstring("Nuevo ejemplo", "Escribe un ejemplo similar:")
            if nuevo:
                self.progreso[self.categoria].append(nuevo)
                self.guardar_progreso()
            messagebox.showinfo("Correcto", Fore.GREEN + "¡Bien hecho!")
        else:
            messagebox.showerror("Incorrecto", Fore.RED + "Revisa tu respuesta.")
        self.timer_running = False
        self.nuevo_ejercicio()

if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaApp(root)
    root.mainloop()
