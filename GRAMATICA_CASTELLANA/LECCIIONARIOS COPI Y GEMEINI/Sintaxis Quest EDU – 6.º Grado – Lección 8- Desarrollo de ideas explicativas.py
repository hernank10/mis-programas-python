import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO EXPLICAMOS MEJOR UNA IDEA EN UN TEXTO?

Cuando escribimos una opinión, podemos desarrollarla así:

🔹 Causa → ¿Por qué ocurre?
    Ejemplo: "Los estudiantes deben reciclar, porque ayuda al planeta."
🔹 Ejemplo → ¿Cuándo ocurre eso?
    Ejemplo: "Muchos niños separan papel y plástico cada semana."
🔹 Definición → ¿Qué significa eso?
    Ejemplo: "Reciclar es usar lo viejo para hacer algo nuevo."
🔹 Comparación → ¿En qué se parece o se diferencia?
    Ejemplo: "Reciclar es mejor que tirar todo a la basura."

✅ Un párrafo argumentativo puede usar una o varias formas para explicar bien una idea.
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La lectura es importante. Por ejemplo, al leer mejoramos vocabulario y comprensión.",
    "Estudiar ciencias nos ayuda. Es decir, entendemos cómo funciona el mundo y la naturaleza.",
    "La educación virtual tiene ventajas. En cambio, la presencial permite más interacción directa.",
    "Tener una mascota es bueno, porque enseñan responsabilidad y cariño.",
]

# 📝 20 frases base para desarrollar
frases_base = [
    "Los niños deben practicar deporte.",
    "Aprender matemáticas es útil.",
    "La música mejora el ánimo.",
    "Los libros enseñan muchas cosas.",
    "Estudiar historia es importante.",
    "Los deberes ayudan a aprender.",
    "Los museos son espacios educativos.",
    "Escribir es una forma de pensar.",
    "Comer frutas es saludable.",
    "Las artes plásticas desarrollan la creatividad.",
    "El trabajo en equipo tiene beneficios.",
    "Aprender otro idioma abre oportunidades.",
    "Las normas escolares enseñan disciplina.",
    "Tener rutinas mejora el día.",
    "Ver documentales aumenta el conocimiento.",
    "La lectura crítica nos hace reflexivos.",
    "Hacer experimentos es divertido y educativo.",
    "Resolver problemas fortalece la mente.",
    "La poesía expresa emociones profundas.",
    "Debatir ideas fomenta el respeto.",
]

elogios = [
    "🌟 ¡Explicación clara y bien construida!",
    "✅ ¡Buen desarrollo argumentativo!",
    "👏 ¡Tu párrafo tiene profundidad!",
    "🧠 ¡Excelente forma de ampliar la idea!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE DESARROLLO EXPLICATIVO:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Ejercicios prácticos
def practicar_desarrollo():
    print("\n📝 DESARROLLA CADA IDEA CON UNA EXPLICACIÓN:")
    total = 0
    for i, frase in enumerate(frases_base, 1):
        print(f"\n{str(i).zfill(2)}. Tesis base: {frase}")
        respuesta = input("👉 Tu desarrollo explicativo: ").strip().lower()
        puntos = 0
        if any(p in respuesta for p in ["porque", "por ejemplo", "es decir", "en cambio", "en comparación", "ya que", "como muestra"]):
            puntos += 1
        if len(respuesta.split()) >= 10:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/60")
    if total >= 50:
        print("🏅 ¡Gran dominio de la explicación argumentativa!")
    elif total >= 35:
        print("👍 Buen intento. Puedes ampliar aún más tus ideas.")
    else:
        print("📘 Practica más cómo explicar con lógica y claridad.")

# ✍️ Desarrollo múltiple
def desarrollo_multiple():
    print("\n✍️ ELIGE UNA IDEA Y DESARRÓLLALA CON TRES FORMAS:")
    idea = input("📝 Escribe tu tesis (una frase): ").strip()
    causa = input("👉 Explica con una causa: ").strip()
    ejemplo = input("👉 Explica con un ejemplo: ").strip()
    comparación = input("👉 Explica con una comparación: ").strip()
    puntos = 0
    if len(causa.split()) >= 8:
        puntos += 1
    if len(ejemplo.split()) >= 8:
        puntos += 1
    if len(comparación.split()) >= 8:
        puntos += 1
    print(f"\n🎯 Puntaje total: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Excelente desarrollo con distintos enfoques!")
    elif puntos == 2:
        print("✅ Buen trabajo. Puedes mejorar un poco la profundidad.")
    else:
        print("📘 Intenta dar más detalle o variedad en tus explicaciones.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 6.º Grado – Lección 8: Desarrollo de ideas explicativas")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 frases 📝")
        print("4. Crear desarrollo múltiple ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_desarrollo()
        elif opcion == "4":
            desarrollo_multiple()
        elif opcion == "5":
            print("👋 ¡Gracias por explicar con profundidad y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
