import random

# Diccionario con palabras de ejemplo y sus reglas
palabras_ejemplo = {
    "calle": "La 'll' se usa al inicio de sílaba.",
    "hoy": "La 'y' se usa al final de sílaba.",
    "muchacho": "El dígrafo 'ch' representa un sonido único.",
    # Agrega más palabras y reglas según sea necesario
}

def verificar_palabra(palabra):
    """Verifica si la palabra contiene 'll', 'y' o dígrafos y muestra información."""
    if 'll' in palabra:
        print(f"La palabra '{palabra}' contiene el dígrafo 'll'.")
    elif 'y' in palabra:
        print(f"La palabra '{palabra}' contiene la letra 'y'.")
    elif 'ch' in palabra:
        print(f"La palabra '{palabra}' contiene el dígrafo 'ch'.")
    else:
        print(f"La palabra '{palabra}' no contiene 'll', 'y' o 'ch'.")

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
    print("¡Bienvenido al programa de práctica de 'll', 'y' y dígrafos!")
    practicar()
