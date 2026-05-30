import tkinter as tk
from tkinter import ttk

class MapaConceptual(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mapa Conceptual de Reglas Gramaticales")
        self.geometry("1000x800")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.dibujar_mapa()
        
    def dibujar_mapa(self):
        # Coordenadas base y configuración
        x, y = 100, 100
        ancho_nodo = 200
        alto_nodo = 80
        espacio = 150
        
        # Reglas principales
        reglas = {
            831: "Concordancia con\npredicados plurales",
            835: "Conjunción 'ni'\ny negación",
            838: "Sujetos unidos\npor 'con'/'tanto como'",
            840: "Adjetivos\nespeciales",
            832: "Sujetos múltiples\ncon 'y'",
            836: "Verbo entre\nsujetos",
            833: "Verbo singular\ncon último sujeto",
            837: "Conjunción 'o'",
            834: "Conjunción\ntácita",
            839: "Adjetivo ante\nmúltiples sustantivos"
        }
        
        # Dibujar nodos y conexiones
        nodos = {}
        for idx, (num, texto) in enumerate(reglas.items()):
            fila = idx // 5
            columna = idx % 5
            x_pos = x + columna * (ancho_nodo + espacio)
            y_pos = y + fila * (alto_nodo + espacio)
            
            nodo = self.canvas.create_rectangle(
                x_pos, y_pos, 
                x_pos + ancho_nodo, y_pos + alto_nodo,
                fill="#E1F5FE", outline="#039BE5",
                width=2
            )
            
            texto_id = self.canvas.create_text(
                x_pos + ancho_nodo/2, y_pos + alto_nodo/2,
                text=f"Regla {num}\n{texto}",
                font=("Arial", 9, "bold"),
                justify=tk.CENTER
            )
            
            nodos[num] = (nodo, texto_id, x_pos, y_pos)
            
        # Conexiones entre reglas relacionadas
        conexiones = [
            (831, 832), (832, 833), (832, 834),
            (835, 838), (836, 837), (838, 840),
            (839, 840), (833, 837), (834, 839)
        ]
        
        for inicio, fin in conexiones:
            x1 = nodos[inicio][2] + ancho_nodo
            y1 = nodos[inicio][3] + alto_nodo/2
            x2 = nodos[fin][2]
            y2 = nodos[fin][3] + alto_nodo/2
            
            self.canvas.create_line(
                x1, y1, x2, y2,
                arrow=tk.LAST, 
                fill="#616161",
                width=1.5,
                dash=(4, 2)
            )
        
        # Etiqueta interactiva
        self.lbl_info = ttk.Label(self, background="white", font=("Arial", 10))
        self.canvas.bind("<Motion>", self.mostrar_info)
        
    def mostrar_info(self, event):
        for num, (nodo, texto_id, x, y) in self.nodos.items():
            bbox = self.canvas.bbox(nodo)
            if bbox[0] < event.x < bbox[2] and bbox[1] < event.y < bbox[3]:
                ejemplos = {
                    831: "EjConcordancia con\npredicados plurales: 'Leer y escribir son actividades...'",
                    838: "Ej: 'El profesor con los alumnos organizaron'",
                    835: "Ej: 'Ni el frío ni el hambre le detuvieron'",
                    840: "Ej: 'Los mismos rey y reina inauguraron...'"
                }
                self.lbl_info.config(text=ejemplos.get(num, ""))
                self.lbl_info.place(x=event.x + 15, y=event.y - 20)
                return
        self.lbl_info.place_forget()

# Modificar la clase principal para agregar el mapa
class AplicacionConcordancia(tk.Tk):
    def __init__(self):
        super().__init__()
        # ... (código anterior) ...
        self.crear_widgets()
        
    def crear_widgets(self):
        # ... (código anterior) ...
        ttk.Button(
            self.main_frame, 
            text="Ver Mapa Conceptual", 
            command=self.abrir_mapa
        ).pack(pady=5)
        
    def abrir_mapa(self):
        MapaConceptual(self)

# ... (resto del código anterior) ...
