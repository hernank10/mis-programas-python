import tkinter as tk
from tkinter import ttk, messagebox

# Datos de las estructuras silábicas
estructuras = {
    'V': [('/a/', 'a'), ('/e/', 'e'), ('/i/', 'i'), ('/o/', 'o'), ('/u/', 'u')],
    'CV': [('/ka/', 'ca'), ('/lo/', 'lo'), ('/pe/', 'pe'), ('/si/', 'si'), ('/tu/', 'tu')],
    'VC': [('/al/', 'al'), ('/es/', 'es'), ('/in/', 'in'), ('/os/', 'os'), ('/un/', 'un')],
    'CVC': [('/pan/', 'pan'), ('/sol/', 'sol'), ('/mar/', 'mar'), ('/pez/', 'pez'), ('/luz/', 'luz')],
    'CCV': [('/flo/', 'flo'), ('/pra/', 'pra'), ('/tri/', 'tri'), ('/kla/', 'cla'), ('/gri/', 'gri')],
    'CCVC': [('/tɾen/', 'tren'), ('/flan/', 'flan'), ('/bɾas/', 'bras'), ('/plom/', 'plom'), ('/gɾis/', 'gris')]
}

class PracticaSilabasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Estructuras Silábicas")
        self.geometry("600x400")
        self.resizable(False, False)
        
        self.current_structure = None
        self.ejemplos = []
        self.indice_ejemplo = 0
        self.puntuacion = 0
        
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        frame = ttk.Frame(self)
        frame.pack(expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text="Elige una estructura silábica:", font=('Arial', 14)).pack(pady=10)
        
        opciones = [
            ('V - Vocal única', 'V'),
            ('CV - Consonante + Vocal', 'CV'),
            ('VC - Vocal + Consonante', 'VC'),
            ('CVC - Consonante-Vocal-Consonante', 'CVC'),
            ('CCV - Grupo consonántico + Vocal', 'CCV'),
            ('CCVC - Grupo consonántico completo', 'CCVC')
        ]
        
        for texto, estructura in opciones:
            btn = ttk.Button(
                frame, 
                text=texto,
                command=lambda e=estructura: self.iniciar_practica(e)
            )
            btn.pack(fill='x', pady=2)
        
        ttk.Button(frame, text="Salir", command=self.destroy).pack(fill='x', pady=10)

    def iniciar_practica(self, estructura):
        self.current_structure = estructura
        self.ejemplos = estructuras[estructura]
        self.indice_ejemplo = 0
        self.puntuacion = 0
        self.mostrar_ejemplo()

    def mostrar_ejemplo(self):
        self.limpiar_pantalla()
        
        frame = ttk.Frame(self)
        frame.pack(expand=True, padx=20, pady=20)
        
        if self.indice_ejemplo < len(self.ejemplos):
            afi, palabra = self.ejemplos[self.indice_ejemplo]
            
            ttk.Label(frame, 
                     text=f"Estructura: {self.current_structure}\nEjemplo {self.indice_ejemplo + 1} de {len(self.ejemplos)}",
                     font=('Arial', 12)).pack(pady=10)
            
            ttk.Label(frame, 
                     text=afi, 
                     font=('Arial', 24, 'bold')).pack(pady=20)
            
            self.entrada = ttk.Entry(frame, font=('Arial', 14))
            self.entrada.pack(pady=10)
            self.entrada.bind('<Return>', lambda e: self.verificar_respuesta())
            
            ttk.Button(frame, 
                      text="Verificar", 
                      command=self.verificar_respuesta).pack(pady=5)
            
            ttk.Button(frame, 
                      text="Menú Principal", 
                      command=self.crear_menu_principal).pack(pady=5)
        else:
            self.mostrar_resultados()

    def verificar_respuesta(self):
        respuesta = self.entrada.get().strip().lower()
        _, palabra_correcta = self.ejemplos[self.indice_ejemplo]
        
        if respuesta == palabra_correcta:
            self.puntuacion += 1
            mensaje = "✓ Correcto!"
        else:
            mensaje = f"✗ Incorrecto. La respuesta correcta es: {palabra_correcta}"
        
        messagebox.showinfo("Resultado", mensaje)
        self.indice_ejemplo += 1
        self.mostrar_ejemplo()

    def mostrar_resultados(self):
        self.limpiar_pantalla()
        
        frame = ttk.Frame(self)
        frame.pack(expand=True, padx=20, pady=20)
        
        porcentaje = (self.puntuacion / len(self.ejemplos)) * 100
        
        ttk.Label(frame, 
                 text="Resultados Finales",
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(frame, 
                 text=f"Estructura: {self.current_structure}\n"
                      f"Puntuación: {self.puntuacion}/{len(self.ejemplos)}\n"
                      f"Porcentaje: {porcentaje:.0f}%",
                 font=('Arial', 12)).pack(pady=20)
        
        ttk.Button(frame, 
                  text="Practicar de nuevo", 
                  command=lambda: self.iniciar_practica(self.current_structure)).pack(pady=5)
        
        ttk.Button(frame, 
                  text="Menú Principal", 
                  command=self.crear_menu_principal).pack(pady=5)

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = PracticaSilabasApp()
    app.mainloop()
