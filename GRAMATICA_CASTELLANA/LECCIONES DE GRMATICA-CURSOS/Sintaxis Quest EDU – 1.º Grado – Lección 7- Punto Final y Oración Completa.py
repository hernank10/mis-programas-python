import random

# 📘 Teoría de la lección
teoria = """
📘 LECCIÓN 7 – ¿DÓNDE TERMINA LA ORACIÓN?

Las oraciones tienen un inicio y un fin. 
Cuando una idea está completa, la cerramos con un punto final (.)

💡 Ejemplo:
✅ "Mi perro juega en el jardín."
⛔ "Mi perro juega" (¿Dónde? ¿Cuándo? Falta algo...)

🎯 El punto final indica que la idea está lista.
"""

# 📚 Ejemplos explicados
ejemplos = [
    {"incompleta": "María juega", "completa": "María juega en el parque."},
    {"incompleta": "El gato duerme", "completa": "El gato duerme bajo la mesa."},
    {"incompleta": "Yo tengo", "completa": "Yo tengo un cuaderno nuevo."},
    {"incompleta": "Pedro corre", "completa": "Pedro corre muy rápido."},
    {"incompleta": "La maestra escribe", "completa": "La maestra escribe en la pizarra."}
]

# 📝 20 Ejercicios de completación
ejercicios = [
    "Mi hermano come",
    "El autobús llega",
    "La casa es",
    "Hoy hace",
    "La vaca vive",
    "El reloj marca",
    "Mi mamá canta",
    "Los niños saltan",
    "La luna brilla",
    "Juan dibuja",
    "Yo escribo",
    "El pájaro vuela",
    "La niña baila",
    "El árbol crece",
    "El tren pasa",
    "La abuela cocina",
    "Ellos estudian",
    "Mi tío pinta",
    "Papá trabaja",
    "Nosotros jugamos"
]

elogios = [
    "🎉 ¡Oración completa!",
    "🧠 ¡Muy bien, terminaste la idea!",
    "✅ ¡Punto final usado correctamente!",
    "👏 ¡Oración clara y cerrada!",
    "🌟 ¡Excelente uso del punto!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for e in ejemplos:
        print(f"⛔ Incompleta: {e['incompleta']}")
        print(f"✅ Completa: {e['completa']}\n")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 COMPLETA LA ORACIÓN CON UN FINAL LÓGICO Y AGREGA EL PUNTO:")
    seleccion = random.sample(ejercicios, 10)
    for i, frase in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Inicia la oración: {frase}")
        respuesta = input("👉 Escribe la oración completa: ").strip()
        if respuesta.endswith("."):
            print(random.choice(elogios))
        else:
            print("⚠️ Recuerda terminar tu oración con un punto final.")

# ✍️ Crear oraciones propias
def escribir_propias():
    print("\n✍️ ESCRIBE 10 ORACIONES COMPLETAS CON PUNTO FINAL:")
    propias = []
    for i in range(1, 11):
        oracion = input(f"👉 Oración {i}: ").strip()
        propias.append(oracion)

    print("\n📘 Tus oraciones escritas:")
    for idx, o in enumerate(propias, 1):
        print(f"{idx}. {o}")
    print("🏅 ¡Muy bien! Cada oración cuenta como una idea completa.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 1.º Grado – Lección 7: Punto Final y Oración Completa")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar con 10 ejercicios 📝")
        print("4. Escribir 10 oraciones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            escribir_propias()
        elif opcion == "5":
            print("👋 ¡Gracias por cerrar tus ideas con claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Iniciar el programa
if __name__ == "__main__":
    menu()
