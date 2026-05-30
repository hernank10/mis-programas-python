import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ModificadoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Modificadores")
        self.root.geometry("800x600")
        
        self.ejemplos_archivo = "modificadores.json"
        self.max_ejemplos = 100
        self.ejemplos_base = [
            {
                "oracion": "Los estudiantes que entran con carnet pueden pedir libros.",
                "tipo": "E",
                "sin_modificador": "Los estudiantes pueden pedir libros.",
                "corregida": "Los estudiantes que entran con carnet pueden pedir libros.",
                "explicacion": "ESENCIAL: Solo los con carnet pueden pedir libros."
            },
            {
                "oracion": "Las ventanas, que dan a la calle, serán reforzadas.",
                "tipo": "X",
                "sin_modificador": "Las ventanas serán reforzadas.",
                "corregida": "Las ventanas, que dan a la calle, serán reforzadas.",
                "explicacion": "EXPLICATIVO: Todas las ventanas dan a la calle."
            }
        ]
        
        self.crear_interfaz_principal()
    
    def crear_interfaz_principal(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="¡Aprende Modificadores!", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        btn_style = ttk.Style()
        btn_style.configure('TButton', font=('Helvetica', 12), padding=10)
        
        ttk.Button(main_frame, text="📚 Teoría", command=self.mostrar_teoria).pack(fill='x', pady=5)
        ttk.Button(main_frame, text="❓ Cuestionario", command=self.iniciar_cuestionario).pack(fill='x', pady=5)
        ttk.Button(main_frame, text="✍️ Crear Ejemplos", command=self.crear_ejemplo).pack(fill='x', pady=5)
        ttk.Button(main_frame, text="📂 Ver Ejemplos", command=self.mostrar_ejemplos).pack(fill='x', pady=5)
        ttk.Button(main_frame, text="🚪 Salir", command=self.root.quit).pack(fill='x', pady=5)
    
    def cargar_ejemplos(self):
        try:
            with open(self.ejemplos_archivo, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def guardar_ejemplos(self, ejemplos):
        with open(self.ejemplos_archivo, 'w') as f:
            json.dump(ejemplos[-self.max_ejemplos:], f, indent=2)
    
    def mostrar_teoria(self):
        teoria_ventana = tk.Toplevel(self.root)
        teoria_ventana.title("Teoría de Modificadores")
        
        texto_teoria = """
        📚 Modificadores Esenciales vs. Explicativos

        1. ESENCIALES (Restrictivos):
        - Definen al sustantivo
        - Sin comas
        - Ejemplo: 
          [Los estudiantes que tienen carnet] pueden pedir libros
          ➔ Solo esos estudiantes

        2. EXPLICATIVOS (No restrictivos):
        - Añaden información extra
        - Entre comas
        - Ejemplo: 
          [Las ventanas, que dan a la calle], serán reforzadas
          ➔ Todas las ventanas

        🔍 Regla práctica:
        1. Elimina el modificador
        2. Si cambia el sentido ➔ Esencial
        3. Si mantiene el sentido ➔ Explicativo
        """
        
        scroll = scrolledtext.ScrolledText(teoria_ventana, wrap=tk.WORD, font=('Helvetica', 12))
        scroll.insert(tk.INSERT, texto_teoria)
        scroll.pack(expand=True, fill='both', padx=20, pady=20)
    
    def iniciar_cuestionario(self):
        self.ejemplos_quiz = self.cargar_ejemplos() + self.ejemplos_base
        random.shuffle(self.ejemplos_quiz)
        self.puntaje = 0
        self.indice_pregunta = 0
        
        self.ventana_quiz = tk.Toplevel(self.root)
        self.ventana_quiz.title("Cuestionario")
        
        self.frame_pregunta = ttk.Frame(self.ventana_quiz, padding=20)
        self.frame_pregunta.pack(expand=True, fill='both')
        
        self.mostrar_siguiente_pregunta()
    
    def mostrar_siguiente_pregunta(self):
        for widget in self.frame_pregunta.winfo_children():
            widget.destroy()
        
        if self.indice_pregunta >= len(self.ejemplos_quiz):
            self.mostrar_resultados()
            return
            
        ejemplo = self.ejemplos_quiz[self.indice_pregunta]
        
        ttk.Label(self.frame_pregunta, text="Oración:", font=('Helvetica', 12, 'bold')).pack(anchor='w')
        ttk.Label(self.frame_pregunta, text=ejemplo['oracion'], font=('Helvetica', 12)).pack(anchor='w', pady=10)
        
        ttk.Label(self.frame_pregunta, text="Tipo (E/X):").pack(anchor='w')
        self.entrada_tipo = ttk.Entry(self.frame_pregunta, width=5)
        self.entrada_tipo.pack(anchor='w')
        
        ttk.Label(self.frame_pregunta, text="Reescribe la oración:").pack(anchor='w', pady=10)
        self.entrada_correccion = ttk.Entry(self.frame_pregunta, width=80)
        self.entrada_correccion.pack(anchor='w', fill='x')
        
        ttk.Button(self.frame_pregunta, text="Enviar", command=lambda: self.verificar_respuesta(ejemplo)).pack(pady=20)
    
    def verificar_respuesta(self, ejemplo):
        tipo = self.entrada_tipo.get().upper()
        correccion = self.entrada_correccion.get().strip()
        
        if tipo not in ('E', 'X'):
            messagebox.showerror("Error", "Ingrese E o X para el tipo")
            return
        
        correcto_tipo = tipo == ejemplo['tipo']
        correcto_redaccion = correccion.lower() == ejemplo['corregida'].lower()
        
        feedback = []
        if correcto_tipo and correcto_redaccion:
            self.puntaje += 20
            feedback.append("¡Doble acierto! +20 puntos")
        elif correcto_tipo:
            self.puntaje += 10
            feedback.append("✓ Tipo correcto (+10 puntos)")
        else:
            feedback.append("✗ Tipo incorrecto")
        
        feedback.append(f"\nExplicación: {ejemplo['explicacion']}")
        feedback.append(f"\nRespuesta correcta: {ejemplo['corregida']}")
        
        messagebox.showinfo("Resultado", "\n".join(feedback))
        self.indice_pregunta += 1
        self.mostrar_siguiente_pregunta()
    
    def mostrar_resultados(self):
        resultado_ventana = tk.Toplevel(self.root)
        resultado_ventana.title("Resultados del Cuestionario")
        
        ttk.Label(resultado_ventana, text=f"Puntaje Final: {self.puntaje}/{len(self.ejemplos_quiz)*20}", 
                 font=('Helvetica', 14, 'bold')).pack(pady=20)
        ttk.Button(resultado_ventana, text="Cerrar", command=resultado_ventana.destroy).pack(pady=10)
    
    def crear_ejemplo(self):
        ventana_crear = tk.Toplevel(self.root)
        ventana_crear.title("Crear Nuevo Ejemplo")
        
        campos = [
            ("Oración:", 'oracion', 60),
            ("Tipo (E/X):", 'tipo', 5),
            ("Sin modificador:", 'sin_modificador', 60),
            ("Corregida:", 'corregida', 60),
            ("Explicación:", 'explicacion', 60)
        ]
        
        self.entries = {}
        for texto, key, width in campos:
            frame = ttk.Frame(ventana_crear, padding=5)
            frame.pack(fill='x')
            ttk.Label(frame, text=texto).pack(side='left')
            entry = ttk.Entry(frame, width=width)
            entry.pack(side='left', expand=True, fill='x')
            self.entries[key] = entry
        
        ttk.Button(ventana_crear, text="Guardar", command=self.guardar_nuevo_ejemplo).pack(pady=10)
    
    def guardar_nuevo_ejemplo(self):
        nuevo = {key: entry.get().strip() for key, entry in self.entries.items()}
        
        if not all(nuevo.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        if nuevo['tipo'].upper() not in ('E', 'X'):
            messagebox.showerror("Error", "El tipo debe ser E o X")
            return
        
        ejemplos = self.cargar_ejemplos()
        ejemplos.append(nuevo)
        self.guardar_ejemplos(ejemplos)
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        self.entries['oracion'].delete(0, tk.END)
    
    def mostrar_ejemplos(self):
        ejemplos = self.cargar_ejemplos()
        
        ventana_ejemplos = tk.Toplevel(self.root)
        ventana_ejemplos.title("Ejemplos Guardados")
        
        scroll = scrolledtext.ScrolledText(ventana_ejemplos, wrap=tk.WORD, font=('Helvetica', 12))
        scroll.pack(expand=True, fill='both', padx=20, pady=20)
        
        for idx, ej in enumerate(ejemplos, 1):
            scroll.insert(tk.END, f"\n◆ Ejemplo {idx} ◆\n")
            scroll.insert(tk.END, f"Original: {ej['oracion']}\n")
            scroll.insert(tk.END, f"Tipo: {'Esencial' if ej['tipo'] == 'E' else 'Explicativo'}\n")
            scroll.insert(tk.END, f"Corregida: {ej['corregida']}\n")
            scroll.insert(tk.END, f"Explicación: {ej['explicacion']}\n")
            scroll.insert(tk.END, "-"*50 + "\n")
        
        scroll.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ModificadoresApp(root)
    root.mainloop()
