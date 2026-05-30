import tkinter as tk

def mostrar_regla():
    texto.set("El punto y coma separa elementos de una lista compleja.\nEjemplo: Traje manzanas, peras y uvas; limones, naranjas y mandarinas.")

ventana = tk.Tk()
ventana.title("Reglas Ortográficas")

texto = tk.StringVar()
texto.set("Haz clic en el botón para ver una regla.")

etiqueta = tk.Label(ventana, textvariable=texto, wraplength=400, justify="left")
etiqueta.pack()

boton = tk.Button(ventana, text="Mostrar Regla", command=mostrar_regla)
boton.pack()

ventana.mainloop()
