import os

# Archivo para guardar el progreso
PROGRESO_ARCHIVO = "progreso_usuario.txt"

def guardar_progreso(categoria, resultado):
    """Guarda el progreso del usuario en un archivo."""
    with open(PROGRESO_ARCHIVO, "a") as archivo:
        archivo.write(f"Categoría: {categoria} | Resultado: {resultado}\n")
    print(f"\nProgreso guardado: {categoria} - {resultado}\n")

def ver_progreso():
    """Muestra el progreso guardado del usuario."""
    if os.path.exists(PROGRESO_ARCHIVO):
        with open(PROGRESO_ARCHIVO, "r") as archivo:
            progreso = archivo.read()
        print("\n--- Progreso del Usuario ---")
        print(progreso)
    else:
        print("\nAún no hay progreso guardado.")

# Ejemplo de cuestionario genérico (puedes personalizar más)
def cuestionario_generico(categoria):
    print(f"\n--- Cuestionario: {categoria} ---")
    preguntas = [
        ("¿Cómo se escribe correctamente? (a) hola (b) ola", "a"),
        ("Elige el artículo correcto: __ gato (a) el (b) los", "a"),
        ("¿Cuál es el sustantivo en la frase 'El perro corre'? (a) perro (b) corre", "a")
    ]
    aciertos = 0
    for i, (pregunta, respuesta_correcta) in enumerate(preguntas, start=1):
        print(f"\nPregunta {i}: {pregunta}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == respuesta_correcta:
            print("¡Correcto!")
            aciertos += 1
        else:
            print("Incorrecto.")
    print(f"\nPuntaje final: {aciertos}/{len(preguntas)}")
    guardar_progreso(categoria, f"{aciertos}/{len(preguntas)}")

# Funciones para cada cuestionario
def practicar_articulos():
    cuestionario_generico("Artículos")

def practicar_sustantivos():
    cuestionario_generico("Sustantivos")

def practicar_adjetivos():
    cuestionario_generico("Adjetivos")

def practicar_verbos():
    cuestionario_generico("Verbos")

def practicar_adverbios():
    cuestionario_generico("Adverbios")

def agregar_cuestionario():
    """Permite agregar una nueva categoría de cuestionario al menú."""
    nueva_categoria = input("\nIntroduce el nombre de la nueva actividad o cuestionario: ").strip()
    nueva_funcion = f"practicar_{nueva_categoria.lower()}"
    globals()[nueva_funcion] = lambda: cuestionario_generico(nueva_categoria)
    print(f"\n¡Nueva categoría '{nueva_categoria}' añadida al menú!")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Practicar artículos")
        print("2. Practicar sustantivos")
        print("3. Practicar adjetivos")
        print("4. Practicar verbos")
        print("5. Practicar adverbios")
        print("6. Agregar nueva actividad/cuestionario")
        print("7. Ver progreso guardado")
        print("0. Salir")

        try:
            opcion = int(input("\nSelecciona una opción: "))
            if opcion == 1:
                practicar_articulos()
            elif opcion == 2:
                practicar_sustantivos()
            elif opcion == 3:
                practicar_adjetivos()
            elif opcion == 4:
                practicar_verbos()
            elif opcion == 5:
                practicar_adverbios()
            elif opcion == 6:
                agregar_cuestionario()
            elif opcion == 7:
                ver_progreso()
            elif opcion == 0:
                print("¡Gracias por practicar! Hasta pronto.")
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el programa
menu_principal()
