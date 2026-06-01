import random

# Diccionario de ejercicios por tema y tipo
EJERCICIOS = {
    "Ortografía": {
        "Nivel 1": {
            "Selección múltiple": [
                {"pregunta": "¿Cuál palabra está escrita correctamente?",
                 "opciones": ["exámen", "examen", "exámenn"],
                 "respuesta": "examen"}
            ],
            # Agrega más tipos aquí
        },
        # Agrega Nivel 2, Nivel 3
    },
    "Morfología": {
        "Nivel 1": {
            "Clasificación de palabras": [
                {"pregunta": "¿Qué tipo de palabra es 'rápidamente'?",
                 "opciones": ["Adjetivo", "Verbo", "Adverbio"],
                 "respuesta": "Adverbio"}
            ]
        }
    },
    # Agrega Sintaxis, más niveles y tipos
}

def seleccionar_opcion(lista_opciones, prompt):
    print(f"\n{prompt}")
    for i, opcion in enumerate(lista_opciones, 1):
        print(f"{i}. {opcion}")
    while True:
        try:
            eleccion = int(input("Elige una opción: ")) - 1
            if 0 <= eleccion < len(lista_opciones):
                return lista_opciones[eleccion]
            else:
                print("Opción inválida, intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa un número válido.")

def ejecutar_ejercicio(ejercicio):
    print("\n🧪 Ejercicio:")
    print(ejercicio["pregunta"])
    for i, opcion in enumerate(ejercicio["opciones"], 1):
        print(f"{i}. {opcion}")
    respuesta = input("Tu respuesta (número): ")
    if ejercicio["opciones"][int(respuesta)-1] == ejercicio["respuesta"]:
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")

def main():
    print("📚 Bienvenido al Entrenador de Escritura en Castellano\n")

    area = seleccionar_opcion(list(EJERCICIOS.keys()), "Selecciona el área del lenguaje:")
    nivel = seleccionar_opcion(list(EJERCICIOS[area].keys()), "Selecciona el nivel:")
    tipo = seleccionar_opcion(list(EJERCICIOS[area][nivel].keys()), "Selecciona el tipo de ejercicio:")

    ejercicios_disponibles = EJERCICIOS[area][nivel][tipo]
    ejercicio = random.choice(ejercicios_disponibles)
    ejecutar_ejercicio(ejercicio)

if __name__ == "__main__":
    main()
