import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class NumerosOrdinalesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entrenador de Numerales Ordinales")
        self.geometry("800x600")
        self.puntos = 0
        self.ejemplos_base = []
        self.ejemplos_personalizados = []
        self.cargar_datos()
        
        self.crear_interfaz()
        self.mostrar_pantalla_principal()

    def cargar_datos(self):
        try:
            with open('ejemplos_base.json', 'r', encoding='utf-8') as f:
                self.ejemplos_base = json.load(f)
            with open('custom_ejemplos.json', 'r', encoding='utf-8') as f:
                self.ejemplos_personalizados = json.load(f)[:100]
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivos de datos no encontrados")

    def guardar_ejemplos(self):
        with open('custom_ejemplos.json', 'w', encoding='utf-8') as f:
            json.dump(self.ejemplos_personalizados, f, ensure_ascii=False, indent=2)

    def crear_interfaz(self):
        # Frame principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Widgets comunes
        self.lbl_puntos = ttk.Label(self.main_frame, text="Puntos: 0", font=('Arial', 12))
        self.btn_atras = ttk.Button(self.main_frame, text="← Volver", command=self.mostrar_pantalla_principal)

        # Pantallas
        self.pantallas = {
            "principal": self.crear_pantalla_principal(),
            "quiz": self.crear_pantalla_quiz(),
            "crear": self.crear_pantalla_crear(),
            "ver": self.crear_pantalla_ver(),
            "conceptos": self.crear_pantalla_conceptos()
        }

    def mostrar_pantalla(self, nombre):
        for pantalla in self.pantallas.values():
            pantalla.pack_forget()
        self.pantallas[nombre].pack(fill=tk.BOTH, expand=True)
        self.btn_atras.pack_forget()
        if nombre != "principal":
            self.btn_atras.pack(side=tk.BOTTOM, pady=10)

    def mostrar_pantalla_principal(self):
        self.mostrar_pantalla("principal")
        self.lbl_puntos.pack_forget()

    def crear_pantalla_principal(self):
        frame = ttk.Frame(self.main_frame)
        
        ttk.Label(frame, text="Entrenador de Numerales Ordinales", 
                font=('Arial', 16, 'bold')).pack(pady=20)
        
        btn_style = ttk.Style()
        btn_style.configure('TButton', font=('Arial', 12), padding=10)
        
        opciones = [
            ("Cuestionario Base", lambda: self.iniciar_quiz('base')),
            ("Cuestionario Personalizado", lambda: self.iniciar_quiz('personalizado')),
            ("Crear Ejemplos", lambda: self.mostrar_pantalla("crear")),
            ("Ver Ejemplos", lambda: self.mostrar_pantalla("ver")),
            ("Conceptos Clave", lambda: self.mostrar_pantalla("conceptos")),
            ("Salir", self.destroy)
        ]
        
        for texto, comando in opciones:
            ttk.Button(frame, text=texto, command=comando).pack(fill=tk.X, padx=50, pady=5)
        
        return frame

    def crear_pantalla_quiz(self):
        frame = ttk.Frame(self.main_frame)
        self.lbl_contexto = ttk.Label(frame, font=('Arial', 14), wraplength=600)
        self.lbl_numero = ttk.Label(frame, font=('Arial', 24, 'bold'))
        self.ent_respuesta = ttk.Entry(frame, font=('Arial', 14))
        self.btn_verificar = ttk.Button(frame, text="Verificar", command=self.verificar_respuesta)
        self.lbl_feedback = ttk.Label(frame, font=('Arial', 12))
        
        self.lbl_contexto.pack(pady=20)
        self.lbl_numero.pack(pady=10)
        self.ent_respuesta.pack(pady=10, ipady=5, fill=tk.X, padx=50)
        self.btn_verificar.pack(pady=10)
        self.lbl_feedback.pack(pady=10)
        
        return frame

    def iniciar_quiz(self, tipo):
        self.mostrar_pantalla("quiz")
        self.lbl_puntos.pack(side=tk.TOP, anchor=tk.NE, padx=20)
        self.ejemplos_quiz = random.sample(
            self.ejemplos_base if tipo == 'base' else self.ejemplos_personalizados,
            min(50, len(self.ejemplos_base))
        )
        self.indice_pregunta = 0
        self.puntos = 0
        self.actualizar_puntos()
        self.mostrar_siguiente_pregunta()

    def mostrar_siguiente_pregunta(self):
        if self.indice_pregunta < len(self.ejemplos_quiz):
            ej = self.ejemplos_quiz[self.indice_pregunta]
            self.lbl_contexto.config(text=ej['contexto'])
            self.lbl_numero.config(text=ej['numero'])
            self.ent_respuesta.delete(0, tk.END)
            self.lbl_feedback.config(text="")
        else:
            messagebox.showinfo("Quiz Finalizado", 
                              f"Puntuación final: {self.puntos}\n"
                              f"Correctas: {self.puntos//2}/{len(self.ejemplos_quiz)}")
            self.mostrar_pantalla_principal()

    def verificar_respuesta(self):
        respuesta = self.ent_respuesta.get().lower().strip()
        correcta = self.ejemplos_quiz[self.indice_pregunta]['correcto']
        
        if respuesta == correcta:
            self.puntos += 2
            feedback = "✔️ Correcto!"
        else:
            self.puntos = max(0, self.puntos - 1)
            feedback = f"❌ Incorrecto. La respuesta correcta era: {correcta}"
        
        self.actualizar_puntos()
        self.lbl_feedback.config(text=feedback)
        self.indice_pregunta += 1
        self.after(1500, self.mostrar_siguiente_pregunta)

    def actualizar_puntos(self):
        self.lbl_puntos.config(text=f"Puntos: {self.puntos}")

    def crear_pantalla_crear(self):
        frame = ttk.Frame(self.main_frame)
        
        ttk.Label(frame, text="Crear Nuevo Ejemplo", font=('Arial', 14)).pack(pady=10)
        
        self.ent_contexto = ttk.Entry(frame, font=('Arial', 12))
        self.ent_numero = ttk.Entry(frame, font=('Arial', 12))
        self.ent_correcto = ttk.Entry(frame, font=('Arial', 12))
        
        campos = [
            ("Contexto:", self.ent_contexto),
            ("Número:", self.ent_numero),
            ("Forma Correcta:", self.ent_correcto)
        ]
        
        for texto, entrada in campos:
            ttk.Label(frame, text=texto).pack(pady=5)
            entrada.pack(fill=tk.X, padx=50, pady=5)
        
        ttk.Button(frame, text="Guardar", command=self.guardar_ejemplo).pack(pady=20)
        
        return frame

    def guardar_ejemplo(self):
        nuevo = {
            'contexto': self.ent_contexto.get(),
            'numero': self.ent_numero.get(),
            'correcto': self.ent_correcto.get().lower()
        }
        
        if len(self.ejemplos_personalizados) < 100:
            self.ejemplos_personalizados.append(nuevo)
            self.guardar_ejemplos()
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            self.ent_contexto.delete(0, tk.END)
            self.ent_numero.delete(0, tk.END)
            self.ent_correcto.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado")

    def crear_pantalla_ver(self):
        frame = ttk.Frame(self.main_frame)
        self.tree = ttk.Treeview(frame, columns=('Contexto', 'Número', 'Correcto'), show='headings')
        
        self.tree.heading('Contexto', text='Contexto')
        self.tree.heading('Número', text='Número')
        self.tree.heading('Correcto', text='Forma Correcta')
        
        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.actualizar_tabla()
        
        return frame

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for ej in self.ejemplos_personalizados:
            self.tree.insert('', tk.END, values=(ej['contexto'], ej['numero'], ej['correcto']))

    def crear_pantalla_conceptos(self):
        frame = ttk.Frame(self.main_frame)
        texto = """REGLAS PRINCIPALES:

1. Solo se usa 'primero' en fechas: 1.º de enero
2. Para días 2-31 se usan cardinales: 2 de mayo
3. Reyes y papas: ordinales hasta XII, luego cardinales
4. Formas compuestas: trigésimo primero (31.º)
5. Variantes válidas: séptimo/seteno
6. Siglos: ordinales (siglo XXI) o cardinales (siglo 21)"""
        
        ttk.Label(frame, text=texto, font=('Arial', 12), justify=tk.LEFT).pack(padx=20, pady=20)
        return frame

if __name__ == "__main__":
    app = NumerosOrdinalesApp()
    app.mainloop()
