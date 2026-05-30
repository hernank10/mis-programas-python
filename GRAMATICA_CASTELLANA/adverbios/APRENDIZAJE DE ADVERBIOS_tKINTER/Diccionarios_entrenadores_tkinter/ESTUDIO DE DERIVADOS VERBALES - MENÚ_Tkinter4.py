import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Configuración inicial de ejemplos
EJEMPLOS_INICIALES = [
    # Infinitivo (15)
    {"categoria": "infinitivo", "ejemplo": "Estudiar es esencial para el éxito."},
    {"categoria": "infinitivo", "ejemplo": "Quiero aprender a tocar el piano."},
    {"categoria": "infinitivo", "ejemplo": "Decidieron viajar a Japón el próximo año."},
    {"categoria": "infinitivo", "ejemplo": "Correr bajo la lluvia puede ser divertido."},
    {"categoria": "infinitivo", "ejemplo": "Es importante escuchar a los demás."},
    {"categoria": "infinitivo", "ejemplo": "Dejó de fumar por su salud."},
    {"categoria": "infinitivo", "ejemplo": "Me gusta leer novelas de misterio."},
    {"categoria": "infinitivo", "ejemplo": "Hablar dos idiomas es una ventaja."},
    {"categoria": "infinitivo", "ejemplo": "Fue difícil entender sus razones."},
    {"categoria": "infinitivo", "ejemplo": "Intentaré terminar el proyecto hoy."},
    {"categoria": "infinitivo", "ejemplo": "Vivir sin miedo es un desafío."},
    {"categoria": "infinitivo", "ejemplo": "Prefiero caminar que tomar el autobús."},
    {"categoria": "infinitivo", "ejemplo": "Oí llamar a la puerta anoche."},
    {"categoria": "infinitivo", "ejemplo": "Ahorrar dinero requiere disciplina."},
    {"categoria": "infinitivo", "ejemplo": "No es fácil olvidar el pasado."},
    
    # Participio (20)
    {"categoria": "participio", "ejemplo": "La puerta está cerrada con llave."},
    {"categoria": "participio", "ejemplo": "Los libros escritos por Cervantes son clásicos."},
    {"categoria": "participio", "ejemplo": "Las cartas fueron enviadas ayer."},
    {"categoria": "participio", "ejemplo": "Tengo las maletas hechas para el viaje."},
    {"categoria": "participio", "ejemplo": "El pastel quemado no se pudo comer."},
    {"categoria": "participio", "ejemplo": "Las flores cortadas adornaban la mesa."},
    {"categoria": "participio", "ejemplo": "Los niños asustados corrieron a casa."},
    {"categoria": "participio", "ejemplo": "El tesoro escondido nunca fue encontrado."},
    {"categoria": "participio", "ejemplo": "La comida preparada por mi abuela es deliciosa."},
    {"categoria": "participio", "ejemplo": "Las ventanas rotas fueron reparadas."},
    {"categoria": "participio", "ejemplo": "He terminado mi tarea."},
    {"categoria": "participio", "ejemplo": "Habían visto esa película antes."},
    {"categoria": "participio", "ejemplo": "¿Has visitado París alguna vez?"},
    {"categoria": "participio", "ejemplo": "Hubiera dicho la verdad si me preguntaban."},
    {"categoria": "participio", "ejemplo": "Habremos llegado al mediodía."},
    {"categoria": "participio", "ejemplo": "Nunca había sentido tanto frío."},
    {"categoria": "participio", "ejemplo": "¿Habéis probado el ceviche peruano?"},
    {"categoria": "participio", "ejemplo": "Hubiesen ganado con más esfuerzo."},
    {"categoria": "participio", "ejemplo": "Había olvidado su nombre por completo."},
    {"categoria": "participio", "ejemplo": "Cuando llegues, ya habré salido."},
    
    # Gerundio (15)
    {"categoria": "gerundio", "ejemplo": "Caminando por el parque, encontré un gato."},
    {"categoria": "gerundio", "ejemplo": "El niño entró a la casa riendo a carcajadas."},
    {"categoria": "gerundio", "ejemplo": "Estudiando diariamente, aprobarás el examen."},
    {"categoria": "gerundio", "ejemplo": "Enviando el paquete a tiempo, evitarás multas."},
    {"categoria": "gerundio", "ejemplo": "Lloviendo tanto, el partido se canceló."},
    {"categoria": "gerundio", "ejemplo": "Me saludó sonriendo amablemente."},
    {"categoria": "gerundio", "ejemplo": "Corriendo rápido, ganó la carrera."},
    {"categoria": "gerundio", "ejemplo": "En amaneciendo, saldremos de viaje."},
    {"categoria": "gerundio", "ejemplo": "Practicando piano todos los días, mejoró su técnica."},
    {"categoria": "gerundio", "ejemplo": "Habiendo terminado su trabajo, se fue a casa."},
    {"categoria": "gerundio", "ejemplo": "Viendo la película, se durmió."},
    {"categoria": "gerundio", "ejemplo": "Escribiendo una novela, descubrió su pasión."},
    {"categoria": "gerundio", "ejemplo": "Bailando salsa, se sintió libre."},
    {"categoria": "gerundio", "ejemplo": "En llegando al aeropuerto, te llamaré."},
    {"categoria": "gerundio", "ejemplo": "Pensando en su futuro, tomó una decisión."}
]

class DerivadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio de Derivados Verbales")
        self.root.geometry("800x600")
        
        # Archivos de datos
        self.ejemplos_file = "ejemplos.json"
        self.usuario_file = "usuario_ejemplos.json"
        
        # Inicializar datos
        self.inicializar_datos()
        self.ejemplos = self.cargar_ejemplos()
        self.ejemplos_usuario = self.cargar_usuario()
        
        # Interfaz
        self.crear_menu_principal()
        self.crear_diapositiva_conceptual()

    def inicializar_datos(self):
        if not os.path.exists(self.ejemplos_file):
            with open(self.ejemplos_file, 'w') as f:
                json.dump(EJEMPLOS_INICIALES, f)

    def cargar_ejemplos(self):
        if os.path.exists(self.ejemplos_file):
            with open(self.ejemplos_file, 'r') as f:
                return json.load(f)
        return []

    def cargar_usuario(self):
        if os.path.exists(self.usuario_file):
            with open(self.usuario_file, 'r') as f:
                return json.load(f)
        return []

    def guardar_ejemplo(self, ejemplo):
        if len(self.ejemplos_usuario) < 100:
            self.ejemplos_usuario.append(ejemplo)
            with open(self.usuario_file, 'w') as f:
                json.dump(self.ejemplos_usuario, f)
            return True
        return False

    def crear_menu_principal(self):
        self.clear_frame()
        
        title = ttk.Label(self.root, text="ESTUDIO DE DERIVADOS VERBALES", font=('Arial', 16, 'bold'))
        title.pack(pady=20)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        buttons = [
            ("Modo Estudio", self.modo_estudio),
            ("Cuestionario", self.cuestionario),
            ("Crear Ejemplos", self.crear_ejemplos),
            ("Ver Ejemplos", self.ver_ejemplos),
            ("Ayuda Conceptual", self.mostrar_ayuda),
            ("Salir", self.root.quit)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(btn_frame, text=text, command=command, width=20)
            btn.pack(pady=5, padx=10)

    def crear_diapositiva_conceptual(self):
        self.help_window = tk.Toplevel(self.root)
        self.help_window.withdraw()
        self.help_window.title("Conceptos Clave")
        
        text = """CONCEPTOS CLAVE:

Infinitivo: 
- Termina en -ar, -er, -ir
- Funciona como sustantivo
- Ejemplo: 'Estudiar es importante'

Participio:
- Termina en -ado/-ido
- Con 'ser/estar' (adjetivo): 'La puerta está cerrada'
- Con 'haber' (invariable): 'He terminado'

Gerundio:
- Termina en -ando/-iendo
- Modifica al verbo principal
- Ejemplo: 'Caminando rápido'"""
        
        self.help_text = scrolledtext.ScrolledText(self.help_window, wrap=tk.WORD, width=60, height=15)
        self.help_text.insert(tk.INSERT, text)
        self.help_text.config(state=tk.DISABLED)
        self.help_text.pack(padx=20, pady=20)

    # ... (Resto de métodos de la clase se mantienen igual como en la versión anterior)
    # [Los métodos restantes (modo_estudio, cuestionario, crear_ejemplos, etc.) 
    #  son idénticos a los de la versión Tkinter anterior]

if __name__ == "__main__":
    root = tk.Tk()
    app = DerivadosApp(root)
    root.mainloop()
