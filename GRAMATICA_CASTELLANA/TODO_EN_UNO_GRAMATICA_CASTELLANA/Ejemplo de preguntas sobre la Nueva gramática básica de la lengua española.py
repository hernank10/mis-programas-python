def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    """Muestra una pregunta y evalúa la respuesta del usuario."""
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3): "))
        if respuesta_usuario == respuesta_correcta:
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            return True
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")
        return False

def cuestionario_rae():
    """🌟📜✏️🕵🏛Cuestionario interactivo sobre la Nueva gramática básica de la lengua española.🌟📜✏️🕵🏛"""
    preguntas = [
        ("🌟📜✏️🕵🏛¿Qué es la Nueva gramática básica de la lengua española?", 
         ["Un diccionario de términos modernos.",
          "Una versión simplificada de la Nueva gramática de la lengua española.",
          "Un manual de conjugación verbal."],
         2),
        ("🌟📜✏️🕵🏛¿En qué año se publicó por primera vez la Nueva gramática básica?", 
         ["2009", "2010", "2011"], 
         2),
        ("🌟📜✏️🕵🏛¿Qué objetivo principal tiene esta gramática?", 
         ["Describir el español hablado solo en España.",
          "Presentar las normas del español en todo el mundo, de forma accesible.",
          "Enseñar el español exclusivamente a extranjeros."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué diferencia la Nueva gramática básica de la Nueva gramática completa?", 
         ["Tiene un enfoque regional.",
          "Es más sencilla y accesible para el público general.",
          "Está dedicada exclusivamente a la fonética."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué fenómeno describe el término 'seseo'?", 
         ["La ausencia de distinción entre /s/ y /z/ en algunas regiones.",
          "La pronunciación aspirada de la /s/.",
          "El uso del pronombre 'vos'."], 
         1),
        ("🌟📜✏️🕵🏛¿Qué aspecto del lenguaje se analiza en la fonología?", 
         ["La estructura de las palabras.", 
          "La organización de los sonidos en una lengua.", 
          "La sintaxis de las oraciones."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué es un diptongo?", 
         ["La unión de dos consonantes en una sílaba.",
          "La unión de dos vocales en una misma sílaba.",
          "La separación de dos vocales en sílabas distintas."], 
         2),
        ("🌟📜✏️🕵🏛¿Cuál es un ejemplo de hiato?", 
         ["Caos", 
          "Casa", 
          "Cauto"], 
         1),
        ("🌟📜✏️🕵🏛¿Qué función tiene el artículo en la oración?", 
         ["Indicar el género y número del sustantivo.", 
          "Modificar al verbo.", 
          "Unir dos oraciones."], 
         1),
        ("🌟📜✏️🕵🏛¿Cuál es un ejemplo de oración compuesta?", 
         ["María canta.", 
          "El perro corre y el gato duerme.", 
          "Llueve mucho."], 
         2),
    ]
    
    print("🌟📜✏️🕵🏛¡Bienvenido al Cuestionario sobre la Nueva gramática básica de la lengua española!🌟📜✏️🕵🏛")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    
    print(f"\n¡Has completado el cuestionario! Tu puntuación final es {puntuacion}/{len(preguntas)}.")

# Llamada al cuestionario
cuestionario_rae()
