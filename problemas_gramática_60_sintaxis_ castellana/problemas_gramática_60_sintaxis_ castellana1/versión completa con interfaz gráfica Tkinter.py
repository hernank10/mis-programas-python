import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

VERBOS = {
    'decir': {
        'complementos': ['nominal', 'subordinado', 'estilo_directo'],
        'preposiciones': [],
        'ejemplos': {
            'correctos': [
                "María dijo la verdad",
                "El niño dijo que tenía hambre",
                "El cartel dice: \"Prohibido pasar\""
            ],
            'incorrectos': [
                "María dijo",
                "El profesor dijo rápidamente"
            ]
        }
    },
    'dar': {
        'complementos': ['objeto indirecto', 'nominal'],
        'preposiciones': ['a'],
        'ejemplos': {
            'correctos': [
                "Dio un regalo a su madre",
                "Le dieron las gracias",
                "El sol da luz a la Tierra"
            ],
            'incorrectos': [
                "El profesor dio",
                "Dieron sin recibir"
            ]
        }
    },
    'poner': {
        'complementos': ['nominal', 'locativo'],
        'preposiciones': ['en', 'sobre'],
        'ejemplos': {
            'correctos': [
                "Puso el libro en la mesa",
                "Vamos a poner música",
                "Pongamos que esto es cierto"
            ],
            'incorrectos': [
                "El estudiante puso",
                "Pusieron rápidamente"
            ]
        }
    }
}

EJERCICIOS = {
    'decir': [
        {
            'oracion': "El profesor dijo ______ durante la clase.",
            'soluciones': ["una explicación", "que comenzaría el examen", "\"presten atención\""],
            'puntos': 10
        }
    ],
    'dar': [
        {
            'oracion': "Los padres dieron ______ a sus hijos.",
            'soluciones': ["un consejo", "que estudiasen", "los buenos días"],
            'puntos': 12
        }
    ],
    'poner': [
        {
            'oracion': "Vamos a poner ______ en la mesa.",
            'soluciones': ["los platos", "atención", "que empiece la cena"],
            'puntos': 15
        }
    ]
}

class SistemaPractica:
    def __init__(self):
        self.datos = self.cargar_datos()
        
    def cargar_datos(self):
        try:
            with open("datos_verbos.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'puntuacion_total': 0,
                'verbos': {verbo: {'puntos': 0, 'ejemplos': []} for verbo in VERBOS}
            }

    def guardar_datos(self):
        with open("datos_verbos.json", "w") as f:
            json.dump(self.datos, f, indent=2, ensure_ascii=False)

    def validar_respuesta(self, verbo, respuesta):
        partes = respuesta.lower().split(verbo)
        if len(partes) < 2 or not partes[1].strip():
            return False, "Falta el complemento requerido"
        
        complemento = partes[1].strip()
        reglas = VERBOS[verbo]
        
        if reglas['preposiciones']:
            if not any(complemento.startswith(p) for p in reglas['preposiciones']):
                return False, f"Requiere preposición: {', '.join(reglas['preposiciones'])}"
        
        if 'nominal' in reglas['complementos'] and any(palabra in complemento for palabra in ['un ', 'una ', 'el ', 'la ']):
            return True, ""
        if 'subordinado' in reglas['complementos'] and complemento.startswith(('que ', 'quien ', 'donde ')):
            return True, ""
        if 'estilo_directo' in reglas['complementos'] and any(c in respuesta for c in ['"', "'", '“']):
            return True, ""
        
        return False, "Estructura del complemento incorrecta"

    def actualizar_puntos(self, verbo, puntos):
        self.datos['verbos'][verbo]['puntos'] += puntos
        self.datos['puntuacion_total'] += puntos
        self.guardar_datos()

    def guardar_ejemplo(self, verbo, plantilla, respuesta, correcto):
        ejemplo = {
            'fecha': datetime.now().isoformat(),
            'oracion': plantilla.replace("______", respuesta) if plantilla else respuesta,
            'correcto': correcto
        }
        self.datos['verbos'][verbo]['ejemplos'].append(ejemplo)
        self.guardar_datos()

class Aplicacion(tk.Tk):
    def __init__(self, sistema):
        super().__init__()
        self.sistema = sistema
        self.title("Práctica de Verbos Transitivos")
        self.geometry("800x600")
        self.configure(bg='#F0F0F0')
        
        self.verbo_actual = None
        self.crear_interfaz()
        
    def crear_interfaz(self):
        self.notebook = ttk.Notebook(self)
        
        # Pestaña principal
        self.frame_principal = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_principal, text="Inicio")
        
        # Pestaña de teoría
        self.frame_teoria = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_teoria, text="Teoría")
        
        # Pestaña de práctica
        self.frame_practica = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_practica, text="Práctica")
        
        self.notebook.pack(expand=True, fill='both')
        self.crear_pestania_principal()
        self.crear_pestania_teoria()
        self.crear_pestania_practica()
    
    def crear_pestania_principal(self):
        frame = self.frame_principal
        ttk.Label(frame, text="¡Bienvenido a la Práctica de Verbos!", 
                 font=('Arial', 16, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text="Verbos disponibles:", 
                 font=('Arial', 12)).pack(pady=10)
        
        for verbo in VERBOS:
            btn = ttk.Button(frame, text=verbo.capitalize(),
                            command=lambda v=verbo: self.mostrar_teoria(v))
            btn.pack(pady=5, padx=20, fill='x')
        
        ttk.Label(frame, text=f"Puntuación Total: {self.sistema.datos['puntuacion_total']}",
                 font=('Arial', 12, 'italic')).pack(pady=20)
    
    def crear_pestania_teoria(self):
        self.texto_teoria = scrolledtext.ScrolledText(self.frame_teoria,
                                                     wrap=tk.WORD,
                                                     font=('Arial', 11))
        self.texto_teoria.pack(expand=True, fill='both', padx=20, pady=20)
    
    def crear_pestania_practica(self):
        frame = self.frame_practica
        self.lbl_ejercicio = ttk.Label(frame, text="", font=('Arial', 12))
        self.lbl_ejercicio.pack(pady=20)
        
        self.entrada_respuesta = ttk.Entry(frame, width=50, font=('Arial', 12))
        self.entrada_respuesta.pack(pady=10)
        
        btn_verificar = ttk.Button(frame, text="Verificar Respuesta",
                                  command=self.verificar_respuesta)
        btn_verificar.pack(pady=10)
        
        self.lbl_feedback = ttk.Label(frame, text="", font=('Arial', 11))
        self.lbl_feedback.pack(pady=10)
        
        self.frame_progreso = ttk.Frame(frame)
        self.frame_progreso.pack(pady=20)
        
    def mostrar_teoria(self, verbo):
        self.notebook.select(self.frame_teoria)
        self.texto_teoria.delete(1.0, tk.END)
        
        teoria = [
            f"Verbo: {verbo.capitalize()}\n\n",
            "Complementos requeridos:\n",
            f"- {', '.join(VERBOS[verbo]['complementos'])}\n\n",
            "Ejemplos correctos:\n"
        ]
        
        for ej in VERBOS[verbo]['ejemplos']['correctos']:
            teoria.append(f"• {ej}\n")
        
        teoria.append("\nEjemplos incorrectos:\n")
        for ej in VERBOS[verbo]['ejemplos']['incorrectos']:
            teoria.append(f"• {ej}\n")
        
        self.texto_teoria.insert(tk.END, ''.join(teoria))
        self.iniciar_practica(verbo)
    
    def iniciar_practica(self, verbo):
        self.verbo_actual = verbo
        self.notebook.select(self.frame_practica)
        self.mostrar_ejercicio()
    
    def mostrar_ejercicio(self):
        ejercicio = random.choice(EJERCICIOS[self.verbo_actual])
        self.ejercicio_actual = ejercicio
        self.lbl_ejercicio.config(text=ejercicio['oracion'])
        self.entrada_respuesta.delete(0, tk.END)
        self.lbl_feedback.config(text="")
    
    def verificar_respuesta(self):
        respuesta = self.entrada_respuesta.get()
        valido, mensaje = self.sistema.validar_respuesta(self.verbo_actual, respuesta)
        
        if valido:
            self.sistema.actualizar_puntos(self.verbo_actual, self.ejercicio_actual['puntos'])
            self.sistema.guardar_ejemplo(self.verbo_actual, 
                                       self.ejercicio_actual['oracion'], 
                                       respuesta, True)
            messagebox.showinfo("Correcto", f"¡Respuesta válida! +{self.ejercicio_actual['puntos']} puntos")
            self.actualizar_puntuacion()
            self.mostrar_ejercicio()
        else:
            self.lbl_feedback.config(text=f"Error: {mensaje}", foreground='red')
            self.sistema.guardar_ejemplo(self.verbo_actual, 
                                       self.ejercicio_actual['oracion'], 
                                       respuesta, False)
    
    def actualizar_puntuacion(self):
        for widget in self.frame_principal.winfo_children():
            if isinstance(widget, ttk.Label) and "Puntuación Total" in widget.cget("text"):
                widget.config(text=f"Puntuación Total: {self.sistema.datos['puntuacion_total']}")

if __name__ == "__main__":
    sistema = SistemaPractica()
    app = Aplicacion(sistema)
    app.mainloop()
