import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿QUÉ PASA PRIMERO, LUEGO Y AL FINAL?

Una secuencia muestra acciones en orden usando conectores como:

🔸 primero
🔸 luego
🔸 después
🔸 por último

✅ Ejemplo:
"Primero me levanto, luego me baño, después desayuno y por último salgo."

Cada paso tiene una acción (verbo) y sigue un orden lógico.
"""

# 📚 Ejemplos guiados
ejemplos = [
    "Primero el niño abre la caja, luego saca los juguetes, después juega y por último guarda todo.",
    "Primero la abuela prepara la masa, luego la amasa, después la cocina y por último sirve las arepas.",
    "Primero me pongo los zapatos, luego tomo mi mochila, después saludo a mi mamá y por último voy al colegio.",
]

# 📝 20 ejercicios incompletos
ejercicios = [
    {"incompleta": "Primero me despierto, luego me baño, después ______ y por último voy a clase.", "ejemplo": "desayuno"},
    {"incompleta": "Primero llega el maestro, luego saluda, después ______ y por último empieza la clase.", "ejemplo": "escribe en la pizarra"},
    {"incompleta": "Primero los niños se alinean, luego entran al salón, después ______ y por último guardan sus cosas.", "ejemplo": "saludan al profesor"},
    {"incompleta": "Primero mamá va al mercado, luego compra frutas, después ______ y por último regresa a casa.", "ejemplo": "paga"},
    {"incompleta": "Primero el pájaro vuela bajo, luego sube al árbol, después ______ y por último canta.", "ejemplo": "se acomoda"},
    {"incompleta": "Primero el niño toma papel, luego lo dobla, después ______ y por último lo pinta.", "ejemplo": "recorta"},
    {"incompleta": "Primero la vaca sale del corral, luego camina, después ______ y por último regresa.", "ejemplo": "come pasto"},
    {"incompleta": "Primero el perro ladra, luego corre, después ______ y por último duerme.", "ejemplo": "juega"},
    {"incompleta": "Primero el sol aparece, luego brilla fuerte, después ______ y por último se oculta.", "ejemplo": "calienta la tierra"},
    {"incompleta": "Primero el niño llega a casa, luego come, después ______ y por último duerme.", "ejemplo": "hace tareas"},
    {"incompleta": "Primero la niña pinta, luego corta, después ______ y por último pega su dibujo.", "ejemplo": "arma su collage"},
    {"incompleta": "Primero el tren arranca, luego acelera, después ______ y por último se detiene.", "ejemplo": "cruza el puente"},
    {"incompleta": "Primero el gato mira la caja, luego se acerca, después ______ y por último duerme dentro.", "ejemplo": "se mete"},
    {"incompleta": "Primero pongo agua en la olla, luego la caliento, después ______ y por último cocino la pasta.", "ejemplo": "echo sal"},
    {"incompleta": "Primero veo la receta, luego busco los ingredientes, después ______ y por último preparo la comida.", "ejemplo": "lavo las verduras"},
    {"incompleta": "Primero el alumno lee la pregunta, luego piensa, después ______ y por último responde.", "ejemplo": "busca la idea"},
    {"incompleta": "Primero ella prende la luz, luego abre el cuaderno, después ______ y por último copia en su libreta.", "ejemplo": "lee el ejemplo"},
    {"incompleta": "Primero tomo la escoba, luego barro la cocina, después ______ y por último descanso.", "ejemplo": "saco la basura"},
    {"incompleta": "Primero llegamos al parque, luego corremos, después ______ y por último merendamos.", "ejemplo": "jugamos"},
    {"incompleta": "Primero el maestro explica, luego muestra ejemplos, después ______ y por último nos pone un reto.", "ejemplo": "responde dudas"},
]

elogios = [
    "🌟 ¡Tu secuencia está bien ordenada!",
    "✅ ¡Muy bien! Usaste una acción lógica.",
    "👏 ¡Tu frase tiene sentido completo!",
    "🧠 ¡Excelente conexión de pasos!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON SECUENCIA COMPLETA:")
    for ej in ejemplos:
        print(f"📝 {ej}")

# 📝 Practicar ejercicios
def practicar():
    print("\n📝 COMPLETA LA SECUENCIA CON UNA ACCIÓN:")
    total = 0
    for i, ej in enumerate(ejercicios, 1):
        print(f"\n{str(i).zfill(2)}. {ej['incompleta']}")
        respuesta = input("👉 ¿Qué falta?: ").strip().lower()
        puntos = 0
        if len(respuesta.split()) >= 2:
            puntos = 3
        elif len(respuesta.split()) == 1:
            puntos = 2
        else:
            puntos = 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total: {total}/60")
    if total >= 50:
        print("🏅 ¡Excelente! Tus acciones tienen orden y claridad.")
    elif total >= 35:
        print("👍 Buen intento. Puedes mejorar la conexión entre pasos.")
    else:
        print("📘 Practica cómo contar pasos en orden con verbos claros.")

# ✍️ Narración personal
def crear_historia():
    print("\n✍️ NARRA UNA HISTORIA CON 4 ACCIONES EN ORDEN:")
    total = 0
    historia = input("📝 Escribe: primero..., luego..., después..., por último...:\n").strip()
    if all(p in historia.lower() for p in ["primero", "luego", "después", "por último"]):
        puntos = 3 if len(historia.split()) >= 12 else 2
    else:
        puntos = 1
    print(f"\n🎯 Tu puntuación: {puntos}/3")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 2.º Grado – Lección 8: Orden de acciones")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 frases incompletas 📝")
        print("4. Escribir una mini historia ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar()
        elif opcion == "4":
            crear_historia()
        elif opcion == "5":
            print("👋 ¡Gracias por contar tus acciones con orden y claridad!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
