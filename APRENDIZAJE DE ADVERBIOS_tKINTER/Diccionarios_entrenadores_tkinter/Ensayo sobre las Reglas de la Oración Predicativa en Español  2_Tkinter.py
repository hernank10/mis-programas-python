# -*- coding: utf-8 -*-
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

MAX_EJEMPLOS = 100

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Ejemplos Gramaticales")
        self.geometry("800x600")
        
        # Cargar datos
        self.datos = self.cargar_datos()
        self.categoria_actual = ""
        
        # Configurar interfaz
        self.crear_widgets()
        self.actualizar_treeview()
        
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo (Categorías y ejemplos)
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # Treeview para categorías y ejemplos
        self.tree = ttk.Treeview(left_frame, columns=('Ejemplos'), show='tree')
        self.tree.heading('#0', text='Categorías')
        self.tree.pack(fill=tk.Y, expand=True)
        
        # Panel derecho (Controles)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Controles de gestión
        ttk.Label(right_frame, text="Categoría:").grid(row=0, column=0, sticky=tk.W)
        self.cat_combobox = ttk.Combobox(right_frame, values=list(self.datos.keys()))
        self.cat_combobox.grid(row=0, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(right_frame, text="Ejemplo:").grid(row=1, column=0, sticky=tk.W)
        self.ej_entry = ttk.Entry(right_frame, width=40)
        self.ej_entry.grid(row=1, column=1, sticky=tk.EW, padx=5)
        
        btn_frame = ttk.Frame(right_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Agregar", command=self.agregar_ejemplo).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Editar", command=self.editar_ejemplo).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_ejemplo).pack(side=tk.LEFT, padx=2)
        
        # Área de diapositiva
        ttk.Label(right_frame, text="Diapositiva:").grid(row=3, column=0, sticky=tk.W)
        self.diapositiva_txt = scrolledtext.ScrolledText(right_frame, width=50, height=15)
        self.diapositiva_txt.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
        
        # Botones inferiores
        ttk.Button(right_frame, text="Generar Diapositiva", command=self.generar_diapositiva).grid(row=5, column=0, pady=5)
        ttk.Button(right_frame, text="Guardar Todo", command=self.guardar_datos).grid(row=5, column=1, pady=5)
        
        # Configurar expansión
        right_frame.columnconfigure(1, weight=1)
        right_frame.rowconfigure(4, weight=1)
        
        # Eventos
        self.tree.bind('<<TreeviewSelect>>', self.seleccionar_elemento)
    
    def cargar_datos(self, archivo="ejemplos.json"):
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "Predicación Completa(Verbos que no requieren complementos: ej:El sol brilla (Brillar no necesita complemento)": [],
            "Predicación Incompleta(Verbos que necesitan complementos)(CD):ej:El niño come una manzana (CD:una manzana).": [],
            "Oraciones Transitivas(Verbos con CD):ej:El jardinero podó los árboles (CD:los árboles).": [],
            "Oraciones Intransitivas(Verbos sin CD, aunque pueden tener otros complementos): ej: El abuelo durmió toda la tarde (CC de tiempo). ": [],
            "Complemento Indirecto( Complementos Indirectos con A y Para): ej:Dedicó el poema a su esposa": []
        }
    
    def guardar_datos(self):
        with open("ejemplos.json", "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Guardado", "Datos guardados correctamente")
    
    def actualizar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for categoria, ejemplos in self.datos.items():
            parent = self.tree.insert('', tk.END, text=f"{categoria} ({len(ejemplos)}/{MAX_EJEMPLOS})")
            for ej in ejemplos:
                self.tree.insert(parent, tk.END, text=ej)
    
    def seleccionar_elemento(self, event):
        item = self.tree.selection()[0]
        texto = self.tree.item(item, 'text')
        
        if self.tree.parent(item) == '':  # Es categoría
            self.categoria_actual = texto.split(' (')[0]
            self.cat_combobox.set(self.categoria_actual)
        else:  # Es ejemplo
            self.ej_entry.delete(0, tk.END)
            self.ej_entry.insert(0, texto)
    
    def agregar_ejemplo(self):
        categoria = self.cat_combobox.get()
        ejemplo = self.ej_entry.get().strip()
        
        if not categoria:
            messagebox.showerror("Error", "Seleccione una categoría")
            return
            
        if not ejemplo:
            messagebox.showerror("Error", "Escriba un ejemplo")
            return
            
        if len(self.datos[categoria]) >= MAX_EJEMPLOS:
            messagebox.showerror("Error", f"Límite de {MAX_EJEMPLOS} ejemplos alcanzado")
            return
            
        self.datos[categoria].append(ejemplo)
        self.actualizar_treeview()
        self.ej_entry.delete(0, tk.END)
    
    def editar_ejemplo(self):
        categoria = self.cat_combobox.get()
        nuevo_ej = self.ej_entry.get().strip()
        
        if not categoria or not nuevo_ej:
            messagebox.showerror("Error", "Seleccione categoría y ejemplo")
            return
            
        try:
            item = self.tree.selection()[0]
            parent = self.tree.parent(item)
            if parent == '':  # Se seleccionó categoría en vez de ejemplo
                raise IndexError
                
            index = self.tree.index(item)
            self.datos[categoria][index] = nuevo_ej
            self.actualizar_treeview()
        except (IndexError, KeyError):
            messagebox.showerror("Error", "Seleccione un ejemplo para editar")
    
    def eliminar_ejemplo(self):
        categoria = self.cat_combobox.get()
        
        try:
            item = self.tree.selection()[0]
            parent = self.tree.parent(item)
            if parent == '':  # Se seleccionó categoría
                raise IndexError
                
            index = self.tree.index(item)
            del self.datos[categoria][index]
            self.actualizar_treeview()
        except (IndexError, KeyError):
            messagebox.showerror("Error", "Seleccione un ejemplo para eliminar")
    
    def generar_diapositiva(self):
        contenido = "--- CLASIFICACIÓN DE ORACIONES ---\n\n"
        for categoria, ejemplos in self.datos.items():
            contenido += f"## {categoria} ##\n"
            for i, ej in enumerate(ejemplos, 1):
                contenido += f"{i}. {ej}\n"
            contenido += "\n"
        
        self.diapositiva_txt.delete(1.0, tk.END)
        self.diapositiva_txt.insert(tk.END, contenido)
        messagebox.showinfo("Listo", "Diapositiva generada en el panel")
    
    def on_closing(self):
        if messagebox.askyesno("Salir", "¿Desea guardar los cambios antes de salir?"):
            self.guardar_datos()
        self.destroy()

if __name__ == "__main__":
    app = Aplicacion()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
