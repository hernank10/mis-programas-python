import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
import os

class NumeralsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprende Numerales Españoles")
        self.root.geometry("800x600")
        
        # Cargar datos
        self.ejemplos = self.cargar_ejemplos('ejemplos_base.json')
        self.ejemplos_usuario = self.cargar_ejemplos('ejemplos_usuario.json')
        
        # Variables de estado
        self.current_practice_index = 0
        self.quiz_score = 0
        
        # Crear interfaz
        self.crear_menu_principal()
        
    def cargar_ejemplos(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def guardar_ejemplos(self):
        with open('ejemplos_usuario.json', 'w', encoding='utf-8') as f:
            json.dump(self.ejemplos_usuario, f, ensure_ascii=False)

    def crear_menu_principal(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="¡Bienvenido al Tutor de Numerales!", 
                 font=('Helvetica', 16, 'bold')).pack(pady=20)
        
        botones = [
            ("Practicar Ejemplos", self.practicar_ejemplos),
            ("Conceptos Teóricos", self.mostrar_conceptos),
            ("Cuestionario Interactivo", self.iniciar_cuestionario),
            ("Mis Ejemplos", self.gestionar_ejemplos),
            ("Salir", self.root.destroy)
        ]
        
        for texto, comando in botones:
            ttk.Button(frame, text=texto, command=comando, width=30).pack(pady=5)

    # --- MÓDULO DE PRÁCTICA ---
    def practicar_ejemplos(self):
        self.current_practice_index = 0
        self.practice_window = tk.Toplevel(self.root)
        self.practice_window.title("Práctica de Ejemplos")
        
        self.lbl_instruccion = ttk.Label(self.practice_window, text="", font=('Helvetica', 12))
        self.lbl_instruccion.pack(pady=20)
        
        self.ent_respuesta = ttk.Entry(self.practice_window, width=50)
        self.ent_respuesta.pack(pady=10)
        
        btn_frame = ttk.Frame(self.practice_window)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_respuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Saltar", command=self.siguiente_ejemplo).pack(side=tk.LEFT, padx=5)
        
        self.siguiente_ejemplo()
    
    def siguiente_ejemplo(self):
        if self.current_practice_index < len(self.ejemplos + self.ejemplos_usuario):
            ejemplo = (self.ejemplos + self.ejemplos_usuario)[self.current_practice_index]
            self.lbl_instruccion.config(
                text=f"Ejemplo {self.current_practice_index+1}/{len(self.ejemplos + self.ejemplos_usuario)}\n\n{ejemplo['frase']}"
            )
            self.ent_respuesta.delete(0, tk.END)
            self.current_practice_index += 1
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
            self.practice_window.destroy()
    
    def verificar_respuesta(self):
        respuesta = self.ent_respuesta.get().strip()
        ejemplo = (self.ejemplos + self.ejemplos_usuario)[self.current_practice_index-1]
        
        if respuesta.lower() == ejemplo["respuesta"].lower():
            messagebox.showinfo("Resultado", "✅ ¡Respuesta Correcta!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. La respuesta correcta era:\n{ejemplo['respuesta']}")
        
        self.siguiente_ejemplo()

    # --- MÓDULO TEÓRICO ---
    def mostrar_conceptos(self):
        concept_window = tk.Toplevel(self.root)
        concept_window.title("Conceptos Teóricos")
        
        texto = """CONCEPTOS CLAVE:

1. NUMERALES DISTRIBUTIVOS:
   - Sendos/sendas: Siempre en plural. Ej: 'Recibieron sendos premios'
   - Cada: Invariable. Ej: 'Cada tres horas'

2. NUMERALES MÚLTIPLOS:
   - Doble, triple, céntuplo
   - Sufijo -tanto: 'cuatrotanto'

3. NUMERALES PARTITIVOS:
   - Fracciones: tercio, cuarto
   - Sufijo -avo: onceavo, veinteavo

4. COLECTIVOS:
   - Grupos: docena, centenar, millar"""
        
        text_widget = tk.Text(concept_window, wrap=tk.WORD, padx=20, pady=20)
        text_widget.insert(tk.END, texto)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH, expand=True)

    # --- CUESTIONARIO ---
    def iniciar_cuestionario(self):
        self.quiz_score = 0
        self.quiz_questions = random.sample(self.ejemplos + self.ejemplos_usuario, 10)
        self.current_question = 0
        
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Cuestionario")
        
        self.lbl_question = ttk.Label(self.quiz_window, text="", wraplength=600)
        self.lbl_question.pack(pady=20)
        
        btn_frame = ttk.Frame(self.quiz_window)
        btn_frame.pack(pady=15)
        
        self.category_buttons = []
        for i, cat in enumerate(["Distributivo", "Múltiplo", "Partitivo", "Colectivo"]):
            btn = ttk.Button(btn_frame, text=cat, command=lambda c=i: self.verificar_categoria(c))
            btn.pack(side=tk.LEFT, padx=5)
            self.category_buttons.append(btn)
        
        self.mostrar_siguiente_pregunta()
    
    def mostrar_siguiente_pregunta(self):
        if self.current_question < len(self.quiz_questions):
            ejemplo = self.quiz_questions[self.current_question]
            self.lbl_question.config(
                text=f"Pregunta {self.current_question+1}/10\n\nClasifica:\n\n{ejemplo['frase']}"
            )
            self.current_question += 1
        else:
            messagebox.showinfo("Resultado", f"Puntuación final: {self.quiz_score}/10")
            self.quiz_window.destroy()
    
    def verificar_categoria(self, categoria_seleccionada):
        ejemplo = self.quiz_questions[self.current_question-1]
        categorias = ["distributivos", "múltiplos", "partitivos", "colectivos"]
        
        if categorias[categoria_seleccionada] == ejemplo["categoria"]:
            self.quiz_score += 1
            messagebox.showinfo("Resultado", "✅ Correcto!")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. Categoría correcta: {ejemplo['categoria'].capitalize()}")
        
        self.mostrar_siguiente_pregunta()

    # --- GESTIÓN DE EJEMPLOS ---
    def gestionar_ejemplos(self):
        self.manage_window = tk.Toplevel(self.root)
        self.manage_window.title("Gestión de Ejemplos")
        
        ttk.Button(self.manage_window, text="Crear Nuevo Ejemplo", 
                  command=self.crear_nuevo_ejemplo).pack(pady=10)
        ttk.Button(self.manage_window, text="Ver Ejemplos Guardados", 
                  command=self.mostrar_ejemplos).pack(pady=10)
        ttk.Button(self.manage_window, text="Guardar Cambios", 
                  command=self.guardar_ejemplos).pack(pady=10)
    
    def crear_nuevo_ejemplo(self):
        nueva_ventana = tk.Toplevel(self.manage_window)
        nueva_ventana.title("Nuevo Ejemplo")
        
        ttk.Label(nueva_ventana, text="Frase con espacio para numeral (_):").pack(pady=5)
        entrada_frase = ttk.Entry(nueva_ventana, width=50)
        entrada_frase.pack(pady=5)
        
        ttk.Label(nueva_ventana, text="Respuesta correcta:").pack(pady=5)
        entrada_respuesta = ttk.Entry(nueva_ventana)
        entrada_respuesta.pack(pady=5)
        
        ttk.Label(nueva_ventana, text="Categoría:").pack(pady=5)
        combo_categoria = ttk.Combobox(nueva_ventana, 
                                     values=["distributivos", "múltiplos", "partitivos", "colectivos"])
        combo_categoria.pack(pady=5)
        
        def guardar():
            nuevo_ejemplo = {
                "frase": entrada_frase.get(),
                "respuesta": entrada_respuesta.get(),
                "categoria": combo_categoria.get()
            }
            self.ejemplos_usuario.append(nuevo_ejemplo)
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            nueva_ventana.destroy()
        
        ttk.Button(nueva_ventana, text="Guardar", command=guardar).pack(pady=10)
    
    def mostrar_ejemplos(self):
        ventana_lista = tk.Toplevel(self.manage_window)
        ventana_lista.title("Ejemplos Guardados")
        
        scrollbar = ttk.Scrollbar(ventana_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista = tk.Listbox(ventana_lista, yscrollcommand=scrollbar.set, width=80)
        for ej in self.ejemplos_usuario:
            lista.insert(tk.END, f"{ej['frase']} -> {ej['respuesta']} ({ej['categoria']})")
        lista.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=lista.yview)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumeralsApp(root)
    root.mainloop()
