import random

teoria = """
📘 LECCIÓN 5 – VERBOS EN FUTURO

Un verbo en futuro muestra una acción que ocurrirá más adelante. 
Nos ayuda a hablar de lo que aún no ha pasado.

🎯 Ejemplos:
- Yo correré mañana. → Verbo: correré
- Ellos viajarán en vacaciones. → Verbo: viajarán
- Tú pintarás un dibujo. → Verbo: pintarás

Formas frecuentes: -é, -ás, -á, -emos, -án
"""

ejemplos = [
    {"oracion": "Mañana visitaré a mi abuela.", "verbo": "visitaré"},
    {"oracion": "Luis jugará con su pelota.", "verbo": "jugará"},
    {"oracion": "Nosotros comeremos helado.", "verbo": "comeremos"},
    {"oracion": "Ellas leerán un cuento divertido.", "verbo": "leerán"},
    {"oracion": "Tú ayudarás en la cocina.", "verbo": "ayudarás"}
]

ejercicios = [
    {"oracion": "Papá cocinará una pizza.", "verbo": "cocinará"},
    {"oracion": "Mis amigos vendrán a jugar.", "verbo": "vendrán"},
    {"oracion": "Yo escribiré una historia.", "verbo": "escribiré"},
    {"oracion": "Tú estudiarás para el examen.", "verbo": "estudiarás"},
    {"oracion": "Ellos pasearán por el parque.", "verbo": "pasearán"},
    {"oracion": "María pintará su dibujo.", "verbo": "pintará"},
    {"oracion": "Nosotros leeremos un cuento.", "verbo": "leeremos"},
    {"oracion": "El perro jugará con su pelota.", "verbo": "jugará"},
    {"oracion": "Mañana saldré temprano.", "verbo": "saldré"},
    {"oracion": "Ustedes traerán los materiales.", "verbo": "traerán"},
    {"oracion": "Carlos cantará en la fiesta.", "verbo": "cantará"},
    {"oracion": "Ellas bailarán en el salón.", "verbo": "bailarán"},
    {"oracion": "Mi hermana ordenará sus libros.", "verbo": "ordenará"},
    {"oracion": "Nosotros iremos al zoológico.", "verbo": "iremos"},
    {"oracion": "El gato dormirá en su cama.", "verbo": "dormirá"},
    {"oracion": "Yo dibujaré animales.", "verbo": "dibujaré"},
    {"oracion": "Mañana veremos una película.", "verbo": "veremos"},
    {"oracion": "Tú prepararás la mochila.", "verbo": "prepararás"},
    {"oracion": "Mi prima responderá el mensaje.", "verbo": "responderá"},
    {"oracion": "Ellos construirán una torre.", "verbo": "construirán"}
]

elogios = [
    "🎉 ¡Muy bien!",
    "🧠 ¡Detectaste el verbo en futuro!",
    "🌈 ¡Excelente!",
    "👏 ¡Respuesta correcta!",
    "⭐ ¡Genial análisis!"
]

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS RESUELTOS:")
    for ej in ejemplos:
        print(f"🔹 Oración: {ej['oracion']}")
        print(f"👉 Verbo en futuro: {ej['verbo']}\n")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Oración: {ej['oracion']}")
        respuesta = input("👉 ¿Cuál es el verbo en futuro?: ").strip().lower()
        if respuesta == ej["verbo"]:
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Era: '{ej['verbo']}'.")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia obtenida: Maestro del Futuro! 🚀")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIOS EJEMPLOS")
    print("Escribe 20 oraciones con verbos en futuro (ej. 'Yo correré mañana.'):\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Ejemplo {i}: ").strip()
        personales.append(frase)

    print("\n📘 Tus ejemplos creados:")
    for idx, f in enumerate(personales, 1):
        print(f"{idx}. {f}")
    print("🏅 ¡Excelente trabajo creativo!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 2.º Primaria – Lección 5")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir 20 ejemplos propios ✍️")
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
            print("👋 ¡Gracias por explorar el futuro de las palabras!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
