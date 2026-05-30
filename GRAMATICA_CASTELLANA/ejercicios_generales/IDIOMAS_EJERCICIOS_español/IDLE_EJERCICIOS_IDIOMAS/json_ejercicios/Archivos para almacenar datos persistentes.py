import json

# Archivos para almacenar datos persistentes
PROGRESO_ARCHIVO = "progreso_completo.json"
EJERCICIOS_ARCHIVO = "ejercicios_completo.json"


def cargar_datos(archivo):
    """Carga datos desde un archivo JSON."""
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def guardar_datos(archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def inicializar_datos():
    """Inicializa datos básicos de ejercicios."""
    ejercicios = {
        "el_o_el": [
            ("___ libro que me diste es muy interesante.", "el"),
            ("___ está leyendo una novela de misterio.", "él"),
        ],
        "formular_preguntas": [
            ("Tengo 18 años", "¿Cuántos años tienes?"),
            ("Trabajo como secretaria en una empresa", "¿En qué trabajas?"),
            ("Estudio Filosofía en Salamanca", "¿Qué estudias y dónde?"),
            ("El próximo verano voy a Chile", "¿Cuándo y a dónde vas?"),
        ],
        "posesivos": [
            ("Este es ___ cuaderno.", "mi"),
            ("___ coche está estacionado en la calle.", "su"),
            ("Estas son ___ ideas.", "nuestras"),
        ],
        "verbos_presente": [
            ("Yo ___ todas las mañanas (correr).", "corro"),
            ("Ellos ___ cartas (escribir).", "escriben"),
            ("Nosotros ___ juntos (trabajar).", "trabajamos"),
        ],
        "numerales": [
            ("¿Cuántos años tienes?", "dieciocho"),
            ("¿Cuál es tu número de teléfono?", "cuatrocientos cinco"),
        ],
        "demostrativos": [
            ("Este pastel está más sabroso que ___ de ayer.", "aquel"),
            ("No me gusta ___ falda en el escaparate.", "esa"),
        ],
        "imperativos": [
            ("___ el arroz (cocer).", "Cuece"),
            ("___ la carne (cortar).", "Corta"),
            ("___ las verduras (mezclar).", "Mezcla"),
        ],
    }
    guardar_datos(EJERCICIOS_ARCHIVO, ejercicios)


def completar_ejercicio(categoria):
    """Permite practicar ejercicios de una categoría."""
    ejercicios = cargar_datos(EJERCICIOS_ARCHIVO).get(categoria, [])
    if not ejercicios:
        print("\nNo hay ejercicios disponibles en esta categoría.\n")
        return

    progreso = cargar_datos(PROGRESO_ARCHIVO)
    if categoria not in progreso:
        progreso[categoria] = []

    print(f"\nEjercicios de la categoría: {categoria}\n")
    for i, (pregunta, respuesta) in enumerate(ejercicios, start=1):
        if i in progreso[categoria]:
            continue

        print(f"{i}. {pregunta}")
        respuesta_usuario = input("Tu respuesta: ").strip()
        if respuesta_usuario.lower() == respuesta.lower():
            print("¡Correcto!")
            progreso[categoria].append(i)
            guardar_datos(PROGRESO_ARCHIVO, progreso)
        else:
            print(f"Incorrecto. La respuesta correcta es: '{respuesta}'")

    print("\n¡Terminaste esta categoría!\n")


def agregar_ejercicio():
    """Permite agregar nuevos ejercicios a una categoría."""
    print("\nAgregar nuevo ejercicio:")
    categoria = input("Ingrese la categoría (ejemplo: el_o_el, posesivos, etc.): ").strip()
    if not categoria:
        print("La categoría no puede estar vacía.")
        return

    pregunta = input("Escribe la pregunta del ejercicio: ").strip()
    respuesta = input("Escribe la respuesta correcta: ").strip()

    if not pregunta or not respuesta:
        print("La pregunta y la respuesta no pueden estar vacías.")
        return

    ejercicios = cargar_datos(EJERCICIOS_ARCHIVO)
    if categoria not in ejercicios:
        ejercicios[categoria] = []

    ejercicios[categoria].append((pregunta, respuesta))
    guardar_datos(EJERCICIOS_ARCHIVO, ejercicios)
    print("\n¡Ejercicio agregado exitosamente!\n")


def mostrar_menu():
    """Muestra el menú principal del programa."""
    while True:
        print("\n*** Menú Principal ***")
        print("1. Practicar 'el' o 'él'")
        print("2. Formular preguntas")
        print("3. Completar con posesivos")
        print("4. Completar con verbos en presente")
        print("5. Responder con numerales")
        print("6. Completar con demostrativos")
        print("7. Completar con imperativos")
        print("8. Agregar más ejercicios")
        print("9. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            completar_ejercicio("el_o_el")
        elif opcion == "2":
            completar_ejercicio("formular_preguntas")
        elif opcion == "3":
            completar_ejercicio("posesivos")
        elif opcion == "4":
            completar_ejercicio("verbos_presente")
        elif opcion == "5":
            completar_ejercicio("numerales")
        elif opcion == "6":
            completar_ejercicio("demostrativos")
        elif opcion == "7":
            completar_ejercicio("imperativos")
        elif opcion == "8":
            agregar_ejercicio()
        elif opcion == "9":
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Inténtalo nuevamente.")


# Ejecución principal
if __name__ == "__main__":
    inicializar_datos()
    mostrar_menu()
