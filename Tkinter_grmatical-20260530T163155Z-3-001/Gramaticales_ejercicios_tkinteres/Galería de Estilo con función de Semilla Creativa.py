import tkinter as tk
import json
import os
from tkinter import messagebox

class GaleriaEstiloFrame(tk.Frame):
    def __init__(self, master, controller=None):
        super().__init__(master, bg="#f1f8f6")
        self.controller = controller

        tk.Label(self, text="🌟 Galería de Estilo", font=("Georgia", 20), bg="#f1f8f6").pack(pady=20)

        self.marco = tk.Canvas(self, bg="#f1f8f6")
        self.scroll = tk.Scrollbar(self, orient="vertical", command=self.marco.yview)
        self.frame_tarjetas = tk.Frame(self.marco, bg="#f1f8f6")
        self.frame_tarjetas.bind("<Configure>", lambda e: self.marco.configure(scrollregion=self.marco.bbox("all")))
        self.marco.create_window((0, 0), window=self.frame_tarjetas, anchor="nw")
        self.marco.configure(yscrollcommand=self.scroll.set)
        self.marco.pack(side="left", fill="both", expand=True)
        self.scroll.pack(side="right", fill="y")

        self.cargar_tarjetas()

        tk.Button(self, text="← Volver", command=lambda: controller.mostrar_capitulo("MenuPrincipal") if controller else None).pack(pady=10)

    def cargar_tarjetas(self):
        archivo = "galeria_estilo.json"
        if not os.path.exists(archivo):
            tk.Label(self.frame_tarjetas, text="Aún no hay fragmentos destacados.", bg="#f1f8f6", font=("Georgia", 12)).pack(pady=10)
            return

        with open(archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
            except:
                tk.Label(self.frame_tarjetas, text="Error al cargar la galería.", bg="#f1f8f6").pack()
                return

        for entrada in datos:
            marco = tk.Frame(self.frame_tarjetas, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
            tk.Label(marco, text=f"📝 {entrada['tipo']}", font=("Georgia", 12, "bold"), bg="#ffffff").pack(anchor="w")
            cuerpo = tk.Text(marco, height=5, wrap="word", font=("Georgia", 11), bg="#ffffff", bd=0)
            cuerpo.insert("1.0", entrada["contenido"])
            cuerpo.configure(state="disabled")
            cuerpo.pack(pady=5)

            botones = tk.Frame(marco, bg="#ffffff")
            tk.Button(botones, text="📋 Copiar", command=lambda t=entrada["contenido"]: self.copiar_fragmento(t)).pack(side="left", padx=5)
            tk.Button(botones, text="🌱 Usar como semilla", command=lambda t=entrada["contenido"]: self.usar_como_semilla(t)).pack(side="left", padx=5)
            botones.pack()

            marco.pack(padx=20, pady=10, fill="x")

    def copiar_fragmento(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        messagebox.showinfo("✨ Copiado", "El fragmento fue copiado al portapapeles.")

    def usar_como_semilla(self, texto):
        if hasattr(self.controller, "precargar_redaccion"):
            self.controller.precargar_redaccion(texto)
            self.controller.mostrar_capitulo("RedaccionTiposTextoFrame")
        else:
            messagebox.showwarning("¡Ups!", "No se pudo enlazar con la pantalla de redacción.")
