import random

# === Archivo para guardar reflexiones y ejemplos ===
archivo_usuario = "mis_ejercicios_y_reflexiones.txt"

# === Teoría ===
teoria = """
CONSTRUCCIÓN INCORRECTA:
Dos verbos principales, uno que rige indicativo y otro que rige subjuntivo, no pueden compartir una única subordinada.
Cada uno exige su propio modo.

EJEMPLO INCORRECTO:
- "Creo y deseo que venga."
   → INCORRECTO: 'creo' exige indicativo, 'deseo' exige subjuntivo.
   → CORRECTO: "Creo que vendrá y deseo que venga." o "Creo que vendrá y lo deseo."

SOLUCIÓN:
✓ Separar las subordinadas
✓ Usar pronombres para evitar repeticiones
✓ Mantener el modo verbal adecuado

FUNCIONA EN:
- Cualquier tiempo verbal (presente, pasado, futuro)
- Cualquier sujeto
"""

# === Lista de ejercicios ===
ejercicios_base = [
    {
        "incorrecta": "Creo y deseo que ella venga.",
        "correctas": ["Creo que ella vendrá y deseo que ella venga.", "Creo que vendrá y lo deseo."]
    },
    {
        "incorrecta": "Afirmo y pido que respetes la norma.",
        "correctas": ["Afirmo que respetas la norma y pido que la respetes.", "Afirmo que la respetas y pido que la respetes."]
    },
    {
        "incorrecta": "Sé y espero que lleguen a tiempo.",
        "correctas": ["Sé que llegarán a tiempo y espero que lleguen a tiempo.", "Sé que llegarán y lo espero."]
    },
]

# === Modo práctica normal ===
def practicar_ejercicios():
    print("\n=== EJERCICIOS DE CORRECCIÓN ===\n")
    ejercicios = ejercicios_base.copy()
    random.shuffle(ejercicios)
    puntuacion = 0

    for i, ej in enumerate(ejercicios):
        print(f"Ejercicio {i+1}:")
        print("Oración incorrecta:")
        print(">>", ej["incorrecta"])
        respuesta = input("Corrige la oración:\n>> ").strip().lower()

        if any(resp.lower() == respuesta for resp in ej["correctas"]):
            print("✅ ¡Correcto!")
            puntuacion += 1
        else:
            print("❌ Incorrecto. Algunas formas correctas serían:")
            for cor in ej["correctas"]:
                print("→", cor)
        print()

    print(f"Tu puntuación: {puntuacion}/{len(ejercicios)}")

# === Guardar reflexiones ===
def guardar_reflexion():
    print("\n=== GUARDAR REFLEXIÓN O EJEMPLO ===")
    texto = input("Escribe tu reflexión o ejemplo para guardar:\n>> ")
    with open(archivo_usuario, "a", encoding="utf-8") as file:
        file.write("✍️ " + texto + "\n")
    print("✅ Guardado correctamente.\n")

# === Crear ejercicio personalizado ===
def crear_ejercicio():
    print("\n=== CREAR TU PROPIO EJERCICIO ===")
    incorrecta = input("Escribe una oración incorrecta:\n>> ")
    correctas = input("Escribe al menos una corrección (separa varias con '|'):\n>> ").split('|')
    ejercicios_base.append({
        "incorrecta": incorrecta.strip(),
        "correctas": [c.strip() for c in correctas]
    })
    print("✅ Ejercicio agregado a la práctica.\n")

# === Reescribir oración técnica o literaria ===
def reescribir_oracion():
    print("\n=== REESCRIBIR ORACIÓN EN LENGUAJE SIMPLE ===")
    oracion = input("Escribe una oración técnica o literaria:\n>> ")
    simplificada = input("Reescribe esa oración en un lenguaje claro o directo:\n>> ")
    with open(archivo_usuario, "a", encoding="utf-8") as file:
        file.write("🔁 Técnica: " + oracion + "\n➡️ Simple: " + simplificada + "\n\n")
    print("✅ Reescritura guardada.\n")

# === Modo práctica extendida ===
def practica_extendida():
    print("\n=== MODO PRÁCTICA EXTENDIDA ===")
    for i in range(1, 101):
        print(f"\nEjercicio {i}/100:")
        oracion = input("Escribe una oración incorrecta (o deja en blanco para terminar):\n>> ")
        if not oracion.strip():
            break
        correccion = input("Escribe la corrección adecuada:\n>> ")
        with open("practica_extendida.txt", "a", encoding="utf-8") as file:
            file.write(f"Incorrecta: {oracion}\nCorrecta: {correccion}\n\n")
    print("✅ Práctica extendida guardada en 'practica_extendida.txt'.")

# === Menú principal ===
def main():
    print("=== PROGRAMA DE ESTUDIO SINTÁCTICO – MODO COMPLETO ===\n")
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Leer la teoría")
        print("2. Practicar ejercicios")
        print("3. Guardar reflexión o ejemplo")
        print("4. Crear tu propio ejercicio")
        print("5. Reescribir oración técnica o literaria")
        print("6. Modo práctica extendida (100 ejemplos)")
        print("7. Salir")
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            print(teoria)
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            guardar_reflexion()
        elif opcion == "4":
            crear_ejercicio()
        elif opcion == "5":
            reescribir_oracion()
        elif opcion == "6":
            practica_extendida()
        elif opcion == "7":
            print("¡Hasta luego! Tus avances están guardados.")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

# Ejecutar
if __name__ == "__main__":
    main()
