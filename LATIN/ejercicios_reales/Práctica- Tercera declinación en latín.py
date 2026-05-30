import random

# Diccionario de sustantivos de la tercera declinación
# Formato: nominativo singular: [genitivo, género, significado]
sustantivos = {
    "rex": ["regis", "m", "rey"],
    "mater": ["matris", "f", "madre"],
    "homo": ["hominis", "m", "hombre"],
    "pater": ["patris", "m", "padre"],
    "corpus": ["corporis", "n", "cuerpo"],
    "nomen": ["nominis", "n", "nombre"],
    "civis": ["civis", "m/f", "ciudadano"],
    "hostis": ["hostis", "m", "enemigo"],
    "amor": ["amoris", "m", "amor"],
    "lex": ["legis", "f", "ley"],
}

# Casos latinos
casos = ["nominativo", "genitivo", "dativo", "acusativo", "ablativo", "vocativo"]

# Reglas de formación simplificadas para la tercera declinación
def declinar(palabra, genitivo, genero):
    tema = genitivo[:-2]  # se elimina "-is" del genitivo
    if palabra.endswith("is") or palabra.endswith("es"):
        # sustantivos parisílabos (ej. civis, hostis)
        terminaciones_sg = ["", "is", "i", "em", "e", ""]
        terminaciones_pl = ["es", "ium", "ibus", "es", "ibus", "es"]
    else:
        # sustantivos imparisílabos (ej. rex, mater, amor)
        if genero == "n":
            terminaciones_sg = ["", "is", "i", "", "e", ""]
            terminaciones_pl = ["a", "um", "ibus", "a", "ibus", "a"]
        else:
            terminaciones_sg = ["", "is", "i", "em", "e", ""]
            terminaciones_pl = ["es", "um", "ibus", "es", "ibus", "es"]

    singular = [tema + t for t in terminaciones_sg]
    plural = [tema + t for t in terminaciones_pl]

    # Corrección para nominativo/vocativo singular (se conserva la forma del nominativo original)
    singular[0] = palabra
    singular[5] = palabra

    return singular, plural

# Generar un ejercicio
def ejercicio():
    palabra, (genitivo, genero, significado) = random.choice(list(sustantivos.items()))
    singular, plural = declinar(palabra, genitivo, genero)

    print(f"\nSustantivo: {palabra}, {genitivo} ({genero}) → {significado}")
    print("Declina en singular y plural:")

    for i, caso in enumerate(casos):
        print(f"{caso.capitalize()} singular: {singular[i]}")
        print(f"{caso.capitalize()} plural: {plural[i]}")

# Programa principal
def main():
    print("=== Práctica: Tercera declinación en latín ===")
    for i in range(10):  # genera 10 ejercicios
        ejercicio()

if __name__ == "__main__":
    main()
