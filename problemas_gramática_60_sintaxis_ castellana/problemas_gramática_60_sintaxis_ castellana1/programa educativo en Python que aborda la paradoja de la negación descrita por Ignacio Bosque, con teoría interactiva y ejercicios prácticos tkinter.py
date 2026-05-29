import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class NegacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paradoja de la Negación - Bosque 1980")
        self.root.geometry("800x600")
        
        self.crear_menu_principal()
        self.cargar_estilos()
        self.ejercicios = [
            {
                "tipo": "opcion_multiple",
                "pregunta": "¿Cuántas interpretaciones tiene 'Es imposible que nada mejore'?",
                "opciones": {"a": "Solo 1", "b": "2 contradictorias", "c": "Depende del verbo"},
                "respuesta": "b",
                "explicacion": "Correcto! Presenta la dualidad existencial/universal descrita por Bosque"
            },
            {
                "tipo": "traduccion",
                "pregunta": "Reescribe la oración para conservar solo la lectura existencial:\n'Ella niega que nada importe'",
                "respuesta": "Ella niega que algo importe",
                "explicacion": "¡Exacto! Sustituir 'nada' por 'algo' elimina la ambigüedad"
            }
        ]
        self.ejercicio_actual = 0
        self.puntaje = 0

    def cargar_estilos(self):
        style = ttk.Style()
        style.configure("Titulo.TLabel", font=('Arial', 14, 'bold'), foreground='#2c3e50')
        style.configure("Botones.TButton", font=('Arial', 12), padding=10)
        style.configure("FeedbackCorrecto.TLabel", foreground='green')
        style.configure("FeedbackError.TLabel", foreground='red')

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        frame = ttk.Frame(self.root)
        frame.pack(expand=True, padx=50, pady=50)
        
        ttk.Label(frame, text="ESTUDIO DE LA AMBIGÜEDAD EN LA NEGACIÓN", style="Titulo.TLabel").pack(pady=20)
        
        botones = [
            ("Teoría", self.mostrar_teoria),
            ("Ejercicios", self.mostrar_ejercicios),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            ttk.Button(frame, text=texto, command=comando, style="Botones.TButton").pack(fill=tk.X, pady=5)

    def mostrar_teoria(self):
        self.limpiar_pantalla()
        
        teoria = """
        LA PARADOJA DE LA NEGACIÓN (Bosque 1980)
        
        1. Ambivalencia de 'nada':
        - Lectura existencial: ¬∃x(P(x)) → "No hay algo que..."
        - Lectura universal negativa: ¬◊¬∀x(P(x)) → "Todo debe..."
        
        2. Factores clave:
           • Modo subjuntivo
           • Posición sintáctica
           • Ámbito de operadores
        
        Ejemplo clásico:
        [Es imposible que nada cambie] ≡ 
           a) ¬∃x(cambiar(x)) 
           b) ¬◊¬∀x(cambiar(x))
        """
        
        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        texto = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 12))
        texto.insert(tk.INSERT, teoria)
        texto.configure(state='disabled')
        texto.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(frame, text="Volver", command=self.crear_menu_principal).pack(pady=10)

    def mostrar_ejercicios(self):
        self.limpiar_pantalla()
        self.ejercicio_actual = 0
        self.puntaje = 0
        self.mostrar_ejercicio_actual()

    def mostrar_ejercicio_actual(self):
        self.limpiar_pantalla()
        ejercicio = self.ejercicios[self.ejercicio_actual]
        
        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text=ejercicio["pregunta"], wraplength=700, style="Titulo.TLabel").pack(pady=10)
        
        if ejercicio["tipo"] == "opcion_multiple":
            self.respuesta_var = tk.StringVar()
            for op, texto in ejercicio["opciones"].items():
                rb = ttk.Radiobutton(frame, text=f"{op}) {texto}", 
                                    variable=self.respuesta_var, 
                                    value=op)
                rb.pack(anchor=tk.W, pady=5)
        else:
            self.entrada_respuesta = ttk.Entry(frame, width=50, font=('Arial', 12))
            self.entrada_respuesta.pack(pady=10)
        
        ttk.Button(frame, text="Verificar", command=lambda: self.verificar_respuesta(ejercicio)).pack(pady=10)
        ttk.Button(frame, text="Volver al menú", command=self.crear_menu_principal).pack(pady=5)

    def verificar_respuesta(self, ejercicio):
        if ejercicio["tipo"] == "opcion_multiple":
            respuesta = self.respuesta_var.get()
        else:
            respuesta = self.entrada_respuesta.get().strip().lower()
        
        correcto = False
        if ejercicio["tipo"] == "opcion_multiple":
            correcto = respuesta == ejercicio["respuesta"]
        else:
            correcto = ejercicio["respuesta"].lower() in respuesta.lower()
        
        if correcto:
            self.puntaje += 1
            mensaje = f"✅ {ejercicio['explicacion']}"
            color = "FeedbackCorrecto.TLabel"
        else:
            mensaje = f"❌ {ejercicio['explicacion']}\nRespuesta correcta: {ejercicio['respuesta']}"
            color = "FeedbackError.TLabel"
        
        feedback = ttk.Label(self.root, text=mensaje, wraplength=700, style=color)
        feedback.pack(pady=10)
        
        self.root.after(2000, self.siguiente_ejercicio)

    def siguiente_ejercicio(self):
        self.ejercicio_actual += 1
        if self.ejercicio_actual < len(self.ejercicios):
            self.mostrar_ejercicio_actual()
        else:
            messagebox.showinfo("Resultado", 
                              f"Puntuación final: {self.puntaje}/{len(self.ejercicios)}")
            self.crear_menu_principal()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NegacionApp(root)
    root.mainloop()
