import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 7 – ¿CÓMO CONECTAMOS NUESTRAS IDEAS?

Los conectores son palabras que ayudan a unir frases o partes de una oración.

🎯 Tipos de conectores simples:
- Aditivos: y, también
- De causa: porque
- De contraste: pero, aunque
- De consecuencia: entonces

💡 Ejemplo:
"Juan estudió mucho y pasó el examen."
"Me quedé en casa porque estaba lloviendo."
"Quería ir al parque, pero estaba cerrado."
"Jugamos todo el día, entonces estábamos cansados."
"""

# 📚 Ejemplos guiados
ejemplos = [
    {"frase": "Quiero comer helado ___ tengo hambre.", "sugerido": "porque"},
    {"frase": "Fuimos al cine ___ vimos una película divertida.", "sugerido": "y"},
    {"frase": "Estaba cansado ___ terminó su tarea.", "sugerido": "pero"},
    {"frase": "Le dolía la cabeza, ___ no fue al colegio.", "sugerido": "entonces"},
    {"frase": "Pedro estudia mucho ___ quiere sacar buenas notas.", "sugerido": "porque"}
]

# 📝 20 frases incompletas para practicar
ejercicios = [
    {"frase": "Me levanté temprano ___ preparé el desayuno.", "conector": "y"},
    {"frase": "No jugué al fútbol ___ estaba lloviendo.", "conector": "porque"},
    {"frase": "María quiere salir ___ no tiene permiso.", "conector": "pero"},
    {"frase": "Llovió toda la tarde, ___ no fuimos al parque.", "conector": "entonces"},
    {"frase": "Estudié todo el día ___ mañana tengo examen.", "conector": "porque"},
    {"frase": "Fui a la tienda ___ compré pan.", "conector": "y"},
    {"frase": "José es simpático ___ tímido.", "conector": "pero"},
    {"frase": "Estábamos cansados ___ seguimos jugando.", "conector": "pero"},
    {"frase": "Me gusta correr ___ andar en bicicleta.", "conector": "y"},
    {"frase": "No entendí la tarea ___ estaba difícil.", "conector": "porque"}
]

elogios = [
    "🎉 ¡Conector bien elegido!",
    "🧠 ¡Tus ideas están conectadas!",
    "✅ ¡Buena unión entre frases!",
    "👏 ¡Muy bien, eso tiene sentido!",
    "🌟 ¡Construcción clara y lógica!"
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON CONECTORES:")
    for ej in ejemplos:
        print(f"📝 {ej['frase']} → Sugerido: '{ej['sugerido']}'")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 COMPLETA LA FRASE CON EL CONECTOR CORRECTO:")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. {ej['frase'].replace('___', '_____')}")
        respuesta = input("👉 Escribe el conector: ").strip().lower()
        if respuesta == ej['conector']:
            print(random.choice(elogios))
        else:
            print(f"⚠️ El conector esperado era: '{ej['conector']}'")

# ✍️ Crear oraciones propias
def escribir_propias():
    print("\n✍️ ESCRIBE 5 PARES DE IDEAS CONECTADAS CON UNA PALABRA:")
    propias = []
    for i in range(1, 6):
        frase1 = input(f"👉 Idea 1 ({i}): ").strip()
        conector = input("🔗 Conector que las une: ").strip()
        frase2 = input("👉 Idea 2: ").strip()
        oracion = f"{frase1} {conector} {frase2}"
        propias.append(oracion)

    print("\n📘 Tus oraciones completas:")
    for idx, o in enumerate(propias, 1):
        print(f"{idx}. {o}")
    print("🏅 ¡Excelente trabajo conectando ideas!")

# 🎮 Menú interactivo
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 5.º Grado – Lección 7: Conectores Simples")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir frases propias ✍️")
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
            print("👋 ¡Gracias por unir tus ideas con claridad y lógica!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
