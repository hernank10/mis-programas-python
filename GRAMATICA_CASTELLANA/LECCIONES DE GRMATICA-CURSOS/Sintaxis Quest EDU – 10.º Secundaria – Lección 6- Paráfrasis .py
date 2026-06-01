import random

# 📘 TEORÍA
teoria = """
📘 LECCIÓN 6 – PARÁFRASIS ARGUMENTATIVA

Una paráfrasis consiste en decir lo mismo con palabras distintas, manteniendo la idea original pero usando nueva estructura.

🔹 TIPOS DE REFORMULACIÓN:
1. Lexical → cambiar palabras sin alterar el sentido
   Ej.: "Los jóvenes deben cuidar el planeta."
         → "Los adolescentes tienen que proteger la Tierra."

2. Sintáctica → cambiar el orden o el tipo de estructura
   Ej.: "La lectura diaria mejora la comprensión."
         → "Comprender mejor es un efecto de leer todos los días."

3. Argumentativa → expresar la idea original desde una opinión propia, reforzando o matizando
   Ej.: "Aunque muchos creen que es aburrido, leer fortalece el pensamiento crítico."
"""

# 📚 EJEMPLOS EXPLICADOS
ejemplos = [
    {
        "original": "El deporte favorece la salud física.",
        "lexical": "La actividad deportiva mejora el bienestar corporal.",
        "sintactica": "Mejorar la salud física es posible mediante el deporte.",
        "argumentativa": "Aunque algunos lo ven como ocio, el deporte fortalece el cuerpo y previene enfermedades."
    },
    {
        "original": "La música influye en nuestras emociones.",
        "lexical": "Las melodías afectan cómo nos sentimos.",
        "sintactica": "Sentir distintas emociones puede depender del tipo de música que escuchamos.",
        "argumentativa": "Si se escucha con atención, la música puede moldear nuestro estado emocional."
    },
    {
        "original": "Estudiar ciencias desarrolla el pensamiento lógico.",
        "lexical": "Aprender materias científicas mejora la capacidad de razonar.",
        "sintactica": "Razonar con lógica es una habilidad que se potencia al estudiar ciencias.",
        "argumentativa": "Aunque muchos temen a la ciencia, su estudio fortalece el análisis racional."
    }
]

# 📝 20 EJERCICIOS
ejercicios = [
    {
        "original": "Leer cada día mejora la expresión escrita.",
        "parafrasis": "La lectura diaria ayuda a escribir mejor."
    },
    {
        "original": "Cuidar el medio ambiente es responsabilidad de todos.",
        "parafrasis": "Todos debemos proteger la naturaleza."
    },
    {
        "original": "Estudiar con amigos puede ser más dinámico.",
        "parafrasis": "Aprender en grupo puede resultar más entretenido."
    },
    {
        "original": "Las redes sociales influyen en cómo nos comunicamos.",
        "parafrasis": "La forma en que interactuamos está afectada por las plataformas digitales."
    },
    {
        "original": "Dormir bien mejora el rendimiento escolar.",
        "parafrasis": "El descanso adecuado beneficia el desempeño académico."
    },
    {
        "original": "Practicar arte potencia la creatividad.",
        "parafrasis": "El ejercicio artístico estimula el pensamiento original."
    },
    {
        "original": "Consumir frutas aporta vitaminas al cuerpo.",
        "parafrasis": "Las frutas suministran nutrientes esenciales al organismo."
    },
    {
        "original": "La lectura de novelas amplía el vocabulario.",
        "parafrasis": "Leer historias permite adquirir nuevas palabras."
    },
    {
        "original": "Estudiar en silencio mejora la concentración.",
        "parafrasis": "La tranquilidad favorece el enfoque durante el estudio."
    },
    {
        "original": "La educación es clave para el desarrollo social.",
        "parafrasis": "El progreso de la sociedad depende de una buena formación educativa."
    }
]

elogios = [
    "🌟 ¡Paráfrasis precisa!",
    "🧠 ¡Buena reformulación!",
    "👏 ¡Gran transformación sintáctica!",
    "⭐ ¡Excelente interpretación de sentido!",
    "🎯 ¡Fidelidad semántica lograda!"
]

# 📘 FUNCIONES

def mostrar_teoria():
    print(teoria)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS EXPLICADOS:")
    for e in ejemplos:
        print(f"\n🔹 Original: {e['original']}")
        print(f"🟢 Lexical: {e['lexical']}")
        print(f"🔵 Sintáctica: {e['sintactica']}")
        print(f🟣 Argumentativa: {e['argumentativa']}")

def practicar_ejercicios():
    print("\n📝 EJERCICIOS (10 al azar):")
    seleccion = random.sample(ejercicios, 10)
    aciertos = 0
    for i, ej in enumerate(seleccion, 1):
        print(f"\n{str(i).zfill(2)}. Frase original: {ej['original']}")
        respuesta = input("👉 Escribe una paráfrasis equivalente: ").strip().lower()
        if ej['parafrasis'].lower() in respuesta:
            print(random.choice(elogios))
            aciertos += 1
        else:
            print(f"😅 Una opción correcta sería: '{ej['parafrasis']}'")

    print(f"\n🎓 Resultados: {aciertos}/10")
    if aciertos >= 8:
        print("🏅 ¡Insignia ganada: Transformador del Pensamiento! 🔄")

def crear_ejemplos_usuario():
    print("\n✍️ CREA TUS PROPIAS PARÁFRASIS")
    print("Escribe 20 frases originales y luego parafrasea cada una:\n")
    personales = []
    for i in range(1, 21):
        frase = input(f"👉 Frase original {i}: ").strip()
        reformulada = input(f"🔄 Parafrasea {i}: ").strip()
        personales.append((frase, reformulada))

    print("\n📘 Tus paráfrasis creadas:")
    for idx, (f, r) in enumerate(personales, 1):
        print(f"{idx}. Original: {f}")
        print(f"    Reformulada: {r}")
    print("🏅 ¡Gran trabajo interpretativo!")

def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 10.º Secundaria – Lección 6: Paráfrasis y Reformulación")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos explicados 📚")
        print("3. Practicar ejercicios 📝")
        print("4. Escribir 20 paráfrasis propias ✍️")
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
            print("👋 ¡Gracias por transformar las ideas con estilo y sentido!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
