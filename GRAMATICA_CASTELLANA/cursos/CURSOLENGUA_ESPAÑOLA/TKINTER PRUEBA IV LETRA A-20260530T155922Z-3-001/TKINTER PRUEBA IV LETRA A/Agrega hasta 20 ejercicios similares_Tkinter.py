import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- DATOS DEL EJERCICIO ---------------------------- #
ejercicios = [
    {
        "pregunta": "Completa la palabra: cab__llo (animal)",
        "respuesta": "caballo",
        "regla": "Se escribe con 'll' porque es un sustantivo que proviene del latín 'caballus'."
    },
    {
        "pregunta": "Completa la palabra: flori__ero (objeto para flores)",
        "respuesta": "floricero",
        "regla": "Se escribe con 'c' porque forma parte del sufijo -icero, que indica profesión u oficio."
    },
    {
        "pregunta": "Completa: feliz__dad (estado de ánimo)",
        "respuesta": "felicidad",
        "regla": "Se escribe con 'c' porque las palabras terminadas en -icidad van con 'c'."
    },
    {
        "pregunta": "Completa: apa__ionante (emocionante)",
        "respuesta": "apasionante",
        "regla": "Lleva 's' porque no hay ningún motivo ortográfico para usar 'c' o 'z'."
    },
    {
        "pregunta": "Completa: velo__dad (rapidez)",
        "respuesta": "velocidad",
        "regla": "Las palabras terminadas en -icidad/-idad van con 'c'."
    },
    # Agrega hasta 20 ejercicios similares...
]

puntaje = 0
modo_examen = False
indice_actual = 0
respuestas_usuario = []

# ---------------------------- FUNCIONES DE LA APP ---------------------------- #
def cargar_ejercicio():
    global indice_actual
    if indice_actual < len(ejercicios):
        entrada_respuesta.delete(0, tk.END)
        lbl_pregunta.config(text=ejercicios[indice_actual]["pregunta"])
        lbl_resultado.config(text="")
    else:
        mostrar_resultado()

def verificar_respuesta():
    global puntaje, indice_actual
    user_input = entrada_respuesta.get().strip().lower()
    correcta = ejercicios[indice_actual]["respuesta"]
    respuestas_usuario.append((ejercicios[indice_actual]["pregunta"], user_input, correcta))

    if user_input == correcta:
        puntaje += 1
        if not modo_examen:
            lbl_resultado.config(text="✔ Correcto", fg="green")
    else:
        if not modo_examen:
            lbl_resultado.config(text=f"✘ Incorrecto. Respuesta: {correcta}", fg="red")

    indice_actual += 1
    ventana.after(1000, cargar_ejercicio)

def mostrar_regla():
    regla = ejercicios[indice_actual]["regla"]
    messagebox.showinfo("Regla ortográfica", regla)

def mostrar_resultado():
    ventana_principal.pack_forget()
    resultado_final.pack()
    lbl_final.config(text=f"Has obtenido {puntaje} de {len(ejercicios)} respuestas correctas.")
    detalles = ""
    for preg, user, corr in respuestas_usuario:
        detalles += f"\n{preg}\nTu respuesta: {user}\nCorrecta: {corr}\n"
    txt_detalles.insert(tk.END, detalles)

def iniciar_modo(modo):
    global modo_examen, puntaje, indice_actual, respuestas_usuario
    modo_examen = (modo == "examen")
    puntaje = 0
    indice_actual = 0
    respuestas_usuario = []
    menu_inicio.pack_forget()
    ventana_principal.pack()
    cargar_ejercicio()

# ---------------------------- INTERFAZ GRÁFICA ---------------------------- #
ventana = tk.Tk()
ventana.title("Práctica ortográfica: Uso de C, S y Z")
ventana.geometry("600x400")

menu_inicio = tk.Frame(ventana)
menu_inicio.pack(pady=100)

lbl_bienvenida = tk.Label(menu_inicio, text="Elige el modo de práctica", font=("Arial", 16))
lbl_bienvenida.pack(pady=20)

btn_practica = tk.Button(menu_inicio, text="Modo Práctica", width=20, command=lambda: iniciar_modo("practica"))
btn_examen = tk.Button(menu_inicio, text="Modo Examen", width=20, command=lambda: iniciar_modo("examen"))

btn_practica.pack(pady=10)
btn_examen.pack(pady=10)

ventana_principal = tk.Frame(ventana)

lbl_pregunta = tk.Label(ventana_principal, text="Pregunta aparecerá aquí", font=("Arial", 14), wraplength=500)
lbl_pregunta.pack(pady=20)

entrada_respuesta = tk.Entry(ventana_principal, font=("Arial", 14))
entrada_respuesta.pack(pady=10)

btn_verificar = tk.Button(ventana_principal, text="Verificar", command=verificar_respuesta)
btn_verificar.pack(pady=5)

btn_ver_regla = tk.Button(ventana_principal, text="Ver regla", command=mostrar_regla)
btn_ver_regla.pack(pady=5)

lbl_resultado = tk.Label(ventana_principal, text="", font=("Arial", 12))
lbl_resultado.pack(pady=10)

resultado_final = tk.Frame(ventana)
lbl_final = tk.Label(resultado_final, text="", font=("Arial", 16))
lbl_final.pack(pady=20)

txt_detalles = tk.Text(resultado_final, height=10, width=70)
txt_detalles.pack()

btn_salir = tk.Button(resultado_final, text="Salir", command=ventana.quit)
btn_salir.pack(pady=10)

ventana.mainloop()
