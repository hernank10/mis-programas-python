import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class GramaticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Estructuras Gramaticales")
        self.root.geometry("1000x700")
        
        # Configuración inicial
        self.total_user_ejemplos = 0
        self.current_review_index = 0
        self.user_ejemplos = []
        
        # Estructuras gramaticales
        self.estructuras = {
            "Con + infinitivo": {
                "función": "Acción acompañada/condición suficiente",
                "ejemplos": [
                    "Con estudiar todos los días, aprobarás el examen.",
                    "Con llegar temprano, evitamos las multas."
                ]
            },
            "Después de + infinitivo": {
                "función": "Acción posterior",
                "ejemplos": [
                    "Después de comer, lavamos los platos.",
                    "Después de correr, me duele el cuerpo."
                ]
            },
            # ... (agregar otras estructuras)
        }
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Pestañas
        self.crear_pestana_info()
        self.crear_pestana_practica()
        self.crear_pestana_creacion()
        self.crear_pestana_revision()
    
    def crear_pestana_info(self):
        # Pestaña de información
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Estructuras")
        
        # Treeview para mostrar estructuras
        self.tree = ttk.Treeview(frame, columns=('Función', 'Ejemplos'), show='headings')
        self.tree.heading('#0', text='Estructura')
        self.tree.heading('Función', text='Función')
        self.tree.heading('Ejemplos', text='Ejemplos')
        
        # Scrollbar
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        
        # Insertar datos
        for estructura, datos in self.estructuras.items():
            ejemplos = "\n".join(datos['ejemplos'])
            self.tree.insert('', 'end', text=estructura, 
                            values=(datos['función'], ejemplos))
        
        self.tree.pack(side='left', fill='both', expand=True)
        scroll.pack(side='right', fill='y')
    
    def crear_pestana_practica(self):
        # Pestaña de práctica
        self.frame_practica = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_practica, text="Práctica")
        
        # Componentes
        lbl_instruccion = ttk.Label(self.frame_practica, 
                                  text="Completa la oración:", 
                                  font=('Arial', 14))
        lbl_instruccion.pack(pady=10)
        
        self.lbl_oracion = ttk.Label(self.frame_practica, 
                                   font=('Arial', 12), 
                                   wraplength=600)
        self.lbl_oracion.pack(pady=10)
        
        self.ent_respuesta = ttk.Entry(self.frame_practica, font=('Arial', 12))
        self.ent_respuesta.pack(pady=10, ipadx=50)
        
        btn_verificar = ttk.Button(self.frame_practica, text="Verificar", 
                                 command=self.verificar_respuesta)
        btn_verificar.pack(pady=10)
        
        self.lbl_resultado = ttk.Label(self.frame_practica, font=('Arial', 12))
        self.lbl_resultado.pack(pady=10)
        
        self.nueva_oracion_practica()
    
    def crear_pestana_creacion(self):
        # Pestaña de creación
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Crear Oraciones")
        
        # Componentes
        lbl_estructura = ttk.Label(frame, text="Selecciona una estructura:")
        lbl_estructura.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.cmb_estructura = ttk.Combobox(frame, 
                                          values=list(self.estructuras.keys()),
                                          state='readonly')
        self.cmb_estructura.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        
        self.txt_oracion = scrolledtext.ScrolledText(frame, width=60, height=4,
                                                   font=('Arial', 12))
        self.txt_oracion.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        btn_guardar = ttk.Button(frame, text="Guardar Oración", 
                               command=self.guardar_oracion)
        btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.lbl_contador = ttk.Label(frame, text="Ejemplos guardados: 0/100")
        self.lbl_contador.grid(row=3, column=0, columnspan=2)
    
    def crear_pestana_revision(self):
        # Pestaña de revisión
        self.frame_revision = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_revision, text="Revisión")
        
        # Componentes
        self.lbl_revision = ttk.Label(self.frame_revision, 
                                     font=('Arial', 14),
                                     wraplength=600)
        self.lbl_revision.pack(pady=20)
        
        self.txt_intento = scrolledtext.ScrolledText(self.frame_revision, 
                                                   width=60, height=4,
                                                   font=('Arial', 12))
        self.txt_intento.pack(pady=10)
        
        btn_comparar = ttk.Button(self.frame_revision, text="Comparar", 
                                command=self.comparar_intento)
        btn_comparar.pack(pady=10)
        
        self.lbl_comparacion = ttk.Label(self.frame_revision, 
                                       font=('Arial', 12),
                                       wraplength=600)
        self.lbl_comparacion.pack(pady=10)
        
        btn_siguiente = ttk.Button(self.frame_revision, text="Siguiente", 
                                 command=self.siguiente_ejemplo)
        btn_siguiente.pack(pady=10)
    
    def nueva_oracion_practica(self):
        todas_oraciones = []
        for datos in self.estructuras.values():
            todas_oraciones.extend(datos['ejemplos'])
        
        if todas_oraciones:
            self.oracion_actual = random.choice(todas_oraciones)
            parte_blanco = self.oracion_actual.split()[0]
            self.oracion_blanco = self.oracion_actual.replace(parte_blanco, "______")
            self.lbl_oracion.config(text=self.oracion_blanco)
            self.ent_respuesta.delete(0, 'end')
            self.lbl_resultado.config(text="")
    
    def verificar_respuesta(self):
        respuesta = self.ent_respuesta.get().strip()
        correcta = self.oracion_actual.split()[0]
        
        if respuesta.lower() == correcta.lower():
            self.lbl_resultado.config(text="✅ ¡Correcto!", foreground='green')
        else:
            self.lbl_resultado.config(text=f"❌ Incorrecto. La respuesta correcta es: {correcta}", 
                                    foreground='red')
        
        self.root.after(1500, self.nueva_oracion_practica)
    
    def guardar_oracion(self):
        estructura = self.cmb_estructura.get()
        oracion = self.txt_oracion.get("1.0", 'end').strip()
        
        if not estructura:
            messagebox.showwarning("Advertencia", "Selecciona una estructura primero")
            return
            
        if not oracion:
            messagebox.showwarning("Advertencia", "Escribe una oración antes de guardar")
            return
            
        if self.total_user_ejemplos >= 100:
            messagebox.showwarning("Límite alcanzado", "Has llegado al máximo de 100 ejemplos")
            return
            
        # Agregar a la estructura correspondiente
        if estructura in self.estructuras:
            self.estructuras[estructura]['ejemplos'].append(oracion)
            self.total_user_ejemplos += 1
            self.user_ejemplos.append(oracion)
            self.actualizar_contador()
            messagebox.showinfo("Éxito", "Oración guardada correctamente")
            self.txt_oracion.delete('1.0', 'end')
    
    def actualizar_contador(self):
        self.lbl_contador.config(text=f"Ejemplos guardados: {self.total_user_ejemplos}/100")
    
    def iniciar_revision(self):
        if not self.user_ejemplos:
            messagebox.showinfo("Información", "Crea algunos ejemplos primero")
            return
            
        self.current_review_index = 0
        self.mostrar_ejemplo_revision()
    
    def mostrar_ejemplo_revision(self):
        if self.current_review_index < len(self.user_ejemplos):
            self.lbl_revision.config(text=self.user_ejemplos[self.current_review_index])
            self.txt_intento.delete('1.0', 'end')
            self.lbl_comparacion.config(text="")
    
    def comparar_intento(self):
        original = self.user_ejemplos[self.current_review_index]
        intento = self.txt_intento.get("1.0", 'end').strip()
        
        comparacion = f"Original: {original}\nTu versión: {intento}"
        self.lbl_comparacion.config(text=comparacion)
    
    def siguiente_ejemplo(self):
        self.current_review_index += 1
        if self.current_review_index < len(self.user_ejemplos):
            self.mostrar_ejemplo_revision()
        else:
            messagebox.showinfo("Fin", "¡Has revisado todos tus ejemplos!")
            self.current_review_index = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = GramaticaApp(root)
    root.mainloop()
