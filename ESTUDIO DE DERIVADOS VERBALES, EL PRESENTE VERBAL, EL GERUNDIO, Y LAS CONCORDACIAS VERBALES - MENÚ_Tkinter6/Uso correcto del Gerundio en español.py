import random

# Listas de ejemplos por categoría
ejemplos_sujeto = [
    "Comprendiendo las consecuencias, aceptó su castigo.",
    "Sintiéndose enfermo, pidió permiso para irse.",
    "Viendo que no había solución, abandonó el proyecto.",
    "Reflexionando sobre su vida, encontró paz.",
    "Recordando sus promesas, mantuvo la calma."
]

ejemplos_objeto = [
    "Vi a los niños jugando en la plaza.",
    "Escuché a Laura cantando en el baño.",
    "Observé al pintor esbozando un retrato.",
    "Encontré a mi hermana estudiando para el examen.",
    "Oí al violinista ensayando en su habitación."
]

# Función para mostrar el menú
def mostrar_menu():
    print("\n=== MENU: USO DEL GERUNDIO ===")
    print("1. Gerundio relacionado al sujeto (motivo o causa)")
    print("2. Gerundio relacionado al objeto directo (acción percibida)")
    print("3. Salir")

# Función para practicar ejemplos de una categoría
def practicar_gerundios(ejemplos_categoria, categoria_nombre):
    print(f"\n--- CATEGORÍA: {categoria_nombre} ---\n")
    print("Ejemplo para guiarte:")
    print(random.choice(ejemplos_categoria))
    print("\nAhora escribe 10 ejemplos similares:")

    ejemplos_usuario = []

    for i in range(1, 11):
        ejemplo = input(f"Escribe el ejemplo {i}: ")
        ejemplos_usuario.append(ejemplo)

    print("\n¡Muy bien! Ahora, vamos a crear más oraciones.")
    while len(ejemplos_usuario) < 100:
        nuevo = input(f"Escribe una nueva oración similar (Total {len(ejemplos_usuario)+1}/100): ")
        ejemplos_usuario.append(nuevo)

    print("\n¡Felicidades! Has escrito 100 oraciones para esta categoría.")
    print("Aquí tienes tus oraciones:")
    for idx, oracion in enumerate(ejemplos_usuario, 1):
        print(f"{idx}. {oracion}")

# Programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            practicar_gerundios(ejemplos_sujeto, "Gerundio relacionado al sujeto")
        elif opcion == "2":
            practicar_gerundios(ejemplos_objeto, "Gerundio relacionado al objeto directo")
        elif opcion == "3":
            print("¡Gracias por practicar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
