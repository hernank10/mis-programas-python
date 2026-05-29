import re

def mostrar_teoria():
    print("\n📘 TEORÍA:")
    print("La construcción 'un amigo mío' es típica del español.")
    print("Consiste en: artículo indefinido + sustantivo + posesivo pospuesto.")
    print("Ejemplos: un amigo mío, una prima tuya, unos colegas suyos.")
    print("Equivale a: 'uno de mis amigos' en inglés o francés.\n")

def mostrar_ejemplos():
    ejemplos = [
        "Un amigo mío vive en Barcelona.",
        "Una prima suya trabaja en una embajada.",
        "Un profesor nuestro escribió ese libro.",
        "Un vecino tuyo me saludó ayer.",
        "Una colega mía viaja mucho por trabajo."
    ]
    print("\n📚 EJEMPLOS DE USO:")
    for ej in ejemplos:
        print(f"- {ej}")
    print()

def ejercicio_redaccion():
    print("✍️ EJERCICIO DE REDACCIÓN:")
    print("Redacta 3 oraciones utilizando la estructura: artículo + sustantivo + posesivo pospuesto.")
    respuestas = []
    for i in range(1, 4):
        oracion = input(f"{i}. Escribe tu oración: ").strip()
        respuestas.append(oracion)

    print("\n✅ VERIFICACIÓN DE ESTRUCTURA:")
    patron = re.compile(r'\b(un|una|unos|unas)\s+\w+\s+(mío|mía|míos|mías|tuyo|tuya|tuyos|tuyas|suyo|suya|suyos|suyas|nuestro|nuestra|nuestros|nuestras)\b', re.IGNORECASE)
    
    for idx, oracion in enumerate(respuestas, 1):
        if patron.search(oracion):
            print(f"{idx}. ✔️ Correcta: {oracion}")
        else:
            print(f"{idx}. ❌ No se detectó la estructura: {oracion}")

def menu():
    while True:
        print("\n🧠 PRÁCTICA DE LA CONSTRUCCIÓN 'UN AMIGO MÍO'")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Hacer ejercicio de redacción")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            ejercicio_redaccion()
        elif opcion == "4":
            print("¡Hasta pronto! Sigue practicando. 📖")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
