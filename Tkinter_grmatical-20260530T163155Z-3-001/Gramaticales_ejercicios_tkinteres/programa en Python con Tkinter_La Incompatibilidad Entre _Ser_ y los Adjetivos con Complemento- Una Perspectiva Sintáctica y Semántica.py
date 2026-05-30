import tkinter as tk
from tkinter import messagebox

def mostrar_explicacion():
    explicacion = (
        "En español, algunos adjetivos pueden usarse con 'ser' y 'estar', pero no siempre con complemento.\n"
        "Ejemplo: \n"
        "- Es casado (*con María) (Incorrecto)\n"
        "- Está casado (con María) (Correcto)\n\n"
        "Este fenómeno se debe a la diferencia entre predicación individual y episódica.\n"
        "Ser denota propiedades inherentes y tiende a rechazar complementos."
    )
    messagebox.showinfo("Explicación", explicacion)

def mostrar_ejemplos():
    ejemplos = (
        "Ejemplos:\n"
        "1. Juan es orgulloso (*de su hijo).\n"
        "2. Juan está orgulloso (de su hijo).\n"
        "3. Pedro es atento (*con sus clientes).\n"
        "4. Pedro está atento (con sus clientes).\n"
    )
    messagebox.showinfo("Ejemplos", ejemplos)

def verificar_ejercicio():
    respuesta = entrada.get()
    if "ser" in respuesta and "con" in respuesta:
        mensaje = "Revisa tu oración. ¿Seguro que 'ser' admite complemento?"
    else:
        mensaje = "¡Bien hecho! Parece que entendiste la regla."
    messagebox.showinfo("Revisión", mensaje)

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Práctica sobre 'Ser' y Adjetivos con Complemento")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Elige una opción para practicar:", font=("Arial", 12))
etiqueta.pack(pady=10)

boton_explicacion = tk.Button(ventana, text="Ver Explicación", command=mostrar_explicacion)
boton_explicacion.pack(pady=5)

boton_ejemplos = tk.Button(ventana, text="Ver Ejemplos", command=mostrar_ejemplos)
boton_ejemplos.pack(pady=5)

etiqueta_ejercicio = tk.Label(ventana, text="Escribe una oración con 'ser' o 'estar' y un adjetivo:")
etiqueta_ejercicio.pack(pady=10)

entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

boton_verificar = tk.Button(ventana, text="Verificar Ejercicio", command=verificar_ejercicio)
boton_verificar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=20)

ventana.mainloop()
