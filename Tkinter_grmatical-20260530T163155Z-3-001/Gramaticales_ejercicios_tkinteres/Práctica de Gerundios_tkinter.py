import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import pyperclip

class GerundioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Gerundios")
        self.root.geometry("1000x700")
        
        self.categorias = {
            "Instantaneidad": [
                "Estoy escribiendo un mensaje urgente",
                "Mi hermana está cocinando la cena",
                "Los niños están jugando en el jardín"
            ],
            "Duración": [
                "Llevo horas estudiando para el examen",
                "Estamos renovando la casa desde enero",
                "Siguen trabajando en el proyecto"
            ],
            "Repetición": [
                "Siempre está quejándose del clima",
                "El reloj sigue sonando cada hora",
                "Está enviando mensajes sin parar"
            ]
        }
        
        self.gramatica = {
            "Simultaneidad": "El gerundio debe expresar acciones en progreso o simultáneas",
            "Posterioridad": "✖ Nunca uses gerundio para acciones sucesivas\nEj: 'Llegó al trabajo yéndose temprano'",
            "Verbos estado": "✖ Evita gerundios con verbos de estado\nEj: 'Estoy sabiendo la respuesta'",
            "Causalidad": "Solo usa 'porque' si la causa es directa y simultánea"
        }
        
        self.crear_interfaz()
        self.cargar_categorias()
        
    def crear_interfaz(self):
        # Panel izquierdo - Categorías y ejemplos
        frame_izq = ttk.Frame(self.root)
        frame_izq.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
        
        self.lista_categorias = ttk.Treeview(frame_izq, columns=('categoria'), show='tree')
        self.lista_categorias.heading('#0', text='Categorías')
        self.lista_categorias.bind('<<TreeviewSelect>>', self.mostrar_ejemplos)
        self.lista_categorias.pack(fill=tk.Y, expand=True)
        
        # Panel central - Ejemplos y edición
        frame_centro = ttk.Frame(self.root)
        frame_centro.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.txt_ejemplos = scrolledtext.ScrolledText(frame_centro, wrap=tk.WORD)
        self.txt_ejemplos.pack(fill=tk.BOTH, expand=True)
        
        frame_controles = ttk.Frame(frame_centro)
        frame_controles.pack(pady=10)
        
        ttk.Label(frame_controles, text="Sujeto:").pack(side=tk.LEFT)
        self.entry_sujeto = ttk.Entry(frame_controles, width=15)
        self.entry_sujeto.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_controles, text="Verbo:").pack(side=tk.LEFT)
        self.entry_verbo = ttk.Entry(frame_controles, width=15)
        self.entry_verbo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_controles, text="Generar nuevo", 
                  command=self.generar_ejemplo).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_controles, text="Copiar", 
                  command=self.copiar_texto).pack(side=tk.LEFT)
        
        # Panel derecho - Gramática
        frame_der = ttk.Frame(self.root)
        frame_der.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
        
        self.txt_gramatica = scrolledtext.ScrolledText(frame_der, 
                                                     width=30, 
                                                     wrap=tk.WORD,
                                                     state=tk.DISABLED)
        self.txt_gramatica.pack(fill=tk.Y, expand=True)
        self.actualizar_gramatica("\n".join(self.gramatica.values()))
        
    def cargar_categorias(self):
        for categoria in self.categorias:
            self.lista_categorias.insert('', tk.END, text=categoria, iid=categoria)
    
    def mostrar_ejemplos(self, event):
        categoria = self.lista_categorias.selection()[0]
        self.txt_ejemplos.config(state=tk.NORMAL)
        self.txt_ejemplos.delete(1.0, tk.END)
        
        for ejemplo in self.categorias[categoria]:
            self.txt_ejemplos.insert(tk.END, ejemplo + '\n', 'normal')
            self.resaltar_gerundio(ejemplo + '\n')
        
        self.txt_ejemplos.config(state=tk.DISABLED)
    
    def resaltar_gerundio(self, texto):
        palabras = texto.split()
        for palabra in palabras:
            limpia = palabra.strip('.,;¿?¡!').lower()
            if re.search(r'(ando|iendo)$', limpia):
                inicio = self.txt_ejemplos.search(palabra, '1.0', stopindex=tk.END)
                if inicio:
                    fin = f"{start}+{len(palabra)}c"
                    self.txt_ejemplos.tag_add('gerundio', inicio, fin)
        
        self.txt_ejemplos.tag_config('gerundio', underline=True, 
                                   foreground='blue')
    
    def generar_ejemplo(self):
        sujeto = self.entry_sujeto.get().capitalize()
        verbo = self.entry_verbo.get().lower()
        
        if not sujeto or not verbo:
            messagebox.showwarning("Error", "Debe ingresar sujeto y verbo")
            return
        
        gerundio = self.generar_gerundio(verbo)
        nuevo_ejemplo = f"{sujeto} está {gerundio}"
        
        self.txt_ejemplos.config(state=tk.NORMAL)
        self.txt_ejemplos.insert(tk.END, nuevo_ejemplo + '\n', 'normal')
        self.resaltar_gerundio(nuevo_ejemplo + '\n')
        self.txt_ejemplos.config(state=tk.DISABLED)
        
        categoria = self.lista_categorias.selection()[0]
        self.categorias[categoria].append(nuevo_ejemplo)
    
    def generar_gerundio(self, verbo):
        if verbo.endswith('ar'):
            return verbo[:-2] + 'ando'
        elif verbo.endswith(('er', 'ir')):
            return verbo[:-2] + 'iendo'
        return verbo + ' (gerundio irregular)'
    
    def copiar_texto(self):
        texto = self.txt_ejemplos.get(tk.SEL_FIRST, tk.SEL_LAST)
        pyperclip.copy(texto)
    
    def actualizar_gramatica(self, texto):
        self.txt_gramatica.config(state=tk.NORMAL)
        self.txt_gramatica.delete(1.0, tk.END)
        self.txt_gramatica.insert(tk.END, texto)
        self.txt_gramatica.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerundioApp(root)
    root.mainloop()
