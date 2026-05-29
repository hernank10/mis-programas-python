import random
import json

# Frases de ejemplo
frases = [
    {"texto": "Hernán Cortés llega a Tenochtitlán en 1519.", "categoria": "Presente Histórico"},
    {"texto": "Ayer terminé de leer un libro fascinante.", "categoria": "Pasado"},
    {"texto": "Mañana presentaré mi proyecto en la escuela.", "categoria": "Futuro"},
    {"texto": "Cristóbal Colón zarpa hacia América en 1492.", "categoria": "Presente Histórico"},
    {"texto": "Mis padres celebrarán su aniversario de bodas.", "categoria": "Futuro"},
    {"texto": "El mes pasado visitamos las ruinas de Machu Picchu.", "categoria": "Pasado"},
]

# Función para cambiar tiempo verbal
def cambiar_tiempo(frase, categoria):
    if categoria == "Pasado":
        return frase.replace("ó", "a").replace("ió", "e")  # muy básico
    elif categoria == "Futuro":
        return frase.replace("é", "o")  # muy básico
    elif categoria == "Presente Histórico":
        return frase.replace("a", "ó")  # básico
    else:
        return frase

# Función para mostrar una frase aleatoria
def mostrar_frase():
    frase = random.choice(frases)
    print("\nFrase:")
    print(frase["texto"])
    respuesta = input("¿Qué categoría crees que es? (Presente Histórico/Pasado/Futuro): ")
    if respuesta.lower() == frase["categoria"].lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. Era: {frase['categoria']}")

    cambiar = input("¿Deseas cambiar el tiempo verbal de esta frase? (s/n): ")
    if cambiar.lower() == "s":
        nueva = cambiar_tiempo(frase["texto"], frase["categoria"])
        print(f"Frase con tiempo cambiado: {nueva}")

# Función para agregar frases nuevas
def agregar_frase():
    if len(frases) >= 100:
        print("Ya alcanzaste el límite de 100 frases.")
        return
    texto = input("Escribe tu nueva frase: ")
    categoria = input("¿Qué categoría es? (Presente Histórico/Pasado/Futuro): ")
    frases.append({"texto": texto, "categoria": categoria})
    print("Frase guardada.")

# Función para guardar las frases en archivo
def guardar_frases():
    with open("mis_frases.json", "w", encoding="utf-8") as f:
        json.dump(frases, f, ensure_ascii=False, indent=4)
    print("Frases guardadas en 'mis_frases.json'.")

# Función para ver todas las frases
def ver_frases():
    for i, frase in enumerate(frases, start=1):
        print(f"{i}. {frase['texto']} ({frase['categoria']})")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Practicar identificando categorías")
        print("2. Agregar nueva frase")
        print("3. Ver todas las frases")
        print("4. Guardar frases")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_frase()
        elif opcion == "2":
            agregar_frase()
        elif opcion == "3":
            ver_frases()
        elif opcion == "4":
            guardar_frases()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
