# Lista de 90 oraciones con adjetivos
oraciones = [
    "El lenguaje de programación Python es altamente programable y adaptable a una variedad de aplicaciones.",
    "La arquitectura modular del sistema facilita la reutilización de componentes en diferentes partes del software.",
    "El algoritmo de búsqueda implementado es altamente eficiente y puede manejar grandes conjuntos de datos en tiempo récord.",
    "El código está organizado de manera estructurada, lo que facilita su comprensión y mantenimiento a largo plazo.",
    "La aplicación sigue un enfoque orientado a objetos, lo que permite una mayor modularidad y reutilización del código.",
    # Las oraciones restantes están abreviadas para mantener el tamaño del mensaje

    # Completa la lista con las oraciones restantes
]

# Función para identificar el adjetivo en una oración
def identificar_adjetivo(oracion):
    palabras = oracion.split()  # Dividir la oración en palabras
    adjetivos = []  # Lista para almacenar los adjetivos encontrados

    for palabra in palabras:
        if palabra.endswith(","):  # Eliminar la coma al final de la palabra si existe
            palabra = palabra[:-1]
        if palabra.endswith(".") or palabra.endswith("?") or palabra.endswith("!"):  # Eliminar signos de puntuación
            palabra = palabra[:-1]

        # Verificar si la palabra es un adjetivo
        if palabra.lower() in adjetivos_castellano:
            adjetivos.append(palabra)

    return adjetivos

# Función para reescribir la oración
def reescribir_oracion(oracion, adjetivo):
    return oracion.replace(adjetivo, "__________")  # Reemplazar el adjetivo con un espacio en blanco

# Lista de los 90 adjetivos castellanos
adjetivos_castellano = [
    "programable", "modular", "eficiente", "estructurado", "orientado",
    "dinámico", "estático", "compilado", "interpretado", "reutilizable",
    # Los adjetivos restantes están abreviados para mantener el tamaño del mensaje

    # Completa la lista con los adjetivos restantes
]

# Verificar que haya 90 oraciones en la lista
print("Número de oraciones en la lista:", len(oraciones))

# Iterar sobre cada oración y pedir al usuario que identifique el adjetivo y reescriba la oración
for idx, oracion in enumerate(oraciones, start=1):
    print(f"Oración {idx}: {oracion}")
    adjetivo_identificado = identificar_adjetivo(oracion)
    
    if adjetivo_identificado:
        adjetivo_identificado = adjetivo_identificado[0]  # Tomar el primer adjetivo identificado
        print(f"Identifica el adjetivo en la oración: '{adjetivo_identificado}'")
        
        # Pedir al usuario que reescriba la oración con el adjetivo oculto
        oracion_reescrita = reescribir_oracion(oracion, adjetivo_identificado)
        respuesta_usuario = input(f"Reescribe la oración con el adjetivo oculto: '{oracion_reescrita}'\n")
        print()

        # Verificar si la respuesta del usuario es correcta
        if respuesta_usuario.strip().lower() == oracion.lower():
            print("¡Correcto!")
        else:
            print("Incorrecto. La oración correcta es:", oracion)
    else:
        print("No se encontró ningún adjetivo en esta oración.\n")
