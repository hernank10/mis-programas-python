import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – Estructura del párrafo argumentativo completo

1️⃣ Tesis → La idea principal que defiende el texto  
2️⃣ Desarrollo → Razón, causa, ejemplo que la apoya  
3️⃣ Contraargumento → Opinión contraria expresada con respeto  
4️⃣ Refutación → Respuesta lógica para fortalecer tu postura

🎯 Ejemplo:
"Tener mascota enseña responsabilidad.
Algunos creen que es solo una carga.
Sin embargo, cuidar un animal forma rutinas, empatía y compromiso."
"""

# 🧠 Ejemplos guiados
ejemplos = [
    {
        "tesis": "Los adolescentes deben participar en decisiones escolares.",
        "desarrollo": "Así fortalecen su sentido de pertenencia y aprenden sobre democracia.",
        "contra": "Algunos opinan que no tienen suficiente madurez.",
        "refuta": "Sin embargo, con orientación pueden aportar ideas valiosas y aprender a dialogar."
    },
    {
        "tesis": "La poesía debe enseñarse como parte del currículo.",
        "desarrollo": "Permite expresar emociones y comprender el lenguaje figurado.",
        "contra": "Algunos creen que es difícil y poco útil.",
        "refuta": "No obstante, al explicarla con ejemplos cercanos, despierta sensibilidad y reflexión."
    }
]

# 🎯 Frases base para completar (20 temas)
temas = [
    {
        "tesis": "El trabajo en grupo mejora el aprendizaje.",
        "desarrollo": "Se desarrollan habilidades como comunicación, empatía y responsabilidad compartida.",
        "contra": "Algunos piensan que no todos trabajan igual.",
    },
    {
        "tesis": "Aprender otro idioma abre puertas.",
        "desarrollo": "Permite comunicarse con más personas y conocer otras culturas.",
        "contra": "Muchos creen que es difícil y no lo usarán nunca.",
    },
    {
        "tesis": "Las excursiones escolares enriquecen el conocimiento.",
        "desarrollo": "Conectan lo aprendido con experiencias reales fuera del aula.",
        "contra": "Hay quienes opinan que son costosas y no necesarias.",
    },
    {
        "tesis": "La lectura digital tiene el mismo valor que la impresa.",
        "desarrollo": "Facilita el acceso y permite personalizar la experiencia.",
        "contra": "Algunos creen que la pantalla distrae y no se reflexiona igual.",
    },
    {
        "tesis": "La educación artística desarrolla el pensamiento creativo.",
        "desarrollo": "Estimula la imaginación, la expresión personal y el análisis visual.",
        "contra": "Muchos dicen que no tiene aplicación profesional clara.",
    },
    {
        "tesis": "Estudiar filosofía en secundaria es valioso.",
        "desarrollo": "Ayuda a formular preguntas, argumentar y reflexionar.",
        "contra": "Algunos piensan que son conceptos abstractos difíciles.",
    },
    {
        "tesis": "El uso de tecnología en clase mejora la motivación.",
        "desarrollo": "Los recursos digitales permiten aprender de forma dinámica e interactiva.",
        "contra": "Hay quienes sostienen que los estudiantes se distraen más.",
    },
    {
        "tesis": "Escribir diarios personales fortalece la salud emocional.",
        "desarrollo": "Permite procesar lo vivido y reconocer emociones.",
        "contra": "Muchos creen que es una pérdida de tiempo o algo íntimo sin valor escolar.",
    },
    {
        "tesis": "Los adolescentes deberían tener espacios de debate escolar.",
        "desarrollo": "Aprenden a opinar, escuchar y respetar otras ideas.",
        "contra": "Algunos sostienen que el debate genera conflicto.",
    },
    {
        "tesis": "La educación ambiental debe ser transversal en todas las áreas.",
        "desarrollo": "Forma conciencia ecológica y conecta con realidades actuales.",
        "contra": "Algunos opinan que es tema de ciencias, no de todas las materias.",
    }
]

elogios = [
    "🌟 Tu refutación fortalece la idea.",
    "✅ Buena estructura lógica.",
    "👏 Tu párrafo se lee claro y completo.",
    "🧠 Excelente razonamiento y respeto al otro punto de vista.",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS DE PÁRRAFOS COMPLETOS:")
    for ej in ejemplos:
        print(f"📝 {ej['tesis']}\n{ej['desarrollo']}\n{ej['contra']}\n{ej['refuta']}\n")

# 📝 Práctica guiada con refutación
def practicar():
    print("\n📝 AGREGA UNA REFUTACIÓN LÓGICA:")
    total = 0
    for i, tema in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {tema['tesis']}")
        print(f"   Desarrollo: {tema['desarrollo']}")
        print(f"   Contraargumento: {tema['contra']}")
        refuta = input("👉 Tu refutación: ").strip().lower()
        puntos = 0
        if any(p in refuta for p in ["sin embargo", "aunque", "no obstante", "en cambio", "pero", "a pesar de"]):
            puntos += 1
        if len(refuta.split()) >= 10:
            puntos += 1
        if "." in refuta or "," in refuta:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/30")

# ✍️ Composición libre
def redactar_completo():
    print("\n✍️ ESCRIBE UN PÁRRAFO COMPLETO:")
    tesis = input("📝 Tesis: ").strip()
    desarrollo = input("👉 Desarrollo o causa: ").strip()
    contra = input("👉 Contraargumento: ").strip()
    refuta = input("👉 Refutación lógica: ").strip()
    texto = f"{tesis} {desarrollo} {contra} {refuta}"
    puntos = 0
    if any(p in refuta.lower() for p in ["sin embargo", "aunque", "no obstante", "en cambio", "pero", "a pesar de"]):
        puntos += 1
    if len(texto.split()) >= 40:
        puntos += 1
    if "." in texto:
        puntos += 1
    print(f"\n🎯 Tu puntuación: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu párrafo está estructurado y sólido!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes mejorar la refutación.")
    else:
        print("📘 Revisa cómo unir las ideas con coherencia y claridad.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 8.º Grado – Lección 8: Párrafo argumentativo completo")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar refutaciones 📝")
        print("4. Redactar tu propio párrafo ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar()
        elif opcion == "4":
            redactar_completo()
        elif opcion == "5":
            print("👋 ¡Gracias por pensar con profundidad y respeto!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
