import random
import os

# Archivo para guardar ejemplos personalizados
archivo_guardado = "ejemplos_guardados.txt"

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

# EJEMPLOS INICIALES
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

# Leer ejemplos guardados si existen
def cargar_ejemplos_guardados():
    if not os.path.exists(archivo_guardado):
        return []
    with open(archivo_guardado, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [{"oracion": line[2:].strip(), "correcta": line.startswith("✓")} for line in lines]

# Guardar nuevos ejemplos
def guardar_nuevo_ejemplo(ejemplo, correcta):
    with open(archivo_guardado, "a", encoding="utf-8") as f:
        prefijo = "✓ " if correcta else "✘ "
        f.write(prefijo + ejemplo.strip() + "\n")

# UNIR TODOS LOS EJEMPLOS
def obtener_todos_los_ejemplos():
    guardados = cargar_ejemplos_guardados()
    ejemplos = [{"oracion": e, "correcta": True} for e in ejemplos_correctos] + \
               [{"oracion": e, "correcta": False} for e in ejemplos_incorrectos] + \
               guardados
    return ejemplos[:100]  # Limitar a 100 ejemplos

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

# FUNCIÓN PARA AGREGAR EJEMPLOS
def agregar_ejemplos():
    print("\n✍️ Agregar nuevo ejemplo (máximo 100). Escribe 'salir' para terminar.")
    total_actual = len(obtener_todos_los_ejemplos())
    while total_actual < 100:
        oracion = input("Escribe una oración (o 'salir'): ").strip()
        if oracion.lower() == "salir":
            break
        tipo = input("¿Es correcta o incorrecta? (c/i): ").strip().lower()
        if tipo not in ("c", "i"):
            print("Tipo no válido.")
            continue
        guardar_nuevo_ejemplo(oracion, correcta=(tipo == "c"))
        total_actual += 1
        print("Ejemplo guardado.")

# PRÁCTICA DE IDENTIFICACIÓN
def practicar_identificacion():
    ejercicios = obtener_todos_los_ejemplos()
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

# PRÁCTICA DE ANÁLISIS
def practicar_analisis():
    ejercicios = obtener_todos_los_ejemplos()
    random.shuffle(ejercicios)
    print("\n🔍 ANÁLISIS DE ORACIONES (solo lectura):")
    for i, ej in enumerate(ejercicios[:5], start=1):
        print(f"\n{i}. {ej['oracion']}")
        if ej["correcta"]:
            print("✔️ Esta oración es correcta. Su construcción omite un término compartido o usa estructuras simétricas compatibles.")
        else:
            print("❌ Esta oración es incorrecta. Une elementos con diferentes regímenes (por ejemplo, verbos que exigen preposición junto a otros que no).")

# PRÁCTICA DE COMPLETAR ORACIÓN
def practicar_completar():
    pares = [
        ("Espero y me alegraré ___ que vengas.", ["de", ""]),
        ("Tan alto o ___ que tú.", ["más", "menos"]),
        ("Subir y bajar ___ la montaña.", ["de", "a"]),
        ("Acepto y me alegro ___ verte feliz.", ["de", ""]),
        ("Tengo tanto o ___ derecho que tú.", ["más", "menos"]),
    ]
    print("\n✏️ COMPLETA LA ORACIÓN ELIGIENDO LA OPCIÓN CORRECTA:")
    puntuacion = 0

    for i, (frase, opciones) in enumerate(pares[:5], 1):
        print(f"\n{i}. {frase}")
        print("a)", frase.replace("___", opciones[0]))
        print("b)", frase.replace("___", opciones[1]))
        resp = input("¿Cuál es la opción correcta? (a/b): ").strip().lower()

        if (i in [1, 4] and resp == "a") or (i in [2, 3, 5] and resp == "b"):
            print("✅ ¡Correcto!")
            puntuacion += 1
        else:
            print("❌ Incorrecto.")
    print(f"\n🎯 Puntuación: {puntuacion}/5")

# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver teoría")
        print("2. Ver ejemplos por categoría")
        print("3. Practicar: Identificar si es correcta")
        print("4. Practicar: Analizar estructura")
        print("5. Practicar: Completar oración")
        print("6. Agregar nuevos ejemplos")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_identificacion()
        elif opcion == "4":
            practicar_analisis()
        elif opcion == "5":
            practicar_completar()
        elif opcion == "6":
            agregar_ejemplos()
        elif opcion == "7":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# EJECUTAR PROGRAMA
menu()
