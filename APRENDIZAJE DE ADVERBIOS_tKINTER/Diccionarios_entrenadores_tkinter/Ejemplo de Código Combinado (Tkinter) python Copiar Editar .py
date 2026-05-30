import tkinter as tk
from tkinter import messagebox

# Diccionario con ejemplos de lecciones (solo mostramos 3 por brevedad)
lecciones = {
    1: {"titulo": "Uso de la tilde", "contenido": "Aprende a usar la tilde correctamente."},
    2: {"titulo": "Uso de 'b' y 'v'", "contenido": "Reglas para distinguir palabras con 'b' y 'v'."},
    3: {"titulo": "El pluscuamperfecto", "contenido": "Ejemplo: Yo había estudiado antes del examen."},
    # ... puedes agregar hasta 100
}

# Diccionario con ejercicios (solo unos ejemplos)
ejercicios = {
    1: {"pregunta": "¿Cuál palabra lleva tilde?", "opciones": ["camion", "avion", "café"], "respuesta": "café"},
    2: {"pregunta": "¿Cuál palabra se escribe con 'b'?", "opciones": ["tubo", "tuvo", "hube"], "respuesta": "tubo"},
    3: {"pregunta": "Completa: Ella ______ terminado antes de salir.", "opciones": ["hubiera", "había", "haya"], "respuesta": "había"},
}

# Función para mostrar la lección
def abrir_leccion(num):
    ventana_leccion = tk.Toplevel()
    ventana_leccion.title(f"Lección {num}: {lecciones[num]['titulo']}")
    
    contenido = lecciones[num]['contenido']
    tk.Label(ventana_leccion, text=contenido, wraplength=400, justify="left").pack(pady=10)

    # Botón para acceder al ejercicio relacionado
    if num in ejercicios:
        tk.Button(ventana_leccion, text="Ejercicio relacionado", command=lambda: mostrar_ejercicio(num)).pack(pady=10)

# Función para mostrar un ejercicio
def mostrar_ejercicio(num):
    ejercicio = ejercicios.get(num)
    if not ejercicio:
        messagebox.showinfo("Ejercicio", "No hay ejercicio disponible para esta lección.")
        return

    ventana_ejercicio = tk.Toplevel()
    ventana_ejercicio.title("Ejercicio Interactivo")

    tk.Label(ventana_ejercicio, text=ejercicio["pregunta"], font=("Arial", 12)).pack(pady=10)

    def verificar(respuesta):
        if respuesta == ejercicio["respuesta"]:
            messagebox.showinfo("Correcto", "¡Bien hecho! Respuesta correcta.")
        else:
            messagebox.showerror("Incorrecto", "Respuesta incorrecta. Inténtalo de nuevo.")

    for opcion in ejercicio["opciones"]:
        tk.Button(ventana_ejercicio, text=opcion, command=lambda r=opcion: verificar(r)).pack(pady=5)

# Función para abrir la sección de ejercicios generales
def abrir_ejercicios_generales():
    ventana_general = tk.Toplevel()
    ventana_general.title("Ejercicios Interactivos Generales")

    for num in ejercicios:
        tk.Button(ventana_general, text=f"Ejercicio {num}", command=lambda n=num: mostrar_ejercicio(n)).pack(pady=3)

# Interfaz principal
ventana = tk.Tk()
ventana.title("Curso de Lengua Castellana")
ventana.geometry("500x600")

tk.Label(ventana, text="Curso de Lengua Castellana", font=("Helvetica", 16, "bold")).pack(pady=10)

# Botón de ejercicios generales
tk.Button(ventana, text="Ejercicios Interactivos", bg="lightblue", command=abrir_ejercicios_generales).pack(pady=10)

# Lista de botones de lecciones (puedes expandir hasta 100)
for i in range(1, 4):  # Cambia a range(1, 101) para mostrar las 100 lecciones
    tk.Button(ventana, text=f"Lección {i}: {lecciones[i]['titulo']}", command=lambda i=i: abrir_leccion(i)).pack(pady=2)

ventana.mainloop()
