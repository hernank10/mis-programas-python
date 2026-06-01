import random

def menu_principal():
    tipos = [
        "Selección múltiple",
        "Completar oraciones",
        "Detectar errores",
        "Reescribir frases",
        "Ordenar oraciones",
        "Clasificación de palabras",
        "Conjugación verbal",
        "Uso correcto de tildes",
        "Identificación de funciones sintácticas",
        "Transformación de oraciones"
    ]
    
    while True:
        print("\n📚 MENÚ DE EJERCICIOS")
        for i, tipo in enumerate(tipos, 1):
            print(f"{i}. {tipo}")
        print("0. Salir")

        opcion = input("Selecciona el tipo de ejercicio: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        elif opcion in map(str, range(1, 11)):
            ejecutar_ejercicio(int(opcion))
        else:
            print("❌ Opción inválida")

def ejecutar_ejercicio(opcion):
    if opcion == 1:
        seleccion_multiple()
    elif opcion == 2:
        completar_oracion()
    elif opcion == 3:
        detectar_error()
    elif opcion == 4:
        reescribir_frase()
    elif opcion == 5:
        ordenar_oracion()
    elif opcion == 6:
        clasificar_palabra()
    elif opcion == 7:
        conjugar_verbo()
    elif opcion == 8:
        uso_tildes()
    elif opcion == 9:
        identificar_funcion()
    elif opcion == 10:
        transformar_oracion()

# 🎯 Funciones por tipo de ejercicio

def seleccion_multiple():
    print("\n🧪 Selección múltiple")
    pregunta = "¿Cuál palabra está escrita correctamente?"
    opciones = ["exámen", "examen", "exámenn"]
    respuesta = "examen"
    mostrar_opciones(pregunta, opciones, respuesta)

def completar_oracion():
    print("\n🧪 Completar oración")
    pregunta = "Completa la frase: El ___ está caliente."
    opciones = ["café", "cafe", "cafè"]
    respuesta = "café"
    mostrar_opciones(pregunta, opciones, respuesta)

def detectar_error():
    print("\n🧪 Detectar errores")
    frase = "Los niño juega en el parque."
    print(f"Frase: {frase}")
    print("¿Qué tipo de error contiene?")
    opciones = ["Concordancia", "Ortografía", "Puntuación"]
    respuesta = "Concordancia"
    mostrar_opciones("Tipo de error:", opciones, respuesta)

def reescribir_frase():
    print("\n🧪 Reescribir frase")
    original = "Yo comí pizza ayer."
    print(f"Frase original: {original}")
    esperado = "Yo comeré pizza mañana."
    entrada = input("Reescríbela en futuro: ")
    if entrada.strip().lower() == esperado.lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Respuesta esperada: {esperado}")

def ordenar_oracion():
    print("\n🧪 Ordenar oración")
    palabras = ["mañana", "iremos", "a", "la", "playa"]
    print("Desordena las palabras:")
    print(" / ".join(palabras))
    respuesta = "mañana iremos a la playa"
    entrada = input("Escribe la oración ordenada: ")
    if entrada.strip().lower() == respuesta.lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Respuesta esperada: {respuesta}")

def clasificar_palabra():
    print("\n🧪 Clasificación de palabras")
    palabra = "rápidamente"
    opciones = ["Adjetivo", "Adverbio", "Sustantivo"]
    respuesta = "Adverbio"
    mostrar_opciones(f"¿Qué tipo de palabra es '{palabra}'?", opciones, respuesta)

def conjugar_verbo():
    print("\n🧪 Conjugación verbal")
    pregunta = "¿Primera persona del verbo 'vivir' en presente?"
    opciones = ["vivo", "vive", "vivimos"]
    respuesta = "vivo"
    mostrar_opciones(pregunta, opciones, respuesta)

def uso_tildes():
    print("\n🧪 Uso correcto de tildes")
    pregunta = "¿Cuál lleva tilde según la RAE?"
    opciones = ["camion", "camión", "camione"]
    respuesta = "camión"
    mostrar_opciones(pregunta, opciones, respuesta)

def identificar_funcion():
    print("\n🧪 Identificación sintáctica")
    frase = "El perro duerme en la alfombra."
    pregunta = "¿Cuál es el sujeto?"
    opciones = ["El perro", "duerme", "en la alfombra"]
    respuesta = "El perro"
    mostrar_opciones(pregunta, opciones, respuesta)

def transformar_oracion():
    print("\n🧪 Transformación de oración")
    original = "Pedro lee el libro."
    print(f"Frase original: {original}")
    esperado = "El libro es leído por Pedro."
    entrada = input("Transforma a voz pasiva: ")
    if entrada.strip().lower() == esperado.lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Respuesta esperada: {esperado}")

def mostrar_opciones(pregunta, opciones, respuesta):
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    entrada = input("Tu respuesta (número): ")
    try:
        eleccion = opciones[int(entrada) - 1]
        if eleccion == respuesta:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. Respuesta: {respuesta}")
    except:
        print("❌ Entrada inválida.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu_principal()
