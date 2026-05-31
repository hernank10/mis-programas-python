import json
from colorama import init, Fore, Style
import pygame

# Inicializar Colorama y Pygame
init(autoreset=True)
pygame.mixer.init()

# Archivos de sonido
SONIDO_CORRECTO = "correcto.mp3"  # Asegúrate de tener un archivo correcto.mp3 en tu carpeta
SONIDO_INCORRECTO = "incorrecto.mp3"  # Asegúrate de tener un archivo incorrecto.mp3 en tu carpeta

# Archivo para guardar progreso
ARCHIVO_PROGRESO = "progreso_gramatica.json"

# Datos iniciales: conceptos, ejemplos y ejercicios
datos_gramatica = {
    "conceptos": {
        "Sujeto": "La persona, animal o cosa que realiza la acción en la oración.",
        "Predicado": "La parte de la oración que describe la acción realizada por el sujeto.",
        "Verbo": "La palabra que indica una acción, estado o proceso.",
        "Sustantivo": "Palabra que designa personas, animales, cosas, lugares o ideas.",
        "Adjetivo": "Palabra que describe o califica a un sustantivo."
    },
    "ejemplos": {
        "Sujeto": "El perro juega en el parque.",
        "Predicado": "Los niños corren alegremente.",
        "Verbo": "María canta una canción.",
        "Sustantivo": "El libro está en la mesa.",
        "Adjetivo": "El auto rojo es rápido."
    },
    "ejercicios": [
        {"pregunta": "¿Cuál es el sujeto en esta oración: 'La luna ilumina la noche'?", "respuesta": "La luna"},
        {"pregunta": "Identifica el verbo en esta oración: 'El pájaro canta en el árbol.'", "respuesta": "canta"},
        {"pregunta": "¿Qué parte de la oración es: 'corre rápidamente'?", "respuesta": "Predicado"},
        {"pregunta": "¿Qué tipo de palabra es: 'feliz' en 'El niño está feliz'?", "respuesta": "Adjetivo"}
    ]
}

# Cargar progreso desde el archivo JSON
def cargar_progreso():
    try:
        with open(ARCHIVO_PROGRESO, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"puntaje": 0, "fallos": []}

# Guardar progreso en el archivo JSON
def guardar_progreso(progreso):
    with open(ARCHIVO_PROGRESO, "w") as archivo:
        json.dump(progreso, archivo)

# Reproducir sonido
def reproducir_sonido(archivo):
    try:
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except pygame.error:
        print(Fore.RED + f"No se pudo reproducir el sonido: {archivo}")

# Mostrar menú principal
def mostrar_menu():
    print(Fore.BLUE + "\n--- MENÚ PRINCIPAL ---")
    print(Fore.CYAN + "1. Leer📖  conceptos gramaticales📖 ")
    print(Fore.CYAN + "2. Ver ejemplos😊📖")
    print(Fore.CYAN + "3. Practicar ejercicios")
    print(Fore.CYAN + "4. Repetir ejercicios fallados🎯😊📖")
    print(Fore.CYAN + "5. Agregar nuevo contenido📚 📚 📚 ")
    print(Fore.CYAN + "6. Revisar progreso📚 📚 📚 🤔")
    print(Fore.RED + "7. Borrar progreso🚀🚀🚀")
    print(Fore.RED + "8. Salir🚀🚀")

# Mostrar conceptos gramaticales
def mostrar_conceptos():
    print(Fore.YELLOW + "\n--- CONCEPTOS GRAMATICALES ---")
    for concepto, definicion in datos_gramatica["conceptos"].items():
        print(Fore.GREEN + f"{concepto}: " + Fore.WHITE + definicion)

# Mostrar ejemplos
def mostrar_ejemplos():
    print(Fore.YELLOW + "\n--- EJEMPLOS ---")
    for concepto, ejemplo in datos_gramatica["ejemplos"].items():
        print(Fore.GREEN + f"{concepto}: " + Fore.WHITE + ejemplo)

# Practicar ejercicios
def practicar_ejercicios(progreso):
    print(Fore.YELLOW + "\n--- EJERCICIOS ---")
    for ejercicio in datos_gramatica["ejercicios"]:
        print(Fore.CYAN + ejercicio["pregunta"])
        respuesta = input(Fore.WHITE + "Tu respuesta: ").strip()
        if respuesta.lower() == ejercicio["respuesta"].lower():
            print(Fore.GREEN + "¡Correcto!")
            reproducir_sonido(SONIDO_CORRECTO)
            progreso["puntaje"] += 1
        else:
            print(Fore.RED + f"Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
            reproducir_sonido(SONIDO_INCORRECTO)
            progreso["fallos"].append(ejercicio)
    return progreso

# Repetir ejercicios fallados
def repetir_fallados(progreso):
    if not progreso["fallos"]:
        print(Fore.YELLOW + "No tienes ejercicios fallados para repetir.")
        return progreso

    print(Fore.YELLOW + "\n--- REPETIR EJERCICIOS FALLADOS ---")
    fallos_actualizados = []
    for ejercicio in progreso["fallos"]:
        print(Fore.CYAN + ejercicio["pregunta"])
        respuesta = input(Fore.WHITE + "Tu respuesta: ").strip()
        if respuesta.lower() == ejercicio["respuesta"].lower():
            print(Fore.GREEN + "¡Correcto!")
            reproducir_sonido(SONIDO_CORRECTO)
            progreso["puntaje"] += 1
        else:
            print(Fore.RED + f"Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
            reproducir_sonido(SONIDO_INCORRECTO)
            fallos_actualizados.append(ejercicio)
    progreso["fallos"] = fallos_actualizados
    return progreso

# Agregar nuevo contenido
def agregar_contenido():
    print(Fore.YELLOW + "\n--- AGREGAR CONTENIDO ---")
    tipo = input(Fore.CYAN + "¿Qué quieres agregar? (concepto/ejemplo/ejercicio): ").strip().lower()
    if tipo == "concepto":
        concepto = input(Fore.GREEN + "Nombre del concepto: ").strip()
        definicion = input(Fore.GREEN + "Definición del concepto: ").strip()
        datos_gramatica["conceptos"][concepto] = definicion
        print(Fore.GREEN + "Concepto agregado exitosamente.")
    elif tipo == "ejemplo":
        concepto = input(Fore.GREEN + "Nombre del concepto relacionado: ").strip()
        ejemplo = input(Fore.GREEN + "Ejemplo: ").strip()
        datos_gramatica["ejemplos"][concepto] = ejemplo
        print(Fore.GREEN + "Ejemplo agregado exitosamente.")
    elif tipo == "ejercicio":
        pregunta = input(Fore.GREEN + "Escribe la pregunta del ejercicio: ").strip()
        respuesta = input(Fore.GREEN + "Escribe la respuesta correcta: ").strip()
        datos_gramatica["ejercicios"].append({"pregunta": pregunta, "respuesta": respuesta})
        print(Fore.GREEN + "Ejercicio agregado exitosamente.")
    else:
        print(Fore.RED + "Opción no válida. Intenta de nuevo.")

# Revisar progreso
def revisar_progreso(progreso):
    print(Fore.MAGENTA + f"\nTu puntaje actual es: {progreso['puntaje']}")
    print(Fore.MAGENTA + f"Ejercicios pendientes de corregir: {len(progreso['fallos'])}")

# Borrar progreso
def borrar_progreso():
    return {"puntaje": 0, "fallos": []}

# Programa principal
def main():
    progreso = cargar_progreso()
    while True:
        mostrar_menu()
        opcion = input(Fore.WHITE + "Selecciona una opción: ").strip()
        if opcion == "1":
            mostrar_conceptos()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            progreso = practicar_ejercicios(progreso)
            guardar_progreso(progreso)
        elif opcion == "4":
            progreso = repetir_fallados(progreso)
            guardar_progreso(progreso)
        elif opcion == "5":
            agregar_contenido()
        elif opcion == "6":
            revisar_progreso(progreso)
        elif opcion == "7":
            progreso = borrar_progreso()
            guardar_progreso(progreso)
            print(Fore.GREEN + "Progreso borrado exitosamente.")
        elif opcion == "8":
            print(Fore.MAGENTA + "¡Gracias por usar el programa! ¡Hasta pronto!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
