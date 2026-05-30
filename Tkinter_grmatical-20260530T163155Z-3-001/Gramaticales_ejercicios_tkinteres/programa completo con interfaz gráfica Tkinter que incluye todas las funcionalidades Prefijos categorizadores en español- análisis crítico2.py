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
        
    # [...] (Configuración de estilos y widgets igual al código anterior)

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
        letras = list(self.palabra_actual["palabra"])
        # ... (resto del método igual al código anterior)
        
    def mostrar_pista(self):
        if not self.pista_mostrada and self.puntaje >= 5:
            pista = (
                f"Prefijo: {self.palabra_actual['palabra'][:3].upper()}\n"
                f"Base: {self.palabra_actual['base']} ({'sustantivo'})\n"
                f"Categoría resultante: {self.palabra_actual['categoria']}\n"
                f"Longitud: {len(self.palabra_actual)['palabra']} letras"
            )
            messagebox.showinfo("Análisis Morfológico", pista)
            self.puntaje -= 5
            self.pista_mostrada = True
            self.actualizar_interfaz()
        
    # ... (resto de métodos igual al código anterior)

if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaPrefijosApp(root)
    root.mainloop()
