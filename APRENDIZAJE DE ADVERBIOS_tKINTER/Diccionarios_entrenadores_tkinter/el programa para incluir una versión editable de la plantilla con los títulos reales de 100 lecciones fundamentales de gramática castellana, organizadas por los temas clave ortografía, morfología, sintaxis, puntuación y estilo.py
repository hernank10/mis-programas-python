import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Curso de Gramática Castellana")
root.geometry("600x450")

# Diccionario de lecciones organizadas por tema
lecciones = {
    "Ortografía": [
        "Uso de la B y V", "Reglas de la C, S y Z", "Uso de la G y J", "Uso de la H",
        "Uso de la LL y Y", "Uso de la R y RR", "Uso de la M y N", "Acentuación de palabras agudas",
        "Acentuación de palabras graves", "Acentuación de palabras esdrújulas"
    ],
    "Morfología": [
        "Tipos de palabras: sustantivos", "Tipos de palabras: adjetivos", "Tipos de palabras: verbos",
        "Tipos de palabras: adverbios", "Conjunción y preposición", "Pronombres personales y demostrativos",
        "El artículo y sus usos", "Flexión verbal y conjugación", "Modos y tiempos verbales", "Verbos regulares e irregulares"
    ],
    "Sintaxis": [
        "Estructura de la oración", "Sujeto y predicado", "Complementos del verbo",
        "Concordancia entre sujeto y verbo", "Tipos de oración", "Oraciones simples y compuestas",
        "Oraciones subordinadas", "Oraciones impersonales", "Uso del gerundio y participio",
        "Construcciones enfáticas"
    ],
    "Puntuación": [
        "Uso del punto y la coma", "Uso del punto y coma", "Uso de los dos puntos",
        "Uso de comillas y paréntesis", "Uso del guion y raya", "Uso de la interrogación y exclamación",
        "Uso de los puntos suspensivos", "Errores comunes en puntuación", "Uso de conectores en textos",
        "Puntuación en el discurso directo"
    ],
    "Estilo y Redacción": [
        "Claves de una buena redacción", "Coherencia y cohesión textual", "Uso adecuado de sinónimos y antónimos",
        "El párrafo y su estructura", "Cómo evitar el pleonasmo", "Uso de la voz activa y pasiva",
        "Errores frecuentes en la redacción", "Uso de conectores argumentativos", "Cómo construir una conclusión efectiva",
        "Revisión y corrección de textos"
    ]
}

# Variables globales
indice_actual = 0
tema_actual = list(lecciones.keys())[0]
texto_leccion = tk.StringVar()

# Función para mostrar lección
def mostrar_leccion():
    global tema_actual, indice_actual
    temas = lecciones[tema_actual]
    texto_leccion.set(f"{tema_actual} - {temas[indice_actual]}\nAquí va el contenido de la lección...")

# Función para cambiar de lección
def cambiar_leccion(direccion):
    global indice_actual
    if direccion == "siguiente" and indice_actual < len(lecciones[tema_actual]) - 1:
        indice_actual += 1
    elif direccion == "anterior" and indice_actual > 0:
        indice_actual -= 1
    mostrar_leccion()

# Función para cambiar de tema
def cambiar_tema(nuevo_tema):
    global tema_actual, indice_actual
    tema_actual = nuevo_tema
    indice_actual = 0
    mostrar_leccion()

# Menú de selección de temas
frame_temas = tk.Frame(root)
frame_temas.pack(pady=10)
tk.Label(frame_temas, text="Selecciona un tema:", font=("Arial", 12)).pack(side=tk.LEFT)
for tema in lecciones.keys():
    tk.Button(frame_temas, text=tema, command=lambda t=tema: cambiar_tema(t)).pack(side=tk.LEFT)

# Área de contenido de la lección
contenido = tk.Label(root, textvariable=texto_leccion, wraplength=500, font=("Arial", 12))
contenido.pack(pady=20)

# Botones de navegación
boton_anterior = tk.Button(root, text="⬅ Anterior", command=lambda: cambiar_leccion("anterior"))
boton_siguiente = tk.Button(root, text="Siguiente ➡", command=lambda: cambiar_leccion("siguiente"))
boton_anterior.pack(side=tk.LEFT, padx=20)
boton_siguiente.pack(side=tk.RIGHT, padx=20)

# Mostrar primera lección
mostrar_leccion()

# Ejecutar la aplicación
root.mainloop()
