import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO RESPONDEMOS CON CRITERIO A IDEAS QUE NO SON NUESTRAS?

En un texto argumentativo avanzado, se puede:

1️⃣ Escuchar una postura ajena  
2️⃣ Identificar qué partes compartimos y cuáles no  
3️⃣ Responder con respeto, argumentos y claridad

🎯 Tipos de respuesta crítica:
• Acuerdo parcial → "Coincido en parte con..."  
• Matiz → "Si bien es cierto que..., también debemos considerar..."  
• Réplica razonada → "Aunque respeto esa postura, pienso que..."

✅ Esto no busca ganar, sino **pensar con criterio**.
"""

# 📚 Posturas ajenas para evaluar
posturas = [
    "Los celulares deberían prohibirse en clase porque generan distracción.",
    "Los estudiantes no deberían participar en decisiones escolares, porque aún no tienen suficiente criterio.",
    "El arte no es tan importante como las ciencias en el currículo escolar.",
    "Los exámenes son la mejor forma de evaluar el aprendizaje.",
    "La filosofía es inútil para la vida cotidiana.",
    "Las redes sociales solo generan superficialidad en los jóvenes.",
    "No es necesario enseñar a escribir bien, basta con usar mensajes cortos.",
    "La escuela no necesita cambiar, ha funcionado así por años.",
    "Los adolescentes no saben trabajar en grupo porque se distraen.",
    "Los debates escolares causan discusiones innecesarias."
]

# 🧠 Conectores útiles
conectores_acuerdo = ["Coincido parcialmente", "Es cierto que", "Si bien", "Estoy de acuerdo en parte"]
conectores_respuesta = ["Sin embargo", "También debemos considerar", "Por eso", "No podemos olvidar que"]

elogios = [
    "🌟 ¡Tu respuesta muestra criterio y respeto!",
    "✅ ¡Buen manejo de la postura ajena!",
    "👏 ¡Tu matiz está bien expresado!",
    "🧠 ¡Pensamiento crítico y diálogo argumentativo!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplo guiado
def mostrar_ejemplos():
    print("\n📚 EJEMPLO DE RESPUESTA CON CRITERIO:")
    print("Postura ajena: 'Los celulares deberían prohibirse en clase porque generan distracción.'")
    print("Tu respuesta: 'Es cierto que pueden distraer, pero también pueden ser herramientas educativas si se usan con normas claras.'")

# 📝 Evaluar posturas
def practicar_respuesta():
    print("\n📝 RESPONDE A CADA POSTURA CON UN MATIZ, UN ACUERDO PARCIAL O UNA RÉPLICA RAZONADA:")
    total = 0
    for i, postura in enumerate(posturas, 1):
        print(f"\n{str(i).zfill(2)}. Postura ajena:\n🗣️ {postura}")
        respuesta = input("👉 Tu respuesta crítica: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in conectores_acuerdo):
            puntos += 1
        if any(c in respuesta for c in conectores_respuesta):
            puntos += 1
        if len(respuesta.split()) >= 12:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/30")

# ✍️ Composición libre
def redactar_libre():
    print("\n✍️ ESCRIBE UNA RÉPLICA CRÍTICA A UNA POSTURA QUE ELIJAS:")
    postura = input("🗣️ ¿Cuál es la postura ajena?: ").strip()
    respuesta = input("👉 Tu respuesta crítica: ").strip().lower()
    puntos = 0
    if any(c in respuesta for c in conectores_acuerdo + conectores_respuesta):
        puntos += 1
    if len(respuesta.split()) >= 20:
        puntos += 1
    if "." in respuesta and "," in respuesta:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu respuesta muestra madurez y diálogo argumentativo!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes afinar el matiz o agregar argumentos más claros.")
    else:
        print("📘 Intenta combinar respeto y firmeza en tu postura personal.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Grado – Lección 9: Evaluación de postura ajena")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplo guiado 📚")
        print("3. Practicar con 10 posturas 📝")
        print("4. Redactar tu propia réplica crítica ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_respuesta()
        elif opcion == "4":
            redactar_libre()
        elif opcion == "5":
            print("👋 ¡Gracias por pensar, responder y escribir con respeto y criterio!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
