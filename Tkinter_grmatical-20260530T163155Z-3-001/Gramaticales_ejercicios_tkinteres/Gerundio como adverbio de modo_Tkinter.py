import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re

class GerundioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Gerundios")
        self.total_oraciones = 0
        self.categoria_actual = None
        
        self.categorias = {
            '1': {
                'nombre': 'Gerundio como adverbio de modo',
                'ejemplos': [
                    "El niño pasó la clase **platicando**.",
                    "Mi hermana llegó **saltando** de alegría.",
                    "Vengo **muriéndome** de hambre."
                ]
            },
            '2': {
                'nombre': 'Gerundio antepuesto/pospuesto',
                'ejemplos': [
                    "**Gritando**, el profesor explicó la lección.",
                    "El profesor explicó la lección **gritando**."
                ]
            },
            '3': {
                'nombre': 'Estructuras elípticas',
                'ejemplos': [
                    "Tú siempre **trabajando**, y tu hijo, **durmiendo**.",
                    "Yo **leyendo**, ellos **viendo** televisión."
                ]
            }
        }
        
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        # Marco principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Práctica de Gerundios como Adverbio", 
                 font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        # Progreso
        self.progreso = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, 
                                       length=300, mode='determinate')
        self.progreso.pack(pady=10)
        self.actualizar_progreso()
        
        # Botones de categorías
        categorias_frame = ttk.Frame(main_frame)
        categorias_frame.pack(pady=20)
        
        for key in self.categorias:
            btn = ttk.Button(categorias_frame, text=self.categorias[key]['nombre'],
                            command=lambda k=key: self.abrir_categoria(k))
            btn.pack(side=tk.LEFT, padx=10, pady=5)
            
        # Botón de salida
        ttk.Button(main_frame, text="Salir", command=self.root.quit).pack(pady=10)
    
    def actualizar_progreso(self):
        self.progreso['value'] = self.total_oraciones
        self.root.title(f"Práctica de Gerundios ({self.total_oraciones}/100)")
        
    def abrir_categoria(self, categoria_key):
        if self.total_oraciones >= 100:
            messagebox.showinfo("¡Completado!", "Ya has alcanzado las 100 oraciones")
            return
            
        self.categoria_actual = categoria_key
        self.contador = 0
        
        # Crear ventana de categoría
        self.cat_window = tk.Toplevel(self.root)
        self.cat_window.title(f"Práctica: {self.categorias[categoria_key]['nombre']}")
        
        # Marco de contenido
        content_frame = ttk.Frame(self.cat_window, padding=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ejemplos
        ttk.Label(content_frame, text="Ejemplos:", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W)
        for ejemplo in self.categorias[categoria_key]['ejemplos']:
            ttk.Label(content_frame, text=ejemplo.replace('**', '')).pack(anchor=tk.W)
        
        # Entrada de texto
        ttk.Label(content_frame, text="\nEscribe tu oración:", font=('Helvetica', 11)).pack(anchor=tk.W)
        
        self.txt_entrada = scrolledtext.ScrolledText(content_frame, height=4, width=50)
        self.txt_entrada.pack(pady=10)
        self.txt_entrada.bind("<Return>", lambda e: self.procesar_oracion())
        
        # Botón de envío
        ttk.Button(content_frame, text="Enviar oración", 
                  command=self.procesar_oracion).pack(pady=5)
        
        # Contador
        self.lbl_contador = ttk.Label(content_frame, 
                                    text=f"Oraciones creadas: {self.contador}/10")
        self.lbl_contador.pack()
    
    def subrayar_gerundios(self, texto):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            limpia = re.sub(r'[^\wáéíóúñ]', '', palabra.lower())
            if re.search(r'(ando|iendo)$', limpia):
                resultado.append(f"[{palabra}]")
            else:
                resultado.append(palabra)
        return ' '.join(resultado)
    
    def procesar_oracion(self):
        texto = self.txt_entrada.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Entrada vacía", "Por favor escribe una oración")
            return
            
        if self.contador >= 10:
            messagebox.showinfo("Categoría completa", "¡Has completado 10 oraciones!")
            self.cat_window.destroy()
            return
            
        # Subrayar gerundios
        texto_procesado = self.subrayar_gerundios(texto)
        messagebox.showinfo("Gerundio subrayado", f"Tu oración:\n{texto_procesado}")
        
        self.contador += 1
        self.total_oraciones += 1
        self.lbl_contador.config(text=f"Oraciones creadas: {self.contador}/10")
        self.actualizar_progreso()
        self.txt_entrada.delete("1.0", tk.END)
        
        if self.contador >= 10:
            self.cat_window.destroy()
            if self.total_oraciones >= 100:
                messagebox.showinfo("¡Felicidades!", "Has alcanzado las 100 oraciones")

if __name__ == "__main__":
    root = tk.Tk()
    app = GerundioApp(root)
    root.mainloop()
