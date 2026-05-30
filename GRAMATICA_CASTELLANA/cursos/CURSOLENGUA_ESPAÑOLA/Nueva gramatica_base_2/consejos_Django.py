import time

# Lista de consejos sobre Django en voz activa
consejos_django = [
    "Usa modelos para estructurar tus datos.",
    "Define vistas en funciones o clases según sea necesario.",
    "Utiliza el ORM de Django para interactuar con la base de datos.",
    "Implementa formularios para gestionar la entrada de datos.",
    "Aprovecha el sistema de autenticación de Django.",
    # ... Agrega aquí los 95 consejos restantes ...
]

# Diccionario para almacenar definiciones personalizadas de Django
diccionario_django = {}

# Función para mostrar consejos y medir la precisión del usuario
def mostrar_consejos():
    print("\n--- Lista de Consejos sobre Django ---")
    for i, consejo in enumerate(consejos_django, start=1):
        print(f"{i}. {consejo}")

    print("\nAhora, escribe cada consejo nuevamente:")

    inicio = time.time()
    correctos = 0
    resultados = []

    for i, consejo in enumerate(consejos_django, start=1):
        entrada = input(f"{i}. Escribe el consejo: ").strip()

        if entrada.lower() == consejo.lower():
            correctos += 1
            resultado = f"{i}. Correcto ✅"
        else:
            resultado = f"{i}. Incorrecto ❌ - Tu respuesta: {entrada} - Correcto: {consejo}"

        resultados.append(resultado)

    fin = time.time()
    tiempo_total = fin - inicio

    # Guardar los resultados en un archivo
    with open("resultados.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\n--- Resultados de la sesión ---\n")
        archivo.write(f"Consejos escritos correctamente: {correctos}/{len(consejos_django)}\n")
        archivo.write(f"Tiempo total: {tiempo_total:.2f} segundos\n")
        archivo.writelines("\n".join(resultados) + "\n")

    print(f"\n¡Finalizado! Has escrito {correctos}/{len(consejos_django)} consejos correctamente.")
    print(f"Tiempo total: {tiempo_total:.2f} segundos.")
    print("Los resultados se han guardado en 'resultados.txt'.")

# Función para convertir un consejo de voz activa a pasiva
def convertir_a_pasiva():
    consejo = input("\nEscribe un consejo en voz activa: ").strip()
    pasiva = f"El consejo es aplicado: {consejo.lower()}"
    print(f"En voz pasiva: {pasiva}")

# Función para convertir un consejo de voz pasiva a activa
def convertir_a_activa():
    consejo = input("\nEscribe un consejo en voz pasiva: ").strip()
    activa = f"Aplica el consejo: {consejo.lower()}"
    print(f"En voz activa: {activa}")

# Función para traducir un consejo al inglés
def traducir_a_ingles():
    consejo = input("\nEscribe un consejo en español para traducir: ").strip()
    print(f"Traducción al inglés: (Traducción pendiente)")

# Función para agregar términos al diccionario de Django
def agregar_diccionario():
    termino = input("\nIngresa un término de Django: ").strip()
    definicion = input("Ingresa su definición: ").strip()
    diccionario_django[termino] = definicion
    print(f"Término '{termino}' agregado al diccionario.")

    # Guardar en archivo
    with open("diccionario_django.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{termino}: {definicion}\n")

# Función para mostrar el diccionario de Django
def mostrar_diccionario():
    if diccionario_django:
        print("\n--- Diccionario de Django ---")
        for termino, definicion in diccionario_django.items():
            print(f"{termino}: {definicion}")
    else:
        print("\nEl diccionario está vacío.")

# Menú principal
while True:
    print("\nMenú Principal")
    print("1. Mostrar todos los consejos y escribirlos nuevamente")
    print("2. Convertir un consejo de voz activa a pasiva")
    print("3. Convertir un consejo de voz pasiva a activa")
    print("4. Traducir un consejo al inglés")
    print("5. Agregar un término al diccionario de Django")
    print("6. Mostrar el diccionario de Django")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_consejos()
    elif opcion == "2":
        convertir_a_pasiva()
    elif opcion == "3":
        convertir_a_activa()
    elif opcion == "4":
        traducir_a_ingles()
    elif opcion == "5":
        agregar_diccionario()
    elif opcion == "6":
        mostrar_diccionario()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

