# Programa interactivo: Reglas del Presente Simple en Inglés
# Autor: Hernán + ChatGPT
# Aprender conjugación del inglés desde el castellano

# Diccionario con las reglas
rules = {
    "1": {
        "nombre": "Forma básica sin cambios (I, you, we, they)",
        "sintaxis": "Sujeto (I/You/We/They) + verbo en forma base",
        "semantica": "Acciones habituales, gustos, rutinas o hechos generales",
        "ejemplo": "I work every day. (Yo trabajo todos los días)"
    },
    "2": {
        "nombre": "Tercera persona singular con -s (He, She, It)",
        "sintaxis": "Sujeto (He/She/It) + verbo + -s",
        "semantica": "Marca la tercera persona singular",
        "ejemplo": "He works in a hospital. (Él trabaja en un hospital)"
    },
    "3": {
        "nombre": "Excepción -es (-ss, -sh, -ch, -x, -o)",
        "sintaxis": "Verbo terminado en -ss, -sh, -ch, -x, -o → + es",
        "semantica": "Mantiene la sonoridad y ortografía",
        "ejemplo": "She watches TV. (Ella ve televisión)"
    },
    "4": {
        "nombre": "Cambio ortográfico -y → -ies",
        "sintaxis": "Verbo terminado en consonante + y → cambia y por i + es",
        "semantica": "Evita combinaciones incorrectas",
        "ejemplo": "He studies English. (Él estudia inglés)"
    },
    "5": {
        "nombre": "Usos semánticos: hábitos y verdades universales",
        "sintaxis": "Sujeto + verbo (según regla 1–4)",
        "semantica": "Expresa rutinas, verdades científicas o permanentes",
        "ejemplo": "The Earth moves around the sun. (La Tierra gira alrededor del sol)"
    }
}

def mostrar_menu():
    print("\n=== MENÚ DE REGLAS DEL PRESENTE SIMPLE EN INGLÉS ===")
    for key, value in rules.items():
        print(f"{key}. {value['nombre']}")
    print("0. Salir")

def practicar_regla(opcion):
    regla = rules[opcion]
    print(f"\n📘 {regla['nombre']}")
    print(f"👉 Sintaxis: {regla['sintaxis']}")
    print(f"👉 Significado/Semántica: {regla['semantica']}")
    print(f"👉 Ejemplo: {regla['ejemplo']}\n")

    # Pregunta 1: recordar la regla
    recordar = input("✍ Escribe de memoria la regla (sintaxis): ")
    if recordar.strip().lower() == regla["sintaxis"].lower():
        print("✅ Correcto, la recordaste bien.")
    else:
        print(f"❌ No exacto. La sintaxis es: {regla['sintaxis']}")

    # Pregunta 2: escribir el ejemplo
    ejemplo_usuario = input("\n✍ Escribe el ejemplo tal como se mostró: ")
    if ejemplo_usuario.strip().lower() == regla["ejemplo"].lower():
        print("✅ Muy bien, escribiste el ejemplo correctamente.")
    else:
        print(f"❌ No exacto. El ejemplo correcto es: {regla['ejemplo']}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Elige una categoría de regla (0 para salir): ")

    if opcion == "0":
        print("👋 Gracias por practicar las reglas del presente simple. ¡Hasta pronto!")
        break
    elif opcion in rules:
        practicar_regla(opcion)
    else:
        print("⚠️ Opción no válida, intenta de nuevo.")
