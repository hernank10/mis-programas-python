import random

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

# === Lista de oraciones incorrectas y sus correcciones ===
ejercicios = [
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
    {
        "incorrecta": "Compruebo y deseo que funcione.",
        "correctas": ["Compruebo que funciona y deseo que funcione.", "Compruebo que funciona y lo deseo."]
    },
    {
        "incorrecta": "Digo y deseo que me escuchen.",
        "correctas": ["Digo que me escuchan y deseo que me escuchen.", "Digo que me escuchan y lo deseo."]
    },
]

def practicar_ejercicios():
    print("\n=== EJERCICIOS DE CORRECCIÓN ===\n")
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

# === Menú principal ===
def main():
    print("=== PROGRAMA DE ESTUDIO SINTÁCTICO ===\n")
    print("¿Qué deseas hacer?")
    print("1. Leer la teoría")
    print("2. Practicar con ejercicios")
    print("3. Salir")

    while True:
        opcion = input("Elige una opción (1-3): ")
        if opcion == "1":
            print(teoria)
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            print("¡Hasta luego! Sigue practicando.")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
