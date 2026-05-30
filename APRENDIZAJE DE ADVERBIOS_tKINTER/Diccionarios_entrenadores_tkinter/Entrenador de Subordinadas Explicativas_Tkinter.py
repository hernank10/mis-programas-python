import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import random
from pathlib import Path

class SubordinadasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entrenador de Subordinadas Explicativas")
        self.geometry("800x600")
        self.ejemplos_file = "ejemplos_guardados.json"
        self.max_ejemplos = 100
        
        self.teoria_content = """📚 TEORÍA: Frases Subordinadas Explicativas
1. Funcionan como modificadores no esenciales
2. Van entre comas
3. Se refieren al último elemento de la principal
Ej: "El río Magdalena, que es el más largo de Colombia, cruza varias regiones.\""""
        
        self._crear_widgets()
        self._cargar_ejemplos()
    
    def _crear_widgets(self):
        # Notebook para secciones
        self.notebook = ttk.Notebook(self)
        
        # Pestañas
        self.teoria_frame = TeoriaFrame(self.notebook, self.teoria_content)
        self.practica_frame = PracticaFrame(self.notebook, self)
        self.crear_frame = CrearFrame(self.notebook, self)
        
        self.notebook.add(self.teoria_frame, text="📚 Teoría")
        self.notebook.add(self.practica_frame, text="✍️ Practicar")
        self.notebook.add(self.crear_frame, text="➕ Crear Ejemplos")
        
        self.notebook.pack(expand=True, fill='both')

    def _cargar_ejemplos(self):
        try:
            if Path(self.ejemplos_file).exists():
                with open(self.ejemplos_file, 'r') as f:
                    self.ejemplos_guardados = json.load(f)
            else:
                self.ejemplos_guardados = []
        except:
            self.ejemplos_guardados = []

    def guardar_ejemplo(self, ejemplo):
        if len(self.ejemplos_guardados) >= self.max_ejemplos:
            messagebox.showwarning("Límite alcanzado", "Se ha alcanzado el máximo de 100 ejemplos guardados.")
            return False
        
        self.ejemplos_guardados.append(ejemplo)
        with open(self.ejemplos_file, 'w') as f:
            json.dump(self.ejemplos_guardados, f, indent=2)
        return True

class TeoriaFrame(ttk.Frame):
    def __init__(self, parent, content):
        super().__init__(parent)
        self.text = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Arial', 12))
        self.text.insert(tk.INSERT, content)
        self.text.configure(state='disabled')
        self.text.pack(expand=True, fill='both', padx=10, pady=10)

class PracticaFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        # Controles principales
        self.frame_superior = ttk.Frame(self)
        self.frame_inferior = ttk.Frame(self)
        
        # Elementos
        self.lbl_principal = ttk.Label(self.frame_superior, text="Frase principal:")
        self.txt_principal = tk.Text(self.frame_superior, height=3, width=60, wrap=tk.WORD)
        
        self.lbl_subordinada = ttk.Label(self.frame_superior, text="Subordinada explicativa:")
        self.ent_subordinada = ttk.Entry(self.frame_superior, width=60)
        
        self.btn_comprobar = ttk.Button(self.frame_inferior, text="Comprobar", command=self.validar_subordinada)
        self.lbl_feedback = ttk.Label(self.frame_inferior, text="", wraplength=500)
        
        # Layout
        self.frame_superior.pack(pady=10)
        self.frame_inferior.pack(pady=10)
        
        self.lbl_principal.grid(row=0, column=0, sticky='w')
        self.txt_principal.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_subordinada.grid(row=1, column=0, sticky='w')
        self.ent_subordinada.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_comprobar.pack(pady=5)
        self.lbl_feedback.pack(pady=5)
        
        self.cargar_ejemplo_aleatorio()
    
    def cargar_ejemplo_aleatorio(self):
        if self.app.ejemplos_guardados:
            ejemplo = random.choice(self.app.ejemplos_guardados)
            self.txt_principal.delete('1.0', tk.END)
            self.txt_principal.insert(tk.END, ejemplo['principal'])
            self.ent_subordinada.delete(0, tk.END)
    
    def validar_subordinada(self):
        principal = self.txt_principal.get('1.0', tk.END).strip()
        subordinada = self.ent_subordinada.get().strip()
        
        # Validación básica
        errores = []
        if not subordinada.startswith(", ") or not subordinada.endswith("."):
            errores.append("Formato incorrecto: Debe comenzar con coma y espacio, y terminar con punto")
            
        # Obtener último elemento de la principal
        ultimo_elemento = principal.split()[-1].rstrip('.,')
        
        if ultimo_elemento not in subordinada:
            errores.append(f"El antecedente '{ultimo_elemento}' no está presente")
        
        # Mostrar resultados
        if errores:
            feedback = "❌ Errores encontrados:\n" + "\n- ".join(errores)
            self.lbl_feedback.config(foreground='red')
        else:
            feedback = "✅ ¡Correcto! La subordinada está bien construida"
            self.lbl_feedback.config(foreground='green')
            self.after(1500, self.cargar_ejemplo_aleatorio)
        
        self.lbl_feedback.config(text=feedback)

class CrearFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self._crear_formulario()
    
    def _crear_formulario(self):
        ttk.Label(self, text="Crear nuevo ejemplo", font=('Arial', 14)).pack(pady=10)
        
        self.frame_form = ttk.Frame(self)
        self.frame_form.pack(pady=10)
        
        # Campos del formulario
        ttk.Label(self.frame_form, text="Frase principal:").grid(row=0, column=0, sticky='w')
        self.ent_principal = ttk.Entry(self.frame_form, width=50)
        self.ent_principal.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.frame_form, text="Subordinada explicativa:").grid(row=1, column=0, sticky='w')
        self.ent_subordinada = ttk.Entry(self.frame_form, width=50)
        self.ent_subordinada.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.frame_form, text="Antecedente:").grid(row=2, column=0, sticky='w')
        self.ent_antecedente = ttk.Entry(self.frame_form, width=50)
        self.ent_antecedente.grid(row=2, column=1, padx=5, pady=5)
        
        btn_guardar = ttk.Button(self, text="Guardar ejemplo", command=self.guardar_ejemplo)
        btn_guardar.pack(pady=10)
        
        self.lbl_status = ttk.Label(self, text="")
        self.lbl_status.pack()
    
    def guardar_ejemplo(self):
        ejemplo = {
            'principal': self.ent_principal.get(),
            'subordinada': self.ent_subordinada.get(),
            'antecedente': self.ent_antecedente.get()
        }
        
        # Validación
        if not all(ejemplo.values()):
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
            return
        
        if self.app.guardar_ejemplo(ejemplo):
            self.lbl_status.config(text="✅ Ejemplo guardado correctamente", foreground='green')
            self.ent_principal.delete(0, tk.END)
            self.ent_subordinada.delete(0, tk.END)
            self.ent_antecedente.delete(0, tk.END)
        else:
            self.lbl_status.config(text="❌ Error al guardar el ejemplo", foreground='red')

if __name__ == "__main__":
    app = SubordinadasApp()
    app.mainloop()
