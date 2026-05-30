import json
import tkinter as tk
from tkinter import ttk, messagebox
from random import shuffle

class AplicacionSubordinadas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Subordinadas Adverbiales")
        self.archivo = "ejemplos_subordinadas.json"
        
        self.ejemplos = self.cargar_ejemplos()
        self.crear_interfaz()
    
    def cargar_ejemplos(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def guardar_ejemplos(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.ejemplos, f, ensure_ascii=False, indent=2)
    
    def crear_interfaz(self):
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        
        # Pestañas
        self.practicar_frame = ttk.Frame(self.notebook)
        self.lista_frame = ttk.Frame(self.notebook)
        self.editar_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.practicar_frame, text="Practicar")
        self.notebook.add(self.lista_frame, text="Ver Ejemplos")
        self.notebook.add(self.editar_frame, text="Editar/Crear")
        self.notebook.pack(expand=True, fill='both')
        
        # Configurar cada pestaña
        self.crear_pestaña_practicar()
        self.crear_pestaña_lista()
        self.crear_pestaña_editar()
    
    def crear_pestaña_practicar(self):
        frame = self.practicar_frame
        self.current_practice = None
        self.score = 0
        
        # Controles
        self.lbl_ejemplo = ttk.Label(frame, text="", wraplength=400)
        self.lbl_ejemplo.pack(pady=10)
        
        ttk.Label(frame, text="Antecedente:").pack()
        self.ent_antecedente = ttk.Entry(frame)
        self.ent_antecedente.pack()
        
        ttk.Label(frame, text="Sustitución por adverbio:").pack()
        self.ent_sustitucion = ttk.Entry(frame)
        self.ent_sustitucion.pack()
        
        self.btn_verificar = ttk.Button(frame, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=10)
        
        self.lbl_resultado = ttk.Label(frame, text="")
        self.lbl_resultado.pack()
        
        self.lbl_puntuacion = ttk.Label(frame, text="Puntuación: 0/0")
        self.lbl_puntuacion.pack()
        
        self.iniciar_practica()
    
    def iniciar_practica(self):
        shuffle(self.ejemplos)
        self.practice_queue = self.ejemplos.copy()
        self.mostrar_siguiente_ejemplo()
    
    def mostrar_siguiente_ejemplo(self):
        if not self.practice_queue:
            messagebox.showinfo("Práctica completada", f"Puntuación final: {self.score}/{len(self.ejemplos)*2}")
            return
            
        self.current_practice = self.practice_queue.pop()
        self.lbl_ejemplo.config(text=self.current_practice['oracion'])
        self.ent_antecedente.delete(0, tk.END)
        self.ent_sustitucion.delete(0, tk.END)
    
    def verificar_respuesta(self):
        antecedente = self.ent_antecedente.get().strip()
        sustitucion = self.ent_sustitucion.get().strip()
        
        correcto_antecedente = antecedente.lower() == self.current_practice['antecedente'].lower()
        correcto_sustitucion = sustitucion.lower() == self.current_practice['sustitucion_adverbio'].lower()
        
        resultados = []
        if correcto_antecedente:
            resultados.append("✓ Antecedente correcto")
            self.score +=1
        else:
            resultados.append(f"✗ Antecedente: {self.current_practice['antecedente']}")
        
        if correcto_sustitucion:
            resultados.append("✓ Sustitución correcta")
            self.score +=1
        else:
            resultados.append(f"✗ Sustitución: {self.current_practice['sustitucion_adverbio']}")
        
        self.lbl_resultado.config(text="\n".join(resultados))
        total = (len(self.ejemplos) - len(self.practice_queue)) * 2
        self.lbl_puntuacion.config(text=f"Puntuación: {self.score}/{total}")
        
        self.root.after(2000, self.mostrar_siguiente_ejemplo)
    
    def crear_pestaña_lista(self):
        frame = self.lista_frame
        
        # Treeview para mostrar ejemplos
        self.tree = ttk.Treeview(frame, columns=('Categoría', 'Oración'), show='headings')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Oración', text='Oración')
        self.tree.column('Categoría', width=100)
        self.tree.column('Oración', width=400)
        
        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Actualizar datos
        self.actualizar_lista()
    
    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for ejemplo in self.ejemplos:
            self.tree.insert('', 'end', values=(ejemplo['categoria'], ejemplo['oracion']))
    
    def crear_pestaña_editar(self):
        frame = self.editar_frame
        self.current_edit = None
        
        # Campos del formulario
        campos = [
            ('Categoría', 'categoria'),
            ('Oración principal', 'principal'),
            ('Subordinada', 'subordinada'),
            ('Conjunción', 'conjuncion'),
            ('Antecedente', 'antecedente'),
            ('Sustitución', 'sustitucion_adverbio')
        ]
        
        self.entries = {}
        for i, (label, key) in enumerate(campos):
            ttk.Label(frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[key] = entry
        
        # Botones
        btn_guardar = ttk.Button(frame, text="Guardar", command=self.guardar_edicion)
        btn_guardar.grid(row=len(campos), column=1, pady=10)
        
        btn_nuevo = ttk.Button(frame, text="Nuevo", command=self.nueva_edicion)
        btn_nuevo.grid(row=len(campos), column=0, pady=10)
    
    def nueva_edicion(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.current_edit = None
    
    def guardar_edicion(self):
        datos = {key: entry.get() for key, entry in self.entries.items()}
        
        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        datos['oracion'] = f"{datos['principal']} {datos['subordinada']}"
        
        if self.current_edit is None:
            self.ejemplos.append(datos)
        else:
            self.ejemplos[self.current_edit] = datos
        
        self.guardar_ejemplos()
        self.actualizar_lista()
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        self.nueva_edicion()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSubordinadas(root)
    root.geometry("600x400")
    root.mainloop()
