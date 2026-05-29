# Este programa demuestra los conceptos básicos de Python para una lección educativa simple.
# Módulo 1: Fundamentos y Planificación del Proyecto.

# 1. Planificación de la lección:
# Objetivo: Enseñar 3 palabras básicas en inglés a hispanohablantes.
# Tema: Vocabulario de animales.
# Mecánica: El programa mostrará una palabra en español y el usuario debe escribir su equivalente en inglés.

# 2. Conceptos clave de Python:
# Variables para almacenar información.
nombre_usuario = ""
puntaje = 0

# Diccionario (tipo de dato) para almacenar las palabras.
# Un diccionario es ideal para guardar pares de clave-valor.
vocabulario_animales = {
    "perro": "dog",
    "gato": "cat",
    "pato": "duck"
}

# 3. Interacción con el usuario.
print("¡Bienvenido a tu primera lección de vocabulario!")
print("Por favor, ingresa tu nombre para empezar.")
nombre_usuario = input("Tu nombre: ")

print(f"\n¡Hola, {nombre_usuario}!")
print("Vamos a aprender 3 palabras de animales en inglés.")
print("Escribe la traducción de la palabra en español.")

# 4. El bucle de la lección (iteración).
# Usamos un bucle 'for' para recorrer cada palabra en nuestro diccionario.
for palabra_espanol, palabra_ingles in vocabulario_animales.items():
    print(f"\n¿Cómo se dice '{palabra_espanol}' en inglés?")
    respuesta_usuario = input("Tu respuesta: ").strip().lower()

    # 5. Lógica de validación (condicionales).
    # Usamos una estructura 'if-else' para verificar la respuesta del usuario.
    if respuesta_usuario == palabra_ingles:
        print("¡Correcto!")
        puntaje += 1
    else:
        print(f"Incorrecto. La respuesta correcta es '{palabra_ingles}'.")

# 6. Mostrar el resultado final.
print("\n--- Lección Terminada ---")
print(f"¡{nombre_usuario}, has completado la lección!")
print(f"Tu puntaje final es: {puntaje} de {len(vocabulario_animales)}.")
print("¡Felicidades!")
