import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import pyperclip

class GerundioTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrenador de Gerundios")
        self.root.geometry("1000x700")
        
        # Datos iniciales
        self.categorias = {
            "Simultaneidad": [
                "El niño terminó la tarea silbando una canción",
                "La bailarina giró extendiendo los brazos",
                "El chef preparó la cena cantando"
            ],
            "Modo": [
                "El perro escapó saltando la cerca",
                "El bombero rescató al gato trepando al árbol",
                "El vendedor cerró el trato negociando hábilmente"
            ],
            "Errores Comunes": [
                "✖ Terminó el examen yéndose del aula → ✓ Salió después de terminar",
                "✖ Leyó el libro entendiéndolo después → ✓ Lo entendió al final"
            ]
        }
        
        self.ejercicios = [
            "El niño comió helado (derramar)",
            "La actriz declamó (gesticular)",
            "El ciclista avanzó (pedalear)"
        ]
        
        self.puntaje = 0
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Panel izquierdo - Categorías
        self.frame_izq = ttk.Frame(self.root)
        self.frame_izq.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        ttk.Label(self.frame_izq, text="Categorías", font=('Arial', 12, 'bold')).pack(pady=5)
        self.lista_categorias = ttk.Treeview(self.frame_izq, height=15, selectmode='browse')
        self.lista_categorias.pack()
        
        for categoria in self.categorias:
            self.lista_categorias.insert('', tk.END, text=categoria, iid=categoria)
        
        # Panel central - Ejemplos y práctica
        self.frame_central = ttk.Frame(self.root)
        self.frame_central.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.notebook = ttk.Notebook(self.frame_central)
        self.pestaña_ejemplos = ttk.Frame(self.notebook)
        self.pestaña_ejercicios = ttk.Frame(self.notebook)
        self.notebook.add(self.pestaña_ejemplos, text="Ejemplos")
        self.notebook.add(self.pestaña_ejercicios, text="Ejercicios")
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de ejemplos
        self.txt_ejemplos = scrolledtext.ScrolledText(self.pestaña_ejemplos, wrap=tk.WORD)
        self.txt_ejemplos.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.frame_controles = ttk.Frame(self.pestaña_ejemplos)
        self.frame_controles.pack(pady=10)
        
        ttk.Label(self.frame_controles, text="Sujeto:").pack(side=tk.LEFT)
        self.entry_sujeto = ttk.Entry(self.frame_controles, width=15)
        self.entry_sujeto.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(self.frame_controles, text="Verbo:").pack(side=tk.LEFT)
        self.entry_verbo = ttk.Entry(self.frame_controles, width=15)
        self.entry_verbo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(self.frame_controles, text="Crear Oración", 
                  command=self.crear_oracion).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_controles, text="Copiar", 
                  command=self.copiar_texto).pack(side=tk.LEFT)
        
        # Pestaña de ejercicios
        self.frame_ejercicio = ttk.Frame(self.pestaña_ejercicios)
        self.frame_ejercicio.pack(pady=20)
        
        self.lbl_ejercicio = ttk.Label(self.frame_ejercicio, font=('Arial', 12))
        self.lbl_ejercicio.pack(pady=10)
        
        self.txt_respuesta = ttk.Entry(self.frame_ejercicio, width=50)
        self.txt_respuesta.pack(pady=10)
        
        ttk.Button(self.frame_ejercicio, text="Verificar", 
                  command=self.verificar_respuesta).pack(pady=5)
        
        self.lbl_puntaje = ttk.Label(self.frame_ejercicio, text="Puntaje: 0")
        self.lbl_puntaje.pack(pady=5)
        
        # Eventos
        self.lista_categorias.bind('<<TreeviewSelect>>', self.mostrar_ejemplos)
        self.cargar_ejercicio()
    
    def mostrar_ejemplos(self, event):
        categoria = self.lista_categorias.selection()[0]
        self.txt_ejemplos.config(state=tk.NORMAL)
        self.txt_ejemplos.delete(1.0, tk.END)
        
        for ejemplo in self.categorias[categoria]:
            self.txt_ejemplos.insert(tk.END, ejemplo + '\n')
            self.resaltar_gerundio(ejemplo + '\n')
        
        self.txt_ejemplos.config(state=tk.DISABLED)
    
    def resaltar_gerundio(self, texto):
        palabras = re.findall(r'\b\w+(?:ando|iendo)\b', texto)
        for palabra in palabras:
            start = self.txt_ejemplos.search(palabra, 1.0, stopindex=tk.END)
            while start:
                end = f"{start}+{len(palabra)}c"
                self.txt_ejemplos.tag_add('gerundio', start, end)
                start = self.txt_ejemplos.search(palabra, end, tk.END)
        
        self.txt_ejemplos.tag_config('gerundio', underline=True, 
                                   foreground='blue', font=('Arial', 10, 'underline'))
    
    def crear_oracion(self):
        sujeto = self.entry_sujeto.get().strip()
        verbo = self.entry_verbo.get().strip().lower()
        
        if not sujeto or not verbo:
            messagebox.showwarning("Error", "Debe ingresar sujeto y verbo")
            return
        
        gerundio = self.generar_gerundio(verbo)
        nueva_oracion = f"{sujeto} está {gerundio}"
        
        categoria = self.lista_categorias.selection()[0]
        self.categorias[categoria].append(nueva_oracion)
        
        self.txt_ejemplos.config(state=tk.NORMAL)
        self.txt_ejemplos.insert(tk.END, nueva_oracion + '\n')
        self.resaltar_gerundio(nueva_oracion + '\n')
        self.txt_ejemplos.config(state=tk.DISABLED)
    
    def generar_gerundio(self, verbo):
        if verbo.endswith('ar'):
            return verbo[:-2] + 'ando'
        elif verbo.endswith(('er', 'ir')):
            return verbo[:-2] + 'iendo'
        return verbo + ' (gerundio irregular)'
    
    def copiar_texto(self):
        try:
            texto = self.txt_ejemplos.get(tk.SEL_FIRST, tk.SEL_LAST)
            pyperclip.copy(texto)
        except tk.TclError:
            messagebox.showwarning("Error", "Seleccione texto para copiar")
    
    def cargar_ejercicio(self):
        if self.ejercicios:
            ejercicio = self.ejercicios.pop(0)
            self.lbl_ejercicio.config(text=ejercicio)
            self.txt_respuesta.delete(0, tk.END)
        else:
            self.lbl_ejercicio.config(text="¡Todos los ejercicios completados!")
            self.txt_respuesta.config(state=tk.DISABLED)
    
    def verificar_respuesta(self):
        respuesta = self.txt_respuesta.get()
        if re.search(r'\b\w+(ando|iendo)\b', respuesta):
            self.puntaje += 10
            messagebox.showinfo("Correcto", "¡Buen uso del gerundio!")
        else:
            self.puntaje = max(0, self.puntaje -5)
            messagebox.showerror("Error", "Falta gerundio (-ando/-iendo)")
        
        self.lbl_puntaje.config(text=f"Puntaje: {self.puntaje}")
        self.cargar_ejercicio()

if __name__ == "__main__":
    root = tk.Tk()
    app = GerundioTrainer(root)
    root.mainloop()
