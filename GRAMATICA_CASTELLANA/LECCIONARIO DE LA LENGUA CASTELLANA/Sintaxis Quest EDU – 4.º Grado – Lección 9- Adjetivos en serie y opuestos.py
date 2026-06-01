import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO DESCRIBIMOS COMPARANDO?

🔹 Los adjetivos ayudan a decir cómo son las cosas.

🔸 Podemos usar varios juntos → adjetivos en serie:
Ejemplo: "El gato es pequeño, suave y dormilón."

🔸 También podemos usar adjetivos opuestos:
Ejemplo: "Mi casa es grande pero la de mi abuela es pequeña."

🔹 Algunos pares de adjetivos opuestos:
- grande / pequeño
- alegre / triste
- limpio / sucio
- rápido / lento
- nuevo / viejo
- amable / grosero
- fuerte / débil
- alto / bajo
"""

# 📚 Ejemplos guiados
ejemplos = [
    "El carro es nuevo, brillante y veloz.",
    "Mi hermana es amable, creativa y alegre.",
    "La montaña es alta pero el cerro es bajo.",
    "La sopa está caliente y deliciosa; el jugo está frío y ácido.",
]

# 📝 10 frases para expandir con adjetivos en serie
frases_serie = [
    "El caballo trota.",
    "La niña juega.",
    "Mi mochila está en el piso.",
    "El parque tiene árboles.",
    "Mi habitación está ordenada.",
    "El robot camina.",
    "La torta sabe bien.",
    "Mi amigo pinta.",
    "La maestra explica.",
    "El gato duerme.",
]

# 📝 10 pares para comparar con adjetivos opuestos
pares_comparar = [
    ("Mi casa", "Tu casa"),
    ("El perro de Juan", "El gato de Lucía"),
    ("La bicicleta", "El auto"),
    ("Mi cuaderno", "Tu libro"),
    ("El día", "La noche"),
    ("El pastel", "La ensalada"),
    ("Mi primo", "Tu prima"),
    ("Este pantalón", "Ese suéter"),
    ("El maestro", "El alumno"),
    ("La calle", "El sendero"),
]

elogios = [
    "🌟 ¡Buen contraste!",
    "✅ ¡Adjetivos claros y precisos!",
    "👏 ¡Muy bien comparado!",
    "🧠 ¡Oración rica en detalle!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Práctica: adjetivos en serie
def practicar_serie():
    print("\n📝 AGREGA 2 O MÁS ADJETIVOS A CADA FRASE:")
    total = 0
    for i, frase in enumerate(frases_serie, 1):
        print(f"\n{str(i).zfill(2)}. Frase base: {frase}")
        respuesta = input("👉 Tu versión con adjetivos: ").strip()
        puntos = 0
        if "," in respuesta:
            puntos += 1
        if len(respuesta.split()) >= 6:
            puntos += 1
        if any(adj in respuesta.lower() for adj in ["grande", "pequeño", "alegre", "triste", "nuevo", "viejo", "rápido", "lento", "limpio", "sucio", "amable", "grosero"]):
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total: {total}/30")

# 📝 Comparar con opuestos
def comparar_opuestos():
    print("\n📝 COMPARA LOS DOS ELEMENTOS USANDO ADJETIVOS OPUESTOS:")
    total = 0
    for i, (a, b) in enumerate(pares_comparar, 1):
        print(f"\n{str(i).zfill(2)}. Compara: {a} / {b}")
        respuesta = input("👉 Tu comparación: ").strip()
        puntos = 0
        if "pero" in respuesta or "aunque" in respuesta:
            puntos += 1
        if len(respuesta.split()) >= 8:
            puntos += 1
        if any(adj in respuesta.lower() for adj in ["grande", "pequeño", "alegre", "triste", "nuevo", "viejo", "rápido", "lento", "limpio", "sucio", "amable", "grosero", "fuerte", "débil", "alto", "bajo"]):
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total: {total}/30")

# ✍️ Creativo: descripción doble
def descripcion_doble():
    print("\n✍️ DESCRIBE A DOS PERSONAJES DIFERENTES:")
    print("📝 Usa al menos un adjetivo para cada uno y señala una diferencia.")
    respuesta = input("👉 Tu descripción: ").strip()
    cantidad = sum(1 for adj in ["grande", "pequeño", "alegre", "triste", "limpio", "sucio", "rápido", "lento", "amable", "grosero"] if adj in respuesta.lower())
    puntos = 3 if cantidad >= 3 else 2 if cantidad >= 2 else 1 if quantity >= 1 else 0
    print(f"🎯 Puntaje: {puntos}/3")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 4.º Grado – Lección 9: Adjetivos en serie y opuestos")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar frases con adjetivos en serie 📝")
        print("4. Comparar usando adjetivos opuestos 🧩")
        print("5. Escribir una descripción doble ✍️")
        print("6. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_serie()
        elif opcion == "4":
            comparar_opuestos()
        elif opcion == "5":
            descripcion_doble()
        elif opcion == "6":
            print("👋 ¡Gracias por describir con palabras llenas de color y contraste!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
