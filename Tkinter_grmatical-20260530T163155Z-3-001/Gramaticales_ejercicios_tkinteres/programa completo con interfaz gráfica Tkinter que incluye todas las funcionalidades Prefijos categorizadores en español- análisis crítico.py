import tkinter as tk
from tkinter import ttk, messagebox
import random

class PracticaPrefijosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Practicador de Prefijos Avanzado")
        self.root.geometry("800x600")
        self.configure_styles()
        self.create_widgets()
        self.inicializar_juego()

        def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Arial', 12), foreground='#2c3e50')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#2980b9')
        self.style.map('Level.TLabel', foreground=[('!disabled', '#27ae60')])

        def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Cabecera
        self.lbl_titulo = ttk.Label(main_frame, text="✍️ PRÁCTICA DE PREFIJOS", style='Title.TLabel')
        self.lbl_titulo.pack(pady=10)
        
        # Panel de información
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=10)
        
        self.lbl_puntaje = ttk.Label(info_frame, text="Puntaje: 0")
        self.lbl_puntaje.pack(side=tk.LEFT, padx=10)
        
        self.lbl_nivel = ttk.Label(info_frame, text="Nivel: 1", style='Level.TLabel')
        self.lbl_nivel.pack(side=tk.RIGHT, padx=10)
        
        # Panel de juego
        game_frame = ttk.Frame(main_frame)
        game_frame.pack(pady=20)
        
        # Palabra oculta
        self.lbl_palabra_oculta = ttk.Label(game_frame, text="", 
                                          font=('Courier New', 28, 'bold'),
                                          foreground='#34495e')
        self.lbl_palabra_oculta.pack(pady=15)
        
        # Entrada de usuario
        self.entrada = ttk.Entry(game_frame, font=('Arial', 16), width=25)
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)
        
        # Botones
        btn_frame = ttk.Frame(game_frame)
        btn_frame.pack(pady=15)
        
        self.btn_verificar = ttk.Button(btn_frame, text="Verificar", 
                                      command=self.verificar_respuesta)
        self.btn_verificar.pack(side=tk.LEFT, padx=5)
        
        self.btn_pista = ttk.Button(btn_frame, text="Pista (-5 pts)", 
                                  command=self.mostrar_pista)
        self.btn_pista.pack(side=tk.LEFT, padx=5)
        
        # Historial
        self.historial = ttk.Treeview(main_frame, columns=('Intento', 'Resultado'), 
                                    show='headings', height=8)
        self.historial.heading('Intento', text='Intento')
        self.historial.heading('Resultado', text='Resultado')
        self.historial.column('Intento', width=400)
        self.historial.column('Resultado', width=150)
        self.historial.pack(fill=tk.BOTH, expand=True, pady=10)
        # [...] (Configuración de estilos y widgets igual al código anterior


    def inicializar_juego(self):
        self.palabras = [
            {"palabra": "polisílabo", "categoria": "adjetivo", "base": "sílaba"},
            {"palabra": "multicolor", "categoria": "adjetivo", "base": "color"},
            {"palabra": "pluricelular", "categoria": "adjetivo", "base": "célula"},
            {"palabra": "monocromo", "categoria": "adjetivo", "base": "cromo"},
            {"palabra": "bicéfalo", "categoria": "adjetivo", "base": "cabeza"},
            {"palabra": "tricolor", "categoria": "adjetivo", "base": "color"},
            {"palabra": "pluriempleado", "categoria": "adjetivo", "base": "empleo"},
            {"palabra": "multiforme", "categoria": "adjetivo", "base": "forma"},
            {"palabra": "monoteísta", "categoria": "adjetivo", "base": "teísmo"},
            {"palabra": "antinatural", "categoria": "adjetivo", "base": "naturaleza"},
            {"palabra": "extraterrestre", "categoria": "adjetivo", "base": "terrestre"},
            {"palabra": "plurilingüe", "categoria": "adjetivo", "base": "lengua"},
            {"palabra": "multiusos", "categoria": "adjetivo", "base": "uso"},
            {"palabra": "monorriel", "categoria": "adjetivo", "base": "riel"},
            {"palabra": "bidimensional", "categoria": "adjetivo", "base": "dimensión"},
            {"palabra": "pluricultural", "categoria": "adjetivo", "base": "cultura"},
            {"palabra": "monocultivo", "categoria": "sustantivo", "base": "cultivo"},
            {"palabra": "multinacional", "categoria": "adjetivo", "base": "nación"},
            {"palabra": "antibalas", "categoria": "adjetivo", "base": "bala"},
            {"palabra": "hipersónico", "categoria": "adjetivo", "base": "sonido"},
            {"palabra": "sobrenatural", "categoria": "adjetivo", "base": "naturaleza"},
            {"palabra": "antihistórico", "categoria": "adjetivo", "base": "historia"},
            {"palabra": "multidisciplinar", "categoria": "adjetivo", "base": "disciplina"},
            {"palabra": "monorítmico", "categoria": "adjetivo", "base": "ritmo"},
            {"palabra": "plurianual", "categoria": "adjetivo", "base": "año"},
            {"palabra": "bilingüe", "categoria": "adjetivo", "base": "lengua"},
            {"palabra": "multipolar", "categoria": "adjetivo", "base": "polo"},
            {"palabra": "anticáncer", "categoria": "adjetivo", "base": "cáncer"},
            {"palabra": "monocultural", "categoria": "adjetivo", "base": "cultura"},
            {"palabra": "supersónico", "categoria": "adjetivo", "base": "sonido"},
            {"palabra": "pluripartidista", "categoria": "adjetivo", "base": "partido"},
            {"palabra": "multicapa", "categoria": "adjetivo", "base": "capa"},
            {"palabra": "antivirus", "categoria": "sustantivo", "base": "virus"},
            {"palabra": "monocorde", "categoria": "adjetivo", "base": "cuerda"},
            {"palabra": "pluriemocional", "categoria": "adjetivo", "base": "emoción"},
            {"palabra": "multifacético", "categoria": "adjetivo", "base": "faceta"},
            {"palabra": "antisocial", "categoria": "adjetivo", "base": "sociedad"},
            {"palabra": "monosilábico", "categoria": "adjetivo", "base": "sílaba"},
            {"palabra": "plurivalente", "categoria": "adjetivo", "base": "valor"},
            {"palabra": "multicéntrico", "categoria": "adjetivo", "base": "centro"},
            {"palabra": "anticorrosivo", "categoria": "adjetivo", "base": "corrosión"},
            {"palabra": "monoteísmo", "categoria": "sustantivo", "base": "teísmo"},
            {"palabra": "pluridireccional", "categoria": "adjetivo", "base": "dirección"},
            {"palabra": "multirracial", "categoria": "adjetivo", "base": "raza"},
            {"palabra": "antideslizante", "categoria": "adjetivo", "base": "desliz"},
            {"palabra": "monolítico", "categoria": "adjetivo", "base": "piedra"},
            {"palabra": "plurisensorial", "categoria": "adjetivo", "base": "sentido"},
            {"palabra": "multilateral", "categoria": "adjetivo", "base": "lado"},
            {"palabra": "antifraude", "categoria": "adjetivo", "base": "fraude"}
        ]
        self.porcentaje_ocultar = 30
        self.puntaje = 0
        self.racha = 0
        self.palabra_actual = {}
        self.generar_nueva_palabra()
        self.actualizar_interfaz()
        
    def generar_nueva_palabra(self):
        self.palabra_actual = random.choice(self.palabras)
        self.palabra_oculta = self.ocultar_letras()
        self.intentos = 0
        self.pista_mostrada = False
        
    def ocultar_letras(self):
        letras = list(self.palabra_actual)
        permitidas = [i for i, c in enumerate(letras) if c.isalpha()]
        num_ocultas = max(1, int(len(permitidas) * self.porcentaje_ocultar // 100))
        ocultas = random.sample(permitidas, num_ocultas)
        return ''.join(['_' if i in ocultas else c for i, c in enumerate(letras)])
        
    def actualizar_interfaz(self):
        self.lbl_palabra_oculta.config(text=self.palabra_oculta)
        self.lbl_puntaje.config(text=f"Puntaje: {self.puntaje}")
        self.lbl_nivel.config(text=f"Nivel: {self.porcentaje_ocultar//10}")
        self.entrada.delete(0, tk.END)
        
    def verificar_respuesta(self, event=None):
        respuesta = self.entrada.get().strip().lower()
        if respuesta == self.palabra_actual.lower():
            self.manejar_acierto()
        else:
            self.manejar_error(respuesta)
        
    def manejar_acierto(self):
        self.puntaje += 10
        self.racha += 1
        self.actualizar_dificultad()
        self.historial.insert('', 'end', values=(self.palabra_actual, "✅ Correcto"))
        self.generar_nueva_palabra()
        self.actualizar_interfaz()
        
    def manejar_error(self, respuesta):
        self.intentos += 1
        self.racha = 0
        self.historial.insert('', 'end', values=(respuesta, "❌ Incorrecto"))
        
        if self.intentos >= 2:
            self.historial.insert('', 'end', values=(f"Respuesta: {self.palabra_actual}", "💡 Solución"))
            self.generar_nueva_palabra()
            self.actualizar_interfaz()
        
    def actualizar_dificultad(self):
        if self.racha % 3 == 0 and self.porcentaje_ocultar < 70:
            self.porcentaje_ocultar += 10
            messagebox.showinfo(
                "¡Nivel Superior!", 
                f"¡Nuevo nivel {self.porcentaje_ocultar//10}!\nLetras ocultas: {self.porcentaje_ocultar}%"
            )
        
    def mostrar_pista(self):
        if not self.pista_mostrada and self.puntaje >= 5:
            pista = (
                f"Prefijo: {self.palabra_actual[:3].upper()}\n"
                f"Longitud: {len(self.palabra_actual)} letras\n"
                f"Categoría: Adjetivo"
            )
            messagebox.showinfo("Pista", pista)
            self.puntaje -= 5
            self.pista_mostrada = True
            self.actualizar_interfaz()
        elif self.puntaje < 5:
            messagebox.showwarning("Puntos insuficientes", "¡Necesitas al menos 5 puntos para obtener una pista!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaPrefijosApp(root)
    root.mainloop()
