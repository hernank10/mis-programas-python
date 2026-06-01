def escribir_ejemplos_usuario():
    print("\n📝 CREA TUS PROPIOS EJEMPLOS")
    print("Escribe 20 oraciones que correspondan a esta lección.\n")
    ejemplos_usuario = []
    for i in range(1, 21):
        oracion = input(f"👉 Ejemplo {i}: ").strip()
        ejemplos_usuario.append(oracion)

    print("\n📘 ¡Aquí están tus ejemplos!")
    for idx, frase in enumerate(ejemplos_usuario, 1):
        print(f"{idx}. {frase}")
    print("🏅 ¡Bien hecho! Puedes usarlos para crear tus propios ejercicios.")

# Agregar al menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – Lección X")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir tus propios ejemplos ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            escribir_ejemplos_usuario()
        elif opcion == "5":
            print("👋 ¡Gracias por personalizar tu aprendizaje sintáctico!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")
