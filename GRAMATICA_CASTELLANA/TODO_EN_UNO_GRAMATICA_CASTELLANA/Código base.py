import json
import os

# Función para cargar progreso
def cargar_progreso():
    if os.path.exists("progreso.json"):
        with open("progreso.json", "r") as archivo:
            return json.load(archivo)
    return {}

# Función para guardar progreso
def guardar_progreso(progreso):
    with open("progreso.json", "w") as archivo:
        json.dump(progreso, archivo, indent=4)

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- Aprende Gramática Española ---")
    print("1. Introducción y Teoría")
    print("2. Ejercicios Prácticos")
    print("3. Cuestionarios")
    print("4. Ver Progreso")
    print("5. Salir")
    return input("Selecciona una opción: ")

# Función para mostrar teoría
def mostrar_teoria():
    categorias = {
        "1": "Adverbios",
        "2": "Preposiciones",
        "3": "Conjunciones",
        "4": "Pronombres",
        "5": "Volver al menú"
    }
    while True:
        print("\n--- Categorías de Gramática ---")
        for clave, categoria in categorias.items():
            print(f"{clave}. {categoria}")
        opcion = input("Selecciona una categoría: ")
        if opcion == "5":
            break
        elif opcion in categorias:
            print(f"\n--- Teoría sobre {categorias[opcion]} ---")
            print(f"Reglas, ejemplos y definiciones sobre {categorias[opcion]}. (Próximamente más contenido)")
        else:
            print("Opción no válida. Intenta nuevamente.")

# Función para ejercicios prácticos
def ejercicios_practicos(progreso):
    print("\n--- Ejercicios Prácticos ---")
    print("Escribe ejemplos de adverbios, preposiciones, etc. Aquí se calificará tu respuesta.")
    categoria = input("Selecciona una categoría (adverbios, preposiciones, etc.): ").lower()
    respuesta = input(f"Escribe un ejemplo correcto de {categoria}: ")
    # Simulación de corrección
    print("¡Bien hecho!" if respuesta else "Respuesta incorrecta. Intenta nuevamente.")
    progreso[categoria] = progreso.get(categoria, 0) + 1

# Función para cuestionarios
def cuestionarios(progreso):
    print("\n--- Cuestionario ---")
    preguntas = [
        {"pregunta": "¿Qué es un adverbio?", "respuesta": "Una palabra que modifica a un verbo."},
        {"pregunta": "¿Cuántas preposiciones existen?", "respuesta": "23"}
    ]
    for idx, q in enumerate(preguntas):
        print(f"{idx+1}. {q['pregunta']}")
        respuesta = input("Tu respuesta: ")
        if respuesta.strip().lower() == q["respuesta"].lower():
            print("¡Correcto!")
            progreso["cuestionarios"] = progreso.get("cuestionarios", 0) + 1
        else:
            print(f"Incorrecto. La respuesta era: {q['respuesta']}")

# Función para ver progreso
def ver_progreso(progreso):
    print("\n--- Progreso del Usuario ---")
    if progreso:
        for categoria, puntos in progreso.items():
            print(f"{categoria.capitalize()}: {puntos} puntos")
    else:
        print("Aún no has comenzado a practicar. ¡Empieza hoy!")

# Programa principal
def main():
    progreso = cargar_progreso()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicios_practicos(progreso)
        elif opcion == "3":
            cuestionarios(progreso)
        elif opcion == "4":
            ver_progreso(progreso)
        elif opcion == "5":
            guardar_progreso(progreso)
            print("¡Gracias por aprender con nosotros! Progreso guardado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
