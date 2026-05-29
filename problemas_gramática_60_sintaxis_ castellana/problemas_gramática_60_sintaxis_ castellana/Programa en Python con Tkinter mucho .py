import tkinter as tk
from tkinter import messagebox

# Función para mostrar ejemplos
def mostrar_ejemplos():
    ejemplos = [
        "María ha sufrido mucho en su vida.",  # Intensidad
        "Antonio piensa mucho en ella.",  # Frecuencia o duración
        "Ha comido mucho.",  # Cantidad
        "*Ana viene mucho de familia aristocrática."  # Agramaticalidad
    ]
    ejemplos_texto = "\n".join([f"{i + 1}. {ejemplo}" for i, ejemplo in enumerate(ejemplos)])
    messagebox.showinfo("Ejemplos de interpretaciones de 'mucho'", ejemplos_texto)

# Función para practicar ejercicios
def practicar_ejercicios():
    ejercicios = [
        {"oracion": "María ha sufrido ___ en su vida.", "respuesta": "mucho", "interpretacion": "intensidad"},
        {"oracion": "Antonio piensa ___ en ella.", "respuesta": "mucho", "interpretacion": "frecuencia o duración"},
        {"oracion": "Ha comido ___.", "respuesta": "mucho", "interpretacion": "cantidad"},
        {"oracion": "*Ana viene ___ de familia aristocrática.", "respuesta": "mucho", "interpretacion": "agramaticalidad"}
    ]

    def verificar_respuesta():
        respuesta_usuario = entrada_respuesta.get().strip().lower()
        if respuesta_usuario == ejercicio_actual["respuesta"].lower():
            messagebox.showinfo("Resultado", f"¡Correcto! 🎉\nInterpretación: {ejercicio_actual['interpretacion']}")
        else:
            messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta es: '{ejercicio_actual['respuesta']}'.")
        siguiente_ejercicio()

    def siguiente_ejercicio():
        nonlocal indice_ejercicio
        indice_ejercicio += 1
        if indice_ejercicio < len(ejercicios):
            ejercicio_actual = ejercicios[indice_ejercicio]
            etiqueta_oracion.config(text=ejercicio_actual["oracion"])
            entrada_respuesta.delete(0, tk.END)
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejercicios!")
            ventana_ejercicios.destroy()

    # Crear una nueva ventana para los ejercicios
    ventana_ejercicios = tk.Toplevel()
    ventana_ejercicios.title("Practicar con ejercicios")

    indice_ejercicio = 0
    ejercicio_actual = ejercicios[indice_ejercicio]

    # Etiqueta con la oración a completar
    etiqueta_oracion = tk.Label(ventana_ejercicios, text=ejercicio_actual["oracion"])
    etiqueta_oracion.pack(pady=10)

    # Entrada para la respuesta del usuario
    entrada_respuesta = tk.Entry(ventana_ejercicios)
    entrada_respuesta.pack(pady=10)

    # Botón para verificar la respuesta
    boton_verificar = tk.Button(ventana_ejercicios, text="Verificar", command=verificar_respuesta)
    boton_verificar.pack(pady=10)

# Función principal
def main():
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Práctica: Interpretaciones de 'mucho'")

    # Botón para ver ejemplos
    boton_ejemplos = tk.Button(ventana_principal, text="Ver ejemplos", command=mostrar_ejemplos)
    boton_ejemplos.pack(pady=10)

    # Botón para practicar ejercicios
    boton_ejercicios = tk.Button(ventana_principal, text="Practicar con ejercicios", command=practicar_ejercicios)
    boton_ejercicios.pack(pady=10)

    # Botón para salir
    boton_salir = tk.Button(ventana_principal, text="Salir", command=ventana_principal.destroy)
    boton_salir.pack(pady=10)

    # Iniciar el bucle principal de la ventana
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
