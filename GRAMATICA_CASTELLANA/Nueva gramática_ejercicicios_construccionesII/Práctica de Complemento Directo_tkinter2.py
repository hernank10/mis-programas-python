import random

teoria = """
EL COMPLEMENTO DIRECTO (CD)

El complemento directo, también llamado objeto directo, es la parte de la oración que recibe directamente la acción del verbo.

Se reconoce al preguntar “¿qué + verbo?” Ejemplo: “Leí un libro.” ¿Qué leí? — Un libro (CD).

No lleva preposición y puede ser un sustantivo, un pronombre o una proposición sustantiva.

Ejemplos:
- Escribí una carta. → ¿Qué escribí? → Una carta (CD)
- Cocinamos una paella. → ¿Qué cocinamos? → Una paella (CD)
"""

ejemplos_correctos = [
    "Leí un libro interesante.",
    "Cocinamos una paella deliciosa.",
    "Ella escribió una carta larga.",
    "Compré un regalo para mi madre.",
    "Pintaron la casa de azul.",
    "Escucharon una canción alegre.",
    "Perdiste las llaves del coche.",
    "Rompimos el vaso sin querer.",
    "Encontré una moneda antigua.",
    "Bebí un jugo de naranja.",
]

ejemplos_incorrectos = [
    "Leí un interesante libro.",  # CD está mal posicionado
    "Cocinamos paella una deliciosa.",  # desorden
    "Ella carta escribió una.",  # orden incorrecto
    "Compré para mi madre un regalo.",  # CD separado por C.I.
    "Pintaron azul la casa de.",  # confuso
]

categorias = {
    "Cotidianas": [
        "Limpiamos el salón principal.",
        "Lavaron la ropa sucia.",
        "Perdiste las llaves del coche."
    ],
    "Escolares": [
        "Estudié el capítulo cinco.",
        "Escribí un poema de amor.",
        "Leí un libro interesante."
    ],
    "Emocionales": [
        "Perdonó su error.",
        "Ella contó una historia graciosa.",
        "Celebramos el cumpleaños de Ana."
    ],
    "Tecnológicas": [
        "Descargué la aplicación nueva.",
        "Tradujeron el texto al español.",
        "Publicaron el artículo en línea."
    ],
    "Creativas": [
        "Dibujó un paisaje hermoso.",
        "Escribí un poema de amor.",
        "Filmamos un documental."
    ]
}

def mostrar_menu():
    print("\n📚 MENÚ PRINCIPAL")
    print("1. Ver teoría del complemento directo")
    print("2. Practicar con ejemplos correctos")
    print("3. Detectar errores en ejemplos incorrectos")
    print("4. Practicar por categorías")
    print("5. Salir")

def practicar_correctos():
    print("\n📝 Elige el complemento directo en cada oración:")
    for oracion in random.sample(ejemplos_correctos, 5):
        print(f"Oración: {oracion}")
        respuesta = input("¿Cuál es el complemento directo? → ").lower().strip()
        if respuesta in oracion.lower():
            print("✅ ¡Correcto!")
        else:
            print("❌ Intenta de nuevo. El CD estaba en:", oracion)

def practicar_incorrectos():
    print("\n❌ Detecta el error en estas oraciones (estructura del CD):")
    for oracion in random.sample(ejemplos_incorrectos, 3):
        print(f"Oración: {oracion}")
        input("¿Cuál es el error en el complemento directo? → ")
        print("💡 Revisa el orden o posición del CD. Puedes reescribir la oración correctamente.\n")

def practicar_por_categoria():
    print("\n📂 Categorías disponibles:")
    for i, cat in enumerate(categorias.keys(), 1):
        print(f"{i}. {cat}")
    opcion = int(input("Selecciona una categoría por número: "))
    seleccion = list(categorias.keys())[opcion - 1]
    print(f"\n🔍 Practicando categoría: {seleccion}")
    for oracion in categorias[seleccion]:
        print(f"Oración: {oracion}")
        respuesta = input("¿Cuál es el complemento directo? → ").lower().strip()
        if respuesta in oracion.lower():
            print("✅ ¡Correcto!\n")
        else:
            print(f"❌ Incorrecto. Revisa bien la oración.\n")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-5): ")

    if opcion == "1":
        print("\n📖 TEORÍA")
        print(teoria)
    elif opcion == "2":
        practicar_correctos()
    elif opcion == "3":
        practicar_incorrectos()
    elif opcion == "4":
        practicar_por_categoria()
    elif opcion == "5":
        print("👋 ¡Hasta luego! Sigue practicando.")
        break
    else:
        print("⚠️ Opción no válida. Intenta otra vez.")
