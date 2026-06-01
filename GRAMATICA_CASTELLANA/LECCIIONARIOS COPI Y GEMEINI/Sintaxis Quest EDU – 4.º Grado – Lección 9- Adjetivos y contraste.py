import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO DESCRIBIMOS Y COMPARAMOS CON ADJETIVOS?

Los adjetivos son palabras que describen algo. Podemos:

🔹 Usar varios adjetivos → "Mi perro es pequeño, cariñoso y juguetón."
🔸 Usar adjetivos opuestos → "La casa de Marta es grande, pero la mía es pequeña."

🎯 Describir es mirar con palabras. Comparar es usar contraste.
"""

# 📚 Ejemplos guiados
ejemplos = [
    "El autobús es grande, amarillo y ruidoso.",
    "La bicicleta de Pedro es ligera, azul y rápida.",
    "Mi habitación es pequeña, ordenada y silenciosa.",
    "El perro de Luisa es blanco, peludo y dormilón.",
    "Mi cuaderno es viejo, arrugado y descolorido."
]

# 📝 Frases base para agregar adjetivos
frases_describir = [
    "Mi mochila es",
    "El gato de mi abuela es",
    "La pelota de fútbol es",
    "Mi cuaderno es",
    "La montaña parece",
    "El helado sabe",
    "El coche de papá es",
    "La silla es",
    "Mi habitación se ve",
    "La luna está"
]

# 📝 Frases base para comparar con contraste
frases_contraste = [
    ("La casa de Luis es", "La casa de Ana es"),
    ("El parque del centro es", "El parque del barrio es"),
    ("Mi desayuno fue", "El desayuno de Juan fue"),
    ("El clima en Bogotá es", "El clima en Santa Marta es"),
    ("La ropa de invierno es", "La ropa de verano es"),
    ("Mi cuaderno está", "El de mi hermano está"),
    ("El gato de Marta es", "El mío es"),
    ("Su dibujo es", "El mío es"),
    ("La mochila nueva es", "La mochila vieja es"),
    ("Mi voz suena", "La de ella suena")
]

elogios = [
    "🌟 ¡Gran descripción con detalles!",
    "✅ ¡Los adjetivos hacen que tu frase brille!",
    "👏 ¡Buen contraste entre los dos objetos!",
    "🧠 ¡Estás describiendo como un escritor profesional!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE ADJETIVOS EN SERIE:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Describir con varios adjetivos
def practicar_descripcion():
    print("\n📝 AGREGA 2 O MÁS ADJETIVOS A CADA FRASE:")
    total = 0
    for i, base in enumerate(frases_describir, 1):
        print(f"\n{str(i).zfill(2)}. Frase base: {base}...")
        frase = input("👉 Tu frase completa: ").strip().lower()
        puntos = 0
        if "," in frase and len(frase.split()) >= 6:
            puntos += 2
        if any(op in frase for op in ["grande", "pequeño", "rápido", "lento", "viejo", "nuevo"]):
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje descriptivo: {total}/30")

# 📝 Comparar con contraste
def practicar_contraste():
    print("\n📝 ESCRIBE DOS FRASES USANDO ADJETIVOS OPUESTOS:")
    total = 0
    for i, (a, b) in enumerate(frases_contraste, 1):
        print(f"\n{str(i).zfill(2)}. Frase 1: {a}...")
        frase1 = input("👉 Completa frase 1: ").strip().lower()
        print(f"   Frase 2: {b}...")
        frase2 = input("👉 Completa frase 2: ").strip().lower()
        puntos = 0
        opuestos = [("grande", "pequeño"), ("rápido", "lento"), ("nuevo", "viejo"), ("ordenado", "desordenado")]
        for a, b in opuestos:
            if a in frase1 and b in frase2 or b in frase1 and a in frase2:
                puntos += 2
        if len(frase1.split()) >= 5 and len(frase2.split()) >= 5:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje comparativo: {total}/30")

# ✍️ Composición libre
def redactar_creativa():
    print("\n✍️ ESCRIBE UNA DESCRIPCIÓN DE 3 ORACIONES:")
    oraciones = []
    total = 0
    for i in range(1, 4):
        frase = input(f"📝 Oración {i}: ").strip().lower()
        puntos = 0
        if len(frase.split()) >= 6 and "," in frase:
            puntos += 1
        if any(adj in frase for adj in ["grande", "pequeño", "rápido", "lento", "nuevo", "viejo"]):
            puntos += 1
        if any(conj in frase for conj in ["pero", "aunque", "sin embargo"]):
            puntos += 1
        oraciones.append(frase)
        print(f"🎯 Puntos: {puntos}/3")
        total += puntos
    print(f"\n📊 Puntaje creativo: {total}/9")
    print("📝 Tu texto completo:")
    for f in oraciones:
        print(f"- {f.capitalize()}.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 4.º Grado – Lección 9: Adjetivos y contraste")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar descripción 📝")
        print("4. Practicar comparación ✍️")
        print("5. Crear tu propio texto ✍️")
        print("6. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_descripcion()
        elif opcion == "4":
            practicar_contraste()
        elif opcion == "5":
            redactar_creativa()
        elif opcion == "6":
            print("👋 ¡Gracias por describir con imaginación y precisión!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
