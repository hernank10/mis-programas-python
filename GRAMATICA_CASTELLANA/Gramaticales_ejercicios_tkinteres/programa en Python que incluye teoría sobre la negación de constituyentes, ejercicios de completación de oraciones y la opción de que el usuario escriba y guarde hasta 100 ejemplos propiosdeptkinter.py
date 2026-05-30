"""
PROGRAMA DE NEGACIÓN DE CONSTITUYENTES CON TKINTER
Versión: 2.0
Características:
- Interfaz gráfica moderna
- 15 ejercicios de completación
- Sistema de progreso
- Paleta de colores personalizada
- Teoría interactiva
"""
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Configuración inicial
EJERCICIOS_GUARDADOS = "ejercicios_negacion.json"
MAX_EJEMPLOS = 100

# Paleta de colores
COLORES = {
    'fondo': '#F0F7FF',
    'boton': '#4A90E2',
    'texto': '#2D3748',
    'correcto': '#48BB78',
    'error': '#F56565'
}

# Teoría ampliada
TEORIA = {
    'Introducción': [
        "La negación de constituyentes modifica elementos específicos, no toda la oración",
        "Dos patrones principales:\n- Posición inicial sin contraste (No + cuantificador)\n- Posición final con estructura contrastiva (no X, sino Y)"
    ],
    'Reglas principales': [
        "Los cuantificadores universales (todo, siempre) admiten negación inicial",
        "Los referentes específicos (nombres, numerales) requieren contraste",
        "Los cuantificadores gradativos (muchos, pocos) forman unidades con 'no'"
    ],
    'Ejemplos': [
        "Correcto: No todos vinieron\nIncorrecto: No Juan llegó temprano (falta contraste)",
        "Correcto: Comieron no tres, sino cuatro\nIncorrecto: No algunos estaban cansados"
    ]
}

# Ejercicios ampliados (15 en total)
EJERCICIOS_COMPLETACION = [
    {'enunciado': "___ pocos estudiantes entendieron la explicación", 'solucion': ['No']},
    {'enunciado': "Han comido ___ dos, ___ tres postres", 'solucion': ['no', 'sino']},
    {'enunciado': "___ todo lo que reluce es oro", 'solucion': ['No']},
    {'enunciado': "Eligieron ___ el vestido rojo, ___ el azul", 'solucion': ['no', 'sino']},
    {'enunciado': "___ muchos sino pocos aprobaron el examen", 'solucion': ['No']},
    {'enunciado': "Necesitamos ___ cinco ___ siete voluntarios", 'solucion': ['no', 'sino']},
    {'enunciado': "___ siempre es fácil tomar decisiones difíciles", 'solucion': ['No']},
    {'enunciado': "El ganador fue ___ Pedro ___ su hermano", 'solucion': ['no', 'sino']},
    {'enunciado': "___ todas las películas tienen final feliz", 'solucion': ['No']},
    {'enunciado': "Viajarán ___ a Francia ___ a Italia", 'solucion': ['no', 'sino']},
    {'enunciado': "___ muchos días de vacaciones nos quedan", 'solucion': ['No']},
    {'enunciado': "El paquete llegará ___ hoy ___ mañana", 'solucion': ['no', 'sino']},
    {'enunciado': "___ todo está perdido cuando hay esperanza", 'solucion': ['No']},
    {'enunciado': "Prefiero ___ té ___ café por las tardes", 'solucion': ['no', 'sino']},
    {'enunciado': "___ todos los caminos llevan a Roma", 'solucion': ['No']}
]

class AplicacionNegacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Negación de Constituyentes")
        self.geometry("800x600")
        self.configure(bg=COLORES['fondo'])
        self.ejemplos_usuario = []
        self.cargar_ejemplos()
        self.indice_ejercicio = 0
        self.correctas = 0
        self.crear_widgets()
        
    def cargar_ejemplos(self):
        if os.path.exists(EJERCICIOS_GUARDADOS):
            try:
                with open(EJERCICIOS_GUARDADOS, 'r', encoding='utf-8') as f:
                    self.ejemplos_usuario = json.load(f)
            except:
                messagebox.showerror("Error", "No se pudieron cargar los ejemplos guardados")

    def guardar_ejemplos(self):
        with open(EJERCICIOS_GUARDADOS, 'w', encoding='utf-8') as f:
            json.dump(self.ejemplos_usuario, f, ensure_ascii=False, indent=2)

    def crear_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña de teoría
        self.frame_teoria = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_teoria, text='Teoría')
        self.mostrar_teoria()
        
        # Pestaña de ejercicios
        self.frame_ejercicios = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_ejercicios, text='Ejercicios')
        self.preparar_ejercicios()
        
        # Pestaña de redacción
        self.frame_redaccion = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_redaccion, text='Redacción')
        self.preparar_redaccion()
    
    def mostrar_teoria(self):
        scroll = tk.Scrollbar(self.frame_teoria)
        text = tk.Text(self.frame_teoria, wrap=tk.WORD, yscrollcommand=scroll.set,
                      font=('Arial', 12), bg=COLORES['fondo'], fg=COLORES['texto'])
        scroll.config(command=text.yview)
        
        text.tag_configure('titulo', font=('Arial', 14, 'bold'), spacing3=10)
        text.tag_configure('punto', font=('Arial', 12), lmargin1=20, spacing2=5)
        
        for seccion, contenido in TEORIA.items():
            text.insert('end', f"{seccion}\n", 'titulo')
            for item in contenido:
                text.insert('end', f"• {item}\n", 'punto')
            text.insert('end', '\n')
        
        text.config(state='disabled')
        text.pack(side='left', fill='both', expand=True)
        scroll.pack(side='right', fill='y')
    
    def preparar_ejercicios(self):
        self.frame_actual = ttk.Frame(self.frame_ejercicios)
        self.frame_actual.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.lbl_enunciado = ttk.Label(self.frame_actual, 
                                     font=('Arial', 14),
                                     wraplength=600)
        self.lbl_enunciado.pack(pady=20)
        
        self.entradas = []
        self.frame_campos = ttk.Frame(self.frame_actual)
        self.frame_campos.pack(pady=10)
        
        self.lbl_feedback = ttk.Label(self.frame_actual, font=('Arial', 12))
        self.lbl_feedback.pack(pady=10)
        
        btn_verificar = ttk.Button(self.frame_actual, text="Verificar", 
                                 command=self.verificar_respuesta)
        btn_verificar.pack(pady=10)
        
        self.lbl_progreso = ttk.Label(self.frame_actual, 
                                    font=('Arial', 12),
                                    text="Progreso: 0/15")
        self.lbl_progreso.pack(pady=10)
        
        self.mostrar_siguiente_ejercicio()
    
    def mostrar_siguiente_ejercicio(self):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()
        
        ejercicio = EJERCICIOS_COMPLETACION[self.indice_ejercicio]
        partes = ejercicio['enunciado'].split('___')
        self.entradas.clear()
        
        for i in range(len(partes)-1):
            lbl = ttk.Label(self.frame_campos, text=partes[i], font=('Arial', 12))
            lbl.grid(row=0, column=i*2)
            
            entrada = ttk.Entry(self.frame_campos, width=8, font=('Arial', 12))
            entrada.grid(row=0, column=i*2+1, padx=5)
            self.entradas.append(entrada)
        
        lbl_final = ttk.Label(self.frame_campos, text=partes[-1], font=('Arial', 12))
        lbl_final.grid(row=0, column=len(partes)*2)
        
        self.lbl_enunciado.config(text=f"Ejercicio {self.indice_ejercicio + 1} de 15")
    
    def verificar_respuesta(self):
        ejercicio = EJERCICIOS_COMPLETACION[self.indice_ejercicio]
        respuestas_usuario = [e.get().strip() for e in self.entradas]
        correctas = ejercicio['solucion']
        
        if respuestas_usuario == correctas:
            self.correctas += 1
            self.lbl_feedback.config(text="✅ Respuesta Correcta!", foreground=COLORES['correcto'])
        else:
            self.lbl_feedback.config(text=f"❌ Incorrecto. Solución: {' '.join(correctas)}", 
                                   foreground=COLORES['error'])
        
        self.indice_ejercicio += 1
        self.lbl_progreso.config(text=f"Progreso: {self.correctas}/15")
        
        if self.indice_ejercicio < len(EJERCICIOS_COMPLETACION):
            self.mostrar_siguiente_ejercicio()
        else:
            messagebox.showinfo("Resultado Final", 
                              f"¡Has completado todos los ejercicios!\nAciertos: {self.correctas}/15")
            self.indice_ejercicio = 0
            self.correctas = 0
            self.mostrar_siguiente_ejercicio()
    
    def preparar_redaccion(self):
        lbl_instruccion = ttk.Label(self.frame_redaccion, 
                                  text="Escribe oraciones usando negación de constituyentes:",
                                  font=('Arial', 12))
        lbl_instruccion.pack(pady=10)
        
        self.txt_redaccion = scrolledtext.ScrolledText(self.frame_redaccion,
                                                     wrap=tk.WORD,
                                                     width=60,
                                                     height=8,
                                                     font=('Arial', 12))
        self.txt_redaccion.pack(pady=10, padx=20)
        
        btn_guardar = ttk.Button(self.frame_redaccion, text="Guardar Ejemplo",
                               command=self.guardar_ejemplo)
        btn_guardar.pack(pady=5)
        
        self.lbl_ejemplos = ttk.Label(self.frame_redaccion,
                                    text="Tus últimos ejemplos:",
                                    font=('Arial', 12))
        self.lbl_ejemplos.pack(pady=10)
        
        self.lista_ejemplos = tk.Listbox(self.frame_redaccion,
                                       width=70,
                                       height=6,
                                       font=('Arial', 12))
        self.lista_ejemplos.pack(pady=10, padx=20)
        self.actualizar_lista_ejemplos()
    
    def guardar_ejemplo(self):
        ejemplo = self.txt_redaccion.get('1.0', 'end-1c').strip()
        if not ejemplo:
            messagebox.showwarning("Campo Vacío", "Escribe una oración antes de guardar")
            return
        
        if len(self.ejemplos_usuario) >= MAX_EJEMPLOS:
            messagebox.showwarning("Límite Alcanzado", f"Solo se pueden guardar hasta {MAX_EJEMPLOS} ejemplos")
            return
        
        if 'no' in ejemplo.lower() and ('sino' in ejemplo.lower() or any(palabra in ejemplo.lower() for palabra in ['pero', 'aunque'])):
            self.ejemplos_usuario.append(ejemplo)
            self.guardar_ejemplos()
            self.actualizar_lista_ejemplos()
            self.txt_redaccion.delete('1.0', 'end')
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        else:
            messagebox.showwarning("Estructura Incorrecta", "La oración debe contener negación de constituyente con contraste adecuado")
    
    def actualizar_lista_ejemplos(self):
        self.lista_ejemplos.delete(0, 'end')
        for ejemplo in self.ejemplos_usuario[-5:]:
            self.lista_ejemplos.insert('end', ejemplo)

if __name__ == "__main__":
    app = AplicacionNegacion()
    app.mainloop()
