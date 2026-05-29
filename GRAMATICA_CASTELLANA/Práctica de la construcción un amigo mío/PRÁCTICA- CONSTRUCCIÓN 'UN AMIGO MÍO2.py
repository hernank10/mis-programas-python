import re

errores = []

def mostrar_teoria():
    print("\n📘 TEORÍA:")
    print("La construcción 'un amigo mío' se forma con:")
    print("Artículo indefinido + sustantivo + posesivo pospuesto.")
    print("Ejemplo: 'Un amigo mío', 'Una prima suya', 'Unos vecinos nuestros'.\n")
    print("Equivale a: 'Uno de mis amigos' en inglés (One of my friends).\n")

def mostrar_ejemplos():
    ejemplos = [
        "Un amigo mío vive en Barcelona.",
        "Una prima suya trabaja en una embajada.",
        "Un profesor nuestro escribió ese libro.",
        "Un vecino tuyo me saludó ayer.",
        "Una colega mía viaja mucho por trabajo."
    ]
    print("\n📚 EJEMPLOS:")
    for ej in ejemplos:
        print(f"- {ej}")
    print()

def ejercicio_redaccion():
    global errores
    errores.clear()
    print("\n✍️ EJERCICIO DE REDACCIÓN:")
    print("Escribe 3 oraciones con la estructura: artículo + sustantivo + posesivo pospuesto.")
    respuestas = []
    for i in range(1, 4):
        oracion = input(f"{i}. Escribe tu oración: ").strip()
        respuestas.append(oracion)

    print("\n✅ VERIFICACIÓN:")
    patron = re.compile(r'\b(un|una|unos|unas)\s+\w+\s+(mío|mía|míos|mías|tuyo|tuya|tuyos|tuyas|suyo|suya|suyos|suyas|nuestro|nuestra|nuestros|nuestras)\b', re.IGNORECASE)
    
    for idx, oracion in enumerate(respuestas, 1):
        if patron.search(oracion):
            print(f"{idx}. ✔️ Correcta: {oracion}")
        else:
            print(f"{idx}. ❌ Incorrecta: {oracion}")
            errores.append(oracion)

def revisar_errores():
    if not errores:
        print("\n🎉 No hay errores que revisar. ¡Bien hecho!")
        return
    
    print("\n🔁 REPASO DE ERRORES:")
    for i, error in enumerate(errores, 1):
        print(f"{i}. Oración original: {error}")
        correccion = input("   ✏️ Corrige la oración: ")
        patron = re.compile(r'\b(un|una|unos|unas)\s+\w+\s+(mío|mía|míos|mías|tuyo|tuya|tuyos|tuyas|suyo|suya|suyos|suyas|nuestro|nuestra|nuestros|nuestras)\b', re.IGNORECASE)
        if patron.search(correccion):
            print("   ✔️ Corrección válida.")
        else:
            print("   ❌ Aún no cumple la estructura. Intenta de nuevo más tarde.")

def guardar_progreso():
    with open("progreso_construccion.txt", "a", encoding="utf-8") as f:
        f.write("\n--- Respuestas Incorrectas ---\n")
        for oracion in errores:
            f.write(oracion + "\n")
    print("📁 Progreso guardado en 'progreso_construccion.txt'.")

def menu():
    while True:
        print("\n🧠 MENÚ DE PRÁCTICA: CONSTRUCCIÓN 'UN AMIGO MÍO'")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Hacer ejercicio de redacción")
        print("4. Revisar errores")
        print("5. Guardar progreso")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            ejercicio_redaccion()
        elif opcion == "4":
            revisar_errores()
        elif opcion == "5":
            guardar_progreso()
        elif opcion == "6":
            print("¡Hasta pronto! Sigue practicando. ✨")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
