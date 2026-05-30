import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AplicacionEnumeracion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Máster en Enumeración Sintáctica")
        self.geometry("1000x700")
        self.progreso = self.cargar_progreso()
        self.errores = self.cargar_errores()
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        # Configuración del sistema de pestañas
        self.notebook = ttk.Notebook(self)
        
        # Pestañas principales
        self.pestania_teoria = ttk.Frame(self.notebook)
        self.pestania_practica = ttk.Frame(self.notebook)
        self.pestania_estadisticas = ttk.Frame(self.notebook)
        
        self.notebook.add(self.pestania_teoria, text="Teoría")
        self.notebook.add(self.pestania_practica, text="Práctica")
        self.notebook.add(self.pestania_estadisticas, text="Estadísticas")
        self.notebook.pack(expand=True, fill='both')
        
        self.crear_pestania_teoria()
        self.crear_pestania_practica()
        self.crear_pestania_estadisticas()
        
    def crear_pestania_teoria(self):
        # Contenido teórico con diapositivas
        self.texto_teoria = tk.Text(self.pestania_teoria, wrap=tk.WORD)
        scroll = ttk.Scrollbar(self.pestania_teoria, command=self.texto_teoria.yview)
        self.texto_teoria.configure(yscrollcommand=scroll.set)
        
        self.texto_teoria.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        diapositivas = [
            ("Enumeración Sintáctica", "Definición:\nSeparación de elementos análogos con comas.\n\nEjemplo:\n• Correcto: 'inglés, francés, ruso'\n• Incorrecto: 'inglés francés ruso'"),
            ("Reglas Fundamentales", "1. No separar sujeto-verbo\n2. Verbo complemento directo\n3. Complemento indirecto")
        ]
        
        for titulo, contenido in diapositivas:
            self.texto_teoria.insert(tk.END, f"\n\n{titulo}\n{'='*30}\n{contenido}")
            
    def crear_pestania_practica(self):
        # Panel de ejercicios
        frame_controles = ttk.Frame(self.pestania_practica)
        frame_controles.pack(side=tk.TOP, fill=tk.X)
        
        btn_cuestionario = ttk.Button(frame_controles, text="Cuestionario", command=self.iniciar_cuestionario)
        btn_cuestionario.pack(side=tk.LEFT, padx=5)
        
        btn_corregir = ttk.Button(frame_controles, text="Corregir Oraciones", command=self.corregir_oraciones)
        btn_corregir.pack(side=tk.LEFT, padx=5)
        
        btn_crear = ttk.Button(frame_controles, text="Crear Ejercicio", command=self.crear_ejercicio)
        btn_crear.pack(side=tk.LEFT, padx=5)
        
        self.frame_practica = ttk.Frame(self.pestania_practica)
        self.frame_practica.pack(expand=True, fill=tk.BOTH)
        
    def crear_pestania_estadisticas(self):
        # Sistema de reportes
        fig, ax = plt.subplots()
        ax.pie([self.progreso['aciertos'], self.progreso['errores']], 
              labels=['Aciertos', 'Errores'], autopct='%1.1f%%')
        ax.set_title('Rendimiento General')
        
        canvas = FigureCanvasTkAgg(fig, self.pestania_estadisticas)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    def iniciar_cuestionario(self):
        # Lógica completa del cuestionario interactivo
        ventana_cuestionario = tk.Toplevel(self)
        ventana_cuestionario.title("Cuestionario Interactivo")
        
        preguntas = self.cargar_preguntas()
        self.pregunta_actual = 0
        self.respuestas_usuario = []
        
        lbl_pregunta = ttk.Label(ventana_cuestionario, wraplength=800)
        lbl_pregunta.pack(pady=10)
        
        frame_opciones = ttk.Frame(ventana_cuestionario)
        frame_opciones.pack(pady=10)
        
        self.actualizar_pregunta(preguntas, lbl_pregunta, frame_opciones, ventana_cuestionario)
        
    def actualizar_pregunta(self, preguntas, label, frame, ventana):
        # Actualizar interfaz para cada pregunta
        for widget in frame.winfo_children():
            widget.destroy()
            
        if self.pregunta_actual < len(preguntas):
            pregunta = preguntas[self.pregunta_actual]
            label.config(text=pregunta['pregunta'])
            
            for idx, opcion in enumerate(pregunta['opciones']):
                btn = ttk.Radiobutton(frame, text=opcion, value=chr(65+idx),
                                      command=lambda v=chr(65+idx): self.registrar_respuesta(v, preguntas, label, frame, ventana))
                btn.pack(anchor=tk.W)
                
            self.pregunta_actual += 1
        else:
            self.mostrar_resultados(preguntas, ventana)
            
    def registrar_respuesta(self, respuesta, preguntas, label, frame, ventana):
        self.respuestas_usuario.append(respuesta)
        self.actualizar_pregunta(preguntas, label, frame, ventana)
        
    def mostrar_resultados(self, preguntas, ventana):
        # Cálculo y visualización de resultados
        aciertos = sum(1 for p, r in zip(preguntas, self.respuestas_usuario) if r == p['correcta'])
        self.progreso['aciertos'] += aciertos
        self.progreso['errores'] += len(preguntas) - aciertos
        self.guardar_progreso()
        
        tk.Label(ventana, text=f"Resultado: {aciertos}/{len(preguntas)}").pack(pady=20)
        ttk.Button(ventana, text="Ver Detalles", command=lambda: self.mostrar_detalles(preguntas)).pack()
        
    def cargar_preguntas(self):
        # Cargar preguntas desde archivo JSON
        try:
            with open('preguntas.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
            
    # Sistema de progreso y persistencia
    def cargar_progreso(self):
        try:
            with open('progreso.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'aciertos': 0, 'errores': 0, 'ejercicios_completados': 0}
            
    def guardar_progreso(self):
        with open('progreso.json', 'w') as f:
            json.dump(self.progreso, f)
            
    def cargar_errores(self):
        try:
            with open('errores.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
            
    def guardar_errores(self):
        with open('errores.json', 'w') as f:
            json.dump(self.errores, f)
            
    # Resto de funcionalidades (corregir_oraciones, crear_ejercicio, etc.)
    # ... (Implementación similar con widgets Tkinter)

if __name__ == "__main__":
    app = AplicacionEnumeracion()
    app.mainloop()
