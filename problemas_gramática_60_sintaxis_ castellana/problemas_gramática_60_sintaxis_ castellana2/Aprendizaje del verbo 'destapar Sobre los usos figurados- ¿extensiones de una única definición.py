import json
import random

# Archivo para almacenar ejemplos de usuario
FILE_NAME = "ejemplos_usuario.json"

# Datos iniciales
teoria = """
El verbo 'destapar' tiene usos rectos y figurados:
- Uso recto: Se refiere a quitar la tapa de algo (Ej: Destapó la botella).
- Uso figurado: Se refiere a revelar información oculta (Ej: Destaparon un escándalo).
"""

ejercicios_completacion = [
    ("El mesero ______ la olla para servir la sopa.", "destapó"),
    ("El periodista ______ una gran conspiración en el gobierno.", "destapó"),
    ("El fontanero ______ la tubería obstruida.", "destapó"),
    ("La investigación ______ secretos ocultos de la empresa.", "destapó"),
    ("El arqueólogo ______ una tumba antigua.", "destapó")
]

def cargar_ejemplos():
    """Carga los ejemplos guardados del usuario."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_ejemplo(nuevo_ejemplo):
    """Guarda un nuevo ejemplo escrito por el usuario."""
    ejemplos = cargar_ejemplos()
    if len(ejemplos) < 100:
        ejemplos.append(nuevo_ejemplo)
        with open(FILE_NAME, "w") as file:
            json.dump(ejemplos, file, indent=4)
        print("Ejemplo guardado exitosamente.")
    else:
        print("Has alcanzado el límite de 100 ejemplos guardados.")

def realizar_completacion():
    """Ejecuta un ejercicio de completación de oraciones."""
    oracion, respuesta_correcta = random.choice(ejercicios_completacion)
    print(f"Completa la oración: {oracion}")
    respuesta_usuario = input("Tu respuesta: ").strip().lower()
    if respuesta_usuario == respuesta_correcta:
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def ejercicio_redaccion():
    """Permite al usuario escribir una oración y guardarla."""
    ejemplo = input("Escribe una oración usando el verbo 'destapar': ")
    guardar_ejemplo(ejemplo)

def menu():
    """Muestra el menú principal del programa."""
    while True:
        print("\n--- Aprendizaje del verbo 'destapar' ---")
        print("1. Ver teoría")
        print("2. Ejercicio de completación")
        print("3. Ejercicio de redacción")
        print("4. Ver ejemplos guardados")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print(teoria)
        elif opcion == "2":
            realizar_completacion()
        elif opcion == "3":
            ejercicio_redaccion()
        elif opcion == "4":
            ejemplos = cargar_ejemplos()
            if ejemplos:
                print("Ejemplos guardados:")
                for i, ej in enumerate(ejemplos, 1):
                    print(f"{i}. {ej}")
            else:
                print("Aún no hay ejemplos guardados.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
