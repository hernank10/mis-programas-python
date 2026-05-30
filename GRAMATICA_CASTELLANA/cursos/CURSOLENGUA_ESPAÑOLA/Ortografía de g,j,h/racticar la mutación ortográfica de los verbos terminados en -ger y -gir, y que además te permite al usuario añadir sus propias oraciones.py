import random

def practicar_verbos_ger_gir():
    """
    Función para practicar la mutación ortográfica de verbos terminados en -ger y -gir.

    Args:
        None

    Returns:
        None
    """

    verbos = ["infigir", "acoger", "afligir", "escoger", "fingir", "encoger", "elegir", "dirigir", "proteger", "recoger"]

    print("¡Vamos a practicar los verbos terminados en -ger y -gir!")

    while True:
        verbo = random.choice(verbos)
        if verbo.endswith("gir"):
            forma_correcta = verbo[:-2] + "gi"
        else:
            forma_correcta = verbo[:-2] + "ge"

        # Generar una oración aleatoria
        oraciones = {
            "infigir": ["El juez decidió ____ una pena severa.", "No debes ____ dolor a los demás."],
            "acoger": ["Los refugiados fueron ____ en un campamento.", "Siempre estoy dispuesto a ____ a mis amigos."],
            # ... agregar más oraciones para los demás verbos
        }
        oracion = random.choice(oraciones.get(verbo, ["Completa la oración: ____"]))

        print(oracion)
        respuesta = input("Escribe la forma correcta del verbo: ")

        if respuesta.lower() == forma_correcta.lower():
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La forma correcta es: {forma_correcta}")

        # Opción para agregar nuevas oraciones
        agregar_oracion = input("¿Quieres agregar una nueva oración? (si/no): ")
        if agregar_oracion.lower() == "si":
            nuevo_verbo = input("Introduce el verbo (ej: infigir): ")
            nueva_oracion = input("Introduce la oración: ")
            oraciones.setdefault(nuevo_verbo, []).append(nueva_oracion)
            print("¡Oración agregada!")

        continuar = input("¿Quieres continuar? (si/no): ")
        if continuar.lower() != "si":
            break

if __name__ == "__main__":
    practicar_verbos_ger_gir()
