import random

# TEORÍA
teoria = """
CONSTRUCCIONES SINTÁCTICAS CON RÉGIMEN VERBAL DIFERENTE

La gramática establece que no se debe aplicar a dos palabras el régimen (estructura sintáctica) que solo le corresponde a una de ellas, aunque el complemento sea común.

Por ejemplo, es incorrecto decir:
  ✘ 'Espero y me alegraré de que todo le salga bien.'
  → Porque 'esperar' va sin preposición y 'alegrarse' exige 'de que'.

Sin embargo, el uso ha legitimado expresiones como:
  ✓ 'Ir y venir a casa.'
  ✓ 'Tan bueno o mejor que tú.'
  ✓ 'Tengo tanto o más derecho que tú.'

En estos casos, la omisión se considera natural y no entorpece la comprensión.
"""

# EJEMPLOS POR CATEGORÍA
ejemplos_correctos = [
    "Ir y venir a casa.",
    "Subir y bajar del autobús.",
    "Tan bueno o mejor que tú.",
    "Tengo tanto o más derecho que tú.",
    "Cocinar y servir la comida.",
    "Conocer y amar su cultura."
]

ejemplos_incorrectos = [
    "Espero y me alegraré de que todo le salga bien.",
    "Desea y se alegra que todo salga bien.",
    "Insistió y se negó a que lo ayudaran.",
    "Me dijo y se sorprendió de que viniera.",
    "Confía y duda en que lo logre.",
    "Acepto y me alegro que vengas."
]

# UNIR LOS EJERCICIOS
ejercicios = [{"oracion": o, "correcta": True} for o in ejemplos_correctos] + \
             [{"oracion": o, "correcta": False} for o in ejemplos_incorrectos]

# FUNCIÓN PARA MOSTRAR TEORÍA
def mostrar_teoria():
    print("\n📘 TEORÍA GRAMATICAL:\n")
    print(teoria)

# FUNCIÓN PARA MOSTRAR EJEMPLOS
def mostrar_ejemplos():
    print("\n✅ EJEMPLOS CORRECTOS:")
    for e in ejemplos_correctos:
        print("  ✓", e)
    print("\n❌ EJEMPLOS INCORRECTOS:")
    for e in ejemplos_incorrectos:
        print("  ✘", e)

# FUNCIÓN PARA PRACTICAR
def practicar():
    random.shuffle(ejercicios)
    print("\n🧠 PRÁCTICA: Indica si la oración es correcta o incorrecta.")
    puntuacion = 0

    for i, ej in enumerate(ejercicios[:10], start=1):
        print(f"\n{i}. {ej['oracion']}")
        respuesta = input("¿Es correcta? (s/n): ").strip().lower()
        es_correcta = ej["correcta"]

        if (respuesta == "s" and es_correcta) or (respuesta == "n" and not es_correcta):
            print("✅ ¡Correcto!")
            puntuacion += 1
        else:
            print("❌ Incorrecto.")
            print("La oración es", "CORRECTA." if es_correcta else "INCORRECTA.")

    print(f"\n🎯 Tu puntuación: {puntuacion}/10")

# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver teoría")
        print("2. Ver ejemplos por categoría")
        print("3. Practicar con ejercicios")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar()
        elif opcion == "4":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# EJECUTAR
menu()
