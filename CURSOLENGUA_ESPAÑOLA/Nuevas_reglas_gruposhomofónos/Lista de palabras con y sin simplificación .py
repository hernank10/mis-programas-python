import random

# Lista de palabras con y sin simplificación
palabras = [
    ("psicoanálisis", "sicoanálisis"),
    ("psicología", "sicología"),
    # ... (agrega el resto de tus palabras)
]

def generar_ejercicio():
    palabra, simplificada = random.choice(palabras)
    return palabra, simplificada

def corregir_respuesta(palabra, respuesta):
    if respuesta == palabra or respuesta == simplificada:
        return "¡Correcto!"
    else:
        return f"Incorrecto. La respuesta correcta es: {palabra} o {simplificada}"

# Bucle principal para practicar
while True:
    palabra, simplificada = generar_ejercicio()
    respuesta = input(f"Escribe la palabra correctamente: {simplificada} ")
    print(corregir_respuesta(palabra, respuesta))

    # Opción para salir del programa
    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar.lower() != 's':
        break
