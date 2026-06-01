import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO UNIMOS IDEAS CON SENTIDO?

Usamos conectores para unir oraciones y mostrar relación entre ideas:

🔹 De causa → porque, ya que
🔹 De consecuencia → por eso, entonces
🔹 De contraste → aunque, sin embargo
🔹 De simultaneidad → mientras
🔹 De adición → además, también

🎯 Ejemplo:
"Estudia mucho, porque quiere aprender."
"Estaba cansado, pero terminó la tarea."
"Salió el sol, entonces fuimos al parque."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La lluvia era fuerte, por eso no salimos.",
    "Juan juega fútbol, mientras su hermana pinta.",
    "Está nerviosa, aunque ya practicó mucho.",
    "Le gusta la ciencia, además le encanta la lectura.",
    "No tenía hambre, pero comió un poco."
]

# 📝 20 pares de oraciones separadas
ejercicios = [
    ("Mi primo corre rápido.", "Quiere ganar la carrera."),
    ("Está lloviendo mucho.", "La calle está mojada."),
    ("Lucía estudió poco.", "Sacó mala nota."),
    ("Carlos está feliz.", "Ganó el concurso."),
    ("Me gusta el helado.", "Me encanta el chocolate."),
    ("Salí temprano.", "No llegué tarde."),
    ("El perro ladra.", "Hay alguien en la puerta."),
    ("Estaba cansado.", "No quiso dormir."),
    ("El gato duerme.", "El perro juega."),
    ("María no estudió.", "Pasó el examen."),
    ("Luis no tenía dinero.", "No compró nada."),
    ("Ella canta bien.", "También toca el piano."),
    ("Llovía mucho.", "El río creció."),
    ("Luis llegó tarde.", "Le dieron permiso."),
    ("Los niños pintan.", "La maestra los observa."),
    ("La comida estaba fría.", "La calentamos en el horno."),
    ("Mi hermana prepara la torta.", "Yo limpio la cocina."),
    ("No hizo la tarea.", "Tenía fiebre."),
    ("Pedro sabe mucho.", "Ayuda a sus amigos."),
    ("Fui a la tienda.", "Compré pan y leche."),
]

elogios = [
    "🌟 ¡Conector bien usado!",
    "✅ ¡Muy clara la relación de ideas!",
    "👏 ¡Buen trabajo conectando frases!",
    "🧠 ¡La oración tiene lógica y fluidez!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ORACIONES CON CONECTORES:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Práctica de ejercicios
def practicar_conectores():
    print("\n📝 UNE LAS DOS ORACIONES CON UN CONECTOR ADECUADO:")
    total = 0
    for i, (oracion1, oracion2) in enumerate(ejercicios, 1):
        print(f"\n{str(i).zfill(2)}. Parte 1: {oracion1}")
        print(f"     Parte 2: {oracion2}")
        respuesta = input("👉 Escribe la oración unida: ").strip().lower()
        puntos = 0
        conectores = ["porque", "por eso", "aunque", "entonces", "ya que", "sin embargo", "además", "también", "mientras"]
        if any(c in respuesta for c in conectores):
            puntos += 1
        if len(respuesta.split()) >= 8:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje final: {total}/60")
    if total >= 50:
        print("🏅 ¡Excelente dominio de conectores!")
    elif total >= 35:
        print("👍 Buen nivel. Puedes mejorar la variedad y estructura.")
    else:
        print("📘 Practica más el uso de conectores y sentido lógico.")

# ✍️ Crear oraciones propias
def crear_conectores():
    print("\n✍️ ESCRIBE 3 ORACIONES CONECTADAS CON DISTINTOS CONECTORES:")
    total = 0
    for i in range(1, 4):
        oracion = input(f"📝 Oración {i}: ").strip().lower()
        puntos = sum(1 for c in ["porque", "por eso", "aunque", "además", "mientras", "entonces"] if c in oracion)
        puntos = min(puntos, 3)
        print(f"🎯 Puntos: {puntos}/3")
        total += puntos
    print(f"\n📊 Puntaje creativo: {total}/9")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 5.º Grado – Lección 8: Conectores lógicos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 frases con conectores 📝")
        print("4. Escribir tus propias oraciones ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_conectores()
        elif opcion == "4":
            crear_conectores()
        elif opcion == "5":
            print("👋 ¡Gracias por conectar tus ideas con lógica y estilo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
