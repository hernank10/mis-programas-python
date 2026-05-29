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
oraciones = {
    "conjunciones": [
        "Compré leche y pan.",
        "Fui al cine o al teatro.",
        "Estudié mucho, pero no obtuve la calificación que deseaba.",
        "Me gusta leer y escribir.",
        "No tengo dinero, pero tengo tiempo.",
    ],
    "interjecciones": [
        "¡Ah! Me olvidé de las llaves.",
        "¡Cuidado! Se te va a caer el vaso.",
        "¡Hola! ¿Cómo estás?",
        "¡Ay! Me duele la cabeza.",
        "¡Felicidades! Ganaste el premio.",
    ],
    "preposiciones": [
        "El libro está sobre la mesa.",
        "Voy a ir al parque con mis amigos.",
        "Vivo cerca de la playa.",
        "Salí de la casa a las 8 de la mañana.",
        "No puedo vivir sin ti.",
    ],
    "artículos": [
        "El perro de mi amigo es muy peludo.",
        "Compré una manzana y un plátano.",
        "Los niños juegan en el parque.",
        "La casa es muy grande.",
        "El cielo es azul.",
    ],
    "sustantivos": [
        "El perro de mi amigo es muy peludo.",
        "Compré una manzana y un plátano.",
        "Los niños juegan en el parque.",
        "La casa es muy grande.",
        "El cielo es azul.",
    ],
    "adjetivos": [
        "El perro de mi amigo es muy peludo.",
        "Compré una manzana roja y un plátano verde.",
        "Los niños juegan en el parque grande.",
        "La casa es muy grande y hermosa.",
        "El cielo es azul claro.",
    ],
    "verbos": [
        "El perro de mi amigo **corre** muy rápido.",
        "Compré una manzana y un plátano.",
        "Los niños **juegan** en el parque.",
        "La casa **es** muy grande.",
        "El cielo **se ve** azul.",
    ],
    "adverbios": [
        "El perro de mi amigo corre **muy** rápido.",
        "Compré una manzana **rápidamente**.",
        "Los niños juegan **felizmente** en el parque.",
        "La casa es **demasiado** grande.",
        "El cielo **casi siempre** es azul.",
    ],
    "pronombres": [
        "**Yo** compré una manzana y un plátano.",
        "**Ella** es muy inteligente.",
        "**Nosotros** vamos al cine.",
        "**Ellos** juegan en el parque.",
        "**Usted** es muy amable.",
    ],
}

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

# Función para iniciar
