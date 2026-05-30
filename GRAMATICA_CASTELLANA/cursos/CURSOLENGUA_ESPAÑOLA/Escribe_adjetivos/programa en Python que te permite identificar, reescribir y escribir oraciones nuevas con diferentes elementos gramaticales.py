# Función para verificar y reescribir una oración
def verificar_y_reescribir(oracion, tipo_gramatical):
    print("La oración es:", oracion)
    elemento_usuario = input(f"¿Cuál es el {tipo_gramatical} de esta oración? ")
    if elemento_usuario.lower() in oracion.lower():
        print("¡Correcto!")
        nueva_oracion = input("Por favor, reescribe la oración: ")
        if nueva_oracion == oracion:
            print("¡Correcto! La oración ha sido reescrita correctamente.")
        else:
            print("La oración reescrita no es correcta.")
    else:
        print(f"Incorrecto. El {tipo_gramatical} de la oración es:", [word for word in oracion.split() if word.lower() in oracion.lower()][0])

# Lista de oraciones con adjetivos
oraciones_adjetivos = [
    "Juan es un chico inteligente.",
    "El perro grande corre rápido.",
    # Añade aquí las 90 oraciones restantes
]

# Lista de oraciones con interjecciones
oraciones_interjecciones = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
    ]

# Lista de oraciones con suatantivos
oraciones_sustantivos = [
    " la cabeza.",
    "sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Añade aquí las oraciones con verbos
oraciones_verbo = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Lista de oraciones con adverbios
# Añade aquí las oraciones con adverbios
oraciones_adverbios = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Lista de oraciones con artículos
# Añade aquí las oraciones con artículos
oraciones_artículos = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Lista de oraciones con pronombres
# Añade aquí las oraciones con pronombres
oraciones_pronombres = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Lista de oraciones con conjunciones
# Añade aquí las oraciones con conjunciones
oraciones_conjunciones = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Lista de oraciones con preposiciones
# Añade aquí las oraciones con preposiciones
oraciones_preposiciones = [
    "¡Ay! Me duele mucho la cabeza.",
    "¡Oh! Qué sorpresa tan agradable.",
    # Añade aquí las oraciones restantes
]
# Función para pedir al usuario que elija un tipo de oración
def elegir_tipo_oracion():
    print("Elige un tipo de oración para practicar:")
    print("1. Oraciones con adjetivos")
    print("2. Oraciones con interjecciones")
    # Añade aquí las opciones restantes
    opcion = input("Ingrese el número correspondiente al tipo de oración: ")
    return opcion

# Función principal
def main():
    opcion = elegir_tipo_oracion()

    if opcion == "1":
        # Iterar sobre las oraciones con adjetivos
        for oracion in oraciones_adjetivos:
            verificar_y_reescribir(oracion, "adjetivo")
    elif opcion == "2":
        # Iterar sobre las oraciones con interjecciones
        for oracion in oraciones_interjecciones:
            verificar_y_reescribir(oracion, "interjección")
    # Añade aquí las opciones restantes

# Llamar a la función principal
main()
