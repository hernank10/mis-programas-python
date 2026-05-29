# -*- coding: utf-8 -*-
import textwrap

# ================
# Diccionario de categorías y ejemplos
# ================

CATEGORIAS = {
    # Bloque 1: Querer pero no poder
    "Bloque 1: Quieres pero no puedes": {
        "1. Aunque quieras": {
            "ejemplos": [
                "Aunque quieras, no puedes intentarlo.",
                "Aunque quieras, no lo lograrás.",
                "Aunque quieras, no podrás hacerlo hoy.",
                "Aunque quieras, no está en tus manos.",
                "Aunque quieras, no podrás convencerme.",
                "Aunque quieras, no vas a cambiar el pasado.",
                "Aunque quieras, no es posible ahora.",
                "Aunque quieras, no depende de ti.",
                "Aunque quieras, no podrás negarlo.",
                "Aunque quieras, no podrás olvidarlo."
            ],
            "regla": "RAE: 'Aunque' introduce oraciones concesivas. Indican un obstáculo que no impide la acción principal. Puede ir seguido de subjuntivo o indicativo."
        },
        "2. Por más que quieras": {
            "ejemplos": [
                "Por más que quieras, no puedes intentarlo.",
                "Por más que quieras, no lograrás engañarme.",
                "Por más que quieras, no podrás evitarlo.",
                "Por más que quieras, no cambiarás la realidad.",
                "Por más que quieras, no conseguirás hacerlo solo.",
                "Por más que quieras, no lograrás borrar la memoria.",
                "Por más que quieras, no te entenderán.",
                "Por más que quieras, no podrás alcanzar esa meta.",
                "Por más que quieras, no está en tu poder.",
                "Por más que quieras, no será suficiente."
            ],
            "regla": "RAE: 'Por más que' es una construcción concesiva intensiva: enfatiza el contraste entre deseo y posibilidad."
        },
        # ... Aquí se añadirían las demás 8 categorías del bloque 1 ...
    },

    # Bloque 2: No quieres pero puedes
    "Bloque 2: No quieres pero puedes": {
        "1. Por más que no quieras": {
            "ejemplos": [
                "Por más que no quieras, sí puedes intentarlo.",
                "Por más que no quieras, sí puedes ayudar.",
                "Por más que no quieras, sí puedes estudiar.",
                "Por más que no quieras, sí puedes participar.",
                "Por más que no quieras, sí puedes escucharme.",
                "Por más que no quieras, sí puedes dar el primer paso.",
                "Por más que no quieras, sí puedes resolverlo.",
                "Por más que no quieras, sí puedes asistir.",
                "Por más que no quieras, sí puedes entenderlo.",
                "Por más que no quieras, sí puedes cambiar."
            ],
            "regla": "RAE: 'Por más que' + subjuntivo introduce una concesiva. Aquí el obstáculo es la falta de voluntad, pero la acción principal sigue siendo posible."
        },
        "2. Aunque no quieras": {
            "ejemplos": [
                "Aunque no quieras, sí puedes intentarlo.",
                "Aunque no quieras, sí puedes mejorar.",
                "Aunque no quieras, sí puedes aprender algo nuevo.",
                "Aunque no quieras, sí puedes concentrarte.",
                "Aunque no quieras, sí puedes dar una respuesta.",
                "Aunque no quieras, sí puedes colaborar.",
                "Aunque no quieras, sí puedes escuchar.",
                "Aunque no quieras, sí puedes sonreír.",
                "Aunque no quieras, sí puedes hacer el esfuerzo.",
                "Aunque no quieras, sí puedes superar la prueba."
            ],
            "regla": "RAE: 'Aunque' introduce oraciones concesivas. Con subjuntivo expresa un hecho posible o supuesto que no impide la acción principal."
        },
        # ... Aquí se añadirían las demás 8 categorías del bloque 2 ...
    }
}

# ================
# Funciones del programa
# ================

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    bloques = list(CATEGORIAS.keys())
    for i, bloque in enumerate(bloques, start=1):
        print(f"{i}. {bloque}")
    print("0. Salir")

def mostrar_categorias(bloque):
    print(f"\n=== {bloque} ===")
    categorias = list(CATEGORIAS[bloque].keys())
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")
    print("0. Volver")

def mostrar_regla(bloque, categoria):
    regla = CATEGORIAS[bloque][categoria]["regla"]
    print("\n📖 REGLA DE LA RAE:")
    print(textwrap.fill(regla, width=70))

def practicar(bloque, categoria):
    ejemplos = CATEGORIAS[bloque][categoria]["ejemplos"]
    puntaje = 0
    print(f"\n--- Práctica con {categoria} ---")
    for ejemplo in ejemplos:
        print("\nEscribe esta frase exactamente:")
        print(f"👉 {ejemplo}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta == ejemplo:
            print("✅ Correcto")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La forma correcta es:\n   {ejemplo}")
    print(f"\nPuntaje final: {puntaje}/{len(ejemplos)}")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige un bloque (número): ")
        if opcion == "0":
            print("¡Hasta pronto! 👋")
            break
        try:
            bloque = list(CATEGORIAS.keys())[int(opcion)-1]
        except:
            print("Opción no válida, intenta de nuevo.")
            continue

        while True:
            mostrar_categorias(bloque)
            sub_opcion = input("\nElige una categoría: ")
            if sub_opcion == "0":
                break
            try:
                categoria = list(CATEGORIAS[bloque].keys())[int(sub_opcion)-1]
            except:
                print("Opción no válida, intenta de nuevo.")
                continue

            while True:
                print(f"\nHas elegido: {categoria}")
                print("1. Ver regla de la RAE")
                print("2. Practicar con ejemplos")
                print("3. Volver")
                accion = input("Elige una opción: ")
                if accion == "1":
                    mostrar_regla(bloque, categoria)
                elif accion == "2":
                    practicar(bloque, categoria)
                elif accion == "3":
                    break
                else:
                    print("Opción inválida.")

if __name__ == "__main__":
    main()
