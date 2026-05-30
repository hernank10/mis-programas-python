import random

# Sustantivos de la quinta declinación (ejemplos)
sustantivos = {
    "res": "cosa",
    "dies": "día",
    "fides": "fe, confianza",
    "species": "apariencia",
    "acies": "ejército en formación"
}

# Modelos de la quinta declinación
declinacion = {
    "singular": {
        "nominativo": "es",
        "genitivo": "ei",
        "dativo": "ei",
        "acusativo": "em",
        "ablativo": "e"
    },
    "plural": {
        "nominativo": "es",
        "genitivo": "erum",
        "dativo": "ebus",
        "acusativo": "es",
        "ablativo": "ebus"
    }
}

# Función para declinar un sustantivo
def declinar(palabra):
    tema = palabra[:-2]  # Ejemplo: "res" -> "r"
    formas = {}
    for numero, casos in declinacion.items():
        formas[numero] = {}
        for caso, desinencia in casos.items():
            formas[numero][caso] = tema + desinencia
    return formas

# Juego de práctica
def practicar():
    palabra = random.choice(list(sustantivos.keys()))
    traduccion = sustantivos[palabra]
    formas = declinar(palabra)

    print(f"\nDeclina la palabra latina '{palabra}' ({traduccion}) en la quinta declinación:\n")
    for numero, casos in formas.items():
        for caso, correcta in casos.items():
            respuesta = input(f"{numero.capitalize()} {caso.capitalize()}: ")
            if respuesta.strip().lower() == correcta.lower():
                print("✅ Correcto")
            else:
                print(f"❌ Incorrecto. Respuesta esperada: {correcta}")

# Menú principal
def menu():
    while True:
        print("\n--- Práctica de la Quinta Declinación Latina ---")
        print("1. Practicar con un sustantivo aleatorio")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            practicar()
        elif opcion == "2":
            print("¡Vale! Fin del entrenamiento de la quinta declinación.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
