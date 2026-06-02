# Simulador de Relaciones Interactivas

def mostrar_estado_relaciones(relaciones):
    print("\nEstado de Relaciones:")
    for personaje, nivel in relaciones.items():
        print(f"{personaje}: {nivel}")

def interactuar(personaje, relaciones):
    print(f"\nInteractuando con {personaje}.")
    elección = input("¿Qué quieres hacer? (saludar/regalar/conversar): ").lower()
    if elección == 'saludar':
        relaciones[personaje] += 1
        print(f"Has saludado a {personaje}. Nivel de relación: {relaciones[personaje]}")
    elif elección == 'regalar':
        relaciones[personaje] += 2
        print(f"Has regalado algo a {personaje}. Nivel de relación: {relaciones[personaje]}")
    elif elección == 'conversar':
        respuesta = input(f"¿Qué le preguntas a {personaje}? ")
        print(f"{personaje} responde: 'Interesante.'")
        relaciones[personaje] += 1
    else:
        print("Acción no válida.")

def main():
    relaciones = {
        'Ana': 0,
        'Carlos': 0,
        'Beatriz': 0
    }
    print("Bienvenido al Simulador de Relaciones Interactivas.")
    while True:
        acción = input("\n¿Qué quieres hacer? (interactuar/ver relaciones/salir): ").lower()
        if acción == 'interactuar':
            personaje = input("¿Con quién quieres interactuar? (Ana/Carlos/Beatriz): ").capitalize()
            if personaje in relaciones:
                interactuar(personaje, relaciones)
            else:
                print("Personaje no reconocido.")
        elif acción == 'ver relaciones':
            mostrar_estado_relaciones(relaciones)
        elif acción == 'salir':
            print("Gracias por jugar.")
            break
        else:
            print("Acción no válida.")

if __name__ == "__main__":
    main()
