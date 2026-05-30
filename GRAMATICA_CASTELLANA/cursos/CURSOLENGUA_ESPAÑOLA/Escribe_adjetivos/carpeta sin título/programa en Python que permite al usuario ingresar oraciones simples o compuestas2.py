import random

# Lista de palabras de todas las categorías gramaticales
palabras = [
    ("el", "la", "los", "las"),
    ("perro", "gato", "pájaro", "casa", "coche", "libro", "mesa", "silla", "pantalla"),
    ("ama", "odia", "no entiende", "insulta", "sonríe", "escucha", "mira", "toca", "come"),
    ("en", "sobre", "debajo", "delante", "detrás", "cerca", "lejos", "dentro", "fuera"),
    ("ayer", "hoy", "mañana", "pasado", "presente", "futuro"),
    ("grande", "pequeño", "alto", "bajo", "gordo", "flaco", "feliz", "triste", "enojado"),
]

# Función para generar una oración simple
def genera_oracion_simple():
    # Elige una palabra de cada categoría gramatical
    articulo = random.choice(palabras[0])
    sustantivo = random.choice(palabras[1])
    verbo = random.choice(palabras[2])
    adverbio = random.choice(palabras[3])
    tiempo = random.choice(palabras[4])
    adjetivo = random.choice(palabras[5])

    # Crea la oración
    oracion = f"El {articulo} {sustantivo} {verbo} {adverbio} {tiempo} {adjetivo}."

    return oracion

# Función para generar una oración compuesta
def genera_oracion_compuesta():
    # Elige dos palabras de cada categoría gramatical
    articulo1 = random.choice(palabras[0])
    sustantivo1 = random.choice(palabras[1])
    verbo1 = random.choice(palabras[2])
    adverbio1 = random.choice(palabras[3])
    tiempo1 = random.choice(palabras[4])
    adjetivo1 = random.choice(palabras[5])

    articulo2 = random.choice(palabras[0])
    sustantivo2 = random.choice(palabras[1])
    verbo2 = random.choice(palabras[2])
    adverbio2 = random.choice(palabras[3])
    tiempo2 = random.choice(palabras[4])
    adjetivo2 = random.choice(palabras[5])

    # Crea la oración
    oracion = f"El {articulo1} {sustantivo1} {verbo1} {adverbio1} {tiempo1} {adjetivo1} {conector} {articulo2} {sustantivo2} {verbo2} {adverbio2} {tiempo2} {adjetivo2}."

    return oracion

# Ejemplo de oración simple
ejemplo_oracion_simple = genera_oracion_simple()
print(ejemplo_oracion_simple)

# Ejemplo de oración compuesta
ejemplo_oracion_compuesta = genera_oracion_compuesta()
print(ejemplo_oracion_compuesta)

# Entrada del usuario
opcion = input("¿Quieres generar una oración simple (s) o compuesta (c)? ")

# Generación de la oración
if opcion == "s":
    oracion = genera_oracion_simple()
elif opcion == "c":
    oracion = genera_oracion_compuesta()
else:
    print("Opción no válida.")

# Retroalimentación
if oracion is not None:
    print("Oración generada:")
    print(oracion)
    if es_oracion_valida(oracion):
        print("Oración válida.")
    else:
        print("Oración no válida.")
