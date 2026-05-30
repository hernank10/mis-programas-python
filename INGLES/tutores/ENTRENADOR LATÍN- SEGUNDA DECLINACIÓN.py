import random

# Reglas de la segunda declinación
reglas = """
SEGUNDA DECLINACIÓN (masculinos en -us/-er y neutros en -um):

Singular:
Nominativo: -us / -er / -um
Genitivo:   -i
Dativo:     -o
Acusativo:  -um
Ablativo:   -o
Vocativo:   -e / -er / -um

Plural:
Nominativo: -i / -a (neutro)
Genitivo:   -orum
Dativo:     -is
Acusativo:  -os / -a (neutro)
Ablativo:   -is
Vocativo:   -i / -a (neutro)
"""

# Lista de palabras de la segunda declinación
sustantivos = [
    ("amicus", "amigo", "m"),
    ("servus", "esclavo", "m"),
    ("liber", "libro", "m"),
    ("puer", "niño", "m"),
    ("magister", "maestro", "m"),
    ("templum", "templo", "n"),
    ("oppidum", "ciudad pequeña", "n"),
    ("donum", "regalo", "n"),
    ("bellum", "guerra", "n"),
    ("verbum", "palabra", "n")
]

# Casos para practicar
casos = [
    ("Nominativo", {"m": ["us", "i"], "n": ["um", "a"]}),
    ("Genitivo", {"m": ["i", "orum"], "n": ["i", "orum"]}),
    ("Dativo", {"m": ["o", "is"], "n": ["o", "is"]}),
    ("Acusativo", {"m": ["um", "os"], "n": ["um", "a"]}),
    ("Ablativo", {"m": ["o", "is"], "n": ["o", "is"]}),
    ("Vocativo", {"m": ["e", "i"], "n": ["um", "a"]})
]

# Función para generar una forma esperada
def generar_forma(sustantivo, numero, caso):
    nominativo, traduccion, genero = sustantivo
    tema = nominativo[:-2] if nominativo.endswith(("us", "um")) else nominativo
    sufijo = casos[caso][1][genero][0] if numero == "singular" else casos[caso][1][genero][1]
    return tema + sufijo

# Función de ejercicio
def ejercicio():
    sust = random.choice(sustantivos)
    caso = random.randint(0, len(casos)-1)
    numero = random.choice(["singular", "plural"])

    nombre_caso, _ = casos[caso]
    correcta = generar_forma(sust, numero, caso)

    print(f"\nDeclina '{sust[0]}' ({sust[1]}, {sust[2]})")
    print(f"→ {nombre_caso} {numero}:")
    resp = input("Tu respuesta: ").strip()

    if resp == correcta:
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. La forma correcta es: {correcta}")

# Menú principal
def menu():
    while True:
        print("\n=== ENTRENADOR LATÍN: SEGUNDA DECLINACIÓN ===")
        print("1. Ver reglas")
        print("2. Practicar ejercicios (30 rondas)")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(reglas)
        elif opcion == "2":
            for i in range(30):
                ejercicio()
        elif opcion == "3":
            print("Vale, ¡hasta luego!")
            break
        else:
            print("Opción no válida.")

# Ejecutar
if __name__ == "__main__":
    menu()
