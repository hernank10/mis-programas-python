import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO REDACTAMOS UN TEXTO COMPLETO QUE SOSTENGA UNA IDEA?

Un buen texto argumentativo breve incluye:

1️⃣ Tesis → idea que se va a defender  
2️⃣ Desarrollo 1 → razón principal con ejemplo  
3️⃣ Desarrollo 2 → segunda razón con otro ejemplo  
4️⃣ Conclusión → reafirma la idea usando un conector final

🎯 Conectores útiles:
• Para comenzar: "En primer lugar", "Una razón importante es…"  
• Para sumar: "Además", "Otro motivo es…"  
• Para cerrar: "Por eso", "En conclusión", "Por lo tanto"
"""

# 📚 Ejemplos guiados
ejemplos = [
    {
        "tesis": "Los debates escolares ayudan a pensar mejor.",
        "des1": "En primer lugar, permiten que los alumnos escuchen ideas distintas y aprendan a respetarlas.",
        "des2": "Además, al tener que defender su opinión, desarrollan el pensamiento crítico.",
        "cierre": "Por eso, los debates deberían practicarse en muchas materias."
    },
    {
        "tesis": "Tener una mascota enseña responsabilidad.",
        "des1": "En primer lugar, cuidarlas implica atención diaria y compromiso.",
        "des2": "También ayuda a comprender emociones y a convivir con seres vivos.",
        "cierre": "Por lo tanto, tener una mascota es una buena experiencia educativa."
    },
    {
        "tesis": "Leer libros estimula la imaginación.",
        "des1": "Una razón importante es que al leer, el cerebro crea imágenes únicas.",
        "des2": "Además, los libros presentan mundos nuevos que el lector debe interpretar.",
        "cierre": "En conclusión, la lectura fortalece la creatividad."
    }
]

# 📝 Temas base
temas = [
    "Los videojuegos pueden enseñar estrategia.",
    "La educación física mejora la salud mental.",
    "Escribir ayuda a organizar los pensamientos.",
    "La música favorece la concentración en clase.",
    "Dibujar es una forma de expresar emociones.",
    "El trabajo en grupo enseña a respetar ideas.",
    "Las redes sociales deben usarse con responsabilidad.",
    "Tener horarios mejora la organización personal.",
    "La poesía puede servir para entender la vida.",
    "Participar en proyectos escolares desarrolla el compromiso."
]

elogios = [
    "🌟 ¡Tu texto tiene estructura completa!",
    "✅ ¡Tus conectores están bien usados!",
    "👏 ¡Tu tesis es clara y está bien sostenida!",
    "🧠 ¡Excelente forma de organizar tus ideas!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE TEXTOS COMPLETOS:")
    for ej in ejemplos:
        print(f"\n📝 Tesis: {ej['tesis']}\n{ej['des1']}\n{ej['des2']}\n{ej['cierre']}")

# 📝 Practicar con temas base
def practicar_textos():
    print("\n📝 REDACTA UN TEXTO CON ESTRUCTURA EN 4 PARTES:")
    total = 0
    for i, tema in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Tema: {tema}")
        tesis = input("👉 Tesis clara: ").strip()
        des1 = input("👉 Desarrollo 1 con conector: ").strip()
        des2 = input("👉 Desarrollo 2 con conector: ").strip()
        cierre = input("👉 Conclusión con conector final: ").strip()
        texto = f"{tesis} {des1} {des2} {cierre}"
        puntos = 0
        if any(c in des1.lower() for c in ["en primer lugar", "una razón", "un motivo"]):
            puntos += 1
        if any(c in des2.lower() for c in ["además", "también", "otro motivo"]):
            puntos += 1
        if any(c in cierre.lower() for c in ["por eso", "en conclusión", "por lo tanto"]):
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/30")

# ✍️ Redacción libre
def escribir_desde_cero():
    print("\n✍️ ESCRIBE TU TEXTO ARGUMENTATIVO COMPLETO:")
    tesis = input("📝 Tesis: ").strip()
    des1 = input("👉 Desarrollo 1: ").strip()
    des2 = input("👉 Desarrollo 2: ").strip()
    cierre = input("👉 Conclusión: ").strip()
    texto = f"{tesis} {des1} {des2} {cierre}"
    puntos = 0
    if len(texto.split()) >= 40:
        puntos += 1
    if any(c in des1.lower()+des2.lower() for c in ["además", "en primer lugar", "también"]):
        puntos += 1
    if any(c in cierre.lower() for c in ["por eso", "en conclusión", "por lo tanto"]):
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu texto está completo y argumentado con fuerza!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes reforzar tus conectores.")
    else:
        print("📘 Revisa cómo unir cada parte con claridad y sentido.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 7.º Grado – Lección 9: Redacción de texto corto estructurado")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar con 20 temas 📝")
        print("4. Escribir desde cero ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_textos()
        elif opcion == "4":
            escribir_desde_cero()
        elif opcion == "5":
            print("👋 ¡Gracias por construir ideas con orden, convicción y estilo!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
