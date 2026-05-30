import random

# Inventario inicial y emoticones disponibles
emoticons = {
    "⛺": "Tienda de campaña",
    "🔥": "Fogata",
    "🎣": "Caña de pescar",
    "🐎": "Caballo",
    "🏍️": "Motocicleta",
    "🚗": "Automóvil",
    "🎒": "Mochila",
    "🧭": "Brújula",
    "🔦": "Linterna",
    "🛶": "Canoa",
    "🦌": "Ciervo",
}
inventario = []

# Función para mostrar la descripción inicial
def bienvenida():
    print("""
✨ Bienvenidos a la Aventura Estelar ✨
Tomson, la científica Laurent y Koko, su mascota robot, han aterrizado en el bosque Boreal. 
Su misión: recolectar objetos esenciales para sobrevivir y completar su aventura.
""")

# Mostrar menú principal
def mostrar_menu():
    print("\nOpciones del juego:")
    print("1. Buscar objetos")
    print("2. Ver inventario")
    print("3. Usar un objeto")
    print("4. Hablar con Laurent")
    print("5. Hablar con Koko")
    print("6. Salir del juego")
    return input("Elige una opción: ")

# Buscar objetos en el entorno
def buscar_objetos():
    print("\n🔍 Buscando en el área...")
    if random.random() < 0.7:  # 70% de probabilidad de encontrar algo
        objeto = random.choice(list(emoticons.items()))
        if objeto[0] in inventario:
            print(f"🌟 Ya tienes {objeto[1]} ({objeto[0]}).")
        else:
            print(f"🎉 ¡Encontraste {objeto[1]} ({objeto[0]})!")
            inventario.append(objeto[0])
    else:
        print("😔 No encontraste nada. Sigue explorando.")

# Mostrar el inventario actual
def mostrar_inventario():
    if inventario:
        print("\n🎒 Inventario:")
        for item in inventario:
            print(f"{item} - {emoticons[item]}")
    else:
        print("\nTu inventario está vacío. ¡Sigue buscando!")

# Usar un objeto del inventario
def usar_objeto():
    if inventario:
        print("\nElige un objeto para usar:")
        for i, item in enumerate(inventario, 1):
            print(f"{i}. {item} - {emoticons[item]}")
        opcion = int(input("Introduce el número del objeto: "))
        if 1 <= opcion <= len(inventario):
            objeto_usado = inventario.pop(opcion - 1)
            print(f"✨ Usaste {emoticons[objeto_usado]} ({objeto_usado}).")
        else:
            print("❌ Opción no válida.")
    else:
        print("🎒 No tienes objetos para usar.")

# Interactuar con Laurent
def hablar_con_laurent():
    print("\n👩‍🔬 Laurent dice:")
    consejos = [
        "Asegúrate de recolectar suficientes suministros antes de avanzar.",
        "Recuerda, la brújula te ayudará a no perderte.",
        "Una fogata puede ser esencial para calentar el área por la noche.",
    ]
    print(f"💬 {random.choice(consejos)}")

# Interactuar con Koko
def hablar_con_koko():
    print("\n🤖 Koko dice:")
    frases = [
        "¡Beeep boop! ¡Revisemos la zona nuevamente!",
        "Beeep boop... ¿Dónde dejé mi cargador solar?",
        "¡Beeep! ¡Encontré algo brillante cerca!",
    ]
    print(f"💬 {random.choice(frases)}")

# Juego principal
def juego_principal():
    bienvenida()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            buscar_objetos()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            usar_objeto()
        elif opcion == "4":
            hablar_con_laurent()
        elif opcion == "5":
            hablar_con_koko()
        elif opcion == "6":
            print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima aventura!")
            break
        else:
            print("❓ Opción no válida. Intenta de nuevo.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_principal()
