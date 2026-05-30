import random

# Diccionario con palabras de ejemplo y sus reglas
palabras_ejemplo = {
    "calle": "La 'll' se usa al inicio de sílaba.",
    "hoy": "La 'y' se usa al final de sílaba.",
    "muchacho": "El dígrafo 'ch' representa un sonido único.",
    "miel": "La secuencia 'iy' se pronuncia como una sola sílaba.",
    "rey": "La 'y' final de palabra suena como 'i'.",
    # Agrega más palabras y reglas según sea necesario
}

def verificar_palabra(palabra):
    """Verifica si la palabra contiene 'll', 'y', 'i' o dígrafos y muestra información."""
    if 'll' in palabra:
        print(f"La palabra '{palabra}' contiene el dígrafo 'll'.")
    elif 'y' in palabra:
        print(f"La palabra '{palabra}' contiene la letra 'y'.")
    elif 'ch' in palabra:
        print(f"La palabra '{palabra}' contiene el dígrafo 'ch'.")
    elif 'iy' in palabra:
        print(f"La palabra '{palabra}' contiene la secuencia 'iy'.")
    else:
        print(f"No se encontraron 'll', 'y', 'i' o dígrafos en '{palabra}'.")

    # Buscar la palabra en el diccionario de ejemplos
    if palabra in palabras_ejemplo:
        print(palabras_ejemplo[palabra])

def practicar():
    """Función principal para la práctica interactiva."""
    while True:
        palabra = input("Introduce una palabra (o escribe 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        verificar_palabra(palabra)

if __name__ == "__main__":
    print("¡Bienvenido al programa de práctica de ortografía española!")
    print("Este programa te ayudará a practicar el uso de 'll', 'y', 'i' y dígrafos.")
    practicar()
