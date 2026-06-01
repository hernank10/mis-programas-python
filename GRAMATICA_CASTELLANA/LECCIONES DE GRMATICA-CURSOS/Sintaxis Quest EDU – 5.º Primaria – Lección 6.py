import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 6 – SUJETO COMPUESTO Y AMBIGÜEDAD SINTÁCTICA

Un sujeto compuesto tiene dos o más núcleos unidos por una conjunción como 'y', 'o', 'ni'.

🔹 Ejemplo:
- "Mi hermano y mi primo juegan fútbol." → sujeto compuesto = 'Mi hermano y mi primo'

También debemos observar los modificadores que acompañan al sujeto. A veces el orden o la puntuación puede generar ambigüedad.

🎯 Ejemplo ambiguo:
- "Los bomberos y policías valientes ayudaron." ¿Quiénes son valientes? ¿Todos o solo los policías?
"""

# 📚 Ejemplos explicados
ejemplos = [
    {"oracion": "Mi mamá y mi tía cocinan juntas.", "sujeto": "Mi mamá y mi tía"},
    {"oracion": "Los gatos y perros duermen bajo el sol.", "sujeto": "Los gatos y perros"},
    {"oracion": "Carlos y Ana viajan mañana.", "sujeto": "Carlos y Ana"},
    {"oracion": "El niño y la niña dibujan en sus cuadernos.", "sujeto": "El niño y la niña"},
    {"oracion": "Los alumnos y profesores organizan la feria.", "sujeto": "Los alumnos y profesores"}
]

# 📝 Ejercicios
ejercicios = [
    {"oracion": "Juan y Pedro juegan en el parque.", "sujeto": "Juan y Pedro"},
    {"oracion": "Las abejas y mariposas vuelan entre las flores.", "sujeto": "Las abejas y mariposas"},
    {"oracion": "Mi hermana y mi prima pintan juntas.", "sujeto": "Mi hermana y mi prima"},
    {"oracion": "Los niños y niñas bailan en la fiesta.", "sujeto": "Los niños y niñas"},
    {"oracion": "Papá y mamá cocinan la cena.", "sujeto": "Papá y mamá"},
    {"oracion": "El sol y la luna aparecen en cuentos mágicos.", "sujeto": "El sol y la luna"},
    {"oracion": "Mi gato y mi perro juegan con la pelota.", "sujeto": "Mi gato y mi perro"},
    {"oracion": "Carlos y Sofía estudian juntos.", "sujeto": "Carlos y Sofía"},
    {"oracion": "Los árboles y arbustos crecen rápido.", "sujeto": "Los árboles y arbustos"},
    {"oracion": "El lápiz y la goma están en mi mochila.", "sujeto": "El lápiz y la goma"},
    {"oracion": "Los bomberos y policías trabajan duro.", "sujeto": "Los bomberos y policías"},
    {"oracion": "Mi abuelo y mi tío reparan la bicicleta.", "sujeto": "Mi abuelo y mi tío"},
    {"oracion": "Los hermanos y sus amigos ven la película.", "sujeto": "Los hermanos y sus amigos"},
    {"oracion": "Laura y Marta escriben una historia.", "sujeto": "Laura y Marta"},
    {"oracion": "Mi primo y yo corremos por la playa.", "sujeto": "Mi primo y yo"},
    {"oracion": "Las estrellas y planetas brillan en el cielo.", "sujeto": "Las estrellas y planetas"},
    {"oracion": "La maestra y los estudiantes cantan juntos.", "sujeto": "La maestra y los estudiantes"},
    {"oracion": "Tomás y Emma arman el rompecabezas.", "sujeto": "Tomás y Emma"},
    {"oracion": "El tren y el autobús salen temprano.", "sujeto": "El tren y el autobús"},
    {"oracion": "Los cantantes y músicos ensayan hoy.", "sujeto": "Los cantantes y músicos"}
]

elogios = ["🎉 ¡Muy bien!", "🧠 ¡Análisis correcto!", "🌟 ¡Dominio del sujeto compuesto!", "👏 ¡Perfecto!", "⭐ ¡Buen trabajo sintáctico!"]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos explicados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Sujeto compuesto: {ej['sujeto']}\n")

# 📝 Ejercicios
def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Oración: {ej['oracion']}")
        respuesta = input("👉 ¿Cuál es el sujeto compuesto?: ").strip().lower()
        if respuesta == ej["sujeto"].lower():
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: '{ej['sujeto']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia: Detector de Doble Sujeto! 🎭")

# ✍️ Crear oraciones propias
def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS ORACIONES")
    print("Escribe 20 oraciones con sujeto compuesto (ej. 'Mi amigo y mi hermana juegan fútbol.'):\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Oración {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus oraciones creadas:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente creatividad sintáctica!")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 5.º Primaria – Lección 6")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar con 10 ejercicios 📝")
        print("4. Escribir 20 oraciones propias ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            crear_ejemplos_usuario()
        elif opcion == "5":
            print("👋 ¡Gracias por descomponer sujetos y evitar ambigüedades!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
