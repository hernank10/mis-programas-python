import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Reportes(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg=COLORES["fondo"])
        self.controlador = controlador
        self.historial = []
        
        tk.Button(self, text="← Menú principal", 
                 command=lambda: controlador.mostrar_frame("MainMenu"),
                 bg=COLORES["boton"], fg="white").pack(anchor="nw")
        
        self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor=COLORES["fondo"])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(pady=20)
        
        tk.Button(self, text="Generar PDF", command=self.generar_pdf,
                 bg=COLORES["boton"], fg="white").pack()
        
        self.actualizar_grafico()
    
    def agregar_error(self, ejemplo, intento):
        self.historial.append({
            "fecha": time.strftime("%d/%m/%Y %H:%M"),
            "ejemplo": ejemplo,
            "intento": intento
        })
    
    def actualizar_grafico(self):
        self.ax.clear()
        
        categorias = list(self.controlador.recursos.keys())
        errores = [sum(1 for e in self.historial if cat in e["ejemplo"]) for cat in categorias]
        
        bars = self.ax.bar(categorias, errores, color=['#3498DB', '#27AE60', '#E74C3C'])
        self.ax.set_title("Errores por categoría", color='white')
        self.ax.set_facecolor(COLORES["fondo"])
        self.fig.patch.set_facecolor(COLORES["fondo"])
        
        for spine in self.ax.spines.values():
            spine.set_color('white')
        
        self.ax.tick_params(colors='white')
        self.canvas.draw()
    
    def generar_pdf(self):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Reporte de Progreso", ln=1, align='C')
        pdf.cell(200, 10, txt=f"Fecha: {time.strftime('%d/%m/%Y')}", ln=1)
        pdf.cell(200, 10, txt=f"Aciertos: {self.controlador.puntuacion['correctas']}", ln=1)
        pdf.cell(200, 10, txt=f"Errores: {self.controlador.puntuacion['incorrectas']}", ln=1)
        
        pdf.add_page()
        pdf.cell(200, 10, txt="Detalle de Errores:", ln=1)
        for error in self.historial[-10:]:  # Últimos 10 errores
            pdf.multi_cell(0, 10, 
                f"Fecha: {error['fecha']}\n"
                f"Ejemplo: {error['ejemplo']}\n"
                f"Tu intento: {error['intento']}\n"
                "----------------------------------------")
        
        pdf.output("reporte.pdf")
        messagebox.showinfo("Éxito", "Reporte generado: reporte.pdf")
