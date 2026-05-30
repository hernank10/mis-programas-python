import tkinter as tk
from tkinter import ttk, messagebox
import random
import csv
import os

# Configuración inicial
MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "custom_ejemplos.csv"
COLORES = {"fondo": "#2C3E50", "boton": "#3498DB", "texto": "#ECF0F1"}
ENSAYO = """
### **Estrategias para el Dominio de la Puntuación**

1. **Fase Conceptual**: 
Estudia las reglas mediante las diapositivas educativas.
Analiza ejemplos paradigmáticos y diferencias contextuales.

### **Práctica Guiada**
Utiliza los ejercicios de clasificación para identificar patrones.
Revisa tus errores con el sistema de análisis detallado.

### **Producción Activa**
Crea tus propios ejemplos y compártelos.
Practica con el modo de escritura cronometrado.
"""

class GrammarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practicador de Sintaxis")
        self.geometry("1000x700")
        self.configure(bg=COLORES["fondo"])
        self.puntuacion = {"correctas": 0, "incorrectas": 0}
        self.recursos = self.cargar_recursos()
        
        self.container = tk.Frame(self, bg=COLORES["fondo"])
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        for F in (MainMenu, PracticarEscritura, ClasificarOraciones, 
                 OrganizarOraciones, GestionEjemplos, DiapositivasEnsayo, Puntuacion):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_frame("MainMenu")
    
    def mostrar_frame(self, nombre_frame):
        frame = self.frames[nombre_frame]
        frame.tkraise()
        if hasattr(frame, "actualizar"):
            frame.actualizar()
    
    def cargar_recursos(self):
        recursos = {
            "coma_separativa": {
                "ejemplos": [
                    "El equipo ganó el campeonato, y los jugadores recibieron medallas.",
                    "María estudia medicina, y su hermano, derecho."
                ],
                "regla": "Separa dos oraciones completas unidas por 'y'"
            },
            "coma_eliptica": {
                "ejemplos": [
                    "Einstein, genio del siglo XX",
                    "París, ciudad de la luz"
                ],
                "regla": "Omite el verbo en estructuras concisas"
            }
        }
        
        if os.path.exists(ARCHIVO_EJEMPLOS):
            with open(ARCHIVO_EJEMPLOS, 'r', encoding='utf-8') as f:
                lector = csv.reader(f)
                for fila in lector:
                    if len(fila) == 2 and fila[0] in recursos:
                        recursos[fila[0]]["ejemplos"].append(fila[1])
        return recursos

class MainMenu(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        
        tk.Label(self, text="🏫 Practicador de Sintaxis", 
                font=("Arial", 24), bg=COLORES["fondo"], fg="white").pack(pady=20)
        
        botones = [
            ("✍️ Practicar escritura", "PracticarEscritura", "EJERCITAR"),
            ("📚 Clasificar oraciones", "ClasificarOraciones", "CLASIFICAR"),
            ("🔀 Organizar oraciones", "OrganizarOraciones", "ORDENAR"),
            ("💾 Gestionar ejemplos", "GestionEjemplos", "ADMINISTRAR"),
            ("📖 Leer ensayo", "DiapositivasEnsayo", "ESTUDIAR"),
            ("🏆 Ver puntuación", "Puntuacion", "REVISAR"),
            ("🚪 Salir", self.controlador.destroy, "SALIR")
        ]
        
        for texto, comando, accion in botones:
            frame_boton = tk.Frame(self, bg=COLORES["fondo"])
            frame_boton.pack(pady=5)
            
            btn = tk.Button(frame_boton, text=texto, width=25, font=("Arial", 14),
                          bg=COLORES["boton"], fg="white", relief="flat",
                          command=lambda c=comando: self.controlador.mostrar_frame(c) if isinstance(c, str) else c())
            btn.pack(side="left", padx=5)
            
            tk.Label(frame_boton, text=accion, font=("Arial", 10, "bold"), 
                   fg="black", bg=COLORES["fondo"]).pack(side="left")

class PracticarEscritura(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        self.ejemplo_actual = None
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.lbl_base = tk.Label(self, font=("Arial", 14), wraplength=800,
                               bg=COLORES["fondo"], fg="white")
        self.lbl_base.pack(pady=20)
        
        self.entrada = tk.Entry(self, width=80, font=("Arial", 12))
        self.entrada.pack(pady=10)
        
        tk.Button(self, text="✅ Verificar", command=self.verificar,
                bg=COLORES["boton"], fg="white").pack(pady=10)
        
        self.lbl_resultado = tk.Label(self, font=("Arial", 12), wraplength=800,
                                    bg=COLORES["fondo"], fg="white")
        self.lbl_resultado.pack(pady=10)
        
        self.actualizar()
    
    def actualizar(self):
        categoria = random.choice(list(self.controlador.recursos.keys()))
        self.ejemplo_actual = random.choice(
            self.controlador.recursos[categoria]["ejemplos"]
        )
        texto_base = self.ejemplo_actual.replace(",", "").replace(";", "")
        self.lbl_base.config(text=texto_base)
        self.entrada.delete(0, tk.END)
        self.lbl_resultado.config(text="")
    
    def verificar(self):
        intento = self.entrada.get().strip()
        if intento.lower() == self.ejemplo_actual.lower():
            self.controlador.puntuacion["correctas"] += 1
            self.lbl_resultado.config(text="✅ ¡Correcto!", fg="green")
        else:
            self.controlador.puntuacion["incorrectas"] += 1
            self.lbl_resultado.config(text=f"❌ Correcto: {self.ejemplo_actual}", fg="red")
        self.after(2000, self.actualizar)

class ClasificarOraciones(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        self.ejemplo_actual = None
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.lbl_instruccion = tk.Label(self, text="📚 Clasifica la oración:", 
                                      font=("Arial", 14), bg=COLORES["fondo"], fg="white")
        self.lbl_instruccion.pack(pady=10)
        
        self.lbl_ejemplo = tk.Label(self, font=("Arial", 12), wraplength=800,
                                  bg=COLORES["fondo"], fg="white")
        self.lbl_ejemplo.pack(pady=10)
        
        self.opcion_var = tk.StringVar()
        for categoria in self.controlador.recursos.keys():
            rb = tk.Radiobutton(self, text=categoria.replace("_", " ").title(),
                              variable=self.opcion_var, value=categoria,
                              bg=COLORES["fondo"], fg="white", selectcolor=COLORES["fondo"])
            rb.pack(anchor="w")
        
        self.btn_verificar = tk.Button(self, text="✅ Verificar", command=self.verificar,
                                      bg=COLORES["boton"], fg="white")
        self.btn_verificar.pack(pady=10)
        
        self.lbl_resultado = tk.Label(self, font=("Arial", 12), wraplength=800,
                                    bg=COLORES["fondo"], fg="white")
        self.lbl_resultado.pack(pady=10)
        
        self.actualizar()
    
    def actualizar(self):
        self.categoria_correcta = random.choice(list(self.controlador.recursos.keys()))
        self.ejemplo_actual = random.choice(
            self.controlador.recursos[self.categoria_correcta]["ejemplos"]
        )
        self.lbl_ejemplo.config(text=self.ejemplo_actual)
        self.opcion_var.set("")
        self.lbl_resultado.config(text="")
    
    def verificar(self):
        if not self.opcion_var.get():
            messagebox.showwarning("Error", "Selecciona una categoría")
            return
        
        if self.opcion_var.get() == self.categoria_correcta:
            self.controlador.puntuacion["correctas"] += 1
            self.lbl_resultado.config(text="✅ ¡Correcto!", fg="green")
        else:
            self.controlador.puntuacion["incorrectas"] += 1
            self.lbl_resultado.config(text=f"❌ Categoría correcta: {self.categoria_correcta}", fg="red")
        self.after(2000, self.actualizar)

class OrganizarOraciones(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        self.partes = []
        self.drag_label = None
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.lbl_instruccion = tk.Label(self, text="🔀 Organiza las partes de la oración", 
                                      font=("Arial", 14), bg=COLORES["fondo"], fg="white")
        self.lbl_instruccion.pack(pady=10)
        
        self.frame_partes = tk.Frame(self, bg=COLORES["fondo"])
        self.frame_partes.pack(pady=10)
        
        self.frame_destino = tk.Frame(self, bg=COLORES["fondo"], height=100, width=800)
        self.frame_destino.pack(pady=10)
        
        self.btn_verificar = tk.Button(self, text="✅ Verificar", command=self.verificar,
                                      bg=COLORES["boton"], fg="white")
        self.btn_verificar.pack(pady=10)
        
        self.lbl_resultado = tk.Label(self, font=("Arial", 12), wraplength=800,
                                    bg=COLORES["fondo"], fg="white")
        self.lbl_resultado.pack(pady=10)
        
        self.actualizar()
    
    def actualizar(self):
        categoria = random.choice(list(self.controlador.recursos.keys()))
        ejemplo = random.choice(self.controlador.recursos[categoria]["ejemplos"])
        self.partes = ejemplo.split(", ")
        random.shuffle(self.partes)
        
        for widget in self.frame_partes.winfo_children():
            widget.destroy()
        
        for parte in self.partes:
            lbl = tk.Label(self.frame_partes, text=parte, bg="#3498DB", fg="white",
                          padx=10, pady=5, relief="ridge")
            lbl.pack(side="left", padx=5)
            lbl.bind("<Button-1>", self.iniciar_arrastre)
            lbl.bind("<B1-Motion>", self.arrastrar)
            lbl.bind("<ButtonRelease-1>", self.soltar)
        
        for widget in self.frame_destino.winfo_children():
            widget.destroy()
    
    def iniciar_arrastre(self, event):
        self.drag_label = event.widget
    
    def arrastrar(self, event):
        if self.drag_label:
            x = self.drag_label.winfo_x() + event.x
            y = self.drag_label.winfo_y() + event.y
            self.drag_label.place(x=x, y=y)
    
    def soltar(self, event):
        if self.drag_label and self.frame_destino.winfo_containing(event.x_root, event.y_root):
            self.drag_label.place_forget()
            self.drag_label.pack(side="left", padx=5, in_=self.frame_destino)
        self.drag_label = None
    
    def verificar(self):
        orden_usuario = " ".join([lbl["text"] for lbl in self.frame_destino.winfo_children()])
        orden_correcto = ", ".join(self.partes)
        
        if orden_usuario == orden_correcto:
            self.controlador.puntuacion["correctas"] += 1
            self.lbl_resultado.config(text="✅ ¡Orden correcto!", fg="green")
        else:
            self.controlador.puntuacion["incorrectas"] += 1
            self.lbl_resultado.config(text=f"❌ Correcto: {orden_correcto}", fg="red")
        self.after(2000, self.actualizar)

class GestionEjemplos(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.combo_categoria = ttk.Combobox(self, values=list(self.controlador.recursos.keys()))
        self.combo_categoria.pack(pady=5)
        
        self.entrada_ejemplo = tk.Entry(self, width=60, font=("Arial", 12))
        self.entrada_ejemplo.pack(pady=5)
        
        tk.Button(self, text="💾 Guardar ejemplo", command=self.guardar_ejemplo,
                 bg=COLORES["boton"], fg="white").pack(pady=5)
        
        self.txt_ejemplos = tk.Text(self, width=80, height=15, wrap=tk.WORD)
        self.txt_ejemplos.pack(pady=10)
        
        self.actualizar_lista()
    
    def guardar_ejemplo(self):
        categoria = self.combo_categoria.get()
        ejemplo = self.entrada_ejemplo.get().strip()
        
        if not categoria:
            messagebox.showerror("Error", "Selecciona una categoría")
            return
        
        if not ejemplo:
            messagebox.showerror("Error", "El ejemplo no puede estar vacío")
            return
        
        if len(self.controlador.recursos[categoria]["ejemplos"]) >= MAX_EJEMPLOS:
            messagebox.showerror("Error", f"Máximo {MAX_EJEMPLOS} ejemplos por categoría")
            return
        
        try:
            with open(ARCHIVO_EJEMPLOS, 'a', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerow([categoria, ejemplo])
            
            self.controlador.recursos[categoria]["ejemplos"].append(ejemplo)
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {str(e)}")
    
    def actualizar_lista(self):
        self.txt_ejemplos.delete(1.0, tk.END)
        for categoria, datos in self.controlador.recursos.items():
            self.txt_ejemplos.insert(tk.END, f"\n🔖 {categoria.replace('_', ' ').title()} ({len(datos['ejemplos'])} ejemplos):\n")
            for ejemplo in datos["ejemplos"][:5]:
                self.txt_ejemplos.insert(tk.END, f"  • {ejemplo}\n")

class DiapositivasEnsayo(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        self.slides = self.procesar_ensayo(ENSAYO)
        self.current_slide = 0
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.txt_contenido = tk.Text(self, width=80, height=20, wrap=tk.WORD,
                                   font=("Arial", 12), bg=COLORES["fondo"], fg="white")
        self.txt_contenido.pack(pady=20, padx=20)
        
        btn_frame = tk.Frame(self, bg=COLORES["fondo"])
        btn_frame.pack(pady=10)
        
        self.btn_anterior = tk.Button(btn_frame, text="◀ Anterior", command=self.slide_anterior,
                                     bg=COLORES["boton"], fg="white")
        self.btn_anterior.pack(side="left", padx=10)
        
        self.btn_siguiente = tk.Button(btn_frame, text="Siguiente ▶", command=self.slide_siguiente,
                                      bg=COLORES["boton"], fg="white")
        self.btn_siguiente.pack(side="left", padx=10)
        
        self.txt_contenido.tag_configure("titulo", font=("Arial", 14, "bold"), foreground="#3498DB")
        self.txt_contenido.tag_configure("cuerpo", lmargin1=20, lmargin2=20)
        
        self.mostrar_slide()
    
    def procesar_ensayo(self, texto):
        partes = texto.split("###")
        return [p.strip() for p in partes if p.strip()]
    
    def mostrar_slide(self):
        self.txt_contenido.delete(1.0, tk.END)
        lineas = self.slides[self.current_slide].split("\n")
        for linea in lineas:
            if linea.startswith("**"):
                self.txt_contenido.insert(tk.END, linea.strip("*") + "\n", "titulo")
            else:
                self.txt_contenido.insert(tk.END, linea + "\n", "cuerpo")
        self.actualizar_botones()
    
    def actualizar_botones(self):
        self.btn_anterior["state"] = "normal" if self.current_slide > 0 else "disabled"
        self.btn_siguiente["state"] = "normal" if self.current_slide < len(self.slides)-1 else "disabled"
    
    def slide_anterior(self):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.mostrar_slide()
    
    def slide_siguiente(self):
        if self.current_slide < len(self.slides)-1:
            self.current_slide += 1
            self.mostrar_slide()

class Puntuacion(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        tk.Label(self, text="🏆 Puntuación Actual", 
                font=("Arial", 24), bg=COLORES["fondo"], fg="white").pack(pady=20)
        
        tk.Label(self, text=f"✅ Correctas: {self.controlador.puntuacion['correctas']}", 
                font=("Arial", 18), bg=COLORES["fondo"], fg="white").pack(pady=10)
        
        tk.Label(self, text=f"❌ Incorrectas: {self.controlador.puntuacion['incorrectas']}", 
                font=("Arial", 18), bg=COLORES["fondo"], fg="white").pack(pady=10)

if __name__ == "__main__":
    app = GrammarApp()
    app.mainloop()
