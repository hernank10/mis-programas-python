import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from textwrap import dedent

class GerundioPracticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Gerundios - Spanish Tutor")
        self.root.geometry("900x700")
        
        # Configuración inicial
        self.categorias = {
            1: {"nombre": "Instantaneidad", "ejemplos": [], "practicadas": 0},
            2: {"nombre": "Duración", "ejemplos": [], "practicadas": 0},
            3: {"nombre": "Repetición", "ejemplos": [], "practicadas": 0},
            4: {"nombre": "Percepción", "ejemplos": [], "practicadas": 0},
            5: {"nombre": "Simultaneidad", "ejemplos": [], "practicadas": 0},
            6: {"nombre": "Causalidad", "ejemplos": [], "practicadas": 0},
            7: {"nombre": "Concesión/Condición", "ejemplos": [], "practicadas": 0}
        }
        
        self.frases_reescribir = [
            "El niño lee un libro",
            "Los estudiantes hacen la tarea",
            "María cocina paella",
            "Yo escribo un poema",
            "El equipo desarrolla software",
            "Aprendo francés",
            "Los pájaros cantan",
            "El profesor explica la lección",
            "Ellos viajan por Europa",
            "Tú miras la televisión"
        ]
        
        self.puntaje = 0
        self.progreso = {cat: 0 for cat in self.categorias}
        self.cargar_ejemplos_iniciales()
        
        # Interfaz gráfica
        self.crear_menu_principal()
        self.crear_widgets_ayuda()
        
    def cargar_ejemplos_iniciales(self):
        ejemplos_base = [
            (1, "Estoy *escribiendo* un correo ahora mismo"),
            (2, "Llevo horas *estudiando* para el examen"),
            (3, "Siempre está *quejándose* de todo"),
            (4, "Vi al gato *trepando* el árbol"),
            (5, "Entró a la sala *cantando*"),
            (6, "Viendo tu esfuerzo, continuaré ayudando"),
            (7, "Siendo sincero, prefiero otro método")
        ]
        
        for cat_id, ejemplo in ejemplos_base:
            self.categorias[cat_id]["ejemplos"].append(ejemplo)

    def crear_menu_principal(self):
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(self.frame_principal, 
                text="Práctica de Gerundios", 
                font=("Arial", 16, "bold")).pack(pady=10)
                
        botones = [
            ("Ver Ejemplos", self.mostrar_categorias),
            ("Practicar Escritura", self.practicar_escritura),
            ("Reescribir Frases", self.reescribir_frases),
            ("Mi Progreso", self.mostrar_progreso),
            ("Ayuda Gramatical", self.mostrar_ayuda),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            ttk.Button(self.frame_principal, 
                      text=texto, 
                      command=comando,
                      width=25).pack(pady=5)

    def crear_widgets_ayuda(self):
        self.help_text = dedent("""
        REGLAS DEL GERUNDIO:
        1. Expresa acciones en desarrollo: "Estoy comiendo"
        2. Indica acciones simultáneas: "Caminando habla por teléfono"
        3. Forma correcta:
           - AR: ando (hablando)
           - ER/IR: iendo (comiendo/viviendo)
        4. ¡Evita!:
           - Usar para características permanentes
           - Secuencias temporales incorrectas
        """)
        
    def mostrar_categorias(self):
        ventana = tk.Toplevel()
        ventana.title("Seleccionar Categoría")
        
        ttk.Label(ventana, text="Elija una categoría:").pack(pady=10)
        
        for cat_id, datos in self.categorias.items():
            frame = ttk.Frame(ventana)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            ttk.Label(frame, 
                     text=f"{datos['nombre']} ({datos['practicadas']} practicadas)",
                     width=25).pack(side=tk.LEFT)
            
            ttk.Button(frame, 
                      text="Ver Ejemplos",
                      command=lambda c=cat_id: self.mostrar_ejemplos(c)).pack(side=tk.RIGHT)

    def mostrar_ejemplos(self, categoria_id):
        ejemplos = self.categorias[categoria_id]["ejemplos"]
        ventana = tk.Toplevel()
        ventana.title(f"Ejemplos - {self.categorias[categoria_id]['nombre']}")
        
        ttk.Label(ventana, text="Ejemplos (gerundios en *asteriscos*):").pack(pady=10)
        
        for ejemplo in ejemplos:
            ttk.Label(ventana, text=ejemplo).pack(pady=2)
            
        ttk.Button(ventana, 
                  text="Practicar esta categoría",
                  command=lambda: self.iniciar_practica(categoria_id)).pack(pady=10)

    def iniciar_practica(self, categoria_id):
        self.categoria_actual = categoria_id
        self.contador_practica = 0
        
        self.ventana_practica = tk.Toplevel()
        self.ventana_practica.title("Practica de escritura")
        
        ttk.Label(self.ventana_practica, 
                 text=f"Escribe 10 oraciones ({self.categorias[categoria_id]['nombre']})",
                 font=("Arial", 12)).pack(pady=10)
        
        self.frame_entrada = ttk.Frame(self.ventana_practica)
        self.frame_entrada.pack(pady=10)
        
        ttk.Label(self.frame_entrada, text="Oración:").pack(side=tk.LEFT)
        self.entrada_oracion = ttk.Entry(self.frame_entrada, width=50)
        self.entrada_oracion.pack(side=tk.LEFT, padx=10)
        self.entrada_oracion.bind("<Return>", self.validar_oracion)
        
        self.etiqueta_estado = ttk.Label(self.ventana_practica, text="")
        self.etiqueta_estado.pack(pady=5)
        
        self.barra_progreso = ttk.Progressbar(self.ventana_practica, 
                                             orient=tk.HORIZONTAL,
                                             length=300,
                                             mode='determinate')
        self.barra_progreso.pack(pady=10)
        self.actualizar_barra_progreso()

    def validar_oracion(self, event=None):
        oracion = self.entrada_oracion.get()
        if any(palabra.strip("*").endswith(('ando', 'iendo')) for palabra in oracion.split()):
            self.puntaje += 10
            self.contador_practica += 1
            self.categorias[self.categoria_actual]["practicadas"] += 1
            self.progreso[self.categoria_actual] += 10
            self.etiqueta_estado.config(text="✓ Correcto! +10 puntos", foreground="green")
            self.actualizar_barra_progreso()
            
            if self.contador_practica >= 10:
                messagebox.showinfo("Completado", "¡Has completado la práctica!")
                self.ventana_practica.destroy()
                return
        else:
            self.puntaje = max(0, self.puntaje - 5)
            self.etiqueta_estado.config(text="✗ Falta gerundio! -5 puntos", foreground="red")
        
        self.entrada_oracion.delete(0, tk.END)
        self.root.after(1500, lambda: self.etiqueta_estado.config(text=""))

    def actualizar_barra_progreso(self):
        porcentaje = (self.contador_practica / 10) * 100
        self.barra_progreso['value'] = porcentaje

    def reescribir_frases(self):
        self.frase_actual = 0
        self.ventana_reescribir = tk.Toplevel()
        self.ventana_reescribir.title("Reescribir Frases")
        
        self.label_instruccion = ttk.Label(self.ventana_reescribir, 
                                          text="Reescribe la frase usando gerundio:")
        self.label_instruccion.pack(pady=10)
        
        self.label_frase_original = ttk.Label(self.ventana_reescribir, 
                                             font=("Arial", 12, "bold"))
        self.label_frase_original.pack(pady=5)
        
        self.entrada_reescritura = ttk.Entry(self.ventana_reescribir, width=50)
        self.entrada_reescritura.pack(pady=10)
        self.entrada_reescritura.bind("<Return>", self.validar_reescritura)
        
        self.mostrar_siguiente_frase()

    def mostrar_siguiente_frase(self):
        if self.frase_actual < len(self.frases_reescribir):
            self.label_frase_original.config(
                text=f"Original: {self.frases_reescribir[self.frase_actual]}"
            )
            self.entrada_reescritura.delete(0, tk.END)
        else:
            messagebox.showinfo("Completado", "¡Todas las frases practicadas!")
            self.ventana_reescribir.destroy()

    def validar_reescritura(self, event=None):
        original = self.frases_reescribir[self.frase_actual]
        reescrita = self.entrada_reescritura.get()
        
        if any(palabra.endswith(('ando', 'iendo')) in reescrita:
            self.puntaje += 15
            self.progreso[6] += 15  # Categoría especial para reescritura
            messagebox.showinfo("Correcto", 
                               f"Original: {original}\nTu versión: {reescrita}")
            self.frase_actual += 1
            self.mostrar_siguiente_frase()
        else:
            messagebox.showerror("Error", "Incluye un gerundio válido (-ando/-iendo)")
            self.puntaje = max(0, self.puntaje - 5)

    def mostrar_progreso(self):
        ventana = tk.Toplevel()
        ventana.title("Progreso y Puntaje")
        
        ttk.Label(ventana, 
                 text=f"Puntaje Total: {self.puntaje}", 
                 font=("Arial", 14)).pack(pady=10)
        
        for cat_id, datos in self.categorias.items():
            ttk.Label(ventana, 
                     text=f"{datos['nombre']}: {datos['practicadas']} ejercicios").pack(pady=2)
            
        ttk.Label(ventana, 
                 text=f"Frases reescritas: {self.frase_actual}/{len(self.frases_reescribir)}"
                 ).pack(pady=10)

    def mostrar_ayuda(self):
        messagebox.showinfo("Ayuda Gramatical", self.help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerundioPracticaApp(root)
    root.mainloop()
