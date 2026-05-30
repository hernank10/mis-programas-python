import random

# Recursos iniciales y personajes
recursos = {"agua": 50, "alimento": 30, "oxígeno": 100, "energía": 70}
granjas_construidas = 0

personajes = {
    "Tomson": {"rol": "Ingeniero", "especialidad": "Construir estructuras"},
    "Laurent": {"rol": "Científica", "especialidad": "Optimizar recursos"},
    "Koko": {"rol": "Robot Ayudante", "especialidad": "Buscar suministros"}
}

# Introducción narrativa
def introduccion():
    print("""
🌌 Bienvenidos a Marte: Proyecto Granja 🌌

Después de un viaje épico, el equipo compuesto por:
- 👨‍🔧 Tomson, el ingeniero
- 👩‍🔬 Laurent, la científica
- 🤖 Koko, el robot ayudante

Ha aterrizado en la base marciana. Su misión es clara: construir una granja autosuficiente para asegurar la supervivencia en el planeta rojo.

🌱 Tu objetivo:
1️⃣ Gestionar recursos para sobrevivir.
2️⃣ Construir y mantener granjas.
3️⃣ Superar los desafíos del clima y la escasez de recursos.
""")

# Mostrar el estado actual de los recursos
def mostrar_recursos():
    print("\n📊 Estado actual de recursos:")
    for recurso, cantidad in recursos.items():
        print(f"- {recurso.capitalize()}: {cantidad}")

# Menú principal
def mostrar_menu():
    print("\nOpciones del juego:")
    print("1. Construir una granja🏇⛺")
    print("2. Buscar recursos con Koko🐕🤖 ")
    print("3. Optimizar recursos con Laurent👩‍🚀")
    print("4. Revisar estado de los recursos👩‍🚀")
    print("5. Hablar con Tomson👨‍🚀")
    print("6. Salir del juego")
    return input("Elige una opción: ")

# Construir una granja
def construir_granja():
    global granjas_construidas
    print("\n🔧 Tomson👨 está trabajando en la construcción de una granja...")
    if recursos["agua"] >= 20 and recursos["energía"] >= 30:
        granjas_construidas += 1
        recursos["agua"] -= 20
        recursos["energía"] -= 30
        print(f"🌱 ¡Éxito! Ahora tienes {granjas_construidas} granja(s) construida(s).")
    else:
        print("❌ No tienes suficientes recursos para construir una granja.")

# Buscar recursos con Koko
def buscar_recursos():
    print("\n🤖 Koko está explorando el área en busca de recursos...")
    encontrado = random.choice(["agua", "alimento", "oxígeno", "energía", None])
    if encontrado:
        cantidad = random.randint(10, 30)
        recursos[encontrado] += cantidad
        print(f"🎉 Koko encontró {cantidad} unidades de {encontrado}.")
    else:
        print("😔 Koko no encontró nada esta vez.")

# Optimizar recursos con Laurent
def optimizar_recursos():
    print("\n👩‍🔬 Laurent está trabajando en optimizar los recursos...")
    recurso_mejorado = random.choice(list(recursos.keys()))
    cantidad = random.randint(5, 15)
    recursos[recurso_mejorado] += cantidad
    print(f"✨ Laurent mejoró el uso de {recurso_mejorado}, obteniendo {cantidad} unidades adicionales.")

# Hablar con Tomson
def hablar_con_tomson():
    print("\n👨‍🔧 Tomson dice:")
    consejos = [
        "Asegúrate de tener suficiente energía para construir.",
        "Una granja bien gestionada puede producir alimento adicional.",
        "Siempre verifica tus recursos antes de intentar construir."
    ]
    print(f"💬 {random.choice(consejos)}")

# Juego principal
def juego_principal():
    introduccion()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            construir_granja()
        elif opcion == "2":
            buscar_recursos()
        elif opcion == "3":
            optimizar_recursos()
        elif opcion == "4":
            mostrar_recursos()
        elif opcion == "5":
            hablar_con_tomson()
        elif opcion == "6":
            print("\n👋 ¡Gracias por jugar! ¡Buena suerte en Marte!")
            break
        else:
            print("❓ Opción no válida. Intenta de nuevo.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_principal()
