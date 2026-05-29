import tkinter as tk
from tkinter import messagebox

# 20 oraciones incorrectas y sus correcciones
ejercicios = [
    ("El perro ladra y corre, pero el gato dormía y jugaban.", 
     "El perro ladra y corre, pero el gato dormía y jugaba."),
    ("Salimos temprano sin embargo llegamos tarde.", 
     "Salimos temprano; sin embargo, llegamos tarde."),
    ("Yo quiero ir al cine y mi hermano al parque.", 
     "Yo quiero ir al cine y mi hermano quiere ir al parque."),
    ("Porque llovía no salimos.", 
     "Porque llovía, no salimos."),
    ("El niño estudia juega y pinta.", 
     "El niño estudia, juega y pinta."),
    ("Fui a la tienda compre pan y leche.", 
     "Fui a la tienda, compré pan y leche."),
    ("María canta, y baila, y ríe, pero también estudian.", 
     "María canta, baila y ríe, pero también estudia."),
    ("Si tu vienes yo iremos contigo.", 
     "Si tú vienes, yo iré contigo."),
    ("El profesor explico la clase no entendimos.", 
     "El profesor explicó la clase, pero no entendimos."),
    ("Me gusta leer escribir y pintando.", 
     "Me gusta leer, escribir y pintar."),
    ("Llegue tarde estaba lloviendo.", 
     "Llegué tarde porque estaba lloviendo."),
    ("Aunque estaba cansado fui a la fiesta y divertimos.", 
     "Aunque estaba cansado, fui a la fiesta y me divertí."),
    ("Yo estudio todos los días sin embargo no apruebo.", 
     "Yo estudio todos los días; sin embargo, no apruebo."),
    ("Él jugaba fútbol y su hermana a las muñecas.", 
     "Él jugaba fútbol y su hermana jugaba a las muñecas."),
    ("Como hacía frío usamos abrigos.", 
     "Como hacía frío, usamos abrigos."),
    ("Me gusta correr, nadar y que baila.", 
     "Me gusta correr, nadar y bailar."),
    ("Salimos rápido el carro se dañó.", 
     "Salimos rápido, pero el carro se dañó."),
    ("Quiero estudiar medicina y también a viajar.", 
     "Quiero estudiar medicina y también viajar."),
    ("Estaba enfermo fui a la escuela.", 
     "Estaba enfermo, pero fui a la escuela."),
    ("Ella lee escribe y cantaba.", 
     "Ella lee, escribe y canta."),
]

class JuegoGramática:
    def __init__(self, root):
        self.root = root
        self.root.title("Defiende la Gramática (Versión Minimalista)")
        self.root.geometry("600x300")
        
        self.indice = 0
        self.puntaje = 0

        self.oracion_incorrecta = tk.Label(root, text=ejercicios[self.indice][0], wraplength=500, font=("Arial", 12))
        self.oracion_incorrecta.pack(pady=10)

        self.entrada = tk.Entry(root, width=70, font=("Arial", 12))
        self.entrada.pack(pady=10)

        self.boton_comprobar = tk.Button(root, text="Comprobar", command=self.comprobar)
        self.boton_comprobar.pack(pady=5)

        self.boton_siguiente = tk.Button(root, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.pack(pady=5)

        self.label_puntaje = tk.Label(root, text=f"Puntaje: {self.puntaje}", font=("Arial", 12))
        self.label_puntaje.pack(pady=10)

    def comprobar(self):
        respuesta = self.entrada.get().strip()
        correcta = ejercicios[self.indice][1]
        if respuesta == correcta:
            messagebox.showinfo("Correcto ✅", "¡Muy bien! La oración está corregida.")
            self.puntaje += 1
            self.label_puntaje.config(text=f"Puntaje: {self.puntaje}")
        else:
            messagebox.showwarning("Incorrecto ❌", f"La corrección correcta es:\n\n{correcta}")

    def siguiente(self):
        self.indice += 1
        if self.indice < len(ejercicios):
            self.oracion_incorrecta.config(text=ejercicios[self.indice][0])
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showinfo("Fin del juego", f"Juego terminado.\nPuntaje final: {self.puntaje}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoGramática(root)
    root.mainloop()
