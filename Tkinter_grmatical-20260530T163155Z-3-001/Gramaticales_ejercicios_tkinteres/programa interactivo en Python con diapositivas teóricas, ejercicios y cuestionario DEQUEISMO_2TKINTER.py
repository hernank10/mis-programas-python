import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import random

MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "ejemplos.txt"

class AplicacionQueismoDequeismo:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendiendo Queísmo y Dequeísmo")
        self.root.geometry("800x600")
        self.puntaje = 0
        self.current_slide = 0
        self.ejemplos = self.cargar_ejemplos()
        
        self.crear_interfaz_principal()
        
    def cargar_ejemplos(self):
        ejemplos = []
        if os.path.exists(ARCHIVO_EJEMPLOS):
            with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
                for linea in f.readlines():
                    tipo, oracion, correccion = linea.strip().split("|")
                    ejemplos.append((tipo, oracion, correccion))
        return ejemplos
    
    def guardar_ejemplo(self, tipo, oracion, correccion):
        with open(ARCHIVO_EJEMPLOS, "a", encoding="utf-8") as f:
            f.write(f"{tipo}|{oracion}|{correccion}\n")
        self.ejemplos.append((tipo, oracion, correccion))
    
    def crear_interfaz_principal(self):
        self.limpiar_pantalla()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        ttk.Label(main_frame, text="APRENDIENDO QUEÍSMO Y DEQUEÍSMO", 
                 font=("Arial", 16, "bold")).pack(pady=20)
        
        botones = [
            ("📚 Teoría y Ejemplos", self.mostrar_teoria),
            ("✍ Agregar Ejemplo", self.mostrar_formulario_ejemplo),
            ("🎯 Cuestionario Interactivo", self.iniciar_cuestionario),
            ("🗂 Ver Ejemplos", self.mostrar_ejemplos),
            ("🚪 Salir", self.root.destroy)
        ]
        
        for texto, comando in botones:
            ttk.Button(main_frame, text=texto, command=comando, width=30).pack(pady=5)
    
    def mostrar_teoria(self):
        self.limpiar_pantalla()
        teoria = [
            ("Queísmo", "Error de omitir 'de' cuando es necesario:\n\n"
             "Incorrecto: 'Estoy seguro que vendrá'\n"
             "Correcto:   'Estoy seguro DE que vendrá'\n\n"
             "Regla: Si puedes reemplazar con 'de eso', usa DE QUE"),
            
            ("Dequeísmo", "Error de usar 'de que' innecesariamente:\n\n"
             "Incorrecto: 'Pienso de que lloverá'\n"
             "Correcto:   'Pienso QUE lloverá'\n\n"
             "Regla: Si puedes reemplazar con 'eso', usa QUE")
        ]
        
        container = ttk.Frame(self.root)
        container.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.slides = [
            self.crear_diapositiva(container, titulo, contenido) 
            for titulo, contenido in teoria
        ]
        
        nav_frame = ttk.Frame(container)
        nav_frame.pack(pady=10)
        
        ttk.Button(nav_frame, text="Anterior", 
                  command=lambda: self.cambiar_slide(-1)).grid(row=0, column=0, padx=5)
        ttk.Button(nav_frame, text="Siguiente", 
                  command=lambda: self.cambiar_slide(1)).grid(row=0, column=1, padx=5)
        ttk.Button(nav_frame, text="Menú Principal", 
                  command=self.crear_interfaz_principal).grid(row=0, column=2, padx=5)
        
        self.mostrar_slide(0)
    
    def crear_diapositiva(self, parent, titulo, contenido):
        frame = ttk.Frame(parent)
        ttk.Label(frame, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(frame, text=contenido, justify="left").pack(pady=10)
        return frame
    
    def mostrar_slide(self, index):
        if 0 <= index < len(self.slides):
            for slide in self.slides:
                slide.pack_forget()
            self.slides[index].pack(expand=True, fill="both")
            self.current_slide = index
    
    def cambiar_slide(self, direction):
        new_index = self.current_slide + direction
        if 0 <= new_index < len(self.slides):
            self.mostrar_slide(new_index)
    
    def mostrar_formulario_ejemplo(self):
        self.limpiar_pantalla()
        
        form_frame = ttk.Frame(self.root)
        form_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        ttk.Label(form_frame, text="✍ AGREGAR NUEVO EJEMPLO", 
                 font=("Arial", 14)).pack(pady=10)
        
        tipo_var = tk.StringVar()
        ttk.Label(form_frame, text="Tipo de error:").pack()
        ttk.Combobox(form_frame, textvariable=tipo_var, 
                    values=["queismo", "dequeismo"]).pack(pady=5)
        
        ttk.Label(form_frame, text="Oración incorrecta:").pack()
        entrada_incorrecta = ttk.Entry(form_frame, width=50)
        entrada_incorrecta.pack(pady=5)
        
        ttk.Label(form_frame, text="Oración corregida:").pack()
        entrada_correcta = ttk.Entry(form_frame, width=50)
        entrada_correcta.pack(pady=5)
        
        def guardar():
            if len(self.ejemplos) >= MAX_EJEMPLOS:
                messagebox.showerror("Error", f"Límite de {MAX_EJEMPLOS} ejemplos alcanzado")
                return
            
            tipo = tipo_var.get().lower()
            incorrecta = entrada_incorrecta.get().strip()
            correcta = entrada_correcta.get().strip()
            
            if tipo not in ["queismo", "dequeismo"] or not incorrecta or not correcta:
                messagebox.showerror("Error", "Completa todos los campos correctamente")
                return
            
            self.guardar_ejemplo(tipo, incorrecta, correcta)
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            self.crear_interfaz_principal()
        
        ttk.Button(form_frame, text="Guardar Ejemplo", command=guardar).pack(pady=10)
        ttk.Button(form_frame, text="Menú Principal", 
                  command=self.crear_interfaz_principal).pack()
    
    def iniciar_cuestionario(self):
        if not self.ejemplos:
            messagebox.showinfo("Info", "Primero agrega algunos ejemplos")
            return
        
        self.limpiar_pantalla()
        self.puntaje = 0
        self.preguntas = random.sample(self.ejemplos, min(10, len(self.ejemplos)))
        self.current_question = 0
        
        self.quiz_frame = ttk.Frame(self.root)
        self.quiz_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        
        if self.current_question >= len(self.preguntas):
            self.mostrar_resultados()
            return
        
        tipo, incorrecta, correcta = self.preguntas[self.current_question]
        tipo_pregunta = random.choice(["identificacion", "correccion", "clasificacion"])
        
        ttk.Label(self.quiz_frame, text=f"Pregunta {self.current_question + 1}/{len(self.preguntas)}", 
                 font=("Arial", 12)).pack(pady=10)
        
        if tipo_pregunta == "identificacion":
            self.pregunta_identificacion(tipo, incorrecta)
        elif tipo_pregunta == "correccion":
            self.pregunta_correccion(incorrecta, correcta)
        else:
            self.pregunta_clasificacion(incorrecta, correcta)
    
    def pregunta_identificacion(self, tipo, incorrecta):
        ttk.Label(self.quiz_frame, text="Identifica el error en:", 
                 font=("Arial", 12)).pack(pady=5)
        ttk.Label(self.quiz_frame, text=incorrecta, 
                 font=("Arial", 11, "italic")).pack(pady=5)
        
        self.respuesta_var = tk.StringVar()
        opciones = [("Queísmo", "a"), ("Dequeísmo", "b"), ("Correcto", "c")]
        
        for texto, valor in opciones:
            ttk.Radiobutton(self.quiz_frame, text=texto, value=valor, 
                           variable=self.respuesta_var).pack(anchor="w")
        
        ttk.Button(self.quiz_frame, text="Continuar", 
                  command=lambda: self.verificar_respuesta(
                      "a" if tipo == "queismo" else "b" if tipo == "dequeismo" else "c"
                  )).pack(pady=10)
    
    def pregunta_correccion(self, incorrecta, correcta):
        ttk.Label(self.quiz_frame, text="Corrige la oración:", 
                 font=("Arial", 12)).pack(pady=5)
        ttk.Label(self.quiz_frame, text=incorrecta, 
                 font=("Arial", 11, "italic")).pack(pady=5)
        
        self.entrada_correccion = ttk.Entry(self.quiz_frame, width=50)
        self.entrada_correccion.pack(pady=10)
        
        ttk.Button(self.quiz_frame, text="Continuar", 
                  command=lambda: self.verificar_respuesta(
                      self.entrada_correccion.get().strip(), 
                      correcta
                  )).pack()
    
    def pregunta_clasificacion(self, incorrecta, correcta):
        es_correcta = random.random() < 0.5
        oracion = correcta if es_correcta else incorrecta
        
        ttk.Label(self.quiz_frame, text="¿Es correcta esta oración?", 
                 font=("Arial", 12)).pack(pady=5)
        ttk.Label(self.quiz_frame, text=oracion, 
                 font=("Arial", 11, "italic")).pack(pady=5)
        
        self.respuesta_var = tk.StringVar()
        ttk.Radiobutton(self.quiz_frame, text="Correcta", value="a", 
                       variable=self.respuesta_var).pack(anchor="w")
        ttk.Radiobutton(self.quiz_frame, text="Incorrecta", value="b", 
                       variable=self.respuesta_var).pack(anchor="w")
        
        ttk.Button(self.quiz_frame, text="Continuar", 
                  command=lambda: self.verificar_respuesta(
                      "a" if es_correcta else "b"
                  )).pack(pady=10)
    
    def verificar_respuesta(self, correcta, esperada=None):
        respuesta = self.respuesta_var.get() if hasattr(self, 'respuesta_var') else self.entrada_correccion.get().strip()
        
        if esperada is not None:  # Para preguntas de corrección
            correcta = esperada.lower() == respuesta.lower()
        else:
            correcta = respuesta.lower() == correcta.lower()
        
        if correcta:
            self.puntaje += 10
            mensaje = "✅ Respuesta correcta! +10 puntos"
        else:
            mensaje = f"❌ Respuesta incorrecta. La correcta era: {esperada or correcta}"
        
        messagebox.showinfo("Resultado", mensaje)
        self.current_question += 1
        self.mostrar_pregunta()
    
    def mostrar_resultados(self):
        self.limpiar_pantalla()
        result_frame = ttk.Frame(self.root)
        result_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        ttk.Label(result_frame, text="⭐ RESULTADOS FINALES ⭐", 
                 font=("Arial", 16, "bold")).pack(pady=20)
        
        ttk.Label(result_frame, text=f"Puntaje obtenido: {self.puntaje}/100", 
                 font=("Arial", 14)).pack(pady=10)
        
        if self.puntaje == 100:
            mensaje = "🏆 ¡Perfecto! Dominas el tema completamente!"
        elif self.puntaje >= 70:
            mensaje = "👍 ¡Buen trabajo! Sigue practicando"
        else:
            mensaje = "💪 ¡Sigue intentándolo! La práctica hace al maestro"
        
        ttk.Label(result_frame, text=mensaje, font=("Arial", 12)).pack(pady=10)
        ttk.Button(result_frame, text="Menú Principal", 
                  command=self.crear_interfaz_principal).pack(pady=10)
    
    def mostrar_ejemplos(self):
        self.limpiar_pantalla()
        ejemplos_frame = ttk.Frame(self.root)
        ejemplos_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        ttk.Label(ejemplos_frame, text="🗂 EJEMPLOS ALMACENADOS", 
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        scroll = scrolledtext.ScrolledText(ejemplos_frame, wrap=tk.WORD, height=20)
        scroll.pack(expand=True, fill="both")
        
        for idx, (tipo, incorrecta, correcta) in enumerate(self.ejemplos, 1):
            scroll.insert(tk.END, f"{idx}. [{tipo.upper()}]\n")
            scroll.insert(tk.END, f"   Original:   {incorrecta}\n")
            scroll.insert(tk.END, f"   Corregido:  {correcta}\n\n")
        
        scroll.config(state=tk.DISABLED)
        ttk.Button(ejemplos_frame, text="Menú Principal", 
                  command=self.crear_interfaz_principal).pack(pady=10)
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionQueismoDequeismo(root)
    root.mainloop()
