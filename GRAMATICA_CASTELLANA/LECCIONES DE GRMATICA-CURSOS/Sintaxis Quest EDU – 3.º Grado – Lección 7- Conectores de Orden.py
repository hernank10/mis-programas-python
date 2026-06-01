import random

# 📘 Teoría explicada
teoria = """
📘 LECCIÓN 7 – ¿QUÉ SUCEDE PRIMERO, DESPUÉS Y AL FINAL?

Cuando contamos algo, es importante decir las cosas en orden.
Usamos conectores como:

🔹 primero
🔹 luego
🔹 después
🔹 al final

🎯 Ejemplo:
"Primero, me levanto. Luego, me cepillo los dientes. Después, me visto. Al final, desayuno."

Así es más fácil entender lo que pasó.

"""

# 📚 Ejemplos guiados
ejemplos = [
    "Primero, Paula se lavó la cara. Luego, se peinó. Después, buscó su mochila. Al final, fue a la escuela.",
    "Primero, Leo recogió sus juguetes. Luego, ayudó a poner la mesa. Después, comió con su familia. Al final, leyó un cuento.",
    "Primero, desperté temprano. Luego, saludé a mamá. Después, fui al parque. Al final, comí helado."
]

# 📝 20 ejercicios de frases desordenadas
ejercicios = [
    ["se lavó la cara", "fue a la escuela", "se peinó", "buscó su mochila"],
    ["fui al parque", "comí helado", "desperté temprano", "saludé a mamá"],
    ["recogió sus juguetes", "puso la mesa", "comió", "leyó un cuento"],
    ["fue al zoológico", "desayunó", "se vistió", "vio muchos animales"],
    ["entró al salón", "saludó a la maestra", "se sentó", "escribió su nombre"],
    ["salí del colegio", "fui a casa", "almorcé", "jugué con mis amigos"],
    ["me cepillé los dientes", "tomé agua", "me acosté", "apagué la luz"],
    ["me desperté", "me duché", "me vestí", "desayuné"],
    ["se subió al autobús", "se despidió de mamá", "llegó a la escuela", "sacó su cuaderno"],
    ["abrió el regalo", "sonrió", "dijo gracias", "jugó con el juguete"]
]

elogios = [
    "✅ ¡Muy bien organizado!",
    "🎯 ¡Buena secuencia!",
    "🌟 ¡Tus ideas tienen orden!",
    "👏 ¡Excelente uso de conectores!",
    "🧠 ¡Ahora se entiende mejor!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON CONECTORES DE ORDEN:")
    for e in ejemplos:
        print(f"\n📝 {e}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 ORDENA LAS ACCIONES Y AGREGA LOS CONECTORES: primero, luego, después, al final.")
    seleccion = random.sample(ejercicios, 5)
    for i, grupo in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Acciones desordenadas:")
        random.shuffle(grupo)
        for act in grupo:
            print(f"• {act}")
        oracion = input("👉 Escribe tu secuencia completa con conectores: ").strip()
        if any(con in oracion.lower() for con in ["primero", "luego", "después", "al final"]):
            print(random.choice(elogios))
        else:
            print("⚠️ Recuerda usar los conectores para dar orden a la historia.")

# ✍️ Escribir secuencias propias
def escribir_propias():
    print("\n✍️ ESCRIBE 5 HISTORIAS CORTAS CON ORDEN: usa 'primero', 'luego', 'después', 'al final'.")
    propias = []
    for i in range(1, 6):
        secuencia = input(f"👉 Historia {i}: ").strip()
        propias.append(secuencia)

    print("\n📘 Tus historias ordenadas:")
    for idx, s in enumerate(propias, 1):
        print(f"{idx}. {s}")
    print("🏅 ¡Bien hecho! Tus ideas tienen principio, medio y final.")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 3.º Grado – Lección 7: Conectores de Orden")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir 5 historias propias ✍️")
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
            print("👋 ¡Gracias por organizar tus ideas con claridad y orden!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar el programa
if __name__ == "__main__":
    menu()
