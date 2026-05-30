import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

# Configuración inicial
TEORIA = """=== TEORÍA: EL COMPLEMENTO DIRECTO (CD) ===

1. Definición: El CD es la palabra o grupo de palabras que recibe directamente la acción del verbo.
2. Identificación: Pregunte "¿Qué + verbo?" o "¿A quién + verbo?".
3. Sustitución: Reemplazable por "lo", "la", "los", "las".
4. Voz pasiva: El CD se convierte en sujeto paciente."""

preguntas = []

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Complemento Directo")
        self.geometry("800x600")
        
        # Contenedor principal
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Crear frames
        self.frames = {}
        for F in (MenuPrincipal, Teoria, Practicar, CrearEjemplos):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_frame(MenuPrincipal)
    
    def mostrar_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MenuPrincipal(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="Menú Principal", font=('Arial', 20)).pack(pady=20)
        
        botones = [
            ("Teoría", Teoria),
            ("Practicar", Practicar),
            ("Crear Ejemplos", CrearEjemplos),
            ("Salir", lambda: self.controller.destroy())
        ]
        
        for texto, comando in botones:
            ttk.Button(self, text=texto, 
                      command=lambda c=comando: controller.mostrar_frame(c) if isinstance(c, type) else c(),
                      width=20).pack(pady=5)

class Teoria(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="Teoría del Complemento Directo", font=('Arial', 16)).pack(pady=10)
        texto = tk.Text(self, wrap="word", width=80, height=20)
        texto.insert("1.0", TEORIA)
        texto.config(state="disabled")
        texto.pack(padx=10, pady=10)
        
        ttk.Button(self, text="Regresar", command=lambda: controller.mostrar_frame(MenuPrincipal)).pack()

class Practicar(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.puntaje = 0
        self.indice_pregunta = 0
        self.modo = ""
        
        self.configurar_ui()
    
    def configurar_ui(self):
        ttk.Label(self, text="Modo de Práctica", font=('Arial', 16)).pack(pady=10)
        
        self.contenedor_pregunta = ttk.Frame(self)
        self.contenedor_pregunta.pack(pady=20)
        
        ttk.Button(self, text="Regresar", command=lambda: self.controller.mostrar_frame(MenuPrincipal)).pack()
    
    def iniciar_practica(self, modo):
        self.modo = modo
        self.indice_pregunta = 0
        self.puntaje = 0
        random.shuffle(preguntas)
        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        for widget in self.contenedor_pregunta.winfo_children():
            widget.destroy()
        
        if self.indice_pregunta >= len(preguntas):
            self.mostrar_resultados()
            return
        
        pregunta = preguntas[self.indice_pregunta]
        ttk.Label(self.contenedor_pregunta, text=pregunta["oracion"].replace("[", "").replace("]", ""),
                 wraplength=600).pack(pady=10)
        
        if self.modo == "opcion_multiple":
            self.ui_opcion_multiple(pregunta)
        elif self.modo == "escribir":
            self.ui_escribir(pregunta)
        elif self.modo == "verificar":
            self.ui_verificar(pregunta)
    
    def ui_opcion_multiple(self, pregunta):
        opciones = [pregunta["cd_correcto"]] + pregunta["opciones_incorrectas"]
        random.shuffle(opciones)
        
        self.respuesta = tk.StringVar()
        for i, opcion in enumerate(opciones):
            ttk.Radiobutton(self.contenedor_pregunta, 
                           text=opcion,
                           variable=self.respuesta,
                           value=opcion).pack(anchor="w")
        
        ttk.Button(self.contenedor_pregunta, text="Responder", 
                  command=lambda: self.verificar_respuesta(opciones)).pack(pady=10)
    
    def ui_escribir(self, pregunta):
        self.entrada = ttk.Entry(self.contenedor_pregunta, width=50)
        self.entrada.pack(pady=10)
        ttk.Button(self.contenedor_pregunta, text="Responder",
                  command=lambda: self.verificar_respuesta(self.entrada.get())).pack()
    
    def ui_verificar(self, pregunta):
        es_correcta = random.choice([True, False])
        if es_correcta:
            self.respuesta_correcta = True
            texto = pregunta["oracion"]
        else:
            texto = pregunta["oracion"].replace(
                f"[{pregunta['cd_correcto']}]", 
                f"[{random.choice(pregunta['opciones_incorrectas'])}]"
            )
            self.respuesta_correcta = False
        
        ttk.Label(self.contenedor_pregunta, text=texto.replace("[", "").replace("]", ""),
                 wraplength=600).pack()
        
        ttk.Button(self.contenedor_pregunta, text="Sí", 
                  command=lambda: self.verificar_respuesta(True)).pack(side="left", padx=20)
        ttk.Button(self.contenedor_pregunta, text="No", 
                  command=lambda: self.verificar_respuesta(False)).pack(side="right", padx=20)
    
    def verificar_respuesta(self, respuesta):
        pregunta = preguntas[self.indice_pregunta]
        correcto = False
        
        if self.modo == "opcion_multiple":
            correcto = (respuesta == pregunta["cd_correcto"])
        elif self.modo == "escribir":
            correcto = (respuesta.strip().lower() == pregunta["cd_correcto"].lower())
        elif self.modo == "verificar":
            correcto = (respuesta == self.respuesta_correcta)
        
        if correcto:
            self.puntaje += 1
            mensaje = "¡Respuesta correcta! ✅"
        else:
            mensaje = f"❌ Incorrecto. La respuesta correcta era: {pregunta['cd_correcto']}"
        
        messagebox.showinfo("Resultado", mensaje)
        self.indice_pregunta += 1
        self.mostrar_pregunta()
    
    def mostrar_resultados(self):
        for widget in self.contenedor_pregunta.winfo_children():
            widget.destroy()
        
        porcentaje = (self.puntaje / len(preguntas)) * 100 if preguntas else 0
        ttk.Label(self.contenedor_pregunta, 
                 text=f"Puntaje final: {self.puntaje}/{len(preguntas)}\n({porcentaje:.1f}%)",
                 font=('Arial', 14)).pack(pady=20)
        ttk.Button(self.contenedor_pregunta, text="Volver a intentar",
                  command=lambda: self.iniciar_practica(self.modo)).pack()

class CrearEjemplos(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        ttk.Label(self, text="Crear Nuevos Ejemplos", font=('Arial', 16)).pack(pady=10)
        
        self.formulario = ttk.Frame(self)
        self.formulario.pack(pady=20)
        
        ttk.Label(self.formulario, text="Oración con CD entre []:").grid(row=0, column=0, sticky="w")
        self.entrada_oracion = ttk.Entry(self.formulario, width=50)
        self.entrada_oracion.grid(row=0, column=1, padx=5)
        
        self.entradas_incorrectas = []
        for i in range(3):
            ttk.Label(self.formulario, text=f"Opción incorrecta {i+1}:").grid(row=i+1, column=0, sticky="w")
            entrada = ttk.Entry(self.formulario, width=50)
            entrada.grid(row=i+1, column=1, padx=5, pady=2)
            self.entradas_incorrectas.append(entrada)
        
        ttk.Button(self, text="Guardar Ejemplo", command=self.guardar_ejemplo).pack(pady=10)
        ttk.Button(self, text="Regresar", command=lambda: controller.mostrar_frame(MenuPrincipal)).pack()
    
    def guardar_ejemplo(self):
        oracion = self.entrada_oracion.get()
        
        if oracion.count('[') != 1 or oracion.count(']') != 1:
            messagebox.showerror("Error", "Formato incorrecto. Usa exactamente un par de corchetes []")
            return
        
        cd_correcto = oracion[oracion.index('[')+1 : oracion.index(']')].strip()
        if not cd_correcto:
            messagebox.showerror("Error", "El complemento directo no puede estar vacío")
            return
        
        opciones_incorrectas = [e.get().strip() for e in self.entradas_incorrectas]
        if any(not opcion for opcion in opciones_incorrectas):
            messagebox.showerror("Error", "Todas las opciones incorrectas deben estar completas")
            return
        
        preguntas.append({
            "oracion": oracion,
            "cd_correcto": cd_correcto,
            "opciones_incorrectas": opciones_incorrectas
        })
        
        messagebox.showinfo("Éxito", f"Ejemplo guardado! Total: {len(preguntas)}/100")
        self.limpiar_formulario()
    
    def limpiar_formulario(self):
        self.entrada_oracion.delete(0, tk.END)
        for entrada in self.entradas_incorrectas:
            entrada.delete(0, tk.END)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
