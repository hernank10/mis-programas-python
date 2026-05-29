import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from collections import deque

class GrammarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Concordancias Bilingüe")
        self.geometry("800x600")
        self.configure(bg="#F0F0F0")
        
        # Configuración inicial
        self.ejercicios_file = "ejercicios_usuario.json"
        self.max_ejemplos = 100
        self.puntuacion = 0
        self.ejemplos_usuario = deque(maxlen=self.max_ejemplos)
        self.ejercicios_fallados = []
        
        # Cargar datos
        self.cargar_ejemplos()
        
        # Crear interfaz
        self.crear_menu_principal()
        self.crear_widgets_teoria()
        self.crear_widgets_ejercicios()
        self.crear_widgets_redaccion()
        self.crear_barra_estado()
        
        self.mostrar_panel("inicio")

    def crear_menu_principal(self):
        menu_frame = ttk.Frame(self)
        
        estilo = ttk.Style()
        estilo.configure("TButton", padding=6, font=('Arial', 10))
        
        btn_config = {
            "Teoría": lambda: self.mostrar_panel("teoria"),
            "Ejercicios ES": lambda: self.iniciar_ejercicio("completacion"),
            "Práctica EN-ES": lambda: self.iniciar_ejercicio("bilingue"),
            "Redacción": lambda: self.mostrar_panel("redaccion"),
            "Mis Ejemplos": self.mostrar_mis_ejemplos,
            "Repetir Fallados": self.repetir_ejercicios_fallados,
            "Salir": self.destroy
        }
        
        row = 0
        for texto, comando in btn_config.items():
            ttk.Button(menu_frame, text=texto, command=comando).grid(
                row=row, column=0, pady=5, sticky="ew")
            row += 1
        
        menu_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

    def crear_widgets_teoria(self):
        self.teoria_frame = ttk.Frame(self)
        
        texto_teoria = tk.Text(self.teoria_frame, wrap=tk.WORD, width=60, height=20,
                              font=('Arial', 11), bg="white", padx=10, pady=10)
        scroll = ttk.Scrollbar(self.teoria_frame, command=texto_teoria.yview)
        texto_teoria.configure(yscrollcommand=scroll.set)
        
        contenido = (
            "CONCORDANCIAS PARTITIVAS\n\n"
            "1. Definición:\n"
            "   Estructuras que expresan relación parte-todo usando 'de + grupo'.\n"
            "   Ejemplo: 'Ser de los que...', 'Uno de los que...'\n\n"
            "2. Concordancia:\n"
            "   - Normativa: plural (concordancia sintáctica)\n"
            "   - Aceptada: singular (atracción semántica)\n\n"
            "3. Diferencias EN-ES:\n"
            "   Inglés: Concordancia estricta con el sujeto principal\n"
            "   Español: Permite doble concordancia\n"
        )
        
        texto_teoria.insert(tk.END, contenido)
        texto_teoria.config(state=tk.DISABLED)
        
        texto_teoria.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")
        
        ttk.Button(self.teoria_frame, text="Regresar", 
                  command=lambda: self.mostrar_panel("inicio")).grid(pady=10)
        
        self.teoria_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    def crear_widgets_ejercicios(self):
        self.ejercicios_frame = ttk.Frame(self)
        
        self.pregunta_label = ttk.Label(
            self.ejercicios_frame, 
            font=('Arial', 12, 'bold'), 
            wraplength=600
        )
        self.pregunta_label.pack(pady=20)
        
        self.opciones_frame = ttk.Frame(self.ejercicios_frame)
        self.opciones_frame.pack()
        
        self.feedback_label = ttk.Label(
            self.ejercicios_frame, 
            font=('Arial', 11), 
            wraplength=600
        )
        self.feedback_label.pack(pady=15)
        
        ttk.Button(self.ejercicios_frame, text="Siguiente", 
                  command=self.siguiente_pregunta).pack(pady=10)
        
        ttk.Button(self.ejercicios_frame, text="Regresar", 
                  command=lambda: self.mostrar_panel("inicio")).pack()

    def crear_widgets_redaccion(self):
        self.redaccion_frame = ttk.Frame(self)
        
        tk.Label(self.redaccion_frame, 
                text="Escribe oraciones con construcciones partitivas:",
                font=('Arial', 12)).pack(pady=10)
        
        self.entrada_redaccion = tk.Text(
            self.redaccion_frame, 
            height=5, 
            width=60,
            font=('Arial', 11)
        )
        self.entrada_redaccion.pack(pady=10)
        
        ttk.Button(self.redaccion_frame, text="Guardar Ejemplo", 
                  command=self.guardar_ejemplo).pack()
        
        self.lista_ejemplos = tk.Listbox(
            self.redaccion_frame, 
            width=70, 
            height=8,
            font=('Arial', 10)
        )
        self.lista_ejemplos.pack(pady=10)
        
        ttk.Button(self.redaccion_frame, text="Regresar", 
                  command=lambda: self.mostrar_panel("inicio")).pack()

    def crear_barra_estado(self):
        self.barra_estado = ttk.Label(
            self, 
            text=f"Puntuación: {self.puntuacion} | Ejemplos guardados: {len(self.ejemplos_usuario)}",
            relief=tk.SUNKEN
        )
        self.barra_estado.grid(row=1, column=0, columnspan=2, sticky="ew")

    def cargar_ejemplos(self):
        if os.path.exists(self.ejercicios_file):
            with open(self.ejercicios_file, 'r', encoding='utf-8') as f:
                self.ejemplos_usuario = deque(json.load(f), maxlen=self.max_ejemplos)

    def guardar_ejemplo(self):
        texto = self.entrada_redaccion.get("1.0", tk.END).strip()
        if texto:
            self.ejemplos_usuario.append(texto)
            with open(self.ejercicios_file, 'w', encoding='utf-8') as f:
                json.dump(list(self.ejemplos_usuario), f, ensure_ascii=False)
            self.actualizar_barra_estado()
            self.lista_ejemplos.insert(tk.END, texto)
            self.entrada_redaccion.delete("1.0", tk.END)
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        else:
            messagebox.showwarning("Advertencia", "Escribe un ejemplo antes de guardar")

    def mostrar_panel(self, panel):
        frames = [self.teoria_frame, self.ejercicios_frame, self.redaccion_frame]
        for frame in frames:
            frame.grid_forget()
        
        if panel == "teoria":
            self.teoria_frame.grid(row=0, column=1, sticky="nsew")
        elif panel == "ejercicios":
            self.ejercicios_frame.grid(row=0, column=1, sticky="nsew")
        elif panel == "redaccion":
            self.redaccion_frame.grid(row=0, column=1, sticky="nsew")
            self.actualizar_lista_ejemplos()
        else:
            pass

    def iniciar_ejercicio(self, tipo):
        self.current_ejercicio = 0
        self.tipo_ejercicio = tipo
        self.mostrar_pregunta()
        self.mostrar_panel("ejercicios")

    def mostrar_pregunta(self):
        for widget in self.opciones_frame.winfo_children():
            widget.destroy()
        
        ejercicio = ejercicios_bilingue[self.current_ejercicio]
        
        if self.tipo_ejercicio == "bilingue":
            texto = f"EN: {ejercicio['en']}\n\nES: {ejercicio['es']}"
        else:
            texto = ejercicio['es']
        
        self.pregunta_label.config(text=texto)
        
        self.respuesta = tk.StringVar()
        for idx, opcion in enumerate(ejercicio['opciones']):
            ttk.Radiobutton(
                self.opciones_frame, 
                text=opcion, 
                value=idx, 
                variable=self.respuesta
            ).grid(row=idx, column=0, sticky="w", padx=20)

    def siguiente_pregunta(self):
        if not self.respuesta.get():
            messagebox.showwarning("Advertencia", "Selecciona una opción antes de continuar")
            return
        
        ejercicio = ejercicios_bilingue[self.current_ejercicio]
        seleccion = int(self.respuesta.get())
        
        if seleccion == ejercicio['correcta']:
            self.puntuacion += 10
            self.feedback_label.config(
                text=f"✅ Correcto! +10 puntos\n{ejercicio['explicacion']}",
                foreground="green"
            )
        else:
            self.ejercicios_fallados.append(self.current_ejercicio)
            self.feedback_label.config(
                text=f"❌ Incorrecto. La respuesta correcta es: {ejercicio['opciones'][ejercicio['correcta']]}\n{ejercicio['explicacion']}",
                foreground="red"
            )
        
        self.actualizar_barra_estado()
        
        if self.current_ejercicio < len(ejercicios_bilingue) - 1:
            self.current_ejercicio += 1
            self.mostrar_pregunta()
        else:
            messagebox.showinfo("Finalizado", f"Ejercicios completados!\nPuntuación final: {self.puntuacion}")
            self.mostrar_panel("inicio")

    def repetir_ejercicios_fallados(self):
        if not self.ejercicios_fallados:
            messagebox.showinfo("Información", "No tienes ejercicios fallados para repetir")
            return
        
        self.current_ejercicio = 0
        self.tipo_ejercicio = "fallados"
        self.mostrar_pregunta_fallada()
        self.mostrar_panel("ejercicios")

    def mostrar_pregunta_fallada(self):
        # Implementación similar a mostrar_pregunta usando ejercicios_fallados
        pass

    def actualizar_barra_estado(self):
        self.barra_estado.config(
            text=f"Puntuación: {self.puntuacion} | Ejemplos guardados: {len(self.ejemplos_usuario)}"
        )

    def actualizar_lista_ejemplos(self):
        self.lista_ejemplos.delete(0, tk.END)
        for ejemplo in self.ejemplos_usuario:
            self.lista_ejemplos.insert(tk.END, ejemplo)

    def mostrar_mis_ejemplos(self):
        self.mostrar_panel("redaccion")

# Datos de ejercicios
ejercicios_bilingue = [
    {
        "en": "I was one of those who refused the proposal.",
        "es": "Fui de los que se { } a aceptar la propuesta.",
        "opciones": ["negaron", "negó"],
        "correcta": 0,
        "explicacion": "Concordancia plural con 'los que'"
    },
    {
        "en": "She is part of the group that achieved the goals.",
        "es": "Es parte del grupo que { } las metas.",
        "opciones": ["alcanzaron", "alcanzó"],
        "correcta": 1,
        "explicacion": "Singular por concordancia con 'grupo'"
    }
]

if __name__ == "__main__":
    app = GrammarApp()
    app.mainloop()
