import json
import random
import os

MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "ejemplos_guardados.json"

# Cargar ejemplos guardados desde archivo
def cargar_ejemplos():
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, ensure_ascii=False, indent=2)

def agregar_ejemplo_nuevo():
    ejemplos = cargar_ejemplos()
    if len(ejemplos) >= MAX_EJEMPLOS:
        print("⚠️ Ya has alcanzado el máximo de 100 ejemplos.")
        return
    oracion = input("Escribe una oración con complemento directo: ").strip()
    cd = input("¿Cuál es el complemento directo en esa oración? ").strip()
    ejemplos.append({"oracion": oracion, "cd": cd})
    guardar_ejemplos(ejemplos)
    print("✅ Ejemplo guardado con éxito.")

def practicar_con_guardados():
    ejemplos = cargar_ejemplos()
    if not ejemplos:
        print("⚠️ No hay ejemplos guardados.")
        return
    seleccionados = random.sample(ejemplos, min(5, len(ejemplos)))
    for ej in seleccionados:
        print(f"\nOración: {ej['oracion']}")
        respuesta = input("¿Cuál es el complemento directo? → ").lower().strip()
        if respuesta in ej['cd'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. El CD es: {ej['cd']}")

# Preguntas nuevas tipo A y B
def pregunta_tipo_verbo():
    oracion = random.choice(ejemplos_correctos)
    palabras = oracion.split()
    verbo = next((p for p in palabras if p.endswith("é") or p.endswith("ó") or p.endswith("amos")), "¿verbo?")
    print(f"\nOración: {oracion}")
    respuesta = input("¿Qué verbo se usa en esta oración? → ").strip().lower()
    if verbo.lower() in respuesta:
        print("✅ ¡Correcto!")
    else:
        print(f"❌ El verbo principal era: {verbo}")

def pregunta_funcion_subrayada():
    oracion, cd = random.choice([(o, o.split()[2]) for o in ejemplos_correctos])
    print(f"\nOración (palabra subrayada): {oracion.replace(cd, '[' + cd + ']')}")
    respuesta = input("¿Qué función cumple la palabra subrayada? → ").lower().strip()
    if "complemento directo" in respuesta or "objeto directo" in respuesta:
        print("✅ Correcto: es complemento directo.")
    else:
        print("❌ No es correcto. La función era: complemento directo.")

# Ejemplos anteriores
teoria = """\nEL COMPLEMENTO DIRECTO (CD)... (abreviado por claridad)\n"""

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
    "Bebí un jugo de naranja."
]

ejemplos_incorrectos = [
    "Leí un interesante libro.",
    "Cocinamos paella una deliciosa.",
    "Ella carta escribió una.",
    "Compré para mi madre un regalo.",
    "Pintaron azul la casa de."
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

# Menú principal
def mostrar_menu():
    print("\n📚 MENÚ PRINCIPAL")
    print("1. Ver teoría del complemento directo")
    print("2. Practicar con ejemplos correctos")
    print("3. Detectar errores en ejemplos incorrectos")
    print("4. Practicar por categorías")
    print("5. Crear y guardar nuevos ejemplos")
    print("6. Practicar con ejemplos guardados")
    print("7. ¿Qué verbo se usa en la oración?")
    print("8. ¿Qué función cumple la palabra subrayada?")
    print("9. Salir")

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

# Ejecutar programa
while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-9): ")

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
        agregar_ejemplo_nuevo()
    elif opcion == "6":
        practicar_con_guardados()
    elif opcion == "7":
        pregunta_tipo_verbo()
    elif opcion == "8":
        pregunta_funcion_subrayada()
    elif opcion == "9":
        print("👋 ¡Hasta luego! ¡Sigue practicando!")
        break
    else:
        print("⚠️ Opción no válida. Intenta otra vez.")
