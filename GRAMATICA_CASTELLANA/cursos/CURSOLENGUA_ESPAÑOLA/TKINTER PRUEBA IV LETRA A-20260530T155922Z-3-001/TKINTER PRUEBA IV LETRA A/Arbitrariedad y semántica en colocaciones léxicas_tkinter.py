import json
import random
import time
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class AplicacionColocaciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practicador de Colocaciones Léxicas")
        self.geometry("800x600")
        self.configure(bg='#F0F0F0')
        
        self.ARCHIVO_PREGUNTAS = "colocaciones.json"
        self.VIDAS_INICIALES = 3
        self.TIEMPO_POR_NIVEL = {1: 20, 2: 15, 3: 10}
        self.preguntas = self.cargar_preguntas()
        
        self.crear_widgets_principales()
        self.mostrar_menu_principal()

    def crear_widgets_principales(self):
        self.contenedor = ttk.Frame(self)
        self.contenedor.pack(expand=True, fill='both')
        
        self.frames = {}
        for F in (MenuPrincipal, PracticarFrame, CrearPreguntaFrame):
            frame = F(self.contenedor, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_menu_principal(self):
        self.mostrar_frame(MenuPrincipal)

    def mostrar_practicar(self):
        self.frames[PracticarFrame].preparar_quiz()
        self.mostrar_frame(PracticarFrame)

    def mostrar_crear_pregunta(self):
        self.mostrar_frame(CrearPreguntaFrame)

    def mostrar_frame(self, contenedor):
        frame = self.frames[contenedor]
        frame.tkraise()

    def cargar_preguntas(self):
        try:
            with open(self.ARCHIVO_PREGUNTAS, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_pregunta(self, nueva_pregunta):
        self.preguntas.append(nueva_pregunta)
        with open(self.ARCHIVO_PREGUNTAS, "w", encoding="utf-8") as f:
            json.dump(self.preguntas, f, ensure_ascii=False, indent=2)

class MenuPrincipal(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.configurar_ui()

    def configurar_ui(self):
        style = ttk.Style()
        style.configure('Titulo.TLabel', font=('Helvetica', 18, 'bold'), foreground='#2c3e50')
        style.configure('Boton.TButton', font=('Arial', 12), padding=10)

        ttk.Label(self, text="Practicador de Colocaciones Léxicas", 
                 style='Titulo.TLabel').pack(pady=20)

        btn_style = {'style': 'Boton.TButton', 'padding': 10}
        ttk.Button(self, text="Practicar", command=self.controlador.mostrar_practicar,
                  **btn_style).pack(pady=10)
        ttk.Button(self, text="Crear Nueva Pregunta", 
                  command=self.controlador.mostrar_crear_pregunta, **btn_style).pack(pady=10)
        ttk.Button(self, text="Salir", command=self.controlador.quit, **btn_style).pack(pady=10)

class PracticarFrame(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.configurar_ui()
        self.resetear_quiz()

    def configurar_ui(self):
        self.canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.canvas.pack(expand=True, fill='both', padx=20, pady=20)

        self.lbl_tiempo = ttk.Label(self.canvas, font=('Arial', 14), background='white')
        self.lbl_vidas = ttk.Label(self.canvas, font=('Arial', 14), background='white')
        self.lbl_puntaje = ttk.Label(self.canvas, font=('Arial', 14), background='white')
        
        self.lbl_pregunta = ttk.Label(self.canvas, font=('Arial', 14, 'bold'), 
                                    wraplength=600, background='white')
        self.botones_opciones = []
        for i in range(4):
            btn = ttk.Button(self.canvas, style='BotonOpcion.TButton')
            btn.config(command=lambda b=btn: self.verificar_respuesta(b))
            self.botones_opciones.append(btn)
        
        self.btn_siguiente = ttk.Button(self.canvas, text="Siguiente", 
                                       command=self.siguiente_pregunta, state='disabled')

    def resetear_quiz(self):
        self.preguntas = random.sample(self.controlador.preguntas, 
                                      min(10, len(self.controlador.preguntas)))
        self.puntaje = 0
        self.vidas = self.controlador.VIDAS_INICIALES
        self.pregunta_actual = 0
        self.tiempo_restante = 0

    def preparar_quiz(self):
        self.resetear_quiz()
        self.nivel = self.obtener_nivel()
        self.mostrar_pregunta()

    def obtener_nivel(self):
        return simpledialog.askinteger("Nivel", "Elige nivel (1-3):", 
                                      parent=self, minvalue=1, maxvalue=3)

    def mostrar_pregunta(self):
        self.actualizar_ui()
        pregunta = self.preguntas[self.pregunta_actual]
        self.lbl_pregunta.config(text=pregunta['pregunta'])
        
        for i, opcion in enumerate(pregunta['opciones']):
            self.botones_opciones[i].config(text=opcion, state='normal')
        
        self.tiempo_restante = self.controlador.TIEMPO_POR_NIVEL[self.nivel]
        self.actualizar_temporizador()

    def actualizar_ui(self):
        widgets = [self.lbl_tiempo, self.lbl_vidas, self.lbl_puntaje,
                  self.lbl_pregunta, *self.botones_opciones, self.btn_siguiente]
        
        for widget in widgets:
            widget.place_forget()
        
        self.lbl_tiempo.place(x=20, y=20)
        self.lbl_vidas.place(x=200, y=20)
        self.lbl_puntaje.place(x=400, y=20)
        self.lbl_pregunta.place(relx=0.5, rely=0.3, anchor='center')
        
        for i, btn in enumerate(self.botones_opciones):
            btn.place(relx=0.3 + (i%2)*0.4, rely=0.5 + (i//2)*0.15, 
                     anchor='center', width=200, height=40)
        
        self.btn_siguiente.place(relx=0.5, rely=0.9, anchor='center')

    def actualizar_temporizador(self):
        if self.tiempo_restante > 0:
            self.lbl_tiempo.config(text=f"⏳ Tiempo: {self.tiempo_restante}s")
            self.tiempo_restante -= 1
            self.after(1000, self.actualizar_temporizador)
        else:
            self.manejar_tiempo_agotado()

    def manejar_tiempo_agotado(self):
        self.vidas -= 1
        messagebox.showwarning("Tiempo agotado", "¡Se acabó el tiempo!")
        self.verificar_fin_juego()

    def verificar_respuesta(self, boton):
        respuesta = boton['text']
        correcta = self.preguntas[self.pregunta_actual]['respuesta']
        
        for btn in self.botones_opciones:
            btn.config(state='disabled')
            if btn['text'] == correcta:
                btn.config(style='Correcto.TButton')
            else:
                btn.config(style='Incorrecto.TButton' if btn == boton else 'TButton')
        
        if respuesta == correcta:
            self.puntaje += 10
        else:
            self.vidas -= 1
        
        self.actualizar_estado()
        self.btn_siguiente.config(state='normal')

    def actualizar_estado(self):
        self.lbl_vidas.config(text=f"❤️ Vidas: {self.vidas}")
        self.lbl_puntaje.config(text=f"🏆 Puntaje: {self.puntaje}")
        self.verificar_fin_juego()

    def siguiente_pregunta(self):
        self.pregunta_actual += 1
        if self.pregunta_actual < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado_final()

    def verificar_fin_juego(self):
        if self.vidas <= 0:
            messagebox.showinfo("Fin del juego", "¡Se acabaron las vidas!")
            self.mostrar_resultado_final()

    def mostrar_resultado_final(self):
        mensaje = f"Puntaje final: {self.puntaje}\n"
        if self.puntaje >= 80:
            mensaje += "¡Excelente dominio!"
        elif self.puntaje >= 50:
            mensaje += "¡Buen trabajo!"
        else:
            mensaje += "¡Sigue practicando!"
        
        messagebox.showinfo("Resultados", mensaje)
        self.controlador.mostrar_menu_principal()

class CrearPreguntaFrame(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.configurar_ui()

    def configurar_ui(self):
        ttk.Label(self, text="Crear Nueva Pregunta", font=('Helvetica', 16)).pack(pady=20)
        
        campos = [
            ("Pregunta:", 'entrada_pregunta'),
            ("Opción 1:", 'entrada_opcion1'),
            ("Opción 2:", 'entrada_opcion2'), 
            ("Opción 3:", 'entrada_opcion3'),
            ("Opción 4:", 'entrada_opcion4'),
            ("Respuesta correcta:", 'entrada_respuesta'),
            ("Explicación RAE:", 'entrada_explicacion'),
            ("Dificultad (1-3):", 'entrada_dificultad')
        ]
        
        self.entradas = {}
        for texto, nombre in campos:
            frame = ttk.Frame(self)
            frame.pack(pady=5, fill='x')
            ttk.Label(frame, text=texto, width=20).pack(side='left')
            entrada = ttk.Entry(frame, width=40) if "dificultad" not in nombre else \
                     ttk.Combobox(frame, width=37, values=[1, 2, 3])
            entrada.pack(side='left')
            self.entradas[nombre] = entrada
        
        ttk.Button(self, text="Guardar", command=self.guardar_pregunta).pack(pady=20)
        ttk.Button(self, text="Volver", command=self.controlador.mostrar_menu_principal).pack()

    def guardar_pregunta(self):
        try:
            nueva_pregunta = {
                "pregunta": self.entradas['entrada_pregunta'].get(),
                "opciones": [self.entradas[f'entrada_opcion{i}'].get() for i in range(1,5)],
                "respuesta": self.entradas['entrada_respuesta'].get(),
                "explicacion": self.entradas['entrada_explicacion'].get(),
                "dificultad": int(self.entradas['entrada_dificultad'].get())
            }
            
            if not all(nueva_pregunta.values()):
                raise ValueError("Todos los campos son obligatorios")
            
            if nueva_pregunta['respuesta'] not in nueva_pregunta['opciones']:
                raise ValueError("La respuesta debe estar entre las opciones")
            
            self.controlador.guardar_pregunta(nueva_pregunta)
            messagebox.showinfo("Éxito", "Pregunta guardada correctamente")
            self.controlador.mostrar_menu_principal()
            
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

def configurar_estilos():
    style = ttk.Style()
    style.theme_use('clam')
    
    style.configure('TButton', padding=5)
    style.configure('BotonOpcion.TButton', font=('Arial', 11), width=20)
    style.map('Correcto.TButton', background=[('active', '#2ecc71'), ('!active', '#2ecc71')])
    style.map('Incorrecto.TButton', background=[('active', '#e74c3c'), ('!active', '#e74c3c')])

if __name__ == "__main__":
    configurar_estilos()
    app = AplicacionColocaciones()
    app.mainloop()
