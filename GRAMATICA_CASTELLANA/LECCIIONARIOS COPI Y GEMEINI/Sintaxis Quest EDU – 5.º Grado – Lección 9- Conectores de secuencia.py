import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO ORGANIZAMOS LO QUE PASA CUANDO ESCRIBIMOS?

Usamos conectores de secuencia para decir qué pasó primero, después, al final.

🔹 Primero → comienza algo
🔹 Después / Luego → sigue otra cosa
🔹 Entonces → ocurre una consecuencia
🔹 Cuando → marca un momento
🔹 Al final → cierra la secuencia

🎯 Escribir con orden ayuda a que otros nos entiendan mejor.
"""

# 📚 Ejemplos guiados
ejemplos = [
    "Primero desperté, después me duché, y entonces desayuné con mi familia.",
    "Cuando llegamos al parque, corrimos hacia los columpios.",
    "Luego de almorzar, jugamos cartas. Al final, vimos una película juntos.",
    "Mi perro se escapó cuando abrí la puerta. Entonces corrí tras él por la calle.",
    "Primero hicimos el cartel, luego decoramos la mesa, y al final recibimos a los invitados."
]

# 📝 Frases base para ordenar con conectores
acciones_base = [
    ["desayuné", "me vestí", "me desperté"],
    ["vi la película", "compramos palomitas", "entramos al cine"],
    ["empezó a llover", "corrimos al refugio", "jugábamos en el parque"],
    ["fuimos a casa", "salimos del colegio", "esperamos en la entrada"],
    ["me lavé las manos", "comí pizza", "me senté a la mesa"]
]

# ✍️ Retroalimentación motivadora
elogios = [
    "🎉 ¡Buena secuencia temporal!",
    "✅ ¡Tus acciones tienen orden y sentido!",
    "🧠 ¡Usaste bien los conectores!",
    "👏 ¡Tu narración fluye con claridad!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE CONECTORES EN USO:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Ordenar acciones con conectores
def practicar_conectores():
    print("\n📝 ORDENA LAS ACCIONES USANDO CONECTORES:")
    total = 0
    for i, grupo in enumerate(acciones_base, 1):
        print(f"\n{str(i).zfill(2)}. Acciones: {', '.join(grupo)}")
        respuesta = input("👉 Escribe tu versión con conectores: ").strip().lower()
        puntos = 0
        if any(c in respuesta for c in ["primero", "después", "luego", "entonces", "cuando", "al final"]):
            puntos += 1
        if len(respuesta.split()) >= 10:
            puntos += 1
        if "." in respuesta or "," in respuesta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total de puntos: {total}/15")

# ✍️ Narración libre con conectores
def crear_narracion():
    print("\n✍️ ESCRIBE UNA HISTORIA CORTA CON 3 CONECTORES DIFERENTES:")
    texto = input("📝 Tu narración: ").strip().lower()
    conectores_usados = [c for c in ["primero", "después", "entonces", "cuando", "al final"] if c in texto]
    puntos = 0
    if len(conectores_usados) >= 3:
        puntos += 1
    if len(texto.split()) >= 30:
        puntos += 1
    if "." in texto and "," in texto:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu narración tiene ritmo, orden y sentido!")
    elif puntos == 2:
        print("✅ Buen comienzo. Puedes agregar más conectores o detalles.")
    else:
        print("📘 Practica cómo dar orden a lo que cuentas.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 5.º Grado – Lección 9: Conectores de secuencia")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar orden de acciones 📝")
        print("4. Escribir tu historia ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_conectores()
        elif opcion == "4":
            crear_narracion()
        elif opcion == "5":
            print("👋 ¡Gracias por escribir con claridad y tiempo lógico!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
