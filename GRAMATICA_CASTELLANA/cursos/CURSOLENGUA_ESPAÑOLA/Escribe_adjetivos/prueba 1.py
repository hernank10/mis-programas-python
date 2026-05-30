# Lista de elementos gramaticales
elementos_gramaticales = [
    "conjunciones",
    "interjecciones",
    "preposiciones",
    "artículos",
    "sustantivos",
    "adjetivos",
    "verbos",
    "adverbios",
    "pronombres",
]

# Lista de oraciones
oraciones = [
    "Compré leche y pan.",
    "¡Ah! Me olvidé de las llaves.",
    "El perro de mi amigo es muy peludo.",
    "El cielo es tan azul como el mar.",
    "Ella es tan inteligente como su hermano.",
    "La casa es tan grande como un castillo.",
    "Se comportó como si estuviera loco.",
    "Hablaba como si supiera mucho del tema.",
    "Me miró como si me viera por primera vez."
]

# Función para obtener la respuesta del usuario
def obtener_respuesta(pregunta):
    respuesta = input(pregunta)
    return respuesta.strip().lower()

# Función para verificar si la respuesta es correcta
def verificar_respuesta(respuesta, respuesta_correcta):
    return respuesta == respuesta_correcta

# Función para identificar el elemento gramatical
def identificar_elemento_gramatical(oracion):
    for elemento in elementos_gramaticales:
        if elemento in oracion:
            return elemento
    return None

# Función para reescribir la oración
def reescribir_oracion(oracion, elemento, nueva_palabra):
    return oracion.replace(elemento, nueva_palabra)

# Función para mostrar las instrucciones
def mostrar_instrucciones():
    print("Este programa te permite practicar la identificación y reescritura de oraciones con diferentes elementos gramaticales.")
    print("Sigue estos pasos:")
    print("1. Elige el tipo de oración que deseas practicar.")
    print("2. Lee la oración que se te presenta.")
    print("3. Identifica el elemento gramatical en la oración.")
    print("4. Reescribe la oración reemplazando el elemento gramatical por una palabra nueva.")
    print("5. Se te indicará si la reescritura es correcta.")

# Función para iniciar el programa
def iniciar_programa():
    # Mostrar las instrucciones
    mostrar_instrucciones()

    # Elegir el tipo de oración
    tipo_oracion = obtener_respuesta("¿Qué tipo de oración deseas practicar? (conjunciones, interjecciones, etc.) ")

    # Filtrar las oraciones por el tipo elegido
    oraciones_filtradas = [
        oracion for oracion in oraciones if tipo_oracion in oracion
    ]

    # Bucle para recorrer las oraciones
    for i in range(len(oraciones_filtradas)):
        # Mostrar la oración al usuario
        print(f"Oración {i + 1}: {oraciones_filtradas[i]}")

        # Identificar el elemento gramatical
        elemento = identificar_elemento_gramatical(oraciones_filtradas[i])

        # Si se ha encontrado un elemento gramatical
        if elemento:
            # Solicitar al usuario que reescriba la oración
            nueva_palabra = obtener_respuesta(f"¿Qué palabra quieres usar para reemplazar {elemento} en la oración? ")

            # Reescribir la oración
            oracion_reescrita = reescribir_oracion(oraciones_filtradas[i], elemento, nueva_palabra)

            # Verificar si la oración reescrita es correcta
            respuesta_correcta = obtener_respuesta(f"¿La oración reescrita '{oracion_reescrita}' es correcta? (sí/no) ")

            if verificar_respuesta(respuesta_correcta, "sí"):
                print("¡La oración reescrita es correcta!")
            else:
                print("La oración reescrita no es correcta.")

# Iniciar el programa
iniciar_programa()
