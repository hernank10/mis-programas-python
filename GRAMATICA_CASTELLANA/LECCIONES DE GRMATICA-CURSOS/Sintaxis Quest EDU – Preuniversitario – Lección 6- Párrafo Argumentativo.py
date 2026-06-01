import random

# 📘 TEORÍA
teoria = """
📘 LECCIÓN 6 – PÁRRAFO ARGUMENTATIVO COMPLETO

Un párrafo argumentativo bien construido tiene tres partes esenciales:

1. 💡 Idea principal (Tesis):
   - Es la postura clara del autor sobre un tema.

2. 📚 Desarrollo lógico:
   - Incluye razones, datos, ejemplos, conectores y explicaciones.

3. 🎯 Cierre reflexivo:
   - Refuerza la postura o invita a seguir reflexionando.

🎯 Ejemplo:
   "La lectura crítica debe enseñarse desde temprana edad, ya que permite que los estudiantes distingan entre hechos y opiniones.
   A través del análisis textual, aprenden a identificar falacias y sesgos ideológicos.
   Esta habilidad no solo fortalece el pensamiento autónomo, sino que también prepara para la participación activa en la sociedad."
"""

# 📚 EJEMPLOS ANOTADOS
ejemplos = [
    {
        "titulo": "La importancia de la puntualidad",
        "idea": "La puntualidad es una virtud que debe cultivarse en los jóvenes.",
        "desarrollo": "Ser puntual demuestra respeto hacia el tiempo de los demás y fomenta la responsabilidad personal. Además, en contextos académicos o laborales, llegar a tiempo puede marcar la diferencia en la percepción que otros tienen de nosotros.",
        "cierre": "Por tanto, incentivar la puntualidad desde la escuela contribuye a formar ciudadanos comprometidos."
    },
    {
        "titulo": "La educación ambiental en el aula",
        "idea": "Incluir la educación ambiental en el currículo escolar es urgente.",
        "desarrollo": "El cambio climático y la pérdida de biodiversidad exigen que las nuevas generaciones desarrollen conciencia ecológica. Si los estudiantes aprenden a respetar el entorno desde temprana edad, es más probable que adopten prácticas sostenibles.",
        "cierre": "Así, el aula se convierte en un semillero para el futuro verde del planeta."
    }
]

# 📝 20 EJERCICIOS (con partes incompletas)
ejercicios = [
    {
        "titulo": "Tecnología y aprendizaje",
        "idea": "El uso de tecnología en el aula transforma la forma de aprender.",
        "desarrollo": "",
        "cierre": ""
    },
    {
        "titulo": "La lectura como hábito",
        "idea": "",
        "desarrollo": "Leer permite ampliar el vocabulario, mejorar la escritura y estimular la imaginación. Además, facilita la comprensión de textos complejos.",
        "cierre": ""
    },
    {
        "titulo": "Trabajo colaborativo",
        "idea": "",
        "desarrollo": "",
        "cierre": "Esto demuestra que aprender junto a otros fortalece habilidades sociales y académicas."
    }
]

# ✍️ Bloque de creación libre
parrafos_personales = []

# 💾 Guardar en consola
def guardar_parrafos():
    print("\n📘 Tus 10 párrafos redactados:")
    for idx, p in enumerate(parrafos_personales, 1):
        print(f"\n📝 Párrafo {idx}: {p}")
    print("✅ Fin del volcado de párrafos en consola. Puedes copiar y reutilizar.")

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos explicados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS ANOTADOS:")
    for ej in ejemplos:
        print(f"\n🔸 {ej['titulo']}")
        print(f"👉 Idea principal: {ej['idea']}")
        print(f"👉 Desarrollo: {ej['desarrollo']}")
        print(f"👉 Cierre: {ej['cierre']}")

# 📝 Practicar ejercicios
def practicar_ejercicios():
    print("\n📝 EJERCICIOS (completa lo que falta):")
    seleccion = random.sample(ejercicios, 5)
    for i, ej in enumerate(seleccion, 1):
        print(f"\n📄 Título: {ej['titulo']}")
        if not ej['idea']:
            ej['idea'] = input("👉 Escribe la idea principal: ").strip()
        if not ej['desarrollo']:
            ej['desarrollo'] = input("👉 Escribe el desarrollo del párrafo: ").strip()
        if not ej['cierre']:
            ej['cierre'] = input("👉 Escribe el cierre reflexivo: ").strip()
        print("\n✅ Párrafo completo:")
        print(f"{ej['idea']} {ej['desarrollo']} {ej['cierre']}")

# ✍️ Crear 10 párrafos completos
def redactar_parrafos():
    print("\n✍️ REDACTA 10 PÁRRAFOS COMPLETOS:")
    for i in range(1, 11):
        print(f"\n📝 Párrafo {i}")
        idea = input("👉 Idea principal: ").strip()
        desarrollo = input("👉 Desarrollo lógico: ").strip()
        cierre = input("👉 Cierre reflexivo: ").strip()
        parrafo = f"{idea} {desarrollo} {cierre}"
        parrafos_personales.append(parrafo)

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – Preuniversitario – Lección 6: Párrafo Argumentativo")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos anotados 📚")
        print("3. Completar ejercicios incompletos 📝")
        print("4. Redactar 10 párrafos propios ✍️")
        print("5. Guardar párrafos en consola 💾")
        print("6. Salir 👋")
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_ejercicios()
        elif opcion == "4":
            redactar_parrafos()
        elif opcion == "5":
            guardar_parrafos()
        elif opcion == "6":
            print("👋 ¡Gracias por construir ideas con estructura y propósito!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# Ejecutar
if __name__ == "__main__":
    menu()
