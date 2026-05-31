import json

# Archivo para guardar datos de gramática
DATA_FILE = "gramatica_castellana.json"

# Datos iniciales de gramática
initial_data = {
    "conceptos": {
        "Sustantivos": "Palabras que designan personas, animales, cosas, ideas o sentimientos.",
        "Verbos": "Palabras que indican acciones, estados o procesos realizados por el sujeto.",
        "Adjetivos": "Palabras que describen características o cualidades del sustantivo."
    },
    "ejemplos": {
        "Sustantivos": ["casa", "niño", "alegría"],
        "Verbos": ["correr", "estar", "pensar"],
        "Adjetivos": ["bonito", "grande", "inteligente"]
    },
    "ejercicios": {
        "Sustantivos": "Escribe tres sustantivos que designen emociones.",
        "Verbos": "Escribe tres verbos en tiempo presente.",
        "Adjetivos": "Escribe tres adjetivos que describan un paisaje."
    }
}

# Guardar datos iniciales si no existen
try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=4)
    data = initial_data

# Función para mostrar el menú principal
def show_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Leer conceptos gramaticales🌟")
    print("2. Ver ejemplos🎯😊📖")
    print("3. Practicar ejercicios✏️✏️🕵️")
    print("4. Agregar nuevo concepto, ejemplo o ejercicio📚 📚 📚 ")
    print("5. Revisar🚀 progreso📚 📚 📚 🤔")
    print("6. Salir🚀🚀")

# Función para leer conceptos gramaticales
def leer_conceptos():
    print("\n--- Conceptos Gramaticales ---")
    for concepto, definicion in data["conceptos"].items():
        print(f"{concepto}: {definicion}")

# Función para ver ejemplos
def ver_ejemplos():
    print("\n--- Ejemplos de Conceptos ---")
    for concepto, ejemplos in data["ejemplos"].items():
        print(f"{concepto}: {', '.join(ejemplos)}")

# Función para practicar ejercicios
def practicar_ejercicios():
    print("\n--- Ejercicios Prácticos ---")
    for concepto, ejercicio in data["ejercicios"].items():
        print(f"\n{concepto}")
        print(f"Ejercicio: {ejercicio}")
        respuesta = input("Tu respuesta: ")
        print(f"Gracias por tu respuesta: {respuesta}")

# Función para agregar un nuevo concepto, ejemplo o ejercicio
def agregar_nuevo():
    print("\n--- Agregar Nuevo Contenido ---")
    concepto = input("Escribe el nombre del nuevo concepto gramatical: ")
    definicion = input(f"Escribe la definición para {concepto}: ")
    ejemplos = input(f"Escribe algunos ejemplos para {concepto}, separados por comas: ").split(",")
    ejercicio = input(f"Escribe un ejercicio para {concepto}: ")
    
    # Guardar en la base de datos
    data["conceptos"][concepto] = definicion
    data["ejemplos"][concepto] = [ejemplo.strip() for ejemplo in ejemplos]
    data["ejercicios"][concepto] = ejercicio
    
    # Actualizar archivo
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"El concepto '{concepto}' se ha agregado correctamente.")

# Función para revisar progreso
def revisar_progreso():
    print("\n--- Progreso ---")
    for concepto, ejercicio in data["ejercicios"].items():
        print(f"{concepto}: {ejercicio}")

# Programa principal
def main():
    while True:
        show_menu()
        choice = input("\nSelecciona una opción: ")
        if choice == "1":
            leer_conceptos()
        elif choice == "2":
            ver_ejemplos()
        elif choice == "3":
            practicar_ejercicios()
        elif choice == "4":
            agregar_nuevo()
        elif choice == "5":
            revisar_progreso()
        elif choice == "6":
            print("¡Gracias por usar el programa! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
