import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext

class DerivadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio de Derivados Verbales")
        self.root.geometry("800x600")
        
        # Cargar datos
        self.ejemplos_file = "ejemplos.json"
        self.usuario_file = "usuario_ejemplos.json"
        self.ejemplos = self.cargar_ejemplos()
        self.ejemplos_usuario = self.cargar_usuario()
        
        # Crear interfaz
        self.crear_menu_principal()
        self.crear_diapositiva_conceptual()
        
    def cargar_ejemplos(self):
        if os.path.exists(self.ejemplos_file):
            with open(self.ejemplos_file, 'r') as f:
                return json.load(f)
        return []
    
    def cargar_usuario(self):
        if os.path.exists(self.usuario_file):
            with open(self.usuario_file, 'r') as f:
                return json.load(f)
        return []
    
    def guardar_ejemplo(self, ejemplo):
        if len(self.ejemplos_usuario) < 100:
            self.ejemplos_usuario.append(ejemplo)
            with open(self.usuario_file, 'w') as f:
                json.dump(self.ejemplos_usuario, f)
            return True
        return False
    
    def crear_menu_principal(self):
        self.clear_frame()
        
        title = ttk.Label(self.root, text="ESTUDIO DE DERIVADOS VERBALES", font=('Arial', 16, 'bold'))
        title.pack(pady=20)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        buttons = [
            ("Modo Estudio", self.modo_estudio),
            ("Cuestionario", self.cuestionario),
            ("Crear Ejemplos", self.crear_ejemplos),
            ("Ver Ejemplos", self.ver_ejemplos),
            ("Ayuda Conceptual", self.mostrar_ayuda),
            ("Salir", self.root.quit)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(btn_frame, text=text, command=command, width=20)
            btn.pack(pady=5, padx=10)
    
    def crear_diapositiva_conceptual(self):
        self.help_window = tk.Toplevel(self.root)
        self.help_window.withdraw()
        
        text = """CONCEPTOS CLAVE:

Infinitivo: 
- Termina en -ar, -er, -ir
- Funciona como sustantivo
- Ejemplo: 'Estudiar es importante'

Participio:
- Termina en -ado/-ido
- Con 'ser/estar' (adjetivo): 'La puerta está cerrada'
- Con 'haber' (invariable): 'He terminado'

Gerundio:
- Termina en -ando/-iendo
- Modifica al verbo principal
- Ejemplo: 'Caminando rápido'"""
        
        self.help_text = scrolledtext.ScrolledText(self.help_window, wrap=tk.WORD, width=60, height=15)
        self.help_text.insert(tk.INSERT, text)
        self.help_text.config(state=tk.DISABLED)
        self.help_text.pack(padx=20, pady=20)
    
    def mostrar_ayuda(self):
        self.help_window.deiconify()
    
    def modo_estudio(self):
        self.clear_frame()
        self.current_index = 0
        self.total_ejemplos = len(self.ejemplos + self.ejemplos_usuario)
        
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Controles de navegación
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(pady=10)
        
        self.lbl_progreso = ttk.Label(nav_frame, text=f"Ejemplo 1/{self.total_ejemplos}")
        self.lbl_progreso.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(nav_frame, text="Anterior", command=self.anterior_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Siguiente", command=self.siguiente_ejemplo).pack(side=tk.LEFT, padx=5)
        
        # Área de contenido
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.lbl_ejemplo = ttk.Label(content_frame, text="", font=('Arial', 12))
        self.lbl_ejemplo.pack(pady=10)
        
        ttk.Label(content_frame, text="Categoría:").pack()
        self.ent_categoria = ttk.Entry(content_frame, width=20)
        self.ent_categoria.pack(pady=5)
        
        ttk.Label(content_frame, text="Escribe una oración:").pack()
        self.ent_oracion = ttk.Entry(content_frame, width=50)
        self.ent_oracion.pack(pady=5)
        
        self.lbl_feedback = ttk.Label(content_frame, text="")
        self.lbl_feedback.pack(pady=5)
        
        self.mostrar_ejemplo_actual()
    
    def mostrar_ejemplo_actual(self):
        if self.total_ejemplos == 0:
            self.lbl_ejemplo.config(text="No hay ejemplos disponibles")
            return
            
        ejemplo = (self.ejemplos + self.ejemplos_usuario)[self.current_index]
        self.lbl_progreso.config(text=f"Ejemplo {self.current_index + 1}/{self.total_ejemplos}")
        self.lbl_ejemplo.config(text=ejemplo['ejemplo'])
        self.ent_categoria.delete(0, tk.END)
        self.ent_oracion.delete(0, tk.END)
        self.lbl_feedback.config(text="")
    
    def anterior_ejemplo(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.mostrar_ejemplo_actual()
    
    def siguiente_ejemplo(self):
        if self.current_index < self.total_ejemplos - 1:
            self.current_index += 1
            self.mostrar_ejemplo_actual()
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
            self.crear_menu_principal()
    
    def cuestionario(self):
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Cuestionario Interactivo")
        self.quiz_window.geometry("600x400")
        
        self.puntaje = 0
        self.total_preguntas = 10
        self.preguntas = random.sample(self.ejemplos + self.ejemplos_usuario, 
                                      min(10, len(self.ejemplos + self.ejemplos_usuario)))
        
        # Elementos de la interfaz
        self.lbl_pregunta = ttk.Label(self.quiz_window, text="", font=('Arial', 12))
        self.lbl_pregunta.pack(pady=20)
        
        ttk.Label(self.quiz_window, text="Introduce la categoría:").pack()
        self.ent_respuesta = ttk.Entry(self.quiz_window)
        self.ent_respuesta.pack(pady=10)
        
        self.btn_verificar = ttk.Button(self.quiz_window, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=10)
        
        self.lbl_resultado = ttk.Label(self.quiz_window, text="")
        self.lbl_resultado.pack(pady=10)
        
        self.mostrar_siguiente_pregunta()
    
    def mostrar_siguiente_pregunta(self):
        if self.preguntas:
            self.pregunta_actual = self.preguntas.pop(0)
            self.lbl_pregunta.config(text=self.pregunta_actual['ejemplo'])
            self.ent_respuesta.delete(0, tk.END)
            self.lbl_resultado.config(text="")
        else:
            messagebox.showinfo("Resultado", 
                              f"Cuestionario completado!\nPuntaje: {self.puntaje}/{self.total_preguntas}")
            self.quiz_window.destroy()
    
    def verificar_respuesta(self):
        respuesta = self.ent_respuesta.get().lower()
        if respuesta == self.pregunta_actual['categoria']:
            self.puntaje += 1
            self.lbl_resultado.config(text="✅ Correcto!", foreground='green')
        else:
            self.lbl_resultado.config(text=f"❌ Incorrecto. La respuesta correcta es: {self.pregunta_actual['categoria']}", 
                                    foreground='red')
        self.quiz_window.after(1500, self.mostrar_siguiente_pregunta)
    
    def crear_ejemplos(self):
        self.create_window = tk.Toplevel(self.root)
        self.create_window.title("Crear Nuevos Ejemplos")
        
        ttk.Label(self.create_window, text="Ejemplo:").pack(pady=5)
        self.ent_nuevo = ttk.Entry(self.create_window, width=40)
        self.ent_nuevo.pack(pady=5)
        
        self.lbl_categoria = ttk.Label(self.create_window, text="Categoría detectada: ")
        self.lbl_categoria.pack(pady=5)
        
        ttk.Button(self.create_window, text="Guardar", command=self.guardar_nuevo).pack(pady=10)
        ttk.Button(self.create_window, text="Cerrar", command=self.create_window.destroy).pack(pady=5)
        
        self.ent_nuevo.bind("<KeyRelease>", self.actualizar_categoria)
    
    def actualizar_categoria(self, event):
        texto = self.ent_nuevo.get().lower()
        categoria = ""
        
        if texto.endswith(('ar', 'er', 'ir')):
            categoria = 'infinitivo'
        elif texto.endswith(('ado', 'ada', 'idos', 'idas', 'ido', 'ida')):
            categoria = 'participio'
        elif texto.endswith(('ando', 'endo')):
            categoria = 'gerundio'
        
        self.lbl_categoria.config(text=f"Categoría detectada: {categoria.capitalize() if categoria else 'No válida'}")
    
    def guardar_nuevo(self):
        ejemplo = self.ent_nuevo.get().strip()
        categoria = self.lbl_categoria.cget("text").split(": ")[1].lower()
        
        if categoria not in ['infinitivo', 'participio', 'gerundio']:
            messagebox.showerror("Error", "Formato no válido. Revise las terminaciones.")
            return
            
        if len(ejemplo) < 3:
            messagebox.showerror("Error", "El ejemplo debe tener al menos 3 caracteres")
            return
            
        if self.guardar_ejemplo({'categoria': categoria, 'ejemplo': ejemplo}):
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            self.ent_nuevo.delete(0, tk.END)
            self.lbl_categoria.config(text="Categoría detectada: ")
        else:
            messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado")
    
    def ver_ejemplos(self):
        self.view_window = tk.Toplevel(self.root)
        self.view_window.title("Ejemplos Guardados")
        
        container = ttk.Frame(self.view_window)
        container.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(container, yscrollcommand=scrollbar.set, width=80)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        for idx, item in enumerate(self.ejemplos + self.ejemplos_usuario, 1):
            self.listbox.insert(tk.END, f"{idx}. [{item['categoria'].upper()}] {item['ejemplo']}")
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DerivadosApp(root)
    root.mainloop()
